import io
import re
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from extractor import extract_field_report_data
from vision_module import process_inspection_image

load_dotenv()

st.set_page_config(
    page_title="RAG Inspeksi Lapangan",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem;
    }
    .stTextArea textarea {
        font-size: 1.05rem !important;
        border-radius: 8px;
    }
    .stButton>button[data-baseweb="button"] {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button[kind="primary"] {
        background-color: #0F52BA;
        border-color: #0F52BA;
        color: white;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #083c8c;
        border-color: #083c8c;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
        border-radius: 12px;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar UI
with st.sidebar:
    st.title("Tentang Aplikasi")
    st.info(
        "Aplikasi ekstraksi data cerdas berbasis **RAG** dipadukan dengan **Instructor** "
        "untuk otomatisasi pendataan inspeksi lapangan."
    )
    st.markdown("---")
    st.markdown(
        "**Komponen Sistem:**\n"
        "- LlamaIndex (RAG Framework)\n"
        "- OpenRouter (LLM Engine)\n"
        "- Vision AI (Multimodal Analysis)\n"
        "- pgvector (PostgreSQL)\n"
        "- Pydantic & Instructor (Schema Enforcement)\n"
        "- Streamlit (Interface)"
    )
    st.markdown("---")
    st.caption("Versi Multimodal Multi-Foto")

# Main Header
st.title("Sistem Ekstraksi Laporan Inspeksi Lapangan")
st.markdown(
    "Konversi **catatan lapangan tidak terstruktur** dan **foto inspeksi** menjadi "
    "data terstruktur yang tervalidasi terhadap Standard Operating Procedures (SOP)."
)
st.divider()

# Inisialisasi session_state untuk teks yang dihasilkan Vision AI
if "vision_generated_text" not in st.session_state:
    st.session_state["vision_generated_text"] = ""
if "vision_success_msg" not in st.session_state:
    st.session_state["vision_success_msg"] = ""
if "vision_error_msg" not in st.session_state:
    st.session_state["vision_error_msg"] = ""

# Overlay melayang (Modal Dialog) untuk proses loading Vision AI
@st.dialog("Memproses Foto Inspeksi")
def process_photos_dialog(uploaded_files):
    # Menggunakan HTML untuk menengahkan konten teks di dalam popup
    st.markdown(
        """
        <style>
        .loader {
          border: 4px solid #f3f3f3;
          border-top: 4px solid #0F52BA;
          border-radius: 50%;
          width: 40px;
          height: 40px;
          animation: spin 1s linear infinite;
          margin: 0 auto 15px auto;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        </style>
        <div style='text-align: center; margin-bottom: 20px; padding-top: 10px;'>
            <div class="loader"></div>
            <h4 style='margin-bottom: 5px;'>Menganalisis Foto</h4>
            <span style='color: #666; font-size: 0.9em;'>Mengekstrak metadata dan narasi visual melalui Vision AI</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    all_descriptions = []
    error_list = []
    progress_bar = st.progress(0)
    
    for i, file in enumerate(uploaded_files):
        # Update progress bar
        progress_bar.progress((i) / len(uploaded_files), text=f"Memproses {i+1} dari {len(uploaded_files)}: {file.name}")
        
        image_bytes = file.getvalue()
        mime_type = file.type or "image/jpeg"
        
        try:
            description = process_inspection_image(image_bytes, mime_type)
            all_descriptions.append(description)
        except Exception as e:
            err_msg = f"{file.name}: {str(e)}"
            error_list.append(err_msg)
            all_descriptions.append(f"[Gagal memproses {file.name}: {str(e)}]")
    
    progress_bar.progress(1.0, text="Selesai")
    merged_text = " | ".join(all_descriptions)
    st.session_state["vision_generated_text"] = merged_text
    
    if error_list:
        st.session_state["vision_error_msg"] = "\n\n".join(error_list)
        st.session_state["vision_success_msg"] = ""
    else:
        st.session_state["vision_error_msg"] = ""
        st.session_state["vision_success_msg"] = f"{len(all_descriptions)} foto berhasil dianalisis."
    st.rerun()

# Menampilkan pop-up notifikasi (Toast) jika proses berhasil
if st.session_state["vision_success_msg"]:
    st.toast(st.session_state["vision_success_msg"])
    st.session_state["vision_success_msg"] = "" # Bersihkan setelah ditampilkan

if st.session_state["vision_error_msg"]:
    st.error(f"Gagal memproses foto:\n\n{st.session_state['vision_error_msg']}")
    st.session_state["vision_error_msg"] = "" # Bersihkan setelah ditampilkan

# ==========================================
# BAGIAN 1: INPUT
# ==========================================
st.subheader("1. Input Laporan")

input_col_photo, input_col_text = st.columns([4, 6], gap="large")

with input_col_photo:
    with st.container(border=True):
        st.markdown("#### Upload Multi-Foto Inspeksi")
        st.caption("Unggah satu atau beberapa foto lapangan (watermark/geotag) untuk dianalisis Vision AI.")
        
        uploaded_files = st.file_uploader(
            "Upload Multi-Foto Inspeksi (Multi-Select):",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        
        # Container khusus scroll untuk grid foto agar tombol Proses tetap "sticky" di bawah
        with st.container(height=260, border=False):
            if uploaded_files:
                st.markdown(f"**{len(uploaded_files)} foto dipilih:**")
                cols_per_row = min(len(uploaded_files), 3)
                grid_cols = st.columns(cols_per_row)
                
                for idx, file in enumerate(uploaded_files):
                    with grid_cols[idx % cols_per_row]:
                        st.image(file, caption=f"{file.name[:12]}...", use_container_width=True)
            else:
                st.info("Belum ada foto yang diunggah. Pratinjau akan muncul di sini.")
        
        st.write("")  # Spacing
        
        # Tombol ini sekarang dijamin posisinya tetap di bawah (sticky)
        if st.button("Proses Foto Massal dengan Vision AI", type="primary", use_container_width=True, disabled=not uploaded_files):
            process_photos_dialog(uploaded_files)

with input_col_text:
    with st.container(border=True):
        st.markdown("#### Teks Laporan")
        st.caption("Ketik manual, salin catatan, atau biarkan Vision AI mengisi otomatis dari foto.")
        
        # Disamakan tingginya dengan File Uploader + Grid Foto (sekitar 350px)
        messy_report = st.text_area(
            "Teks Catatan Lapangan:",
            value=st.session_state["vision_generated_text"],
            height=370,
            placeholder=(
                "Ketik atau tempel catatan lapangan di sini...\n\n"
                "Atau unggah foto di panel sebelah kiri dan klik 'Proses Foto Massal dengan Vision AI' "
                "untuk mengisi kolom ini secara otomatis."
            ),
            label_visibility="collapsed"
        )
    
        # Tombol Ekstraksi Data Terstruktur sejajar dengan tombol Proses Foto
        if st.button("Ekstrak Data Terstruktur", type="primary", use_container_width=True):
            if not messy_report.strip():
                st.warning("Harap masukkan teks laporan atau unggah foto terlebih dahulu.")
            else:
                with st.spinner("Menganalisis laporan dan mencocokkan dengan SOP..."):
                    try:
                        extracted_data, contexts = extract_field_report_data(messy_report)
                        st.session_state["extracted_data"] = extracted_data
                        st.session_state["contexts"] = contexts
                    except Exception as e:
                        st.error(f"Terjadi kesalahan: {str(e)}")

st.divider()

# ==========================================
# BAGIAN 2: OUTPUT
# ==========================================
st.subheader("2. Hasil Analisis Data")

if "extracted_data" in st.session_state:
    extracted_data = st.session_state["extracted_data"]
    contexts = st.session_state["contexts"]
    data_dict = extracted_data.model_dump()
    
    # Metrik Utama
    m1, m2, m3 = st.columns(3)
    m1.metric("Kategori Produk", str(data_dict.get("kategori_produk", "-")).title())
    m2.metric("Jumlah Stok", f"{data_dict.get('jumlah_stok', 0)}")
    m3.metric("Tanggal Inspeksi", str(data_dict.get("tanggal_inspeksi", "-")))
    
    st.write("")
    
    # Validasi Sistem (CoT Reasoning)
    reasoning = data_dict.get("penjelasan_kalkulasi_tanggal", "")
    if reasoning:
        st.success(f"**Logika Kalibrasi AI:** {reasoning}")
    
    # Detail Hasil (50:50)
    res_col1, res_col2 = st.columns(2, gap="large")
    
    with res_col1:
        with st.container(border=True):
            st.markdown("#### Rincian Data Ekstraksi")
            
            display_data = [
                {"Atribut": "Tanggal Inspeksi", "Informasi": str(data_dict.get("tanggal_inspeksi", "-"))},
                {"Atribut": "Kategori Produk", "Informasi": str(data_dict.get("kategori_produk", "-")).title()},
                {"Atribut": "Jumlah Stok", "Informasi": f"{data_dict.get('jumlah_stok', 0)}"},
                {"Atribut": "Koordinat Lokasi", "Informasi": str(data_dict.get("koordinat_lokasi", "-"))},
                {"Atribut": "Catatan Tambahan", "Informasi": str(data_dict.get("catatan_tambahan", "-"))},
            ]
            st.table(pd.DataFrame(display_data).set_index("Atribut"))
            
            # Generate file Excel
            df_export = pd.DataFrame([data_dict])
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df_export.to_excel(writer, index=False, sheet_name='Data Laporan')
                
                from openpyxl.worksheet.table import Table, TableStyleInfo
                from openpyxl.utils import get_column_letter
                
                workbook = writer.book
                worksheet = writer.sheets['Data Laporan']
                
                max_row = df_export.shape[0] + 1
                max_col = df_export.shape[1]
                tabel_ref = f"A1:{get_column_letter(max_col)}{max_row}"
                
                tab = Table(displayName="TabelInspeksi", ref=tabel_ref)
                style = TableStyleInfo(
                    name="TableStyleMedium9", showFirstColumn=False,
                    showLastColumn=False, showRowStripes=True, showColumnStripes=False
                )
                tab.tableStyleInfo = style
                worksheet.add_table(tab)
                
                for idx, col in enumerate(df_export.columns, 1):
                    worksheet.column_dimensions[get_column_letter(idx)].width = 25
            
            st.download_button(
                label="Unduh Dokumen Excel (.xlsx)",
                data=buffer.getvalue(),
                file_name="hasil_inspeksi.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                type="secondary",
                use_container_width=True
            )
            
        with st.container(border=True):
            st.markdown("#### Referensi SOP (RAG)")
            if contexts:
                for i, ctx in enumerate(contexts):
                    with st.expander(f"Potongan SOP #{i+1}", expanded=(i == 0)):
                        st.write(ctx)
            else:
                st.info("Tidak ada aturan SOP spesifik yang ditarik untuk laporan ini.")

    with res_col2:
        with st.container(border=True):
            st.markdown("#### Peta Lokasi Inspeksi")
            coord_str = str(data_dict.get("koordinat_lokasi", ""))
            # Parser koordinat cerdas: mengenali posisi tertukar dan huruf arah (S/N/E/W)
            lat, lon = None, None
            try:
                # Wajib ada titik desimal untuk menghindari salah tangkap angka biasa (seperti stok/tanggal)
                coord_parts = re.findall(r"(-?\d+\.\d+)\s*°?\s*([SNEW]?)", coord_str, re.IGNORECASE)
                
                if len(coord_parts) >= 2:
                    val1, dir1 = float(coord_parts[0][0]), coord_parts[0][1].upper()
                    val2, dir2 = float(coord_parts[1][0]), coord_parts[1][1].upper()
                    
                    # Terapkan minus berdasarkan S/N/E/W jika huruf arah tersedia
                    if dir1 == "S": val1 = -abs(val1)
                    elif dir1 == "N": val1 = abs(val1)
                    elif dir1 == "W": val1 = -abs(val1)
                    elif dir1 == "E": val1 = abs(val1)
                    
                    if dir2 == "S": val2 = -abs(val2)
                    elif dir2 == "N": val2 = abs(val2)
                    elif dir2 == "W": val2 = -abs(val2)
                    elif dir2 == "E": val2 = abs(val2)
                    
                    # Tentukan mana Latitude dan mana Longitude
                    # Rule 1: Berdasarkan huruf arah
                    if dir1 in ["N", "S"] or dir2 in ["E", "W"]:
                        lat, lon = val1, val2
                    elif dir1 in ["E", "W"] or dir2 in ["N", "S"]:
                        lat, lon = val2, val1
                    # Rule 2: Berdasarkan Range (Latitude harus antara -90 dan 90)
                    elif abs(val1) > 90 and abs(val2) <= 90:
                        lon, lat = val1, val2
                    elif abs(val2) > 90 and abs(val1) <= 90:
                        lon, lat = val2, val1
                    else:
                        # Fallback asumsi urutan standar: Latitude, Longitude
                        lat, lon = val1, val2
            except Exception:
                pass
            
            if lat is not None and lon is not None:
                st.map(pd.DataFrame([{"lat": lat, "lon": lon}]), zoom=10, use_container_width=True)
                st.caption(f"Koordinat: {lat:.6f}, {lon:.6f}")
            else:
                st.info("Koordinat desimal (lat, lon) tidak ditemukan dalam laporan ini.")
            
else:
    st.info("Masukkan teks laporan atau unggah foto di atas, lalu klik **Ekstrak Data Terstruktur** untuk melihat hasil analisis.")

