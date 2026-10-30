"""Cek lembar evaluasi format JLPT terhadap kuncinya.

Pakai: python3 soal/cek-kunci-evaluasi.py soal/evaluasi-bab-01-05

Mencetak teks opsi yang ditunjuk kunci untuk setiap soal (baca satu per satu
untuk memastikan jawabannya benar), lalu jumlah soal, sebaran jawaban 1–4,
dan kanji yang tersisa di lembar siswa.
"""
import collections
import pathlib
import re
import sys

folder = pathlib.Path(sys.argv[1])
blok = folder.name.removeprefix("evaluasi-")
soal = (folder / f"evaluasi-{blok}.md").read_text().split("# Lembar Jawaban")[0]
kunci = (folder / f"kunci-evaluasi-{blok}.md").read_text()

# Kunci cepat: baris tabel berisi pasangan "No | Jwb" berulang.
jawaban = {}
for baris in re.findall(r"^\|(?: \d+ \| \d \|)+$", kunci, re.M):
    for no, jwb in re.findall(r"(\d+) \| (\d)", baris):
        jawaban[int(no)] = int(jwb)

potong = re.split(r"^(\d+)\. ", soal, flags=re.M)
butir = {int(potong[i]): potong[i + 1] for i in range(1, len(potong), 2)}

ANGKA = "１２３４"
for no in sorted(butir):
    jwb = jawaban.get(no)
    if jwb is None:
        print(f"{no:>2}  TIDAK ADA DI KUNCI")
        continue
    # Opsi berakhir di opsi berikutnya ("　　２"), akhir baris, atau akhir butir.
    m = re.search(ANGKA[jwb - 1] + r"　(.*?)(?=　　[１２３４]|  \n|\n|$)", butir[no])
    print(f"{no:>2}  {jwb}  {m.group(1).strip() if m else '?? opsi tidak ditemukan'}")

print("\nJumlah soal:", len(butir), "· di kunci:", len(jawaban))
print("Sebaran jawaban:", dict(sorted(collections.Counter(jawaban.values()).items())))
print("Kanji di lembar siswa:", re.findall(r"[一-鿿]", soal) or "tidak ada")
