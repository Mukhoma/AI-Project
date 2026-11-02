"""
Vision Module untuk Multimodal Inspection Photo Analysis.
Mengirim foto inspeksi lapangan ke Vision AI (OpenRouter) dan menghasilkan
teks narasi laporan berdasarkan metadata foto (watermark, geotag) serta temuan visual.
"""

import os
import io
import base64
from openai import OpenAI
from dotenv import load_dotenv
from PIL import Image, ImageOps


VISION_SYSTEM_PROMPT = (
    "Anda adalah Asisten Inspeksi Lapangan AI. Analisis foto inspeksi ini secara teliti.\n"
    "1. Baca dan ekstrak semua teks dari watermark foto jika ada "
    "(Tanggal, Jam, Alamat lengkap, dan Titik Koordinat GPS seperti Latitude & Longitude).\n"
    "2. Identifikasi objek/perangkat utama yang ada di dalam foto "
    "(misalnya: jenis modem/router, logo vendor seperti Telkom/wifi.id, kelengkapan antena, "
    "kerapian kabel, dan kondisi fisik).\n"
    "3. Susun seluruh temuan tersebut menjadi satu paragraf teks narasi "
    "Laporan Inspeksi Lapangan berantakan dalam bahasa Indonesia baku/semi-baku. "
    "Contoh output: 'Pada tanggal 29 Juli 2026 pukul 14:20 WITA dilakukan inspeksi "
    "di Jl. RE Martadinata No.2, Balikpapan (koordinat 1.267683 S, 116.834256 E). "
    "Ditemukan instalasi perangkat modem wifi.id Telkom...'."
)


def optimize_image(image_bytes: bytes, max_dim: int = 1600) -> tuple[bytes, str]:
    """
    Mengompresi dan me-resize foto agar tidak melebihi batas ukuran/token payload,
    sekaligus menjaga teks watermark/koordinat tetap jelas terbaca oleh OCR.
    """
    try:
        img = Image.open(io.BytesIO(image_bytes))
        img = ImageOps.exif_transpose(img)
        
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=85, optimize=True)
        return buf.getvalue(), "image/jpeg"
    except Exception:
        return image_bytes, "image/jpeg"


# Daftar model Vision gratis di OpenRouter dengan mekanisme fallback otomatis
FALLBACK_VISION_MODELS = [
    "google/gemma-4-26b-a4b-it:free",
    "openrouter/free",
    "meta-llama/llama-3.2-11b-vision-instruct:free",
    "google/gemini-2.0-flash-exp:free",
]


def process_inspection_image(image_bytes: bytes, mime_type: str = "image/jpeg") -> str:
    """
    Memproses foto inspeksi lapangan menggunakan Vision AI dengan auto-fallback jika rate-limited.

    Args:
        image_bytes: Raw bytes dari file gambar yang diupload.
        mime_type: MIME type gambar (default: image/jpeg).

    Returns:
        Teks narasi laporan inspeksi hasil analisis Vision AI.
    """
    load_dotenv()

    or_api_key = os.getenv("OPENROUTER_API_KEY")
    or_base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    if not or_api_key:
        raise ValueError("OPENROUTER_API_KEY belum diatur di file .env")

    client = OpenAI(base_url=or_base_url, api_key=or_api_key)

    # Optimalkan gambar untuk menghemat kuota token & mencegah payload limit
    opt_bytes, opt_mime = optimize_image(image_bytes)

    # Encode gambar ke base64 untuk dikirim via OpenAI-compatible API
    b64_image = base64.b64encode(opt_bytes).decode("utf-8")

    last_error = None
    for model_name in FALLBACK_VISION_MODELS:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "system",
                        "content": VISION_SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Analisis foto inspeksi lapangan berikut dan buat narasi laporannya:",
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{opt_mime};base64,{b64_image}",
                                },
                            },
                        ],
                    },
                ],
                max_tokens=600,
            )
            if response.choices and response.choices[0].message.content:
                return response.choices[0].message.content
        except Exception as e:
            last_error = e
            continue

    if last_error:
        raise last_error
    raise RuntimeError("Semua model vision gagal memproses gambar.")

