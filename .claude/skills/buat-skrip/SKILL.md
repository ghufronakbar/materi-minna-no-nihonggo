---
name: buat-skrip
description: Membuat skrip mengajar Senin penuh (465 menit) untuk satu bab Minna no Nihongo dalam format ringkas yang sudah disetujui, lengkap dengan recall, interaksi sensei–siswa, praktik berpasangan, cek can-do, dan saran Sabtu. Pakai saat pengguna meminta skrip, materi mengajar, rencana pertemuan, atau alur kelas untuk sebuah bab.
argument-hint: "<nomor bab, misal 23>"
---

# Buat skrip mengajar untuk satu bab

Bab yang diminta: $ARGUMENTS (jika kosong, tanyakan nomor babnya ke pengguna).

1. Baca `AGENTS.md`, `00-story.md`, `01-teaching-rules.md`, dan `02-script-guidelines.md` sampai selesai. Semua aturan format, jadwal, dan recall ada di sana.
2. Buka `materi/contoh-script-bab-14-senin-ringkas.md` sebagai patokan format yang sudah disetujui pengguna, `contoh-kasar.md` untuk gaya interaksi, dan satu skrip terbaru di `materi/` untuk melihat konsistensi antarbab.
3. Tentukan pertemuan sebelumnya. Biasanya `materi/script-bab-(N-1)-senin.md`, tetapi ikuti informasi pengguna jika bab sebelumnya dibagi atau dipindah. Dari skrip itu, ambil 2–3 poin yang benar-benar sudah diajarkan untuk recall.
4. Cek cakupan bab di `materi-minna-no-nihonggo.md`, termasuk tabel "Memilih materi untuk recall", lalu pilih bekal dari bab lama yang berkaitan. Pastikan materi baru bab ini tidak dijadikan syarat recall.
5. Ambil kosakata bab dari PDF dengan merender halamannya sebagai gambar (lihat `03-soal-guidelines.md` bagian 1 untuk perintah `pdftoppm` dan letak halaman). Periksa salah ketik PDF. Rujuk `dasar/` untuk bacaan dan bentuk dasar, tanpa menyalin tabelnya ke skrip.
6. Tulis `materi/script-bab-NN-senin.md` (nomor bab dua digit) dengan susunan yang sama seperti skrip lain:
   - Judul `# Skrip ringkas Bab N — Senin penuh`, lalu **Kelas**, **Jadwal**, **Alat**, **Pertemuan sebelumnya**, **Can-do**, **Pegangan kelas**.
   - `## A. Pagi — 07.30–10.00`, `## B. Menjelang siang — 10.15–12.00`, `## C. Siang–sore — 13.00–16.30`, dengan blok bernomor `### n. HH.MM–HH.MM — Judul` dan baris **Pembagian** di setiap blok. Jeda 10.00–10.15 dan 12.00–13.00 ditulis tebal di antara bagian.
   - Blok 1 berisi aisatsu, **Recall pertemuan sebelumnya**, **Recall materi terkait**, **Jika belum ingat**, dan **Keputusan**. Recall aktif setelah istirahat siang, role play terpadu, cek semua siswa, lalu recall akhir dan closing di blok terakhir.
   - `## D. Pegangan singkat sensei — tidak ditampilkan di awal` dan `## E. Jika dijadwalkan pada Sabtu` (270 menit).
7. Jalankan daftar cek di `02-script-guidelines.md` bagian 6. Hitung menit setiap blok dan setiap **Pembagian** sampai totalnya 465 menit tanpa tumpang tindih dengan jeda. Pastikan kedua anggota pasangan bergantian peran, setiap siswa dicek can-do-nya, rumus baru baru dirangkum saat recall akhir, dan bahasa Jepangnya hanya memakai kotoba/bunpou yang sudah atau sedang dipelajari. Panjang sebanding skrip lain (±1.600–2.000 kata).
8. Sampaikan ke pengguna ringkasan alur, asumsi yang dipakai (misalnya pertemuan sebelumnya atau salah ketik di PDF kosakata), dan path file-nya.

Kerjakan hanya bab yang diminta; jika pengguna meminta beberapa bab, buat berurutan supaya recall setiap bab mengacu pada skrip bab sebelumnya. Jika pengguna meminta versi pembanding, simpan sebagai file terpisah dahulu. Jika pengguna mengubah format atau aturan, perbarui `02-script-guidelines.md` setelah perubahan itu disetujui, supaya sesi berikutnya ikut memakai aturan baru.
