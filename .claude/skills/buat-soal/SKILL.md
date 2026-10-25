---
name: buat-soal
description: Membuat tes kotoba (pagi) dan post test (siang) beserta kunci jawabannya untuk satu bab Minna no Nihongo, lalu men-generate PDF A4 untuk dicetak/dibagikan ke siswa. Pakai saat pengguna meminta soal, tes, kuis, ulangan, atau lembar kerja untuk sebuah bab.
argument-hint: "<nomor bab, misal 16>"
---

# Buat soal untuk satu bab

Bab yang diminta: $ARGUMENTS (jika kosong, tanyakan nomor babnya ke pengguna).

1. Baca `03-soal-guidelines.md` sampai selesai. Semua format dan aturan ada di sana.
2. Buka keempat file di `soal/bab-15/` sebagai patokan format yang sudah disetujui pengguna.
3. Ambil kosakata bab dari PDF dengan merender halamannya sebagai gambar (panduan bagian 1). Cek cakupan bunpou di `materi-minna-no-nihonggo.md` dan `materi/script-bab-NN-senin.md`.
4. Tulis keempat file Markdown di `soal/bab-NN/`, nomor bab dua digit.
5. Jalankan `soal/build-pdf.sh soal/bab-NN`, render PDF-nya ke gambar, lalu lihat hasilnya.
6. Jalankan daftar cek di panduan bagian 7. Perbaiki yang belum sesuai, lalu generate ulang.
7. Kirim keempat PDF ke pengguna. Sebutkan asumsi yang dipakai, misalnya bab sebelumnya yang dianggap sudah diajarkan atau salah ketik di PDF kosakata.

Jika pengguna mengubah format atau aturan, perbarui `03-soal-guidelines.md` setelah perubahan itu disetujui, supaya sesi berikutnya ikut memakai aturan baru.
