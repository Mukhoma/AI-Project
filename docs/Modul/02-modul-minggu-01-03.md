# MODUL — MINGGU 1–3
## Blok A · Fondasi: Memahami Mesinnya

**Kapita Selekta: AI Engineering | Sub-CPMK-1 | CPMK-1**

> **Cara memakai modul ini.** Setiap minggu punya empat bagian: **Konsep** (dibaca sebelum kelas), **Prompt Pack** (alat bantu AI untuk minggu itu), **READ → BREAK → FIX → BUILD** (dikerjakan di kelas dan dilanjutkan mandiri), dan **Daftar Periksa** (Anda verifikasi sendiri; tidak ada asisten yang memeriksanya untuk Anda).
>
> Tatap muka hanya 100 menit. Bagian Konsep **tidak** dibacakan ulang di kelas.

---

## Tentang Minggu 1–3: belum ada produk, dan itu disengaja

Tiga minggu pertama tidak menghasilkan produk apa pun. Yang dihasilkan adalah kemampuan menjawab satu pertanyaan yang akan terus muncul sepanjang semester: **kapan model bahasa besar (LLM) memang solusi yang tepat, dan kapan justru alat yang salah.**

Tanpa jawaban itu, bisa jadi Anda membangun sesuatu yang kelihatannya jalan sepanjang semester, lalu gagal saat dievaluasi di Minggu 14 — dan Anda tidak tahu kenapa. Tiga minggu ini untuk mencegah hal itu.

Contoh angka di modul ini memakai **K = 7**. Kode peserta Anda berbeda.

---
---

# MINGGU 1 — Lanskap: AI Engineering Bukan Machine Learning

**Sub-CPMK-1** · Menjelaskan gambaran umum AI generatif dan cara kerja model bahasa besar **(C2)**
**Target akhir minggu:** Anda dapat menempatkan sebuah persoalan pada peta — apakah ia persoalan AI Engineering, persoalan Machine Learning, persoalan basis data, atau bukan persoalan AI sama sekali.
**Catatan penilaian:** Minggu 1 tidak dinilai. Minggu ini menjadi syarat untuk lanjut, dan di sini Anda menerima kode peserta **K**.

---

## 1.1 Konsep

### Empat disiplin yang sering dikira sama

| Disiplin | Pertanyaan utamanya | Hasil khasnya |
|---|---|---|
| Data Science | Apa yang dikatakan data ini? | Temuan, laporan, visualisasi |
| Machine Learning | Bagaimana membuat model yang belajar dari data ini? | Model terlatih beserta metriknya |
| **AI Engineering** | **Bagaimana merakit sistem andal di atas model yang sudah ada?** | **Produk yang jalan, terukur, dan terkendali** |
| Rekayasa Perangkat Lunak | Bagaimana membangun sistem yang benar dan mudah dirawat? | Perangkat lunak |

AI Engineering mengambil cara menguji dan merancang dari Rekayasa Perangkat Lunak, dan kebiasaan mengukur dari Machine Learning. Tapi ada satu perbedaan mendasar: **komponen utamanya (model) tidak deterministik dan tidak bisa Anda kendalikan.** Anda tidak melatih modelnya. Anda tidak dapat memastikan output-nya sama untuk input yang sama. Yang dapat Anda kendalikan hanyalah apa yang masuk, apa yang keluar, dan apa yang terjadi di sekelilingnya.

Seluruh mata kuliah ini membahas tiga hal yang masih bisa Anda kendalikan itu.

### Pergeseran cara berpikir yang paling sulit

Dalam pemrograman biasa, Anda menulis aturan dan komputer menjalankannya persis. Dalam AI Engineering, Anda menulis *maksud* dan model mengartikannya sendiri — kadang tepat, kadang tidak, dan hasilnya bisa berbeda di percobaan berikutnya.

Akibatnya, dan ini sering dilupakan pemula: **sistem Anda tidak bisa disebut "benar", paling jauh "cukup bisa diandalkan untuk kebutuhan tertentu".** Jadi evaluasi bukan tahap terakhir yang dikerjakan kalau sempat. Tanpa evaluasi, klaim apa pun tentang sistem Anda tidak ada artinya.

### Kapan model bahasa besar justru alat yang salah

Empat tanda bahwa Anda tidak membutuhkannya:

1. **Jawabannya pasti.** Menghitung pajak, memvalidasi format NIM, mengurutkan data. Aturan biasa lebih murah, lebih cepat, dan tidak pernah salah.
2. **Kesalahan tidak dapat ditoleransi sama sekali.** Kalau satu jawaban salah berakibat fatal dan tidak ada manusia yang memeriksa, model bahasa bukan pilihan.
3. **Tidak ada cara memeriksa output-nya.** Kalau tidak ada yang bisa menilai jawabannya benar atau salah, sistem Anda hanya terlihat meyakinkan tanpa bisa dipercaya.
4. **Datanya terlalu kecil dan terstruktur.** Sepuluh baris data tidak butuh retrieval; cukup pakai tabel biasa.

Salah satu keterampilan yang dinilai di kelas ini adalah keberanian mengatakan "persoalan ini tidak butuh AI". Karena itu **ketepatan rumusan masalah berbobot 20%** pada produk akhir (Lampiran H): memilih persoalan yang memang cocok untuk AI sama pentingnya dengan membangunnya dengan baik.

### Peta perjalanan semester

```
   Model apa adanya       →  output bebas, format tidak tetap, bisa mengarang
        │  Blok B: kendali
   Structured output      →  format tetap, bisa memanggil tool
        │  Blok C: grounding
   Jawaban dari dokumen   →  bersumber dari dokumen Anda, sumbernya bisa dicek
        │  Blok D: agentic
   Agent                  →  merencanakan, bertindak bertahap, punya guardrails
        │  Blok E: kematangan
   Produk yang teruji     →  kualitas, biaya, dan risikonya sudah diukur
```

---

## 1.2 Prompt Pack — Minggu 1

### A. Prompt Pemetaan Persoalan

```
Saya mahasiswa <PRODI ANDA> semester 5. Saya sedang mencari persoalan
nyata di bidang saya yang layak diselesaikan dengan AI generatif.

Ajukan kepada saya 8 pertanyaan, satu per satu, untuk menggali persoalan
yang benar-benar saya alami — bukan persoalan hipotetis.

Aturan:
- Jangan menyarankan ide sebelum 8 pertanyaan itu selesai.
- Jangan menerima jawaban umum; kalau saya menjawab kabur, gali lebih dalam.
- Setelah selesai, sebutkan 3 persoalan dari jawaban saya, dan untuk
  MASING-MASING sebutkan satu alasan mengapa AI generatif MUNGKIN BUKAN
  jawaban yang tepat.
```

### B. Prompt Uji Klaim

```
Berikut klaim yang saya dengar tentang model bahasa besar:
"<TEMPEL KLAIM YANG ANDA DENGAR>"

1. Nyatakan klaim ini akurat, setengah benar, atau keliru.
2. Jelaskan bagian mana yang benar dan bagian mana yang menyesatkan.
3. Sebutkan apa yang harus saya amati sendiri untuk membuktikannya,
   bukan sekadar mempercayai jawabanmu.
```

### C. Prompt Terlarang

Jangan menempelkan dokumen internal organisasi, data pribadi orang lain, atau data penelitian pihak lain yang belum dipublikasikan ke layanan AI mana pun — termasuk saat "hanya mencoba".

---

## 1.3 READ → BREAK → FIX → BUILD

### READ — Tiga persoalan, pilih disiplinnya (25 menit, tanpa AI)

Ambil tiga persoalan berikut. Untuk masing-masing, tentukan disiplin mana yang sebenarnya dibutuhkan, lalu tuliskan alasannya dalam satu kalimat.

| # | Persoalan | Disiplin yang tepat | Alasan |
|---|---|---|---|
| 1 | Menghitung sisa kuota SKS mahasiswa dari transkrip | | |
| 2 | Memperkirakan jumlah pengunjung pelabuhan bulan depan dari data 5 tahun | | |
| 3 | Meringkas 40 laporan survei lapangan menjadi tabel temuan berformat tetap | | |

Kemudian jawab: **persoalan nomor berapa yang berubah jawabannya kalau jumlah datanya menjadi 40.000, bukan 40?** Jelaskan.

### BREAK — Pertanyaan yang sama, jawaban yang berbeda (25 menit)

> **Alat untuk percobaan ini.** Pakai antarmuka chat mana pun yang Anda punya — kredensial model gateway kelas baru dibutuhkan Minggu 3, jadi jangan menunggu. Catat **model apa dan tanggal berapa** Anda mencobanya di catatan proses: jawaban model berubah antar versi, dan tanpa catatan itu hasil Anda tidak bisa dicek ulang. Hasil Anda **tidak harus sama** dengan hasil teman — yang diamati polanya, bukan angkanya.

Isi kolom prediksi **sebelum** mencoba.

| # | Percobaan | Prediksi Anda | Hasil sebenarnya |
|---|---|---|---|
| 1 | Ajukan satu pertanyaan faktual sempit tentang bidang Anda ke model, tiga kali, di percakapan **baru** tiap kali | | |
| 2 | Ajukan pertanyaan tentang peristiwa yang terjadi bulan lalu | | |
| 3 | Ajukan pertanyaan tentang dokumen internal kampus Anda yang tidak pernah dipublikasikan | | |
| 4 | Tanya hal yang jawabannya tidak ada, misalnya biografi tokoh yang Anda karang namanya | | |

Nomor 3 dan 4 hasilnya mirip, tapi penyebabnya berbeda. Jelaskan bedanya: pada nomor mana model **tidak tahu bahwa ia tidak tahu**?

### FIX — Tidak ada pada minggu ini

Tahap FIX dimulai Minggu 4, setelah Anda punya cukup bekal untuk mengenali masalahnya.

### BUILD — Peta persoalan pribadi (mandiri)

1. Catat kode peserta **K** Anda. Hitung seluruh angka minimum lingkup Anda menurut Lampiran B. Tuliskan di catatan proses.
2. Tuliskan **tiga** calon persoalan dari bidang keilmuan Anda. Untuk masing-masing isi:

| Unsur | Isi |
|---|---|
| Siapa yang mengalaminya | |
| Bagaimana persoalan itu diselesaikan sekarang | |
| Mengapa cara sekarang belum cukup | |
| Apa yang menjadi bukti bahwa sistem berhasil | |
| Sumber dokumen apa yang Anda miliki dan sah dipakai | |
| Satu alasan mengapa AI **mungkin bukan** jawabannya | |

3. Urutkan ketiganya, lalu sebutkan mana yang paling mungkin Anda kerjakan sampai Minggu 16, beserta alasannya.

**Tantangan wajib.** Temukan satu contoh nyata di kampus atau bidang Anda tempat AI generatif **sedang dipakai untuk persoalan yang salah**. Jelaskan mengapa ia salah dan apa yang seharusnya dipakai.

---

## 1.4 Daftar Periksa Mandiri — Minggu 1

- [ ] Kode peserta K dicatat dan seluruh angka lingkup dihitung
- [ ] Tabel READ terisi lengkap dengan alasan
- [ ] Empat baris BREAK punya kolom prediksi terisi **sebelum** percobaan
- [ ] Tiga calon persoalan terisi lengkap enam unsur
- [ ] Tantangan wajib terjawab
- [ ] Catatan proses ditulis memakai template Lampiran C

---
---

# MINGGU 2 — Anatomi: Token, Context Window, Temperature, dan Hallucination

**Sub-CPMK-1** · **(C2, C4)**
**Target akhir minggu:** Anda dapat memperkirakan biaya dan batas sebuah pemanggilan model sebelum menjalankannya, dan menjelaskan bahwa hallucination adalah sifat bawaan model, bukan bug yang bisa diperbaiki sekali jalan.

---

## 2.1 Konsep

### Apa yang sebenarnya dilakukan model bahasa besar

Satu kalimat yang perlu Anda ingat sepanjang semester:

> Model bahasa besar memperkirakan potongan teks berikutnya yang paling mungkin, satu potongan demi satu potongan, berdasarkan semua teks yang sudah ada sebelumnya.

Ia tidak mencari jawaban di basis data. Ia tidak memeriksa kebenaran. Ia tidak "tahu" apa pun dalam arti manusia. Kalimat yang benar dan kalimat yang salah dihasilkan lewat proses yang **persis sama**.

Karena itu, dua hal berikut bukan kontradiksi: model bisa menulis paragraf yang sangat tepat, lalu di kalimat berikutnya mengarang nomor peraturan yang tidak pernah ada. Keduanya berasal dari mekanisme yang sama.

### Token: satuan yang menentukan biaya dan batas

Model tidak melihat huruf atau kata; ia melihat **token**, yaitu potongan teks. Perkiraan kasar untuk teks Indonesia: **satu token ≈ 3 sampai 4 huruf**, jadi satu halaman A4 padat kira-kira 700–900 token.

Yang perlu Anda hitung sendiri, bukan Anda kira-kira:

```
Biaya satu pemanggilan
  = (token input  × tarif input)
  + (token output × tarif output)

Tarif output biasanya BEBERAPA KALI LIPAT tarif input.
```

Artinya: memasukkan dokumen 50 halaman ke setiap pemanggilan bukan cuma lambat, tapi juga mahal — dan biayanya berlipat untuk setiap pengguna. Inilah alasan Blok C ada.

### Context window bukan ingatan

Context window adalah jumlah token maksimum yang dapat dilihat model **dalam satu pemanggilan**. Ia bukan ingatan. Model tidak mengingat percakapan sebelumnya; yang terjadi adalah seluruh percakapan dikirim ulang setiap kali. Itu sebabnya percakapan panjang makin lambat dan makin mahal.

Dua masalah yang akan sering Anda temui:

- **Lost in the middle.** Informasi di tengah teks yang panjang lebih sering terlewat dibanding yang di awal atau akhir.
- **Instruksi makin diabaikan.** System prompt yang bagus di awal percakapan makin sering diabaikan setelah puluhan kali tanya-jawab.

### Temperature: mengatur seberapa "berani" model

Temperature mengatur seberapa sering model boleh memilih kata yang bukan pilihan paling mungkin.

| Temperature | Perilaku | Cocok untuk |
|---|---|---|
| Rendah (0–0,3) | Konsisten, dapat ditebak, cenderung membosankan | Ekstraksi data, klasifikasi, output berformat |
| Sedang (0,4–0,7) | Seimbang | Penjelasan, ringkasan |
| Tinggi (0,8+) | Beragam, kadang ngawur | Brainstorming, variasi bahasa |

Salah kaprah yang paling sering: mengira temperature 0 berarti output **selalu** sama persis. Ia hanya membuat output jauh lebih stabil, bukan dijamin sama.

### Hallucination adalah sifat bawaan

Model dilatih untuk menghasilkan lanjutan teks yang **masuk akal**, bukan yang **benar**. Kalau model tidak punya informasi yang cukup, jawaban yang masuk akal belum tentu benar — dan yang keluar tetap yang masuk akal.

Karena itu hallucination tidak bisa dihilangkan. Yang bisa dilakukan: **mengurangi kemungkinannya** (dengan grounding di Blok C), **membuatnya mudah terdeteksi** (dengan structured output di Blok B), dan **membatasi dampaknya** (dengan guardrails di Blok D). Tiga strategi itulah inti sisa semester ini.

---

## 2.2 Prompt Pack — Minggu 2

### A. Prompt Mengamati Jawaban Model

```
Saya sedang mempelajari perilaku model bahasa besar.

Jawab pertanyaan berikut, lalu di akhir jawaban tambahkan bagian
"TINGKAT KEYAKINAN" berisi: seberapa yakin kamu, bagian mana dari
jawabanmu yang paling mungkin keliru, dan apa yang harus saya
periksa secara mandiri.

Pertanyaan: <PERTANYAAN SEMPIT DARI BIDANG ANDA>
```

### B. Prompt Membandingkan Temperature

```
Saya akan mengirim prompt yang sama beberapa kali dengan pengaturan
berbeda. Bantu saya merancang satu prompt UJI yang perbedaan
output-nya akan TERLIHAT JELAS ketika temperature diubah dari 0 ke 1.

Berikan juga satu prompt uji yang output-nya SEHARUSNYA nyaris
tidak berubah meskipun temperature diubah, dan jelaskan mengapa.
```

### C. Prompt Hitung Biaya

```
Bantu saya menghitung biaya. Konteks:
- Panjang system prompt saya: <N> kata
- Panjang input pengguna khas: <N> kata
- Panjang output khas: <N> kata
- Tarif model: input <X> dan output <Y> per juta token

1. Perkirakan jumlah token tiap bagian (teks Indonesia).
2. Hitung biaya satu pemanggilan.
3. Hitung biaya 100 pengguna × 20 pemanggilan per bulan.
4. Sebutkan bagian mana yang paling menyumbang biaya, dan
   dua cara menurunkannya tanpa mengorbankan kualitas.
Tunjukkan perhitungannya, jangan hanya hasil akhirnya.
```

---

## 2.3 READ → BREAK → FIX → BUILD

### READ — Membaca output dengan kritis (25 menit, tanpa AI)

Ambil satu jawaban model tentang bidang Anda yang panjangnya kira-kira satu paragraf. Uraikan dengan tabel berikut:

| Pernyataan dalam jawaban | Dapat saya verifikasi? | Sumbernya apa? | Benar / salah / tidak bisa dicek |
|---|---|---|---|
| | | | |

Isi sedikitnya lima baris. Lalu jawab: berapa persen pernyataan yang **tidak dapat Anda periksa sama sekali**? Apa artinya angka itu bagi rencana produk Anda?

### BREAK — Enam percobaan (30 menit)

> **Alat untuk percobaan ini.** Percobaan 1 dan 2 butuh **pengaturan temperature**, yang tidak ada di aplikasi chat biasa — pakai konsol atau *playground* penyedia model; versi gratisnya sudah cukup. Percobaan 3–6 boleh di antarmuka mana pun. Kredensial model gateway kelas baru dibutuhkan Minggu 3, jadi jangan menunggu. Catat **model, temperature, dan tanggal** tiap percobaan di catatan proses: tanpa itu hasil Anda tidak bisa dicek ulang, dan laporan pengamatan minggu ini (Tugas 5%) tidak bisa dinilai. Hasil Anda **tidak harus sama** dengan hasil teman — yang diamati polanya, bukan angkanya.

Isi prediksi lebih dulu. Catat output apa adanya, termasuk yang memalukan.

| # | Percobaan | Prediksi Anda | Hasil sebenarnya |
|---|---|---|---|
| 1 | Prompt sama, temperature 0, dijalankan 3 kali | | |
| 2 | Prompt sama, temperature 1, dijalankan 3 kali | | |
| 3 | Minta jawaban ≤50 kata, lalu minta hal yang sama ≤500 kata | | |
| 4 | Tanyakan nomor peraturan/pasal spesifik di bidang Anda, lalu minta model menyebutkan sumbernya | | |
| 5 | Ulangi nomor 4, tetapi tambahkan kalimat: "Jika tidak yakin, jawab TIDAK TAHU" | | |
| 6 | Beri teks 3 halaman, sisipkan satu kalimat aneh di **tengah**, lalu tanyakan isi kalimat itu | | |

Nomor 4 dan 5 adalah inti minggu ini: apakah satu kalimat instruksi mengubah perilaku, dan apakah perubahannya dapat diandalkan? Ulangi nomor 5 sebanyak lima kali dan catat berapa kali ia benar-benar menjawab TIDAK TAHU.

Nomor 6 menguji "lost in the middle". Ulangi dengan kalimat aneh diletakkan di akhir teks dan bandingkan.

### FIX — Tidak ada pada minggu ini

### BUILD — Anggaran dan batas (mandiri)

1. Pilih satu dari tiga calon persoalan Minggu 1 sebagai calon terkuat.
2. Perkirakan untuk persoalan itu: panjang input khas, panjang output khas, jumlah pemanggilan per tugas.
3. Hitung biaya per pemanggilan, per pengguna per bulan, dan untuk 100 pengguna. **Tunjukkan perhitungannya.**
4. Tentukan batas anggaran pribadi Anda untuk semester ini dan tuliskan berapa pemanggilan yang berarti.

**Tantangan wajib.** Rancang satu prompt yang membuat model **mengakui ketidaktahuannya secara konsisten** pada lima pertanyaan yang jawabannya memang tidak ada. Laporkan berapa dari lima yang berhasil, dan prompt versi berapa yang akhirnya bekerja. Kalau tidak ada yang mencapai lima dari lima, laporkan saja — itu bukan kegagalan, itu temuan.

---

## 2.4 Daftar Periksa Mandiri — Minggu 2

- [ ] Tabel uraian jawaban terisi ≥5 baris
- [ ] Enam percobaan BREAK dijalankan dengan prediksi terisi lebih dulu
- [ ] Nomor 5 diulang lima kali dan hasilnya dihitung
- [ ] Perhitungan biaya ditampilkan langkahnya, bukan hanya hasil
- [ ] Tantangan wajib dilaporkan apa adanya, termasuk kalau gagal
- [ ] **Laporan pengamatan perilaku model** dikumpulkan (komponen Tugas, 5%)

---
---

# MINGGU 3 — Lingkungan Kerja dan Model Gateway

**Sub-CPMK-1** · **(C3)**
**Target akhir minggu:** Anda berhasil memanggil model dari lingkungan kerja Anda sendiri, membandingkan sedikitnya dua model pada tugas yang sama, dan menyimpan bukti keduanya.
**Catatan penilaian:** **Kuis 1** di awal pertemuan, 15 menit, materi Minggu 1–2. Kisi-kisi ada di bagian 3.5.

---

## 3.1 Konsep

### Mengapa memakai model gateway, bukan satu penyedia

Kalau produk Anda terhubung langsung ke satu penyedia, Anda terikat padanya: satu kredensial, satu format, satu tarif. Pindah ke model lain yang lebih bagus atau lebih murah jadi repot.

**Model gateway** adalah layanan perantara: satu kredensial, satu format pemanggilan, tapi bisa mengakses banyak model. Manfaatnya bukan sekadar praktis:

| Manfaat | Mengapa penting bagi kelas ini |
|---|---|
| Satu kredensial | Anda tidak perlu mendaftar ke lima layanan |
| Ganti model tanpa mengubah rancangan | Blok E menuntut Anda membandingkan model murah dan mahal |
| Batas anggaran terpusat | Anda tidak dapat menghabiskan uang tanpa sadar |
| Catatan pemakaian | Data biaya Anda di Minggu 14 datang dari sini |

### Memilih model: tiga pertimbangan, bukan satu peringkat

Tidak ada "model terbaik". Ada model yang tepat untuk satu tugas dengan satu batas biaya.

```
        kualitas
           ▲
           │   model besar: pintar, mahal, lambat
           │        ●
           │
           │              ● model menengah: sering cukup
           │
           │   ● model kecil: cepat, murah, cocok untuk tugas rutin
           └──────────────────────────────► biaya
                    (sumbu ketiga: latency)
```

Pola yang dipakai di sistem nyata dan akan Anda pakai di Blok E: **membagi tugas ke beberapa model** — tugas rutin (klasifikasi, ekstraksi, penyaringan) ke model kecil; tugas yang butuh penalaran ke model besar. Di sistem yang sudah dipakai sungguhan, sebagian besar pemanggilan termasuk tugas rutin.

### Kredensial adalah rahasia

API key sama seperti kata sandi, dan terhubung langsung ke tagihan. Tiga aturan yang tidak bisa ditawar:

1. Kunci **tidak pernah** ditulis langsung di dalam file kode.
2. Kunci **tidak pernah** ikut terunggah ke repositori. Pastikan file rahasia masuk .gitignore.
3. Kunci **tidak pernah** ditempelkan ke percakapan AI, termasuk saat meminta bantuan memperbaiki error.

Butir 3 adalah yang paling sering dilanggar di kelas berbasis AI-assisted development. Sebelum menempel pesan error, tutupi kuncinya.

---

## 3.2 Prompt Pack — Minggu 3

### A. Prompt Panduan Instalasi

```
Saya mahasiswa TANPA latar belakang pemrograman. Sistem operasi saya
<Windows/macOS/Linux>. Saya ingin melakukan pemanggilan pertama ke
sebuah model bahasa melalui model gateway <NAMA LAYANAN>.

Aturan menjawab:
- Beri langkah SATU per SATU. Setelah tiap langkah, berhenti dan
  tanyakan apakah langkah itu berhasil sebelum lanjut.
- Jelaskan APA yang dilakukan tiap perintah, bukan hanya menyuruh saya
  menyalinnya.
- Jangan pernah meminta saya menempelkan API key ke percakapan ini.
- Tunjukkan cara menyimpan kunci di luar file kode.
```

### B. Prompt Pembaca Error

```
Saya menemui pesan error berikut. API key SUDAH saya sensor.

<TEMPEL PESAN ERROR>

Jangan langsung memberi perbaikan.
1. Terjemahkan pesan ini ke bahasa manusia: apa yang gagal, di lapisan mana.
2. Sebutkan 3 penyebab paling mungkin, urut dari yang paling sering.
3. Untuk tiap penyebab, sebutkan satu pemeriksaan yang bisa MEMBANTAHNYA.
4. Tanyakan hasil pemeriksaan mana yang ingin kamu lihat lebih dulu.
```

### C. Prompt Pembanding Model

```
Saya akan menjalankan prompt yang sama pada beberapa model untuk
membandingkannya.

Bantu saya menyusun protokol perbandingan yang JUJUR:
- Apa yang harus dibuat sama persis antar-model agar perbandingannya adil
- Berapa kali tiap prompt harus diulang, dan mengapa satu kali tidak cukup
- Kriteria penilaian yang bisa saya terapkan konsisten
- Tabel pencatatan hasil yang mencakup biaya dan latensi, bukan hanya kualitas
```

---

## 3.3 READ → BREAK → FIX → BUILD

### READ — Memahami satu pemanggilan model (20 menit, tanpa AI)

Panduan penyiapan lengkap ada di [lampiran/F-panduan-tool.md](lampiran/F-panduan-tool.md). Setelah pemanggilan pertama Anda berhasil, jangan langsung lanjut. Uraikan dulu bagian-bagiannya:

| Bagian pemanggilan | Isinya pada percobaan Anda | Fungsinya |
|---|---|---|
| Model yang dipilih | | |
| Peran "system" | | |
| Peran "user" | | |
| Temperature | | |
| Batas token output | | |
| Token input terpakai | | |
| Token output terpakai | | |
| Waktu respons (latency) | | |

Lalu jawab: kalau Anda menghapus bagian "system", apa yang Anda **duga** berubah? Jangan dicoba dulu — itu percobaan nomor 1 di tahap berikutnya.

### BREAK — Lima percobaan (25 menit)

| # | Percobaan | Prediksi Anda | Hasil sebenarnya |
|---|---|---|---|
| 1 | Hapus seluruh isi peran "system" | | |
| 2 | Turunkan batas token output menjadi 20 | | |
| 3 | Ganti nama model menjadi nama yang tidak ada | | |
| 4 | Kirim input kosong | | |
| 5 | Jalankan prompt yang sama pada model termurah dan model termahal yang tersedia | | |

Untuk nomor 2, perhatikan **bagaimana** output berakhir. Apakah ia meringkas, atau terpotong di tengah kalimat? Apa artinya itu bagi produk yang output-nya harus berformat tetap?

Untuk nomor 5, catat tiga angka untuk masing-masing model: biaya, waktu respons, dan penilaian kualitas Anda sendiri dalam skala 1–5 beserta alasannya.

### FIX — Tidak ada pada minggu ini

### BUILD — Lingkungan kerja dan catatan pemakaian (mandiri)

1. Simpan file pemanggilan pertama Anda yang berjalan sebagai titik awal produk.
2. Pastikan API key tersimpan di luar file kode dan tidak akan ikut terunggah.
3. Buat file `catatan-pemakaian.md` yang akan Anda isi tiap minggu: tanggal, kegiatan, model, perkiraan token, perkiraan biaya. File ini menjadi bahan laporan biaya Minggu 14 — jadi mulai isi sekarang, jangan menunggu Minggu 14.
4. Jalankan satu prompt uji sederhana pada **tiga** model berbeda dan isi tabel perbandingan.

**Tantangan wajib.** Temukan satu tugas dari calon persoalan Anda yang hasil model termurahnya **tidak dapat dibedakan** dari model termahal. Tunjukkan buktinya berupa output keduanya berdampingan, dan hitung berapa penghematannya kalau tugas itu dijalankan seribu kali.

---

## 3.4 Daftar Periksa Mandiri — Minggu 3

- [ ] Pemanggilan model pertama berhasil dan buktinya tersimpan
- [ ] API key berada di luar file kode dan di luar repositori
- [ ] Tabel uraian pemanggilan terisi lengkap
- [ ] Lima percobaan BREAK dijalankan dengan prediksi lebih dulu
- [ ] Perbandingan tiga model terisi biaya, latency, dan kualitas
- [ ] `catatan-pemakaian.md` dibuat dan sudah berisi baris pertama
- [ ] Tantangan wajib disertai bukti berdampingan

---

## 3.5 Kisi-kisi Kuis 1 (Minggu 3, 15 menit)

Kuis bersifat tutup buku, tanpa AI, lima soal uraian singkat. Yang diuji:

1. Membedakan AI Engineering dari Machine Learning pada satu kasus konkret
2. Menghitung perkiraan token dan biaya dari deskripsi tugas
3. Menjelaskan mengapa hallucination tidak bisa dihilangkan, hanya dikelola
4. Menentukan pengaturan temperature yang tepat untuk satu tugas beserta alasannya
5. Menilai apakah sebuah persoalan layak diselesaikan dengan model bahasa besar

Seluruh jawaban dinilai pada **alasannya**, bukan pada kesimpulannya. Kesimpulan benar tanpa alasan bernilai separuh; kesimpulan berbeda dengan alasan kuat bernilai penuh.
