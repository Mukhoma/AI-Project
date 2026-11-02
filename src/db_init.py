import os
import psycopg2
from dotenv import load_dotenv

def init_db():
    # Load environment variables
    load_dotenv()
    
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL is not set in the environment.")
        return

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cursor = conn.cursor()

        print("Connecting to cloud database and initializing schemas...")

        # 1. Enable pgvector extension
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        print("-> Verified/Enabled pgvector extension.")

        # 2. Create Relational Table for Extracted Data matching the new Pydantic schema
        create_reports_table = """
        CREATE TABLE IF NOT EXISTS laporan_inspeksi (
            id SERIAL PRIMARY KEY,
            tanggal_inspeksi DATE NOT NULL,
            koordinat_lokasi VARCHAR(255) NOT NULL,
            kategori_produk VARCHAR(100) NOT NULL,
            jumlah_stok INTEGER NOT NULL,
            catatan_tambahan TEXT,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_reports_table)
        print("-> Created 'laporan_inspeksi' table for structured extracted data.")

        # 3. Create Table for Vector Store (Document Chunks for SOPs)
        # We assume 1536 dimensions (standard for OpenAI embeddings like text-embedding-ada-002)
        create_chunks_table = """
        CREATE TABLE IF NOT EXISTS document_chunks (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            document_id VARCHAR(255),
            text TEXT NOT NULL,
            metadata JSONB,
            embedding vector(1536)
        );
        """
        cursor.execute(create_chunks_table)
        print("-> Created 'document_chunks' table with pgvector support.")

        cursor.close()
        conn.close()
        print("Database initialization complete.")
        
    except Exception as e:
        print(f"An error occurred during database initialization: {e}")

if __name__ == "__main__":
    init_db()
