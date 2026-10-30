"""Acak posisi jawaban evaluasi format JLPT supaya tidak berpola.

Pakai: python3 soal/acak-jawaban-evaluasi.py soal/evaluasi-bab-06-10

Jalankan setelah soal dan kunci selesai ditulis dan sudah cocok
(cek dengan cek-kunci-evaluasi.py). Opsi benar dipindahkan ke posisi acak
(sebaran 1–4 merata, tidak ada tiga jawaban sama berturut-turut); urutan
opsi lain tetap. Lembar soal, kunci cepat, dan kolom Jwb di tabel kunci
ikut diperbarui. Hasil acakan tetap sama untuk blok yang sama.
"""
import pathlib
import random
import re
import sys

ANGKA = "１２３４"

folder = pathlib.Path(sys.argv[1])
blok = folder.name.removeprefix("evaluasi-")
f_soal = folder / f"evaluasi-{blok}.md"
f_kunci = folder / f"kunci-evaluasi-{blok}.md"
soal = f_soal.read_text()
kunci = f_kunci.read_text()

BARIS_CEPAT = r"^\|(?: \d+ \| \d \|)+$"
lama = {}
for baris in re.findall(BARIS_CEPAT, kunci, re.M):
    for no, jwb in re.findall(r"(\d+) \| (\d)", baris):
        lama[int(no)] = int(jwb)

# Posisi baru: merata, acak tetap per blok, tanpa tiga sama berturut-turut.
nomor = sorted(lama)
target = ([1, 2, 3, 4] * 13)[: len(nomor)]
random.Random(blok).shuffle(target)
baru = dict(zip(nomor, target))
for a, b, c in zip(nomor, nomor[1:], nomor[2:]):
    if baru[a] == baru[b] == baru[c]:
        baru[c] = baru[c] % 4 + 1

# Lembar soal: susun ulang opsi tiap butir.
isi, pemisah, lembar_jawaban = soal.partition("# Lembar Jawaban")
potong = re.split(r"^(\d+)\. ", isi, flags=re.M)
hasil = [potong[0]]
for i in range(1, len(potong), 2):
    no, badan = int(potong[i]), potong[i + 1]
    m = re.search(r"(１　.*?)(?=\n\n|\n(?!\s+[１２３４]　)|$)", badan, re.S)
    teks = m.group(1).rstrip("\n")
    baris = teks.split("\n")
    if len(baris) > 1:  # satu opsi per baris
        indent = re.match(r"\s*", baris[1]).group(0)
        opsi = [re.sub(r"^\s*[１２３４]　", "", b).rstrip() for b in baris]
    else:  # semua opsi dalam satu baris
        opsi = [o[2:] for o in re.split(r"　　(?=[１２３４]　)", teks.strip())]
    assert len(opsi) == 4, (no, opsi)
    opsi.insert(baru[no] - 1, opsi.pop(lama[no] - 1))
    if len(baris) > 1:
        susun = f"{ANGKA[0]}　{opsi[0]}  \n" + "  \n".join(
            f"{indent}{ANGKA[j]}　{opsi[j]}" for j in range(1, 4))
    else:
        susun = "　　".join(f"{ANGKA[j]}　{opsi[j]}" for j in range(4))
    hasil += [f"{no}. ", badan.replace(teks, susun, 1)]
f_soal.write_text("".join(hasil) + pemisah + lembar_jawaban)

# Kunci: kunci cepat, lalu kolom Jwb di tabel per もんだい.
def ganti_cepat(m):
    return re.sub(r"(\d+) \| \d", lambda x: f"{x.group(1)} | {baru[int(x.group(1))]}", m.group(0))

kunci = re.sub(BARIS_CEPAT, ganti_cepat, kunci, flags=re.M)
kunci = re.sub(r"^\| (\d+) \| [1-4] \| (?!\d+ \|)",
               lambda m: f"| {m.group(1)} | {baru[int(m.group(1))]} | ", kunci, flags=re.M)
f_kunci.write_text(kunci)

print("Urutan jawaban baru:", "".join(str(baru[n]) for n in nomor))
