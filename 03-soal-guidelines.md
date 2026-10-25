# Panduan pembuatan soal

**Acuan yang disetujui:** `soal/bab-15/`, berisi tes kotoba, post test, dan kunci masing-masing.

Setiap bab mendapat dua tes yang dicetak atau dibagikan ke siswa. Sumbernya ditulis dalam Markdown supaya mudah direvisi, lalu diubah menjadi PDF A4.

| Tes | Waktu | Tujuan |
|---|---|---|
| Tes kotoba | Pagi, setelah sesi kosakata (*kotoba no junbi*) | Mengecek hafalan kosakata bab |
| Post test | Siang/sore, setelah bunpou bab diajarkan | Mengecek kosakata dalam kalimat, bunpou, dan susunan kalimat |

## 1. Persiapan

1. **Ambil kosakata bab dari PDF** `Kosakata minna no nihongo 1 Bab 1-25.pdf`. Teks PDF ini rusak jika diekstrak (`pdftotext` menghasilkan huruf acak), jadi render halamannya menjadi gambar lalu baca:
   ```bash
   pdftoppm -f 25 -l 26 -r 110 -png "Kosakata minna no nihongo 1 Bab 1-25.pdf" <scratchpad>/bab
   ```
   Bab 14 ada di halaman 23–24 dan Bab 15 di halaman 25–26. Untuk bab lain, render beberapa halaman di resolusi rendah (`-r 60`) untuk mencari judul "Kosa Kata Bab N".
2. **Periksa salah ketik di PDF.** Contoh: di Bab 15, `ソフト` tertulis `オフト`. Pakai bentuk yang benar di soal.
3. **Cek cakupan bunpou** di `materi-minna-no-nihonggo.md` dan di skrip bab terkait (`materi/script-bab-NN-senin.md`). Dari skrip itu, cari tahu pola apa yang baru diajarkan hari itu dan pola lama apa yang sudah dikuasai siswa.

## 2. Aturan bahasa (berlaku untuk semua soal)

- **Hanya hiragana/katakana**, tanpa kanji dan tanpa romaji. Pengecualian: nama dari buku yang memang ditulis dengan huruf Latin, seperti IMC. Kanji hanya boleh muncul di kunci sebagai info guru.
- **Spasi antarkata dan partikel** memakai spasi penuh `　`, sesuai contoh pengguna: `わたし　は　おおさか　に　すんで　います。`
- Akhir kalimat memakai `。`, bukan titik biasa.
- Sebelum Bab 18, kata kerja di Bagian I dan II tes kotoba ditulis dalam bentuk ～ます, karena bentuk kamus baru diajarkan di Bab 18. Mulai Bab 18, ikuti bentuk yang dipakai di daftar kosakata dan sebutkan di instruksi soal.
- Kalimat hanya memakai kosakata bab ini dan kosakata/pola dari bab yang sudah diajarkan. Jika ragu sebuah kata sudah dipelajari, ganti dengan kata yang pasti sudah dikenal.
- Nama tokoh mengikuti buku: ミラーさん, ワンさん, IMC, dan seterusnya.

## 3. Tes kotoba (pagi): 25 soal × 4 = 100

| Bagian | Jumlah | Bentuk |
|---|---|---|
| I. Terjemahkan ke dalam Bahasa Jepang (Huruf Hiragana / Katakana) | 10 (no. 1–10) | `1. Menjual : ……………` |
| II. Terjemahkan ke dalam Bahasa Indonesia | 10 (no. 11–20) | `11. すみます : ……………` (tanpa romaji) |
| III. Melengkapi Kalimat (Pilihan Ganda) | 5 (no. 21–25) | Kalimat dengan `[ ... ]`, opsi a/b/c di baris bawah |

Aturan:
- **Tidak ada jawaban yang bocor antarbagian.** Kata yang ditanyakan di Bagian I tidak boleh muncul di Bagian II atau III, termasuk sebagai opsi atau di dalam kalimat. Sebaliknya juga berlaku.
- **Pilih kata secara merata:** kata kerja, benda, tempat, dan pekerjaan. Bab dengan banyak kosakata (Bab 15 punya 50 kata) cukup diambil sampel 25 kata yang paling berguna.
- **Bagian III hanya memakai bentuk ます dan pola sampai bab sebelumnya**, karena bunpou bab ini belum diajarkan saat tes pagi.
- **Opsi a/b/c harus sejenis:** semua kata kerja atau semua kata benda, supaya tidak bisa dijawab dari jenis katanya saja. Sebisa mungkin satu opsi pengecoh mirip bunyinya (contoh: かんごし/べんごし) atau artinya.
- Pengecoh boleh diambil dari bab lama, misalnya すわります dan たちます dari Bab 14.

## 4. Post test (siang): 20 soal × 5 = 100

| Bagian | Jumlah | Bentuk |
|---|---|---|
| I. Melengkapi Kalimat dengan Kotoba | 10 (no. 1–10) | Kotak kata + `（　　　　　　　　）` di kalimat |
| II. Melengkapi Kalimat dengan Bunpou | 5 (no. 11–15) | `（とります → ＿＿＿＿＿＿＿＿）　も　いい　です　か。` |
| III. Menyusun Kata Menjadi Kalimat | 5 (no. 16–20) | Potongan dipisah `　／　`, garis jawaban di bawahnya |

Aturan:
- **Kotak kata** berisi 10 jawaban ditambah 3 pengecoh, diacak, dan setiap kata hanya dipakai sekali. Kata kerja ditulis di kotak dalam bentuk yang dibutuhkan kalimat (misalnya すんで), karena bagian ini menguji arti, bukan perubahan bentuk.
- **Setiap kalimat di Bagian I hanya boleh cocok dengan satu kata di kotak.** Cek setiap kalimat terhadap semua 13 kata, terutama pengecoh. Contoh yang pernah dibetulkan: 「（　）で はたらいて います」 cocok untuk しやくしょ dan juga はいしゃ, jadi pengecoh はいしゃ diganti. Beri petunjuk konteks di kalimat (「あね は こうむいん です。」) jika perlu.
- **Bagian II dibagi merata ke pola bunpou bab ini.** Contoh Bab 15: 2 soal ～てもいいですか, 1 soal ～てはいけません, 2 soal ～ています.
- **Bab tanpa perubahan kata kerja** (misalnya Bab 1–3): Bagian II berupa isian partikel atau bentuk, **tanpa kotak pilihan** supaya jawaban tidak bisa ditebak dengan eliminasi. Instruksinya: "Isi bagian kosong dengan partikel atau bentuk yang tepat." Contoh: `わたし　（＿＿＿＿＿＿＿＿）　マイク・ミラー　です。` Lihat `soal/bab-01/`.
- **Bagian III:** partikel boleh dijadikan potongan sendiri (`に`, `を`) untuk menguji posisinya. Pilih kalimat yang urutannya jelas. Jika ada urutan lain yang juga benar, tulis di kunci.

## 5. Kunci jawaban (file terpisah)

Judul: `# Kunci Jawaban <Tes> — Bab N`, diikuti baris `**LEMBAR GURU / EVALUASI** · 25 soal × 4 = 100`. Isinya berupa tabel per bagian:

- **Tes kotoba:** Bagian I memuat jawaban dan kanji. Bagian II memuat jawaban dan jawaban lain yang diterima. Bagian III memuat huruf jawaban, kalimat lengkap, dan arti.
- **Post test:** Bagian I memuat jawaban, arti kalimat, dan daftar pengecoh. Bagian II memuat jawaban dan pola yang diuji. Bagian III memuat kalimat jawaban, urutan lain yang diterima, dan arti.
- Tutup dengan **satu atau dua catatan singkat** tentang kesalahan yang mungkin muncul, misalnya jawaban negatif しって います adalah しりません. Jangan menulis penjelasan panjang.

## 6. Struktur file dan generate PDF

```
soal/
  build-pdf.sh                  ← Markdown → PDF A4
  style.css                     ← tampilan PDF (font Hiragino, kop, kotak kata)
  bab-NN/
    tes-kotoba-bab-NN.md
    kunci-tes-kotoba-bab-NN.md
    post-test-bab-NN.md
    kunci-post-test-bab-NN.md
    (keempat .pdf hasil generate)
```

- Nomor bab di nama folder dan file selalu dua digit (`bab-07`, `bab-15`), sama seperti di `materi/`.
- Lembar siswa diawali kop yang sama dengan `soal/bab-15/` (tabel Nama/Tanggal/Nilai dengan satu baris kosong), lalu baris `Waktu: 30 menit · Setiap soal bernilai N.` Salin kerangka dari file Bab 15 lalu ganti isinya.
- Kotak kata ditulis dalam HTML `<div class="kotak-kata"><span>…</span> …</div>` supaya kata tidak terpotong di tengah saat dicetak.

Generate semua PDF di satu folder bab:
```bash
soal/build-pdf.sh soal/bab-15
```
Atau satu file saja: `soal/build-pdf.sh soal/bab-15/post-test-bab-15.md`.

Skrip ini membutuhkan Node.js (menjalankan `npx marked@12.0.2`) dan Google Chrome (headless). Chrome kadang tidak menutup sendiri setelah mencetak; skrip sudah menangani ini dengan menunggu PDF lalu menghentikan Chrome.

## 7. Cek sebelum selesai

1. Jumlah soal dan nilai: 25 × 4 dan 20 × 5. Nomor soal berurutan.
2. Tidak ada kanji atau romaji di lembar siswa.
3. Tes kotoba: tidak ada kata yang bocor antarbagian, Bagian III bebas dari pola baru bab ini, dan opsi a/b/c sejenis.
4. Post test: setiap kalimat Bagian I hanya punya satu jawaban yang cocok dari kotak, termasuk saat dicek terhadap pengecoh.
5. Setiap jawaban di kunci sama dengan soalnya, termasuk huruf opsi pilihan ganda.
6. Render PDF lalu lihat hasilnya (`pdftoppm -r 60 -png file.pdf <scratchpad>/prev`): huruf Jepang tampil, kotak kata tidak terpotong, dan tidak ada soal yang terbelah di antara dua halaman.
