# Spesifikasi Proyek — Satu Produk, Lima Lapisan

**Kapita Selekta: AI Engineering | 2 SKS | Ganjil 2026/2027**

---

## Apa yang Anda bangun

Satu produk digital berbasis AI generatif yang menyelesaikan **satu persoalan nyata dari bidang keilmuan Anda sendiri**.

Bukan tiruan ChatGPT. Bukan "chatbot serbaguna". Satu persoalan spesifik, satu target pengguna yang jelas, dan satu ukuran keberhasilan yang bisa dicek orang lain.

Produk itu dibangun berlapis sejak Minggu 4. Setiap blok menambah satu kemampuan ke sistem yang sama. Pada Minggu 16 Anda memiliki satu karya utuh, bukan lima tugas terpisah.

---

## Mengapa persoalan dari bidang Anda sendiri

Karena mata kuliah ini terbuka lintas prodi, keberagaman peserta diperlakukan sebagai kekuatan. Mahasiswa Kelautan, Perencanaan Wilayah, Sistem Informasi, dan Bisnis Digital akan menghadapi kendala yang berbeda, dan justru perbedaan itu yang membuat sesi peer review bernilai.

Alasan kedua lebih penting: Anda adalah satu-satunya orang di ruangan yang tahu apakah output sistem Anda **benar**. Dosen dapat menilai apakah rancangan Anda masuk akal, tetapi tidak dapat menilai apakah rekomendasi tata ruang atau interpretasi data oseanografi yang dihasilkan sistem Anda dapat dipercaya. Kemampuan menilai itu adalah keahlian Anda — dan modelnya tidak punya.

### Contoh arah persoalan lintas prodi

| Bidang | Persoalan yang layak | Yang membuatnya layak |
|---|---|---|
| Sistem Informasi | Asisten penelusur dokumen SOP internal yang menjawab disertai kutipan pasal | Sumber terbatas dan dapat diverifikasi |
| Perencanaan Wilayah | Pengolah dokumen RTRW yang mengekstraksi ketentuan zonasi jadi tabel terstruktur | Output berformat tetap, benar-salahnya bisa dicek |
| Kelautan / Perikanan | Peringkas laporan survei lapangan menjadi ringkasan berbasis parameter baku | Ada standar rujukan yang jelas |
| Bisnis Digital | Agent reviewer ulasan pelanggan yang mengelompokkan keluhan dan menyusun tindak lanjut | Butuh banyak langkah dan memakai tool |
| Teknik Industri | Pembantu penyusunan instruksi kerja dari dokumen standar mutu | Risiko hallucination nyata dan berdampak |
| Ilmu apa pun | Pembantu kajian pustaka pada satu topik sempit dengan sumber yang Anda kurasi | Mudah diuji, mudah dibuktikan salah |

### Persoalan yang ditolak

Lima jenis tema ditolak pada tahap penetapan, bukan pada tahap penilaian akhir:

1. **AI dipaksakan.** Persoalan yang lebih baik diselesaikan dengan formulir, basis data, atau satu halaman aturan. Kalau jawabannya dapat ditentukan secara pasti, Anda tidak butuh model bahasa.
2. **Tidak bisa dicek benar-salahnya.** Kalau tidak ada cara memeriksa output itu benar atau salah, tidak ada yang dapat dievaluasi pada Minggu 14.
3. **Tanpa sumber pengetahuan yang dapat Anda akses.** Lapisan RAG mengharuskan Anda memiliki dokumen rujukan yang sah untuk dipakai. Kalau dokumennya rahasia atau memang tidak ada, tema itu belum bisa dipakai — cari sudut lain dari bidang yang sama, biasanya ada.
4. **Bergantung pada data pribadi orang sungguhan.** Data rekam medis, data mahasiswa, data pelanggan nyata. Pakai data sintetis atau data terbuka.
5. **Terlalu luas.** "Asisten belajar untuk semua mata kuliah" bukan proyek, itu angan-angan. Persempit sampai bisa dikerjakan sendiri dalam dua belas minggu.

Kalau tema Anda ditolak, Anda punya waktu sampai Minggu 6 untuk menggantinya. Setelah Minggu 6, tema terkunci.

---

## Lingkup wajib yang diturunkan dari kode peserta K

Agar tidak ada dua produk yang identik dan agar beban tiap orang sebanding, sebagian lingkup diturunkan dari **kode peserta K** — nomor urut Anda pada daftar kelas, diterima Minggu 1. Aturan penurunan lengkap ada di [lampiran/B-lembar-tema-proyek.md](lampiran/B-lembar-tema-proyek.md). Ringkasnya:

| Unsur | Aturan | Contoh untuk K = 7 |
|---|---|---|
| Jumlah dokumen rujukan minimum | `5 + (K mod 4)` dokumen | 5 + 3 = **8 dokumen** |
| Jumlah kasus uji minimum | `12 + (K mod 6)` kasus | 12 + 1 = **13 kasus** |
| Jumlah tool yang wajib dipanggil agent | `2 + (K mod 2)` tool | 2 + 1 = **3 tool** |
| Bahasa output wajib | Indonesia; kalau `K` genap, tambah satu mode output ringkas | K ganjil → satu mode |

Angka-angka ini adalah **minimum**, bukan target. Produk yang berhenti tepat di angka minimum masih dapat bernilai sangat baik kalau rancangan dan evaluasinya matang.

---

## Lima lapisan

### Lapisan 1 — Fondasi (Minggu 1–3)

Belum ada produk. Yang ada baru pemahaman dan lingkungan kerja yang sudah siap dipakai.

**Kriteria selesai:**
- [ ] Anda dapat menjelaskan apa yang dilakukan model bahasa besar tanpa memakai kata "berpikir" atau "memahami"
- [ ] Anda dapat menghitung perkiraan biaya satu pemanggilan dari jumlah token input dan output
- [ ] Anda berhasil melakukan pemanggilan model pertama dan menyimpan buktinya
- [ ] Anda punya sedikitnya tiga calon persoalan dari bidang Anda, dengan alasan masing-masing

### Lapisan 2 — Kendali (Minggu 4–6)

Produk pertama kali muncul. Ia menerima input, mengembalikan output yang **berformat tetap**, dan dapat memanggil sedikitnya satu tool di luar dirinya.

**Kriteria selesai:**
- [ ] Tema terkunci dan tercatat pada lembar tema
- [ ] System prompt terdokumentasi, diberi nomor versi, dengan alasan tiap bagiannya
- [ ] Output mengikuti satu schema tetap pada sedikitnya sepuluh input berbeda, termasuk input yang tidak biasa
- [ ] Sedikitnya satu tool eksternal dipanggil dan hasilnya dipakai dalam jawaban
- [ ] Anda dapat menunjukkan satu input yang **membuat sistem gagal**, dan menjelaskan sebabnya

Butir terakhir bukan pengakuan gagal, justru sebaliknya. Setiap sistem pasti punya titik lemah. Kalau Anda belum menemukan satu pun, yang bermasalah bukan sistemnya, tapi cara Anda mengujinya.

### Lapisan 3 — Grounding (Minggu 7–9)

Produk menjawab berdasarkan **dokumen milik Anda**, bukan berdasarkan pengetahuan umum modelnya, dan menyebutkan dari mana jawabannya berasal.

**Kriteria selesai:**
- [ ] Dokumen rujukan sejumlah minimum menurut K, sah untuk dipakai, tercatat asalnya
- [ ] Sistem mengembalikan jawaban beserta rujukan chunk sumbernya
- [ ] Anda dapat menunjukkan satu pertanyaan yang **seharusnya dijawab "tidak ada di dokumen"** dan sistem Anda menjawab demikian
- [ ] Anda dapat menunjukkan satu kasus retrieval yang meleset, dan menjelaskan mengapa chunk yang salah terambil

### Lapisan 4 — Agentic (Minggu 10–13)

Produk berhenti menjadi satu langkah tanya-jawab dan menjadi agent: ia merencanakan, memakai tool, menyimpan state (keadaan terakhir), dan berhenti ketika seharusnya berhenti.

**Kriteria selesai:**
- [ ] Sistem menyelesaikan sedikitnya satu tugas yang butuh banyak langkah secara mandiri
- [ ] Tool sejumlah minimum menurut K, masing-masing dengan batas akses tertulis
- [ ] Ada batas jumlah langkah dan penanganan kalau batas tercapai
- [ ] Ada sedikitnya satu titik **human-in-the-loop** pada tindakan yang tidak dapat dibatalkan
- [ ] Anda dapat menjelaskan mengapa bagian tertentu sistem Anda **sengaja tidak** dibuat agentic

### Lapisan 5 — Kematangan (Minggu 14–16)

Produk tidak lagi sekadar prototipe yang bagus saat demo, tapi sesuatu yang klaimnya bisa dibuktikan.

**Kriteria selesai:**
- [ ] Set uji sejumlah minimum menurut K, dengan jawaban acuan dan kriteria penilaian
- [ ] Laporan evaluasi berisi angka, bukan kesan
- [ ] Perkiraan biaya per pemanggilan dan per seratus pengguna
- [ ] Kajian risiko: *prompt injection*, kebocoran data, bias, dan dampak kalau sistem salah
- [ ] Pernyataan etis: apa yang sistem ini **tidak boleh** dipakai untuk melakukannya

---

## Yang dinilai dan yang tidak

**Dinilai:**
- Ketepatan rumusan persoalan
- Alasan di balik setiap keputusan rancangan
- Kejujuran dan kedalaman pengujian
- Kesadaran risiko
- Kemampuan menjelaskan dan mempertahankan karya saat ditanya

**Tidak dinilai:**
- Keindahan antarmuka
- Jumlah baris kode
- Kecanggihan pustaka yang dipakai
- Apakah Anda menulis kodenya sendiri atau dibantu AI

Produk berbasis terminal (command line) yang dievaluasi dengan jujur lebih bernilai daripada produk dengan tampilan indah yang tidak pernah diuji. Ini bukan retorika; ini rubrik.

---

## Bukan tugas kelompok

Setiap mahasiswa mengerjakan produknya sendiri. Kolaborasi dibatasi pada peer review terstruktur (Minggu 9 dan 12), tempat Anda **mengkritik** karya rekan, bukan mengerjakannya.

Alasannya bukan ketidakpercayaan, tapi konsekuensi dari tidak adanya asisten: pada kelas dengan bimbingan terbatas, kerja kelompok sering berakhir dengan satu orang yang mengerjakan dan sisanya menumpang. Kelas ini mencegahnya sejak awal.
