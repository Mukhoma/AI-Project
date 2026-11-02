import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, Settings
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding

def ingest_sops(data_dir: str):
    load_dotenv()
    
    db_url_str = os.getenv("DATABASE_URL")
    if not db_url_str:
        raise ValueError("DATABASE_URL belum diatur di file .env")
        
    parsed_url = urlparse(db_url_str)

    # Menggunakan konfigurasi OpenRouter untuk Embedding
    or_api_key = os.getenv("OPENROUTER_API_KEY")
    or_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    
    if not or_api_key:
        raise ValueError("OPENROUTER_API_KEY belum diatur di file .env")

    # Override default embed_model untuk menggunakan OpenRouter
    Settings.embed_model = OpenAIEmbedding(
        api_key=or_api_key,
        api_base=or_base_url,
        model="text-embedding-3-small", 
        embed_batch_size=10
    )
    
    print("Menghubungkan ke PostgreSQL Vector Store...")
    vector_store = PGVectorStore.from_params(
        database=parsed_url.path[1:],
        host=parsed_url.hostname,
        password=parsed_url.password,
        port=parsed_url.port or 5432,
        user=parsed_url.username,
        table_name="document_chunks",
        embed_dim=1536
    )
    
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    print(f"Membaca dokumen SOP dari direktori '{data_dir}'...")
    documents = SimpleDirectoryReader(input_dir=data_dir).load_data()
        
    print(f"Berhasil memuat {len(documents)} dokumen. Memulai proses chunking dan embedding via OpenRouter...")
    
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        show_progress=True
    )
    
    print("Ingestion selesai! Data SOP berhasil disimpan ke dalam tabel 'document_chunks'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="data")
    args = parser.parse_args()
    
    ingest_sops(args.data_dir)
