---
name: buat-evaluasi
description: Membuat evaluasi gabungan per 5 bab Minna no Nihongo (Bab 1–5, 6–10, 11–15, 16–20, 21–25) dalam format JLPT — 50 soal pilihan ganda termasuk soal ★ mengurutkan, lembar jawaban, dan kunci dengan kisi-kisi serta rekap kelas — lalu men-generate PDF A4. Pakai saat pengguna meminta evaluasi, ujian blok, tes gabungan, atau soal per 5 bab.
argument-hint: "<blok bab, misal 6-10>"
---

# Buat evaluasi per 5 bab

Blok yang diminta: $ARGUMENTS (jika kosong, tanyakan bloknya ke pengguna: 1–5, 6–10, 11–15, 16–20, atau 21–25).

1. Baca `04-evaluasi-guidelines.md` sampai selesai. Semua format dan aturan ada di sana. Baca juga bagian 2 `03-soal-guidelines.md` untuk aturan bahasa.
2. Buka kedua file Markdown di `soal/evaluasi-bab-01-05/` sebagai patokan format yang sudah disetujui pengguna.
3. Kumpulkan cakupan blok: kunci tes kotoba dan post test di `soal/bab-NN/` untuk kelima bab (sebagai sumber kosakata, sekaligus supaya kalimatnya tidak disalin), `materi-minna-no-nihonggo.md`, dan `materi/script-bab-NN-senin.md`, untuk memastikan pola yang benar-benar diajarkan.
4. Rencanakan kisi-kisi dahulu (bab × もんだい, sesuai sebaran di panduan bagian 1), lalu tulis soal dan kunci di `soal/evaluasi-bab-AA-BB/`, nomor bab dua digit.
5. Jalankan `python3 soal/cek-kunci-evaluasi.py soal/evaluasi-bab-AA-BB`. Baca setiap opsi yang ditunjuk kunci, lalu jalankan daftar cek di panduan bagian 7: satu jawaban benar dan tidak ada jawaban bocor. Setelah itu acak posisi jawaban dengan `python3 soal/acak-jawaban-evaluasi.py soal/evaluasi-bab-AA-BB`, lalu jalankan cek kunci sekali lagi.
6. Generate PDF dengan `soal/build-pdf.sh`, atau dengan `soal/build-pdf-playwright.js` jika Chrome Mac tidak tersedia. Render PDF ke gambar dan lihat tata letaknya. Perbaiki lalu generate ulang bila perlu.
7. Kirim kedua PDF ke pengguna. Sebutkan asumsi yang dipakai dan soal yang perlu keputusan pengguna.

Jika pengguna mengubah format atau aturan, perbarui `04-evaluasi-guidelines.md` (dan file acuan bila perlu) setelah perubahan itu disetujui, supaya sesi berikutnya ikut memakai aturan baru.
