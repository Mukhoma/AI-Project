from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Literal

class LaporanInspeksiLapangan(BaseModel):
    """
    Schema Pydantic untuk ekstraksi data terstruktur dari Laporan Inspeksi Lapangan.
    """
    penjelasan_kalkulasi_tanggal: str = Field(..., description="Langkah-langkah logika Anda dalam mencocokkan kata ganti waktu di teks dengan Referensi Kalender untuk mendapatkan tanggal yang tepat.")
    tanggal_inspeksi: date = Field(..., description="Tanggal inspeksi lapangan dilakukan (format YYYY-MM-DD).")
    koordinat_lokasi: str = Field(..., description="Koordinat lokasi inspeksi (misal: latitude/longitude atau nama tempat).")
    kategori_produk: Literal["produk kelapa", "produk sawit", "lainnya"] = Field(
        ..., 
        description="Kategori produk yang diinspeksi. Harus salah satu dari nilai yang valid."
    )
    jumlah_stok: int = Field(..., description="Jumlah stok produk yang divalidasi selama inspeksi.")
    catatan_tambahan: Optional[str] = Field(None, description="Catatan atau temuan tambahan lainnya.")
