# Panduan agen untuk proyek skrip mengajar

## Baca sebelum membuat atau mengubah skrip

1. `00-story.md` — konteks pengajar, siswa, dan tujuan proyek.
2. `01-teaching-rules.md` — aturan kelas dan jadwal LPK Saitama.
3. `02-script-guidelines.md` — format, tingkat keringkasan, dan cara menyusun skrip.
4. `materi/contoh-script-bab-14-senin-ringkas.md` — **patokan format yang sudah disetujui pengguna**.
5. `contoh-kasar.md` — cuplikan gaya interaksi yang diinginkan.
6. `materi-minna-no-nihonggo.md` dan kosakata bab terkait pada PDF — cakupan materi serta batas bahasa siswa.
7. `dasar/` — pegangan hafalan sensei (bilangan, jam, tanggal, counter, partikel, perubahan bentuk, dll.). Rujuk untuk mengecek bacaan dan bentuk dasar; jangan salin ulang tabelnya ke skrip.

Skill `/buat-skrip <bab>` menjalankan alur pembuatan skrip Senin penuh untuk satu bab dari awal sampai file di `materi/` jadi.

## Membuat soal tes

Untuk tes kotoba, post test, dan kunci jawaban per bab, ikuti `03-soal-guidelines.md`, dengan `soal/bab-15/` sebagai patokan format. Skill `/buat-soal <bab>` menjalankan alur ini dari awal sampai PDF jadi. Versi kanji dari soal yang sama (dengan furigana) dibuat dengan `/buat-soal-kanji <bab>`, mengikuti bagian 8 panduan tersebut.

## Hal yang harus dipertahankan

- Tulis dalam bahasa Indonesia dengan dialog Jepang yang benar dan sesuai materi siswa.
- Ikuti gaya contoh ringkas: alur waktu, ucapan inti sensei, kemungkinan respons siswa, kegiatan, dan cara mengecek pemahaman.
- **Prioritaskan recall materi pertemuan sebelumnya dan materi lama yang berkaitan dengan topik baru.** Tulis apa yang diulang, contoh pertanyaannya, serta tindakan jika siswa belum ingat. Judul “review” saja tidak cukup.
- Pertemuan sebelumnya tidak selalu berarti Bab N−1; satu bab dapat berlangsung beberapa pertemuan.
- Materi baru tidak dijadikan prasyarat. Contoh: bentuk て baru diperkenalkan pada Bab 14, sehingga bukan syarat masuk bab itu jika belum pernah diajarkan.
- Pertahankan interaksi dan praktik siswa. Rumus baru dirangkum setelah siswa melakukan recall akhir.
- Catatan guru dibuat singkat, cukup untuk mencegah salah pengertian. Hindari penjelasan berulang, lampiran panjang, dan uraian setiap kemungkinan respons.
- Ikuti jadwal yang diminta pengguna. Senin penuh berisi 465 menit belajar; Sabtu 270 menit. Jeda Senin tetap mengikuti aturan.
- Jangan menetapkan bab pertemuan pertama sebelum posisi belajar diketahui. Siapkan perkenalan dan interaksi untuk mengetahuinya.

## Hasil kerja

- Simpan skrip dalam `materi/` sebagai Markdown, kecuali pengguna meminta format lain.
- Kerjakan pertemuan/bab yang diminta; pembuatan seluruh bab dilakukan bertahap sesuai arahan pengguna.
- Contoh ringkas Bab 14 adalah acuan gaya, bukan penetapan materi untuk semua pertemuan.
- Sebelum selesai, cek jumlah menit, giliran kedua anggota pasangan, ketepatan bahasa, serta kesesuaian recall dengan materi yang sudah dipelajari.
- Jika pengguna meminta versi pembanding, buat file lain dahulu. Ubah patokan ketika pengguna menyetujui perubahan tersebut.
- Instruksi terbaru pengguna menjadi acuan saat preferensi berubah; selaraskan dokumentasi jika diminta.
