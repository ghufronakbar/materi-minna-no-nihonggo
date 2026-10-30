# Panduan evaluasi per 5 bab

**Acuan yang disetujui:** `soal/evaluasi-bab-01-05/`, berisi lembar soal format JLPT dengan lembar jawaban di halaman terakhir, serta kuncinya.

Evaluasi dibuat untuk setiap blok 5 bab: **1–5, 6–10, 11–15, 16–20, 21–25**. Tes harian per bab (`03-soal-guidelines.md`) mengecek hafalan dan pola satu bab. Evaluasi ini mengecek apakah siswa bisa memakai materi 5 bab sekaligus, dengan format seperti JLPT N5.

## 1. Komposisi: 50 soal × 2 = 100, waktu 60 menit

Semua soal pilihan ganda 1–4.

| もんだい | No | Bentuk | Sebaran |
|---|---|---|---|
| １ Kosakata | 1–10 | Isi （　　） dengan kata yang tepat | 2 per bab |
| ２ Kalimat yang artinya sama | 11–15 | Kalimat bergaris bawah `<u>…</u>`, lalu pilih kalimat yang artinya paling dekat | 1 per bab |
| ３ Bunpou | 16–30 | Isi （　　） dengan partikel, bentuk kata, kata tunjuk/tanya, atau bacaan angka | 3 per bab |
| ４ Mengurutkan (★) | 31–35 | 4 potongan, lalu pilih kata di posisi ★ | 1 per bab |
| ５ Bunpou dalam teks | 36–40 | Teks pendek dengan bagian kosong （３６）–（４０） | Bebas, catat di kisi-kisi |
| ６ Membaca | 41–45 | 2–3 teks pendek (memo, cerita diri), masing-masing 1–3 soal | Bebas |
| ７ Mencari informasi | 46–50 | Papan, jadwal, atau daftar harga, lalu 5 soal | Bebas |

## 2. Aturan bahasa

- Ikuti aturan bahasa `03-soal-guidelines.md` bagian 2: hanya hiragana/katakana, spasi penuh `　` antarkata, dan akhiran `。`.
- Instruksi ditulis dalam bahasa Indonesia. Label `もんだい１` boleh dipakai.
- Opsi ditulis dengan angka lebar penuh dan spasi penuh: `１　いしゃ　　２　ぎんこういん　　３　…`. Opsi yang panjang (kalimat) ditulis satu per baris.
- Hanya memakai kosakata dan pola sampai bab terakhir blok. Bab dari blok sebelumnya boleh muncul sebagai bahan pendukung, tetapi fokus soal ada di blok ini.
- **Kalimat harus baru.** Jangan menyalin soal dari tes per bab di `soal/bab-NN/`. Baca tes-tes itu dahulu supaya tidak mengulangnya.

## 3. Aturan soal

- **Hanya satu opsi yang benar.** Cek setiap pengecoh terhadap kalimatnya. Contoh yang pernah dibetulkan:
  - 「（どこ）の じどうしゃ」: opsi どちら dihapus karena 「どちらの」 juga benar.
  - 「この ネクタイ （を） ください」: opsi も tidak dipakai karena 「も ください」 juga benar.
  - Kalimat sama arti 「この かばん は ワンさん の です」: opsi 「それ は ワンさん の かばん です」 diganti karena bisa diperdebatkan sebagai benar.
- **Opsi harus sejenis**, misalnya semua kata benda, semua partikel, atau semua bentuk kata kerja yang sama.
- **Tidak ada jawaban yang bocor.** Jawaban satu soal tidak boleh muncul dalam frasa yang sama persis di soal lain, terutama di potongan ★, teks もんだい５–７, dan kalimat bergaris bawah もんだい２. Contoh: potongan ★ 「この ワイン は どこ の です か」 membocorkan soal 「（どこ）の じどうしゃ」, sehingga soal ★ diganti.
- **Soal ★ hanya boleh punya satu urutan alami.** Hindari potongan yang bisa ditukar, seperti keterangan waktu atau 「ともだち と」／「きょうと へ」. Pakai urutan yang tetap, misalnya 「くがつ はつか」 dan 「いちまん えん」. Posisi ★ jangan selalu di tempat yang sama.
- **Sebarkan jawaban merata dan acak** di posisi 1–4 (masing-masing sekitar 10–15). Jangan menyusun jawaban berpola (misalnya 1-2-3-4 berulang); siswa bisa menebaknya. Setelah soal dan kunci cocok, jalankan `python3 soal/acak-jawaban-evaluasi.py soal/evaluasi-bab-AA-BB` untuk mengacak posisi jawaban. Skrip ini memperbarui lembar soal, kunci cepat, dan kolom Jwb di tabel kunci sekaligus.
- **Teks bacaan** ditulis paling banyak sekitar 7 kalimat. もんだい７ memakai tema blok, misalnya papan lantai, jam buka, dan harga untuk Bab 1–5.

## 4. Fokus per blok

| Blok | Fokus bunpou dan kosakata |
|---|---|
| 1–5 | です／じゃありません, これ・この・ここ, harga/jam/tanggal, ます・ません・ました・ませんでした, へ・で・と, どこも |
| 6–10 | を・で (tempat, alat), ませんか／ましょう, あげます／もらいます, もう～ました, kata sifat い／な, すき・じょうず・わかります, から (alasan), あります／います, posisi |
| 11–15 | counter, kata benda/sifat lampau, perbandingan, ほしい／たい, ～に いきます (tujuan), bentuk て, てください, ています, てもいい／てはいけません |
| 16–20 | ～て～て, てから, bentuk ない (ないでください, なければなりません), bentuk kamus (ことができます, しゅみは～こと, まえに), bentuk た (ことがあります, たり), なります, bentuk biasa |
| 21–25 | と おもいます／いいました, でしょう, modifikasi kata benda, とき, と (kondisi), くれます, ～てあげます／もらいます／くれます, たら／ても |

Cek ulang cakupannya di `materi-minna-no-nihonggo.md` dan `materi/script-bab-NN-senin.md` untuk setiap bab di blok.

## 5. Struktur file

```
soal/evaluasi-bab-AA-BB/
  evaluasi-bab-AA-BB.md         ← lembar soal + lembar jawaban
  kunci-evaluasi-bab-AA-BB.md
  (kedua .pdf hasil generate)
```

**Lembar soal** (salin kerangka dari `soal/evaluasi-bab-01-05/`):
- Kop Nama/Tanggal/Nilai, lalu baris waktu dan petunjuk lembar jawaban.
- Teks bacaan ditulis sebagai blockquote (`>`), yang di PDF tampil dalam kotak. Papan informasi berupa tabel di dalam blockquote; buat dua pasang kolom supaya ringkas.
- Sisipkan `<div style="break-before: page"></div>` sebelum もんだい７ dan sebelum lembar jawaban. Tambahkan pemisah lain hanya jika ada もんだい yang terbelah.
- Lembar jawaban berupa tabel HTML `<table class="lembar-jawaban">` dengan 5 pasang kolom No／① ② ③ ④. Salin dari file acuan.
- Target panjang: 5 halaman soal dan 1 halaman lembar jawaban.

**Kunci**, dengan urutan:
1. Judul `# Kunci Jawaban Evaluasi — Bab AA–BB` dan baris `**LEMBAR GURU / EVALUASI** · 50 soal × 2 = 100`.
2. **Kunci cepat:** tabel 5 pasang kolom `| No | Jwb |`. Format ini dibaca oleh `soal/cek-kunci-evaluasi.py`, jadi jangan diubah.
3. **Kisi-kisi:** bab × もんだい, berisi nomor soal dan jumlah per bab. Soal yang terutama menguji materi blok sebelumnya (paling banyak sekitar 5 soal, hanya di もんだい５–７) dicatat di baris `Ulang AA–BB`. Contohnya ada di `soal/evaluasi-bab-06-10/`.
4. Tabel per もんだい: もんだい１ memuat kalimat lengkap dan arti; もんだい２ alasan; もんだい３ dan ５ jawaban dan pola yang diuji; もんだい４ kalimat lengkap dengan kata ★ bergaris bawah; もんだい６–７ bukti di teks.
5. Satu atau dua catatan singkat tentang kesalahan yang mungkin muncul.
6. Pemisah halaman, lalu **Rekap Nilai Kelas** (20 baris, skor per もんだい).

## 6. Generate PDF

Di Mac: `soal/build-pdf.sh soal/evaluasi-bab-AA-BB`.
Di lingkungan tanpa Google Chrome Mac (misalnya sesi cloud):
```bash
NODE_PATH=$(npm root -g) node soal/build-pdf-playwright.js soal/evaluasi-bab-AA-BB
```
Hasil di cloud memakai font Jepang yang tersedia di sana, bukan Hiragino.

## 7. Cek sebelum selesai

1. Jalankan `python3 soal/cek-kunci-evaluasi.py soal/evaluasi-bab-AA-BB`. Baca setiap opsi yang ditunjuk kunci, lalu pastikan jumlah soal 50 dan tidak ada kanji. Setelah itu jalankan `soal/acak-jawaban-evaluasi.py`, lalu `cek-kunci-evaluasi.py` sekali lagi untuk memastikan teks opsi yang ditunjuk kunci tidak berubah.
2. Untuk setiap soal, cek bahwa pengecoh tidak ada yang juga benar (bagian 3).
3. Cari jawaban yang bocor antarbagian, terutama ★ dan teks bacaan.
4. Cocokkan kisi-kisi dengan sebaran di bagian 1; jumlah per bab harus sama dengan 50.
5. Render PDF (`pdftoppm -r 60 -png file.pdf <scratchpad>/prev`), lalu lihat hasilnya: tidak ada もんだい yang terbelah, papan informasi satu halaman dengan soalnya, dan lembar jawaban tidak terpotong.
