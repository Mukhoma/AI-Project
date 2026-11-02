import os
import instructor
from openai import OpenAI
from urllib.parse import urlparse
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, Settings
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding

# Import Pydantic schema dari Phase 2
from schema import LaporanInspeksiLapangan

def get_retriever():
    """
    Menghubungkan ke database pgvector dan mengembalikan LlamaIndex retriever.
    """
    db_url_str = os.getenv("DATABASE_URL")
    if not db_url_str:
        raise ValueError("DATABASE_URL belum diatur di file .env")
        
    parsed_url = urlparse(db_url_str)
    
    or_api_key = os.getenv("OPENROUTER_API_KEY")
    or_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    # Konfigurasi LlamaIndex untuk menggunakan OpenRouter API dalam membuat vector (embeddings) saat mencari konteks
    Settings.embed_model = OpenAIEmbedding(
        api_key=or_api_key,
        api_base=or_base_url,
        model="text-embedding-3-small"
    )
    
    vector_store = PGVectorStore.from_params(
        database=parsed_url.path[1:],
        host=parsed_url.hostname,
        password=parsed_url.password,
        port=parsed_url.port or 5432,
        user=parsed_url.username,
        table_name="document_chunks",
        embed_dim=1536
    )
    
    # Load index dari existing vector store (SOP yang sudah di-ingest)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    
    # Konfigurasi retriever untuk mengambil 3 chunk konteks yang paling relevan
    return index.as_retriever(similarity_top_k=3)

def extract_field_report_data(messy_report: str) -> tuple[LaporanInspeksiLapangan, list[str]]:
    """
    Mengambil konteks SOP dari pgvector, lalu menggunakan Instructor + OpenRouter 
    untuk mengekstrak JSON terstruktur sesuai skema LaporanInspeksiLapangan.
    """
    load_dotenv()
    
    or_api_key = os.getenv("OPENROUTER_API_KEY")
    or_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    if not or_api_key:
        raise ValueError("OPENROUTER_API_KEY is not set.")
        
    # Inisialisasi client OpenAI yang di-patch oleh Instructor untuk OpenRouter API
    client = instructor.from_openai(
        OpenAI(
            base_url=or_base_url,
            api_key=or_api_key
        )
    )
    
    # 1. Semantic Search (RAG Retrieval Phase) dengan graceful fallback
    # Jika API embedding OpenRouter (text-embedding-3-small) dibatasi kredit (402),
    # sistem secara elegan membaca seksi dokumen SOP lokal yang relevan.
    contexts = []
    try:
        retriever = get_retriever()
        nodes = retriever.retrieve(messy_report)
        contexts = [node.get_content() for node in nodes]
    except Exception as e:
        print(f"Info: Vector retrieval pgvector dilewati ({e}), menggunakan SOP lokal.")
        sop_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "sop_inspeksi_jaringan.txt")
        if os.path.exists(sop_file_path):
            with open(sop_file_path, "r", encoding="utf-8") as f:
                sop_content = f.read()
                
            lower_report = messy_report.lower()
            sections = sop_content.split("=== ")
            matched_sections = []
            for sec in sections:
                if not sec.strip():
                    continue
                sec_clean = "=== " + sec.strip()
                sec_lower = sec.lower()
                if ("modem" in lower_report and "modem" in sec_lower) or \
                   ("router" in lower_report and "router" in sec_lower) or \
                   ("access point" in lower_report and "access point" in sec_lower) or \
                   ("switch" in lower_report and "switch" in sec_lower) or \
                   ("odp" in lower_report and "odp" in sec_lower) or \
                   ("aturan umum" in sec_lower):
                    matched_sections.append(sec_clean)
            
            contexts = matched_sections if matched_sections else [sop_content]
        else:
            contexts = ["Standard Operating Procedure (SOP) umum."]
    
    context_text = "\n\n---\n\n".join(contexts) if contexts else "Tidak ada aturan SOP yang ditemukan."
    
    from datetime import datetime, timedelta
    today = datetime.now()
    
    days_id = {
        "Monday": "Senin", "Tuesday": "Selasa", "Wednesday": "Rabu",
        "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
    }
    current_day_id = days_id[today.strftime("%A")]
    current_date_str = f"{today.strftime('%Y-%m-%d')} ({current_day_id})"
    
    # Membuat referensi kalender dengan bahasa Indonesia agar LLM bisa mencocokkan kata "Kamis"
    calendar_lines = []
    for i in range(14):
        d = today - timedelta(days=i)
        day_id = days_id[d.strftime("%A")]
        calendar_lines.append(f"- {d.strftime('%Y-%m-%d')} ({day_id})")
    calendar_ref = "\n".join(calendar_lines)
    
    # 2. Construct the RAG Prompt
    system_message = (
        f"Anda adalah AI asisten data ekstraksi yang ahli.\n"
        f"PENTING: Hari ini adalah {current_date_str}.\n"
        f"Referensi Kalender 14 hari terakhir:\n{calendar_ref}\n\n"
        "Tugas Anda adalah mengekstrak data terstruktur dari laporan inspeksi lapangan yang tidak terstruktur/berantakan.\n\n"
        "Anda HARUS mematuhi aturan Standard Operating Procedures (SOP) berikut ini ketika mengekstrak data:\n"
        f"{context_text}\n\n"
        "Panduan Ekstraksi:\n"
        "- Pastikan tanggal dalam format YYYY-MM-DD.\n"
        "- Jika laporan menggunakan kata ganti waktu (contoh: 'Kamis minggu lalu', 'kemarin'), ANDA WAJIB mencocokkan nama harinya dengan tabel Referensi Kalender di atas dan mengambil tanggal yang tepat (misal jika hari ini Senin 7 Sep, Kamis minggu lalu adalah Kamis 3 Sep).\n"
        "- Pastikan koordinat akurat.\n"
        "- Kategori produk wajib sesuai dengan aturan baku dari SOP."
    )
    
    # 3. LLM Extraction (Instructor Phase) dengan auto-fallback jika model rate-limited
    fallback_models = [
        "google/gemma-4-26b-a4b-it:free",
        "openrouter/free",
        "meta-llama/llama-3.3-70b-instruct:free",
    ]
    extracted_data = None
    last_error = None
    for model_name in fallback_models:
        try:
            extracted_data = client.chat.completions.create(
                model=model_name,
                response_model=LaporanInspeksiLapangan,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": f"Laporan Mentah:\n{messy_report}"}
                ],
                max_tokens=1000
            )
            if extracted_data:
                break
        except Exception as e:
            last_error = e
            continue

    if extracted_data is None and last_error:
        raise last_error

    return extracted_data, contexts
