"""
Script untuk menghapus data chunk SOP lama dari pgvector
dan melakukan re-ingest dokumen SOP yang sudah diperbarui.
"""
import os
import psycopg2
from dotenv import load_dotenv

def clear_old_chunks():
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL is not set.")
        return False
    
    try:
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Hapus semua data di tabel LlamaIndex (prefixed dengan 'data_')
        for table in ["data_document_chunks", "document_chunks"]:
            try:
                cursor.execute(f"DELETE FROM {table};")
                print(f"-> Berhasil menghapus data lama dari tabel '{table}'.")
            except Exception as e:
                print(f"-> Tabel '{table}' tidak ditemukan atau kosong, lewati. ({e})")
                conn.rollback()
                conn.autocommit = True
        
        cursor.close()
        conn.close()
        print("Pembersihan selesai.\n")
        return True
    except Exception as e:
        print(f"Error saat membersihkan: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("LANGKAH 1: Menghapus chunk SOP lama...")
    print("=" * 50)
    
    if clear_old_chunks():
        print("=" * 50)
        print("LANGKAH 2: Re-ingest SOP baru...")
        print("=" * 50)
        from ingest import ingest_sops
        ingest_sops("data")
    else:
        print("Gagal membersihkan data lama. Re-ingest dibatalkan.")

