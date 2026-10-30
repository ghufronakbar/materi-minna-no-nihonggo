---
name: buat-soal-kanji
description: Membuat versi kanji (dengan furigana) dari soal per bab yang sudah ada dalam hiragana — tes kotoba, post test, dan kuncinya — lalu men-generate PDF A4. Isi soal tetap sama, hanya penulisannya yang memakai kanji. Pakai saat pengguna meminta soal versi kanji, soal dengan kanji/furigana, atau mengubah soal hiragana ke kanji.
argument-hint: "<nomor bab, misal 15, atau nama folder seperti evaluasi-bab-01-05>"
---

# Buat versi kanji dari soal satu bab

Bab yang diminta: $ARGUMENTS (jika kosong, tanyakan nomor babnya ke pengguna).

1. Baca `03-soal-guidelines.md`, terutama bagian 2, 6, 7, dan **bagian 8 (Versi kanji)**. Semua aturan versi kanji ada di sana.
2. Buka semua file `.md` di `soal/bab-NN/` (nomor bab dua digit). Ini sumber soalnya. Jika foldernya belum ada, hentikan dan sarankan `/buat-soal <bab>` dahulu.
3. Ambil kolom Kanji kosakata bab ini dari PDF dengan merender halamannya sebagai gambar (panduan bagian 1). Untuk kata dari bab lama, render halaman bab tersebut atau pakai kolom kanji di kunci bab itu.
4. Tulis file versi kanji di `soal/bab-NN/kanji/` dengan nama asal ditambah `-kanji`. Salin isi versi hiragana, ganti kata yang ber-kanji dengan notasi furigana `{漢字|かな}`, lalu sesuaikan judul, instruksi Bagian I tes kotoba, Bagian II tes kotoba (tanpa furigana), dan catatan kunci sesuai bagian 8.
5. Jalankan kedua perintah cek di bagian 8 (diff dengan versi hiragana dan cari kanji tanpa furigana). Pastikan setiap perbedaan memang termasuk yang wajar.
6. Jalankan `soal/build-pdf.sh soal/bab-NN/kanji`, render PDF-nya ke gambar (`pdftoppm -r 80 -png`), lalu lihat hasilnya: furigana tampil di atas kanji dan tidak ada `{`/`|` yang tersisa. Jika Chrome Mac tidak tersedia (misalnya sesi cloud), pakai `NODE_PATH=$(npm root -g) node soal/build-pdf-playwright.js soal/bab-NN/kanji`. Pastikan lingkungan itu punya font Jepang; jika tidak, huruf Jepang tampil kosong di PDF.
7. Jalankan daftar cek di bagian 7 (kecuali butir 2) dan bagian 8. Perbaiki yang belum sesuai, lalu generate ulang.
8. Kirim PDF versi kanji ke pengguna. Sebutkan kata yang penulisan kanjinya dipilih sendiri karena tidak ada di PDF kosakata, dan masalah apa pun di versi hiragana yang ditemukan (jangan diperbaiki diam-diam).

Jika pengguna mengubah aturan versi kanji, perbarui bagian 8 `03-soal-guidelines.md` setelah perubahan itu disetujui.
