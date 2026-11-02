# LEMBAR TEMA PROYEK

- Nama            : Muhammad Khoiruddin Marzuq
- NIM             : 10231065
- Program studi   : Sistem Informasi
- Kode peserta K  : [ISI DENGAN NOMOR URUT ANDA]

## Angka lingkup saya
- Dokumen rujukan minimum : 5 + (K mod 4) = ___[cite: 7]
- Kasus uji minimum       : 12 + (K mod 6) = ___[cite: 7]
- Tool minimum            : 2 + (K mod 2) = ___[cite: 7]
- Mode keluaran tambahan  : [coret yang tidak perlu: wajib (K genap) / tidak wajib (K ganjil)][cite: 7]

## 1. Persoalan
Judul kerja produk :

    Smart Extractor: Otomatisasi Ekstraksi Laporan Inspeksi Lapangan Berbasis Multimodal RAG

Siapa yang mengalami persoalan ini (sesebut mungkin, bukan "masyarakat") :

    Tim operasional, teknisi lapangan, dan analis data (khususnya pada penyedia infrastruktur jaringan seperti Telkom Regional).

Bagaimana persoalan ini diselesaikan sekarang :

    Teknisi lapangan memfoto perangkat jaringan, mengetik laporan secara manual dengan format yang tidak standar di aplikasi pesan, lalu admin data menyalin ulang informasi tersebut satu per satu ke dalam lembar kerja (*spreadsheet*) atau basis data operasional.

Mengapa cara sekarang tidak memadai :

    Proses ini memakan waktu, sangat rentan terhadap kesalahan ketik manusia (seperti salah penulisan format koordinat geografis), penamaan kategori perangkat yang tidak konsisten, serta lambatnya proses konsolidasi data visual dari foto lapangan menjadi data terstruktur.

## 2. Mengapa AI generatif
Mengapa persoalan ini TIDAK cukup diselesaikan dengan basis data, formulir, atau seperangkat aturan biasa :

    Kondisi di lapangan menghasilkan laporan berantakan dengan format narasi natural yang sering menggunakan singkatan ("tgl", "kordinat lat"), bahasa non-formal, serta foto perangkat keras ber-watermark. Sistem aturan biasa (*RegEx*) atau formulir kaku tidak mampu mengekstrak informasi geografis, waktu, dan jenis perangkat dari gambar visual dan teks yang tidak beraturan secara bersamaan.

Apa yang membuat persoalan ini menuntut penafsiran bahasa :

    Sistem perlu memahami konteks semantik dari teks untuk membedakan antara tanggal inspeksi aktual ("hari ini jam 14:00") dengan tanggal rencana ("akan dipasang minggu depan"), serta memadukan temuan visual dari perangkat keras jaringan ke dalam narasi bahasa Indonesia yang koheren sebelum diekstrak menjadi struktur JSON.

## 3. Ukuran keberhasilan
Apa yang menjadi bukti bahwa produk ini berhasil :

    Sistem secara konsisten dan akurat menerima masukan teks acak maupun unggahan foto inspeksi lapangan, lalu menghasilkan keluaran data JSON terstruktur (meliputi tanggal YYYY-MM-DD, Latitude/Longitude presisi, jenis perangkat, dan catatan) yang otomatis terindeks ke basis data relasional.

Siapa yang dapat memeriksa keluarannya benar atau salah :

    Admin pendataan operasional atau validator kontrol kualitas yang membandingkan hasil akhir pada sistem (tabel/dashboard) dengan foto dan catatan asli milik teknisi lapangan.

Apa yang terjadi bila keluarannya salah, dan siapa yang menanggungnya :

    Basis data akan merekam data anomali (misalnya titik lokasi terlempar ke wilayah yang salah atau jumlah stok perangkat keliru), yang menuntut analis data atau admin operasional untuk melakukan koreksi manual melalui antarmuka sistem sebelum data digunakan untuk pelaporan akhir.

## 4. Dokumen rujukan
*(Catatan: Sesuaikan baris di bawah agar mencapai total "5 + (K mod 4)"[cite: 7])*

| # | Judul | Penerbit / asal | Tahun | Halaman | Status kelayakan |
|---|---|---|---|---|---|
| 1 | Standar Operasional Prosedur (SOP) Inspeksi Perangkat Jaringan Telkom | Dibuat sendiri (Data sintetik berdasar kasus riil) | 2026 | 3 | Layak |
| 2 | SEOJK tentang Penerapan Manajemen Risiko dalam Penggunaan Teknologi Informasi | Otoritas Jasa Keuangan | 2021 | >3 | Layak |
| 3 | COBIT 2019 Framework: Governance and Management Objectives (Area Operasional) | ISACA | 2018 | >3 | Layak |
| 4 | Panduan Praktik Terbaik Pemeliharaan Infrastruktur Fiber Optik dan Modem | Dokumen Publik / Sintetik | 2025 | 4 | Layak |
| 5 | ITIL 4 Foundation - Service Value System (Insiden & Aset) | AXELOS | 2019 | >3 | Layak |

Konfirmasi:
[x] Seluruh dokumen sah saya pakai[cite: 7]
[x] Tidak ada data pribadi orang sungguhan di dalamnya[cite: 7]
[x] Sedikitnya enam pertanyaan uji saya terjawab oleh kumpulan ini[cite: 7]

## 5. Uji lima kriteria penolakan
Untuk masing-masing, tulis LOLOS beserta alasan satu kalimat.

1. AI tidak dipaksakan pada persoalan deterministik : LOLOS. Karena teks berantakan dan pembacaan foto inspeksi tidak bisa dipecahkan dengan pemrograman berbasis aturan statis murni[cite: 7].
2. Keluaran dapat dibuktikan benar atau salah      : LOLOS. JSON terstruktur yang dihasilkan dengan mudah dicocokkan kembali terhadap foto visual dan teks masukan aslinya[cite: 7].
3. Sumber pengetahuan tersedia dan sah             : LOLOS. Pengetahuan diinjeksi via RAG menggunakan SOP jaringan teknis dan pedoman tata kelola TI publik/sintetik[cite: 7].
4. Tidak bergantung pada data pribadi nyata        : LOLOS. Fokus objek ekstraksi murni seputar koordinat infrastruktur dan kondisi perangkat keras jaringan[cite: 7].
5. Lingkupnya muat dikerjakan seorang diri 12 minggu : LOLOS. Arsitektur modul RAG, Validasi Pydantic, Vision Multimodal, dan UI telah dirancang secara iteratif[cite: 7].

## 6. Batas yang saya tetapkan sendiri
Produk ini TIDAK dimaksudkan untuk :
Menggantikan proses investigasi teknis mendalam jika terjadi kerusakan perangkat masif, atau dipakai sebagai pengambil keputusan otomatis untuk penghapusan nilai aset buku.

Keputusan apa yang TIDAK boleh diserahkan kepada produk ini :
Menjatuhkan vonis final bahwa suatu alat jaringan rusak secara permanen dan harus dibuang, karena AI di sini hanya memfasilitasi ekstraksi laporan pencatatan awal.

## 7. Rencana lapisan
| Blok | Yang akan saya tambahkan | Risiko terbesar |
|---|---|---|
| B — Kendali (Mgg 4–6) | Implementasi Instructor dengan model Pydantic untuk ekstraksi JSON ketat via OpenRouter (Gemma). UI awal memakai Streamlit[cite: 7]. | Model bahasa "berhalusinasi" menyimpang dari format skema JSON yang dipaksakan. |
| C — Grounding (Mgg 7–9) | Penyatuan LlamaIndex dan penyimpanan pgvector (Supabase) untuk membaca SOP Inspeksi Jaringan[cite: 7]. | Kegagalan *connection pooling* ke basis data awan dan inakurasi pengambilan dokumen vektor. |
| D — Agentic (Mgg 10–13) | Penambahan fungsi Multimodal Vision untuk menganalisis batch unggahan banyak foto sekaligus[cite: 7]. | Latensi pemrosesan (API lambat) akibat beban pembacaan berlapis pada banyak resolusi foto. |
| E — Kematangan (Mgg 14–16) | Integrasi tabel `st.data_editor` untuk koreksi manusia langsung di UI dan penyimpanan data riwayat ke tabel relasional Supabase[cite: 7]. | Sinkronisasi alur data dan batasan komponen UI untuk pengalaman interaksi *real-time* yang ideal. |