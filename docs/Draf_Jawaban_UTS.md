# Draf Persiapan UTS: Kapita Selekta AI Engineering
**Proyek:** Sistem RAG & Vision AI untuk Ekstraksi Laporan Inspeksi Lapangan

---

## BAGIAN 1: Presentasi Rancangan Sistem (Slide 1–8)

### Slide 1: Persoalan
* **Siapa yang mengalami:** Tim operasional lapangan (petugas survei) dan staf admin *back-office*.
* **Cara diselesaikan saat ini:** Petugas mengirim laporan via chat (teks berantakan atau sekadar foto). Admin secara manual membaca, menerjemahkan konteks (seperti mencari tahu tanggal dari kata "Kamis lalu"), dan menyalinnya ke Excel.
* **Mengapa belum cukup:** Memakan waktu sangat lama, rawan *human error* (salah ketik koordinat atau salah hitung tanggal relatif), dan rentan melanggar SOP pencatatan perusahaan karena admin tidak selalu hafal seluruh aturan SOP terbaru.

### Slide 2: Mengapa AI Generatif
* **Mengapa bukan basis data/formulir:** Memaksa petugas lapangan mengisi formulir panjang di tengah lapangan sangat tidak praktis dan memperlambat pekerjaan.
* **Mengapa bukan aturan biasa (Regex):** Aturan tradisional (kode) tidak memiliki pemahaman semantik untuk mengubah kalimat relatif *"kemarin sore"* menjadi tanggal pasti (`YYYY-MM-DD`), dan tidak mampu mendeskripsikan secara otomatis objek keras yang ada di dalam sebuah foto fisik (*Vision AI*).

### Slide 3: Rancangan Sistem
*(Alur Visual dari Input ke Output)*
1. **Input:** Multi-Foto atau Teks Laporan dimasukkan lewat antarmuka **Streamlit**.
2. **Vision Processing:** **OpenRouter (gpt-4o-mini)** mengubah gambar menjadi narasi teks (mengekstrak *watermark/geotag* & kondisi perangkat).
3. **Retrieval (RAG):** **LlamaIndex** melakukan *Semantic Search* ke dalam **Supabase pgvector** untuk menarik potongan SOP yang relevan.
4. **Extraction:** LLM + SOP diikat oleh **Instructor & Pydantic** untuk menghasilkan JSON berstruktur baku.
5. **Output:** Tampil di UI berupa Tabel, Peta (*Map*), dan siap di-unduh sebagai Excel.

### Slide 4: Kendali Output
* **Schema & Nilai Valid:** Output dikunci dengan **Pydantic**. Contoh: `tanggal_inspeksi` harus `Date`, `kategori_produk` dibatasi dengan *Literal* (opsi pasti), dan `jumlah_stok` wajib *Integer*. 
* **Penanganan Tidak Valid:** Jika LLM melanggar tipe data, *library* **Instructor** secara otomatis melakukan penolakan (*retry*) agar LLM merevisi JSON-nya. Untuk Peta, ada *script Regex parser* berlapis untuk mencegah aplikasi *crash* jika LLM memberikan huruf arah (S/N/E/W).

### Slide 5: Tool
* **Daftar Tool:** Streamlit (Frontend), OpenRouter (LLM API), Instructor (Validasi), Pydantic (Schema), LlamaIndex (Framework RAG), Supabase pgvector (Vector Database).
* **Batas Akses & Persetujuan Manusia:** Sistem menerapkan *Human-in-the-Loop*. Hasil bacaan foto dari Vision AI dipaparkan di teks area terlebih dahulu agar dapat diedit/disetujui manusia, sebelum tombol ekstraksi RAG akhir ditekan.

### Slide 6: Grounding
* **Dokumen rujukan & Retrieval:** Dokumen SOP (misal: Aturan Inspeksi Jaringan) di-*chunking*, disimpan ke pgvector, lalu di-*retrieve* 3 potongan paling relevan (*Top-K=3*).
* **Jika jawaban tidak ditemukan:** Sistem tidak *crash*, melainkan memberi peringatan *"Tidak ada aturan SOP spesifik yang ditarik"*, dan LLM akan tetap mengekstrak informasi dasar (tanpa panduan khusus SOP).

### Slide 7: Bukti Sejauh Ini
* **Satu Keberhasilan:** Berhasil menyelesaikan "Halusinasi Tanggal Relatif". Dengan menginjeksi Referensi Kalender 14-hari ke dalam *prompt* dan memaksa LLM melakukan langkah *Chain-of-Thought* (CoT) di field pertama JSON, akurasi penentuan tanggal menjadi 100%.
* **Satu Kegagalan:** Ekstraksi LLM terkadang membalik urutan koordinat Latitude & Longitude atau memberikan format nyeleneh. Kegagalan ini ditemukan saat peta Streamlit *error*, dan akhirnya diselesaikan melalui *Regex Parser* manual.

### Slide 8: Risiko dan Rencana
* **Risiko terbesar:** Bergantung penuh pada layanan pihak ketiga (OpenRouter/Supabase). Jika internet mati atau *server API down*, sistem gagal berfungsi. Risiko lain adalah foto yang terlampau buram (*low res*) merusak akurasi bacaan *Vision*.
* **Rencana Minggu 9-16:** Membangun *Agentic Workflow* (agen evaluator untuk memverifikasi ganda hasil ekstraksi agen pertama), serta menyimpan ekstraksi sukses langsung ke dalam tabel relasional (SQL) di Supabase.

---

## BAGIAN 2: Mempertahankan Rancangan (Pertanyaan Wajib & Tanya Jawab)

### Pertanyaan Wajib (Pasti Ditanyakan)

**1. Sebutkan satu keputusan rancangan Anda yang dapat dibuat berbeda, dan jelaskan mengapa Anda memilih yang ini.**
> "Saya *bisa saja* hanya mengandalkan *Prompt Engineering* biasa untuk meminta LLM mengeluarkan format JSON. Namun, saya memutuskan memakai **Instructor + Pydantic**. Saya memilih ini karena jika hanya menggunakan prompt, LLM sering berhalusinasi menyisipkan teks pengantar di luar format JSON. Dengan Instructor, format dikontrol ketat di level API (*Function Calling*), dan ada mekanisme *auto-retry* jika AI salah memberikan tipe data."

**2. Tunjukkan satu input yang membuat sistem Anda gagal, dan jelaskan penyebab utamanya.**
> "Sistem gagal jika pengguna memasukkan koordinat dalam format Derajat-Menit-Detik (DMS), misalnya: *'1 derajat 15 menit LS, 116 derajat BT'*. Penyebab utamanya adalah algoritma *Regex Parser* saya di Streamlit terlalu kaku; ia hanya mencari angka dengan format titik desimal (`\d+\.\d+`). Ini membuktikan bahwa kelemahan sistem AI seringkali justru terletak pada kode logika tradisional yang membungkusnya."

**3. Bagian mana dari karya Anda yang dibuat dengan bantuan AI, dan bagaimana Anda memverifikasinya?**
> "Seluruh antarmuka Streamlit, logika perbaikan Regex Peta, dan arsitektur *Multi-photo uploader* dibuat bersama Agentic AI. Saya memverifikasinya dengan teknik *iterative debugging*. Saat AI memberikan kode Regex untuk Peta, peta saya awalnya malah *crash* karena AI lupa bahwa Lintang Selatan (S) bernilai negatif. Saya mengecek *traceback error*-nya, menolak kode awal AI, dan memaksanya merevisi logika hingga Peta menunjuk titik yang akurat di Balikpapan."

---

### Bank Soal Tambahan (Pertanyaan 1 - 40 Lengkap)

#### A. Persoalan dan Kelayakan
**1. Siapa persisnya yang mengalami persoalan yang Anda pilih? Bagaimana Anda tahu?**
> Pekerja operasional lapangan (seperti inspektor jaringan Telkom) dan admin *back-office*. Saya tahu dari kendala nyata di mana teknisi di lapangan lebih suka mengirim foto/chat singkat daripada mengisi formulir kompleks, yang pada akhirnya membebani admin untuk merekapsitulasi data secara manual.

**2. Bagaimana persoalan ini diselesaikan sekarang, dan mengapa cara itu tidak memadai?**
> Saat ini diselesaikan secara manual: admin membaca chat, menerjemahkan konteks (seperti menghitung tanggal dari kata "kemarin"), lalu mengetik ulang ke Excel. Sangat tidak memadai karena lambat, rawan *human error*, dan SOP sering tidak tervalidasi.

**3. Mengapa persoalan ini tidak cukup diselesaikan dengan basis data atau formulir?**
> Memaksa teknisi mengisi *form* panjang (titik koordinat akurat, memilih kategori) di tengah lapangan atau di atas tiang sangat tidak praktis.

**4. Bagian mana dari persoalan Anda yang sebenarnya tidak butuh model bahasa?**
> Visualisasi Peta (Map) dan tombol *export* tabel hasil ke Excel. Itu adalah murni rekayasa *frontend* (Streamlit) biasa.

**5. Kalau anggaran Anda nol rupiah, bagian mana dari produk ini yang tetap dapat berjalan?**
> Jika akses LLM (OpenRouter) habis/berbayar, hanya antarmuka *UI/Dashboard* (Streamlit) yang akan berjalan, namun proses ekstraksi akan *error* dan mati.

**6. Siapa yang dapat memeriksa output produk Anda benar atau salah? Kalau hanya Anda, apa akibatnya bagi evaluasi nanti?**
> Idealnya Supervisor/Admin yang berhadapan langsung dengan operasional. Jika hanya saya, evaluasinya bersifat teknis (*syntactic*), bukan evaluasi bisnis (apakah datanya berguna di lapangan atau tidak).

**7. Apa yang terjadi kalau produk Anda salah, dan siapa yang menanggungnya?**
> Laporan inspeksi akan keliru (misal salah jumlah stok atau koordinat palsu). Yang menanggung adalah pihak operasional (*back-office*) karena laporan akhir ke manajemen jadi cacat.

**8. Sebutkan satu tanda yang akan membuat Anda menyimpulkan tema ini salah dipilih.**
> Jika ternyata para petugas lapangan merasa sangat mudah dan lebih nyaman mengisi form manual *dropdown* di aplikasi yang sudah ada dibandingkan mengirim foto/teks ke asisten AI ini.

#### B. Karakteristik Model
**9. Jelaskan apa yang dilakukan model bahasa besar tanpa memakai kata “berpikir” atau “memahami”.**
> LLM melakukan kalkulasi probabilitas statistik berbobot tinggi untuk memprediksi potongan kata (*token*) selanjutnya secara berurutan, berdasarkan pola distribusi data yang ia pelajari selama masa pelatihan.

**10. Mengapa hallucination tidak bisa dihilangkan? Apa 3 cara mengelolanya, dan mana yang Anda pakai?**
> Karena LLM pada dasarnya mesin penebak probabilistik, bukan mesin pencari basis data pasti. 3 caranya: Grounding (RAG), Memaksa Struktur (JSON/Schema), dan *Chain of Thought* (CoT). Saya **memakai ketiganya** di proyek ini.

**11. Berapa perkiraan token satu permintaan khas pada produk Anda? Tunjukkan cara Anda menghitungnya.**
> Sekitar 1.500-2.000 token. Hitungannya: Input Foto/Vision memakan ~1.000 token. Konteks SOP (dari RAG) + Sistem Prompt + Input teks ~500 token. Output JSON ~100 token.

**12. Temperature berapa yang Anda pakai, dan mengapa bukan yang lebih tinggi atau lebih rendah?**
> *Temperature = 0* (atau sangat rendah). Karena ini adalah tugas ekstraksi data faktual/kaku (*Data Extraction*), saya tidak ingin model "kreatif" (yang terjadi jika temperatur tinggi) karena bisa menyebabkan halusinasi data lapangan.

**13. Apa perbedaan jendela konteks dan ingatan? Mana yang dimiliki produk Anda?**
> Jendela konteks (*Context Window*) adalah batasan memori dalam SATU kali proses tanya jawab (*stateless*). Ingatan (*Memory*) adalah kemampuan merangkai konteks dari pesan-pesan sebelumnya. Produk saya **hanya menggunakan jendela konteks** (tidak menyimpan riwayat *chat* sebelumnya).

**14. Model apa yang Anda pakai, dan model apa yang Anda tolak? Atas dasar apa?**
> Saya memakai `gpt-4o-mini` via OpenRouter. Saya menolak `google/gemini-2.0-flash-001` di tengah jalan karena API OpenRouter saat itu mengalami kegagalan *endpoint* (404 error) untuk model tersebut, jadi saya pindah ke *gpt-4o-mini* demi stabilitas dan kapabilitas *Vision*.

**15. Tunjukkan satu tugas pada produk Anda yang model termurah sudah memadai. Bagaimana Anda membuktikannya?**
> Ekstraksi laporan teks menjadi JSON sudah sangat memadai dengan model murah (seperti *gpt-4o-mini*). Terbukti karena format Pydantic yang ditugaskan selalu dijawab sempurna berkat *Instructor*, tanpa perlu model *flagship* mahal seperti GPT-4.

#### C. Kendali Output
**16. Tunjukkan system prompt Anda. Petakan setiap bagiannya ke enam bagian.**
> (1) Peran: *Kamu adalah Asisten Ekstraksi...*, (2) Tugas: *Ekstrak data lapangan ini*, (3) Aturan/Konteks RAG: *Gunakan aturan SOP berikut: [CONTEXT]*, (4) Injeksi Referensi: *Hari ini adalah [TANGGAL], berikut kalender 14 hari...*, (5) Syarat Skema: *Gunakan JSON schema yang diwajibkan*, (6) CoT: *Jelaskan kalkulasi kalendermu terlebih dahulu.*

**17. Bagian mana dari instruksi Anda yang kalau dihapus akan paling merusak? Sudahkah Anda mencobanya?**
> Bagian injeksi *Kalender 14-hari Indonesia* dan CoT. Jika dihapus, LLM selalu gagal menebak tanggal absolut dari kata "Kamis lalu". Ya, saya sudah mencobanya di versi awal (V1) dan itu gagal total.

**18. Berapa versi instruksi yang sudah Anda buat? Apa yang berubah dari v1 ke versi sekarang, dan mengapa?**
> 3 versi. V1 hanya perintah JSON. V2 ditambah RAG (SOP). V3 (sekarang) ditambah referensi *Kalender* + logika perhitungan CoT. Alasan perubahannya murni untuk membunuh masalah 'halusinasi waktu' relatif dari bahasa Indonesia sehari-hari.

**19. Tunjukkan schema output Anda. Mengapa field ini ada dan field itu tidak?**
> `penjelasan_kalkulasi_tanggal` saya adakan untuk memaksa LLM berpikir sebelum mencetak tanggal. Saya *tidak* mengadakan field seperti `Nama Petugas` karena di realita laporan fisik/foto, identitas petugas jarang tertulis di dalam foto tersebut.

**20. Nilai apa yang tersedia untuk kasus “tidak dapat ditentukan”? Apa yang terjadi kalau ia tidak ada?**
> Saya menggunakan `Optional[str]` untuk field `catatan_tambahan`, dan opsi `lainnya` di Literal `kategori_produk`. Jika nilai perlindungan ini tidak ada, Pydantic akan *error/crash* saat LLM menemui perangkat aneh di luar modul.

**21. Mengapa field bukti berupa kutipan langsung, bukan ringkasan?**
> Karena ringkasan rentan diubah secara semantik oleh LLM (halusinasi). Kutipan langsung dari dokumen (SOP) menjamin transparansi 100% dari dokumen *grounding* perusahaan.

**22. Apa yang terjadi kalau output tidak valid menurut schema Anda? Tunjukkan mekanismenya berjalan.**
> Validasi *Pydantic* akan melempar *ValidationError*. *Library Instructor* akan menangkap *error* ini, mengirimkannya kembali ke LLM dengan pesan: *"Skema Anda salah di bagian X, tolong perbaiki"*, dan LLM merespons ulang hingga valid (*auto-retry*).

**23. Tunjukkan satu input yang membuat produk Anda menghasilkan output yang tidak valid. Mengapa ia lolos?**
> Input teks kosong atau hanya berisi spasi. Ia lolos memicu API LLM karena bukan nol-karakter, namun LLM bingung dan mungkin berhalusinasi membuat JSON palsu dengan opsi *default*. (Meski di UI Streamlit saya sudah mencegah ini).

#### D. Tool
**24. Sebutkan tool Anda dan kapan masing-masing tidak boleh dipakai.**
> Tool A: *Vision Model* (hanya boleh jika *user* *upload* foto). Tool B: *RAG Retriever* (hanya boleh setelah teks diekstrak/diketik). Tool C: *Pydantic/Instructor* (wajib di fase akhir).

**25. Tool mana yang hanya membaca dan mana yang mengubah sesuatu? Bagaimana perbedaan itu tercermin pada rancangan?**
> *LlamaIndex/pgvector* murni hanya MEMBACA dokumen (Retriever). *Instructor/OpenRouter* MENGUBAH teks/foto mentah menjadi JSON. Rancangan sistem dibuat berurutan: Membaca (Retrieve) dahulu, baru Mengubah (Generate).

**26. Tunjukkan satu pertanyaan yang membuat sistem Anda memilih tool salah. Apa sebabnya?**
> Karena sistem kami menggunakan arsitektur linear (bukan *Agentic Tool Calling* yang murni otonom), sistem kami tidak memilih *tool* yang salah. Ia selalu menjalankan Vision -> RAG -> Instructor secara sekuensial *hardcoded*.

**27. Apa yang terjadi kalau tool Anda gagal? Tunjukkan.**
> Jika LLM OpenRouter gagal/timeout, sistem akan melempar Python *Exception*, tertangkap oleh blok `try-except`, dan UI Streamlit merender kotak merah `st.error()` berisi pesan gagal, membatalkan ekstraksi secara aman.

**28. Mengapa tool yang mengembalikan hasil kosong lebih berbahaya daripada yang mengembalikan error?**
> Hasil kosong (*silence failure*) di pencarian RAG membuat LLM memproses ekstraksi *tanpa rujukan SOP*. User akan mengira hasil JSON itu sudah tervalidasi SOP padahal LLM sedang berhalusinasi dengan pengetahuan umumnya.

#### E. Rancangan RAG
**29. Berapa ukuran chunk Anda, dan mengapa bukan setengahnya atau dua kalinya?**
> Ukuran default LlamaIndex (~1024 token). Jika setengahnya, konteks peraturan SOP terputus. Jika dua kalinya, biaya *embedding* mahal dan menambah polusi memori di jendela konteks (*Context Window*).

**30. Mengapa Anda memotong menurut struktur / menurut jumlah huruf? Apa yang Anda korbankan?**
> Saya memotong berdasarkan *jumlah token/huruf* (algoritma *sliding window* dasar LlamaIndex). Saya mengorbankan integritas struktural (contoh: list urutan SOP panjang mungkin terpotong di tengah jalan).

**31. Berapa chunk yang Anda ambil per pertanyaan? Apa yang terjadi kalau diambil satu, dan kalau diambil sepuluh?**
> Mengambil `Top-K = 3`. Jika 1, referensi mungkin terlalu sempit. Jika 10, LLM akan *overloaded* (distraksi konteks) dan biaya token membengkak secara tidak perlu.

**32. Apa yang dilakukan sistem Anda kalau tidak ada chunk yang cukup mirip? Mengapa itu keputusan etis, bukan teknis?**
> Sistem mencetak informasi *"Tidak ada aturan SOP spesifik ditarik..."*. Ini etis karena saya bersikap transparan kepada pengguna bahwa ekstraksi yang dilakukan LLM selanjutnya murni tanpa dasar landasan SOP perusahaan, bukan *error* teknis semata.

**33. Dari mana dokumen rujukan Anda? Apakah Anda berhak memakainya?**
> Dokumen rujukan (`sop_inspeksi_jaringan.txt`) saya ketik mandiri (*dummy file*) berdasarkan kebiasaan standar pelaporan. Karena ini aset milik saya/internal fiksi untuk tugas, saya 100% berhak menggunakannya.

**34. Tunjukkan satu pertanyaan yang jawabannya tersebar di dua dokumen. Apakah rancangan Anda menanganinya?**
> Jika satu SOP tentang "Modem" dan dokumen kedua tentang "Router", rancangan saya (dengan Top-K=3) akan menarik kedua *chunk* tersebut sekaligus, sehingga LLM bisa mengawinkan instruksi dari keduanya.

**35. Metadata apa yang ikut disimpan bersama chunk, dan mengapa itu penting saat menjawab?**
> Metadata seperti asal/nama *file document*. Penting agar di UI saya bisa menampilkan referensi *Accordion* (contoh: "Potongan SOP #1") untuk transparansi asal-usul dokumen.

#### F. Proses dan Kejujuran
**36. Tunjukkan satu input yang membuat sistem Anda gagal, dan jelaskan sebabnya sampai ke akar.**
> Memasukkan koordinat geografis terbalik atau berformat huruf arah (*misal: 116.8 E, 1.2 S*). Akar masalahnya: LLM mencoba pintar memisahkan angka dan huruf, namun Peta di *Streamlit* (`st.map`) murni butuh *Latitude & Longitude* matematis yang urut dan *floating point*. Akibatnya *library* Peta mengalami *crash*.

**37. Sebutkan satu keputusan rancangan yang dapat dibuat berbeda, dan mengapa Anda memilih yang ini.**
> (Sama seperti no. 1 di Pertanyaan Wajib). Memilih Instructor+Pydantic daripada Prompt Engineering biasa.

**38. Bagian mana dari karya Anda yang dibuat dengan bantuan AI, dan bagaimana Anda memverifikasinya?**
> Antarmuka (UI) Streamlit, Regex parser Peta, dan logika *multi-photo looping*. Saya memverifikasinya dengan eksekusi kode (melihat sendiri jika tata letak/UI rusak), membaca *traceback error* Python di terminal, dan menolak instruksi AI jika gagal berjalan di *environment* nyata saya.

**39. Sebutkan satu hal yang AI berikan kepada Anda dan ternyata salah. Bagaimana Anda menemukannya?**
> AI (Agent) memberikan *Regex parser* Peta yang mengasumsikan angka pertama selalu *Latitude*. Kenyataannya, LLM Vision sering memutar posisi Longitude di depan. Saya menemukan *error* ini ketika Peta Streamlit menolak tampil dengan pesan *error* *Out of bounds* (Latitude > 90).

**40. Prediksi Anda pada tahap BREAK minggu ke berapa yang paling meleset? Apa yang salah dari cara Anda berpikir waktu itu?**
> Saya awalnya berasumsi eksekusi API (OpenRouter) ke model modern seperti *Gemini* akan berjalan mulus selamanya. Namun di kenyataan, penyedia Cloud/API bisa merubah *Endpoint/URL* kapan saja (menghasilkan error 404). Asumsi saya bahwa "Model yang bagus pasti stabil" ternyata salah secara operasional (*deployment*).

