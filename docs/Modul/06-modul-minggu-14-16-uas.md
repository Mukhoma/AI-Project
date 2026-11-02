# MODUL — MINGGU 14–16
## Blok E · Kematangan: Dari Prototipe ke Produk
### Termasuk aturan dan susunan Ujian Akhir Semester

**Kapita Selekta: AI Engineering | Sub-CPMK-5 dan Sub-CPMK-6 | CPMK-2**

> Tiga minggu terakhir tidak menambah fitur baru pada produk Anda. Tujuannya mengubah "kesan" menjadi angka, dan klaim menjadi bukti.

---

## Kenapa prototipe yang bagus saat demo sering gagal

Prototipe diuji oleh pembuatnya sendiri, dengan input pilihan pembuatnya, saat pembuatnya sedang optimis. Produk dipakai orang lain, dengan input yang tidak terduga, di saat kesalahannya benar-benar berdampak.

Empat penyebab yang sering terjadi:

| Penyebab | Yang terlihat saat demo | Yang terjadi kemudian |
|---|---|---|
| Hanya diuji pada kasus ideal | Semuanya berhasil | Gagal pada input pertama yang tidak biasa |
| Tidak ada angka | "Rasanya akurat" | Tidak ada yang tahu kalau kualitasnya turun setelah diubah |
| Biaya tidak dihitung | Murah untuk satu pengguna | Tidak terjangkau untuk seratus pengguna |
| Risiko tidak dipetakan | Belum ada yang menyerang | Serangan pertama langsung berhasil |

Tiga minggu ini membahas keempatnya, satu per satu.

---
---

# MINGGU 14 — Evaluasi Sistematis dan Pengendalian Biaya

**Sub-CPMK-5** · **(C5)**
**Target akhir minggu:** Anda punya angka, bukan sekadar kesan, tentang kualitas dan biaya produk Anda — beserta perbandingannya dengan baseline Minggu 9.

---

## 14.1 Konsep

### Set uji: pekerjaan yang tidak bisa diwakilkan

Set uji (test set) adalah kumpulan pasangan **input** dan **jawaban acuan**, disertai **kriteria penilaian**. Anda harus menyusunnya sendiri karena hanya Anda yang tahu jawaban yang benar di bidang Anda.

Komposisi yang disarankan untuk `12 + (K mod 6)` kasus:

| Jenis kasus | Porsi | Mengapa ada |
|---|:--:|---|
| Kasus umum | ± 40% | Mengukur perilaku sehari-hari |
| Kasus batas (edge case) | ± 25% | Data tidak lengkap, format tidak wajar, ambigu |
| Kasus yang **harus ditolak** | ± 20% | Mengukur kejujuran sistem, bukan kepintarannya |
| Kasus yang pernah gagal | ± 15% | Memastikan kesalahan lama tidak muncul lagi |

Kelompok terakhir diambil dari daftar kegagalan yang Anda kumpulkan sepanjang semester. Kegagalan yang pernah terjadi adalah kasus uji terbaik, karena sudah terbukti bisa terjadi.

### Kriteria penilaian harus bisa dipakai orang lain

Kalau kriteria Anda "jawabannya bagus", dua penilai akan memberi angka berbeda, dan angka itu tidak ada artinya. Kriteria yang baik berupa pertanyaan ya/tidak:

```
Untuk tiap kasus, nilai lima hal, masing-masing YA / TIDAK:
  1. Menjawab pertanyaan yang benar-benar diajukan
  2. Seluruh pernyataan didukung sumber yang dirujuk
  3. Tidak ada pernyataan tambahan tanpa dasar
  4. Format output valid menurut schema
  5. Menolak dengan benar bila memang seharusnya menolak
```

Lima pertanyaan ya/tidak lebih berguna daripada satu skala 1–10, karena angka "7" tidak memberi tahu apa yang perlu diperbaiki, sedangkan "gagal di nomor 3 pada enam kasus" langsung menunjukkan masalahnya.

### LLM-as-a-judge: berguna, tapi harus dicek

Menilai puluhan kasus secara manual itu lambat, jadi model bisa dipakai sebagai penilai. Tiga syarat agar hasilnya bisa dipercaya:

1. **Penilai memakai kriteria ya/tidak yang sama**, bukan diminta "menilai kualitas".
2. **Kalibrasi.** Nilai sendiri minimal sepertiga kasus secara manual, lalu bandingkan dengan penilaian model. Kalau banyak yang berbeda, penilai model tidak layak dipakai untuk sisanya.
3. **Penilai sebaiknya bukan model yang sama dengan yang dinilai.** Model cenderung memberi nilai lebih tinggi pada output-nya sendiri.

Angka kalibrasi ini wajib dilaporkan. Angka evaluasi tanpa kalibrasi tidak jelas artinya.

### Biaya: tiga angka yang wajib Anda punya

```
1. Biaya per permintaan khas       = token input × tarif + token output × tarif
2. Biaya per permintaan TERBURUK   = kasus agent mencapai batas langkah
3. Biaya untuk 100 pengguna/bulan  = (1) × perkiraan pemakaian × 100
```

Angka kedua paling sering dilupakan, dan paling sering membuat produk agentic gagal. Anda sudah mencatatnya di Minggu 10 nomor 2.

Empat cara menurunkan biaya, dari yang paling sering berhasil:

| Cara | Perkiraan penghematan | Kekurangannya |
|---|---|---|
| Bagi tugas: tugas rutin ke model kecil | Besar | Perlu diuji ulang per tugas |
| Pangkas konteks: kirim hanya yang perlu | Besar | Bisa terbuang informasi yang ternyata penting |
| Simpan hasil yang berulang (*caching*) | Sedang–besar | Hasil bisa kedaluwarsa |
| Batasi panjang output | Kecil–sedang | Jawaban terpotong kalau batasnya terlalu ketat |

Setiap cara yang Anda terapkan wajib disertai bukti bahwa **kualitas tidak turun** — diukur dengan set uji yang sama. Hemat biaya tapi kualitas turun itu bukan penghematan, melainkan penurunan kualitas yang disamarkan.

---

## 14.2 Skenario Minggu 14

**Kriteria sukses:**

- [ ] Set uji `12 + (K mod 6)` kasus dengan komposisi sesuai porsi, lengkap jawaban acuan
- [ ] Kriteria penilaian ya/tidak yang bisa dipakai orang lain
- [ ] Seluruh kasus dinilai; kalau memakai penilai model, angka kalibrasi dilaporkan
- [ ] Hasil dibandingkan dengan baseline Minggu 9
- [ ] Tiga angka biaya dihitung dari data nyata `catatan-pemakaian.md`
- [ ] Minimal satu cara penghematan diterapkan, dengan bukti kualitas tidak turun
- [ ] Tiga usulan perbaikan berdasarkan bukti, diurutkan dari dampak terbesar

---

## 14.3 READ → BREAK → FIX → BUILD

### READ — Menilai lima kasus secara manual (25 menit, tanpa AI)

Jalankan lima kasus uji dan nilai sendiri memakai lima pertanyaan ya/tidak:

| # | Kasus | 1 | 2 | 3 | 4 | 5 | Catatan |
|---|---|:-:|:-:|:-:|:-:|:-:|---|

Lalu jawab: pertanyaan nomor berapa yang **paling sulit** Anda nilai secara konsisten? Perbaiki kalimatnya sampai Anda yakin orang lain akan memberi jawaban yang sama.

### BREAK — Enam percobaan (25 menit)

| # | Percobaan | Prediksi Anda | Hasil sebenarnya |
|---|---|---|---|
| 1 | Jalankan set uji dua kali; hitung berapa kasus berubah hasilnya | | |
| 2 | Ganti ke model termurah, jalankan set uji yang sama | | |
| 3 | Pangkas konteks separuh, jalankan set uji yang sama | | |
| 4 | Nilai lima kasus dengan penilai model, bandingkan dengan penilaian manual Anda | | |
| 5 | Naikkan temperature ke 1, jalankan set uji | | |
| 6 | Minta penilai model menilai output yang **sengaja dibuat salah** | | |

Nomor 1 mengukur reproducibility sistem Anda (apakah hasilnya konsisten kalau diulang). Kalau banyak kasus berubah antar-percobaan, berarti semua angka evaluasi Anda punya variance, dan besarnya harus dilaporkan bersama angkanya.

Nomor 6 menguji penilainya, bukan sistemnya. Penilai yang meloloskan output yang jelas salah tidak layak dipakai.

### FIX — Laporan evaluasi yang menyesatkan (20 menit)

Laporan berikut memuat **lima** masalah.

```
HASIL EVALUASI

Sistem diuji pada 30 pertanyaan dan mencapai akurasi 93%.
Penilaian dilakukan otomatis oleh model.
Sistem terbukti andal dan siap dipakai.

Biaya: sangat murah, sekitar Rp50 per pertanyaan.

Perbaikan yang dilakukan: mengganti model ke yang lebih murah,
menghemat 60% biaya.
```

| # | Masalah | Kenapa menyesatkan | Yang seharusnya dilaporkan |
|---|---|---|---|

Satu masalah lebih serius daripada empat lainnya karena membuat semua angka di laporan itu tidak ada artinya. Yang mana?

### BUILD — Laporan evaluasi (mandiri)

Susun `laporan-evaluasi.md` memakai [lampiran/D-template-laporan-evaluasi.md](lampiran/D-template-laporan-evaluasi.md), dan penuhi semua kriteria sukses bagian 14.2.

**Tantangan wajib.** Terapkan satu cara penghematan yang menurunkan biaya minimal 30% **tanpa** menurunkan angka evaluasi. Tunjukkan angka sebelum dan sesudah pada set uji yang sama. Kalau tidak tercapai, laporkan penghematan yang Anda coba, berapa kualitas yang turun, dan pada kasus jenis apa penurunannya terjadi.

---

## 14.4 Daftar Periksa Mandiri — Minggu 14

- [ ] Set uji lengkap sesuai komposisi, dengan jawaban acuan
- [ ] Kriteria ya/tidak diperbaiki sampai bisa dinilai secara konsisten
- [ ] Enam percobaan BREAK dengan prediksi lebih dulu
- [ ] Variance antar-percobaan (nomor 1) dilaporkan bersama angka evaluasi
- [ ] Kalibrasi penilai model dilaporkan kalau penilai model dipakai
- [ ] Lima masalah laporan menyesatkan ditemukan
- [ ] Tiga angka biaya dari data nyata
- [ ] Perbandingan terhadap baseline Minggu 9 tertulis

---
---

# MINGGU 15 — Keamanan, Etika, Bias, dan Tanggung Jawab Profesional

**Sub-CPMK-6** · **(C5)**
**Target akhir minggu:** Anda punya kajian risiko yang jujur tentang produk Anda, dan pernyataan etis yang menyebutkan batas penggunaannya.

---

## 15.1 Konsep

### Risiko keamanan yang relevan untuk produk seperti milik Anda

| Risiko | Bentuknya pada produk mahasiswa | Cara mengatasi yang paling murah |
|---|---|---|
| *Prompt injection* | Dokumen rujukan yang memuat instruksi | Batasi akses tool; sudah dikerjakan Minggu 13 |
| Kebocoran data | Data yang dikirim ke penyedia model tersimpan di luar kendali Anda | Jangan kirim data yang tidak boleh keluar; sensor dulu sebelum dikirim |
| Bocornya system prompt | Isi prompt terlihat oleh pengguna | Sejak awal, anggap isi prompt bukan rahasia |
| Penyalahgunaan | Sistem dipakai untuk hal di luar tujuannya | Batasi cakupan; tolak dengan tegas permintaan di luar cakupan |
| Kredensial terbuka | API key ikut terunggah ke repositori | Cek riwayat repositori Anda; ini benar-benar sering terjadi |

Butir terakhir sebaiknya Anda cek hari ini juga. API key yang pernah terunggah tetap tersimpan di riwayat git meskipun file-nya sudah dihapus.

### Bias itu nyata di produk Anda, bukan sekadar teori

Bias masuk lewat tiga jalan, dan ketiganya ada di produk Anda:

1. **Dari model.** Model dilatih dengan data yang tidak seimbang. Bahasa Indonesia jauh lebih sedikit dibanding bahasa Inggris, dan istilah teknis lokal sering disalahartikan.
2. **Dari dokumen rujukan Anda.** Kalau delapan dokumen Anda semuanya dari satu instansi, sistem Anda hanya mewakili sudut pandang instansi itu — dan menyampaikannya seolah-olah fakta netral.
3. **Dari rancangan Anda.** Kategori yang Anda tetapkan di schema output menentukan apa yang **tidak bisa** dinyatakan sistem. Setiap kategori yang tidak Anda sediakan berarti ada kasus yang akan dipaksa masuk ke kategori lain.

Jalan ketiga paling sering terlewat karena terasa seperti keputusan teknis biasa. Padahal bukan.

### Empat pertanyaan etis yang wajib terjawab

1. **Siapa yang dirugikan kalau sistem ini salah?** Bukan "apakah bisa salah" — pasti bisa. Pertanyaannya: siapa yang menanggung akibatnya.
2. **Apakah pengguna tahu bahwa ia sedang memakai sistem AI?** Dan apakah ia tahu jawabannya bisa salah?
3. **Data siapa yang diproses, dan apakah pemiliknya tahu?**
4. **Untuk apa sistem ini tidak boleh dipakai?** Batas yang Anda tetapkan sendiri, tertulis.

Jawaban pertanyaan keempat menjadi pernyataan etis Anda. Sistem yang tidak menyebutkan batas penggunaannya akan dipakai di luar tujuannya — dan tanggung jawabnya kembali ke pembuatnya.

### Tanggung jawab profesional

Anda memakai AI untuk membangun produk. Itu boleh, bahkan dianjurkan. Tapi tanggung jawabnya tetap di tangan Anda. Kalau sistem Anda memberi rekomendasi salah yang merugikan seseorang, "modelnya yang salah" bukan jawaban profesional — sama seperti seorang insinyur tidak dapat menyalahkan kalkulatornya.

---

## 15.2 Skenario Minggu 15

**Kriteria sukses:**

- [ ] Kajian risiko keamanan: lima risiko di tabel 15.1 dicek untuk produk Anda
- [ ] Kajian bias: ketiga jalan masuk bias dicek, dengan **contoh konkret** dari produk Anda, bukan pernyataan umum
- [ ] Empat pertanyaan etis terjawab
- [ ] Pernyataan etis tertulis: untuk apa sistem ini tidak boleh dipakai
- [ ] Pemberitahuan kepada pengguna: bagaimana sistem menyatakan dirinya AI dan bahwa jawabannya bisa salah
- [ ] Daftar risiko yang **sengaja diterima tanpa diatasi**, beserta alasannya

Butir terakhir butuh kejujuran. Setiap sistem pasti punya risiko yang diterima begitu saja; menyembunyikannya lebih buruk daripada mengakuinya.

---

## 15.3 READ → BREAK → FIX → BUILD

### READ — Melacak alur data (20 menit, tanpa AI)

| Pertanyaan | Jawaban untuk produk Anda |
|---|---|
| Data apa yang masuk ke sistem? | |
| Data apa yang dikirim ke penyedia model? | |
| Data apa yang disimpan, di mana, berapa lama? | |
| Siapa pemilik data itu, dan apakah ia tahu? | |
| Kalau sistem ini berhenti dipakai, data itu jadi apa? | |
| Data apa yang **seharusnya tidak pernah** masuk? | |

Lalu cek: apakah ada mekanisme yang **mencegah** data di baris terakhir masuk, atau Anda hanya berharap itu tidak terjadi?

### BREAK — Enam percobaan (25 menit)

| # | Percobaan | Prediksi Anda | Hasil sebenarnya |
|---|---|---|---|
| 1 | Ajukan pertanyaan yang sama dalam bahasa Indonesia dan Inggris; bandingkan kualitas jawabannya | | |
| 2 | Ajukan pertanyaan memakai istilah lokal atau daerah pada bidang Anda | | |
| 3 | Ajukan kasus yang **tidak cocok** ke satu pun kategori schema Anda | | |
| 4 | Minta sistem melakukan sesuatu yang terdengar wajar tapi di luar tujuannya | | |
| 5 | Masukkan data yang seharusnya tidak boleh masuk; lihat apakah ada yang mencegah | | |
| 6 | Periksa riwayat repositori Anda: adakah kredensial yang pernah terunggah | | |

Nomor 3 menguji bias dari rancangan. Catat ke kategori mana kasus itu dipaksa masuk, dan siapa yang dirugikan kalau itu terjadi berulang kali.

Nomor 6 bukan latihan. Kalau ditemukan, cabut (revoke) API key itu hari ini juga dan laporkan tindakan Anda di catatan proses.

### FIX — Pernyataan etis yang kosong (20 menit)

```
PERNYATAAN ETIS

Sistem ini dikembangkan dengan memperhatikan prinsip etika AI.
Kami berkomitmen pada transparansi, keadilan, dan akuntabilitas.
Sistem ini tidak dimaksudkan untuk menggantikan penilaian manusia.
Data pengguna dijaga kerahasiaannya.
```

1. Jelaskan kenapa keempat kalimat itu tidak bisa dicek benar-salahnya.
2. Tulis ulang masing-masing menjadi pernyataan yang **bisa dicek** oleh orang lain.
3. Sebutkan satu hal penting yang sama sekali tidak disebut dalam pernyataan itu.

### BUILD — Kajian risiko dan pernyataan etis (mandiri)

Susun `kajian-risiko.md` yang memenuhi semua kriteria sukses bagian 15.2. Tulis pernyataan etis sebagai bagian terpisah yang bisa dibaca sendiri, karena akan ditampilkan saat UAS.

**Tantangan wajib.** Tulis satu paragraf berjudul *"Kapan produk saya tidak boleh dipercaya"*, ditujukan ke calon pengguna, dengan bahasa yang dipahami orang awam. Paragraf ini dinilai dari kejujurannya, bukan dari seberapa bagus kesan yang ditimbulkannya. Kalau paragraf Anda menyimpulkan produk Anda hampir selalu bisa dipercaya, klaim itu akan diuji langsung saat UAS dengan kasus dari set uji Anda sendiri.

---

## 15.4 Daftar Periksa Mandiri — Minggu 15

- [ ] Tabel alur data lengkap enam baris, termasuk mekanisme pencegahnya
- [ ] Enam percobaan BREAK dengan prediksi lebih dulu
- [ ] Nomor 6 benar-benar dijalankan pada repositori Anda
- [ ] Kajian bias memuat contoh konkret dari produk sendiri
- [ ] Pernyataan etis bisa dicek oleh orang lain
- [ ] Daftar risiko yang diterima tanpa diatasi tertulis beserta alasannya
- [ ] **Luaran Blok E** dikumpulkan (komponen Proyek, 15%)

---
---

# MINGGU 16 — UJIAN AKHIR SEMESTER
## Demonstrasi Produk, Portofolio, dan Tanya Jawab

**Sub-CPMK 4–6 · Bobot 10% UAS + penilaian akhir komponen Proyek**

---

## 16.1 Bentuk ujian

| Unsur | Ketentuan |
|---|---|
| Demonstrasi langsung | **6 menit** — sistem dijalankan, bukan direkam |
| Pemaparan evaluasi dan risiko | **5 menit** |
| Tanya jawab | **9 menit** |
| Portofolio | Dikumpulkan **H-2 pukul 23.59**. Terlambat = tidak bisa tampil |
| Kasus demo | **Dua kasus dipilih dosen** dari set uji Anda sendiri, diberitahukan saat itu juga |

Ketentuan terakhir adalah inti UAS ini. Anda tidak memilih kasus yang didemokan; dosen memilih dari set uji **yang Anda susun sendiri** — termasuk kemungkinan kasus yang menurut laporan Anda memang gagal.

Kalau sistem gagal pada kasus yang di laporan Anda **sudah disebut** gagal, nilai Anda tidak berkurang. Kalau sistem gagal pada kasus yang Anda klaim berhasil, nilainya berkurang banyak — dan yang dinilai kurang bukan aspek teknis, tapi aspek kejujuran.

---

## 16.2 Isi portofolio

Satu file terkompresi `<NIM>-portofolio.zip`:

| File | Isi |
|---|---|
| `README.md` | Persoalan, siapa penggunanya, cara menjalankan, batas penggunaan |
| `rancangan-sistem.md` | Rancangan akhir; setiap keputusan disertai alasan |
| File produk | Semua file kerja |
| `instruksi/` | Semua versi prompt beserta `CATATAN.md` |
| `set-uji/` | Set uji lengkap dengan jawaban acuan dan kriteria |
| `laporan-evaluasi.md` | Angka, kalibrasi, variance, perbandingan baseline, biaya |
| `kajian-risiko.md` | Risiko, bias, pernyataan etis, risiko yang diterima |
| `guardrails.md` | Batas akses, titik persetujuan, hasil uji serangan, celah yang diketahui |
| `catatan-pemakaian.md` | Catatan biaya sejak Minggu 3 |
| `catatan-proses/` | Seluruh catatan proses mingguan |
| `refleksi.md` | Maksimal 1 halaman; ketentuan di bagian 16.4 |

Portofolio yang tidak lengkap tetap boleh tampil, tapi file yang tidak ada tidak bisa dinilai. Ini perlu ditekankan karena sering terlewat: komponen Proyek bernilai 30%, tiga kali lipat bobot sesi UAS-nya sendiri — jadi cek daftar ini sekali lagi sebelum mengunggah.

---

## 16.3 Pertanyaan saat tanya jawab

Seluruh pertanyaan diambil dari [lampiran/E-bank-pertanyaan-pertanggungjawaban.md](lampiran/E-bank-pertanyaan-pertanggungjawaban.md), bagian UAS. Empat berikut diajukan kepada setiap peserta:

1. Tunjukkan satu bagian sistem Anda dan jelaskan mengapa ia dirancang begitu, serta apa alternatif yang Anda tolak.
2. Sebutkan satu klaim pada laporan evaluasi Anda dan tunjukkan buktinya sekarang juga.
3. Sebutkan celah keamanan yang Anda tahu masih ada, dan kenapa Anda membiarkannya.
4. Bagian mana dari karya ini yang tidak bisa Anda jelaskan sepenuhnya?

Pertanyaan keempat bukan jebakan, tapi jawaban "tidak ada" juga tidak otomatis dapat nilai penuh — jawaban itu akan diuji dengan pertanyaan lanjutan. Menunjuk satu bagian dengan jujur, lalu menjelaskan apa yang Anda pahami dan yang belum, bernilai lebih tinggi daripada mengaku paham semuanya tapi goyah di pertanyaan kedua.

---

## 16.4 Refleksi (bagian dari komponen Sikap dan Profesionalisme)

Maksimal satu halaman, menjawab empat hal:

1. Keputusan rancangan apa yang paling Anda sesali, dan apa yang akan Anda lakukan berbeda?
2. Kesalahan apa yang Anda buat sepanjang semester yang tidak tertangkap oleh siapa pun kecuali Anda sendiri?
3. Bagaimana AI membantu Anda, dan di titik mana ia menyesatkan Anda?
4. Kalau produk Anda dipakai orang sungguhan mulai besok, apa yang paling membuat Anda khawatir?

Pertanyaan kedua dinilai dari kejujurannya, bukan dari seberapa kecil kesalahan yang Anda akui. Enam belas minggu membangun sesuatu pasti menyisakan setidaknya satu kesalahan yang hanya Anda yang tahu — bisa menemukan dan menyebutkannya justru bukti bahwa Anda mengawasi kerja sendiri.

---

## 16.5 Rubrik UAS dan Produk Akhir

**UAS (10%)**

| Aspek | Bobot | Sangat Baik | Cukup | Kurang |
|---|:--:|---|---|---|
| Demonstrasi berjalan | 25% | Kedua kasus berjalan sesuai yang dilaporkan | Satu kasus menyimpang dari laporan | Sistem tidak berjalan |
| Pemaparan evaluasi | 25% | Angka jelas, keterbatasannya disebutkan | Angka ada, keterbatasan tidak disebut | Hanya kesan, bukan angka |
| Tanya jawab | 35% | Menjawab mendalam, mengakui batas pengetahuannya | Sebagian tidak terjawab | Tidak bisa menjelaskan karyanya |
| Ketaatan format | 15% | Tepat waktu, portofolio lengkap | Sedikit melebihi | Melebihi waktu, portofolio tidak lengkap |

**Produk Akhir (30%)** — mengikuti rubrik pada README mata kuliah:

| Aspek | Bobot |
|---|:--:|
| Ketepatan rumusan masalah | 20% |
| Kualitas rancangan sistem | 25% |
| Keandalan dan evaluasi | 25% |
| Kesadaran risiko dan etika | 15% |
| Komunikasi dan kemampuan menjelaskan karya | 15% |

---

## 16.6 Catatan penutup

Anda tidak diminta menjadi ahli AI dalam satu semester. Yang diminta lebih sederhana, tapi lebih berguna: melihat persoalan di bidang Anda sendiri, menilai apakah AI memang solusinya, lalu merancang dan **membuktikan** solusi itu.

Ukurannya bukan seberapa keren produk Anda saat demo. Ukurannya adalah: ketika ada yang bertanya "dari mana Anda tahu ini berhasil?", Anda bisa menjawab dengan bukti.
