"""Membuat Aisatsu_Houkoku.docx dari isi.py.

Jalankan: python3 build.py
Hasil: Aisatsu_Houkoku.docx di folder yang sama.
"""

import re
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

import isi

DIR = Path(__file__).parent
OUT = DIR / "Aisatsu_Houkoku.docx"

FONT_LATIN = "Calibri"
FONT_JP = "Yu Gothic"

TEXT_W = 9638  # A4, margin 2 cm
C_ACCENT = "1F4E79"
C_ROMAJI = "1F6F78"
C_ARTI = "555555"
C_PH = "B35C00"
C_LINE = "D0D7DE"
SHADE_SENSEI = "EEF4FA"
SHADE_HEAD = "DCE8F3"

TOKEN = re.compile(r"\{([^|}]+)\|([^}]+)\}|\[([^\]]*)\]")


# ---------- run & paragraph ----------

def rpr(size=None, bold=False, italic=False, color=None):
    s = f'<w:rFonts w:ascii="{FONT_LATIN}" w:hAnsi="{FONT_LATIN}" w:eastAsia="{FONT_JP}" w:cs="{FONT_LATIN}"/>'
    if bold:
        s += "<w:b/>"
    if italic:
        s += "<w:i/>"
    if color:
        s += f'<w:color w:val="{color}"/>'
    if size:
        s += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    return f"<w:rPr>{s}</w:rPr>"


def run(text, **kw):
    return f'<w:r>{rpr(**kw)}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def ruby(base, reading, size, bold=False, color=None):
    rt = max(size // 2, 8)
    return (
        "<w:r><w:ruby><w:rubyPr>"
        '<w:rubyAlign w:val="distributeSpace"/>'
        f'<w:hps w:val="{rt}"/><w:hpsRaise w:val="{size - 2}"/>'
        f'<w:hpsBaseText w:val="{size}"/><w:lid w:val="ja-JP"/>'
        "</w:rubyPr>"
        f"<w:rt>{run(reading, size=rt, color=color)}</w:rt>"
        f"<w:rubyBase>{run(base, size=size, bold=bold, color=color)}</w:rubyBase>"
        "</w:ruby></w:r>"
    )


def runs(markup, size, jp=True, bold=False, italic=False, color=None):
    """Ubah notasi {漢字|よみ} dan [isian] menjadi run Word."""
    out, pos = [], 0
    for m in TOKEN.finditer(markup):
        if m.start() > pos:
            out.append(run(markup[pos:m.start()], size=size, bold=bold, italic=italic, color=color))
        if m.group(1):
            out.append(ruby(m.group(1), m.group(2), size, bold=bold, color=color))
        else:
            ph = m.group(3).strip()
            if jp:
                text = "（" + (ph or "　　") + "）"
            else:
                text = "(" + (ph or "   ") + ")"
            out.append(run(text, size=size, bold=bold, italic=italic, color=C_PH))
        pos = m.end()
    if pos < len(markup):
        out.append(run(markup[pos:], size=size, bold=bold, italic=italic, color=color))
    return "".join(out)


def para(content, style=None, before=0, after=0, line=None, align=None, keep_next=False,
         border_bottom=None, num=False, page_break=False):
    p = ""
    if style:
        p += f'<w:pStyle w:val="{style}"/>'
    if keep_next:
        p += "<w:keepNext/>"
    if page_break:
        p += "<w:pageBreakBefore/>"
    if num:
        p += '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
    if border_bottom:
        p += f'<w:pBdr><w:bottom w:val="single" w:sz="8" w:space="2" w:color="{border_bottom}"/></w:pBdr>'
    sp = f'w:before="{before}" w:after="{after}"'
    if line:
        sp += f' w:line="{line}" w:lineRule="auto"'
    p += f"<w:spacing {sp}/>"
    if align:
        p += f'<w:jc w:val="{align}"/>'
    return f"<w:p><w:pPr>{p}</w:pPr>{content}</w:p>"


# ---------- table ----------

def cell(content, width, shade=None, span=1, valign="top"):
    pr = f'<w:tcW w:w="{width}" w:type="dxa"/>'
    if span > 1:
        pr += f'<w:gridSpan w:val="{span}"/>'
    if shade:
        pr += f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>'
    pr += f'<w:vAlign w:val="{valign}"/>'
    return f"<w:tc><w:tcPr>{pr}</w:tcPr>{content}</w:tc>"


def table(widths, rows, header=False, outer=True, inside_v=False):
    b = lambda side, on: (f'<w:{side} w:val="single" w:sz="4" w:space="0" w:color="{C_LINE}"/>'
                          if on else f'<w:{side} w:val="nil"/>')
    borders = (b("top", outer) + b("left", inside_v) + b("bottom", outer) + b("right", inside_v)
               + b("insideH", True) + b("insideV", inside_v))
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    trs = []
    for i, r in enumerate(rows):
        trpr = '<w:trPr><w:cantSplit/>' + ('<w:tblHeader/>' if header and i == 0 else '') + '</w:trPr>'
        trs.append(f"<w:tr>{trpr}{r}</w:tr>")
    return (
        "<w:tbl><w:tblPr>"
        f'<w:tblW w:w="{sum(widths)}" w:type="dxa"/>'
        f"<w:tblBorders>{borders}</w:tblBorders>"
        '<w:tblLayout w:type="fixed"/>'
        '<w:tblCellMar><w:top w:w="50" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
        '<w:bottom w:w="50" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar>'
        f"</w:tblPr><w:tblGrid>{grid}</w:tblGrid>{''.join(trs)}</w:tbl>"
        + para("", after=60)
    )


def blok_bahasa(jp, romaji, arti, jp_size=24):
    """Tiga lapis: Jepang (furigana) / romaji / arti."""
    s = para(runs(jp, jp_size), line=264)
    if romaji:
        s += para(runs(romaji, 19, jp=False, italic=True, color=C_ROMAJI), line=240)
    if arti:
        s += para(runs(arti, 18, jp=False, color=C_ARTI), line=240)
    return s


SPEAKER_W = 1450


def dialog(baris):
    widths = [SPEAKER_W, TEXT_W - SPEAKER_W]
    rows = []
    for b in baris:
        if b[0] == "*":
            content = para(runs("▸ " + b[1], 18, jp=False, italic=True, color=C_ARTI))
            rows.append(cell(content, TEXT_W, span=2))
            continue
        who, jp, romaji, arti = b
        shade = SHADE_SENSEI if who == "Sensei" else None
        rows.append(
            cell(para(run(who, size=19, bold=True, color=C_ACCENT), line=264), widths[0], shade)
            + cell(blok_bahasa(jp, romaji, arti), widths[1], shade)
        )
    return table(widths, rows)


# ---------- heading ----------

def h1(nomor, jp, romaji, indo, page_break=True):
    content = (run(f"{nomor}.  ", size=36, bold=True, color=C_ACCENT)
               + runs(jp, 36, bold=True, color=C_ACCENT)
               + run(f"   {romaji} — {indo}", size=26, color=C_ACCENT))
    return para(content, style="Heading1", before=0, after=200, keep_next=True,
                border_bottom=C_ACCENT, page_break=page_break)


def h2(judul, jp=None, romaji=None):
    s = para(run(judul, size=26, bold=True, color=C_ACCENT), style="Heading2",
             before=280, after=40, keep_next=True)
    if jp:
        sub = runs(jp, 22)
        if romaji:
            sub += run("   " + romaji, size=19, italic=True, color=C_ROMAJI)
        s += para(sub, after=100, line=264, keep_next=True)
    return s


def catatan(text):
    return para(runs(text, 19, jp=False, color=C_ARTI), after=80, line=264)


def kotak(isi_xml, shade="F6F8FA"):
    return table([TEXT_W], [cell(isi_xml, TEXT_W, shade)])


def bullet(text):
    return para(runs(text, 20, jp=False), num=True, after=40, line=264)


# ---------- bagian dokumen ----------

def judul():
    s = para(runs("{挨拶|あいさつ}と{報告|ほうこく}", 48, bold=True, color=C_ACCENT),
             align="center", after=40, line=264)
    s += para(run("Aisatsu to Hōkoku", size=30, italic=True, color=C_ROMAJI), align="center", after=20)
    s += para(run("Salam dan Laporan — Pegangan Siswa", size=24, color=C_ARTI), align="center", after=300)

    contoh = (
        para(run("Cara membaca pegangan ini", size=22, bold=True, color=C_ACCENT), after=80)
        + para(run("Setiap kalimat ditulis tiga lapis:", size=19), after=60)
        + blok_bahasa("{失礼|しつれい}します。", "Shitsurei shimasu.", "Permisi.")
        + para(run("Baris 1: tulisan Jepang; huruf kecil di atas kanji adalah cara bacanya (furigana).  "
                   "Baris 2: romaji.  Baris 3: arti.", size=18, color=C_ARTI), before=80, after=80)
        + para(run("Pembicara: ", size=19, bold=True)
               + run("Leader = ketua kelas/piket (リーダー) · Semua = semua siswa (みんな) · "
                     "Siswa = siswa yang bertugas (実習生) · Petugas = anggota piket (係) · "
                     "Sensei = guru (baris berwarna biru)", size=19), after=60)
        + para(run("Isian: ", size=19, bold=True)
               + run("（nama）", size=19, color=C_PH)
               + run(" dan ", size=19)
               + run("（　　）", size=19, color=C_PH)
               + run(" diganti sesuai keadaan. ", size=19)
               + run("（salam）", size=19, color=C_PH)
               + run(" = おはようございます (pagi) / こんにちは (siang) / こんばんは (malam).", size=19))
    )
    return s + kotak(contoh)


def bagian_aisatsu():
    s = h1(1, "{挨拶|あいさつ}", "Aisatsu", "Salam", page_break=True)
    for i, sesi in enumerate(isi.AISATSU, 1):
        s += h2(f"1.{i}  {sesi['judul']}", sesi["jp"])
        s += dialog(sesi["baris"])
    return s


def tabel_counter():
    widths = [1500, 1100, 4838, 2200]
    head = "".join(cell(para(run(t, size=19, bold=True)), w, SHADE_HEAD)
                   for t, w in zip(["Counter", "Romaji", "Dipakai untuk", "Pertanyaan"], widths))
    rows = [head]
    for c, rom, guna, tanya, tanya_rom in isi.COUNTER:
        rows.append(
            cell(para(runs(c, 24), line=264), widths[0])
            + cell(para(run(rom, size=19, italic=True, color=C_ROMAJI)), widths[1])
            + cell(para(run(guna, size=19)), widths[2])
            + cell(para(runs(tanya, 22), line=264)
                   + para(run(tanya_rom, size=17, italic=True, color=C_ROMAJI)), widths[3])
        )
    return table(widths, rows, header=True)


def tabel_bacaan():
    n = len(isi.BACAAN)
    no_w = 640
    col_w = (TEXT_W - no_w) // n
    widths = [no_w] + [col_w] * n
    head = cell(para(run("No.", size=19, bold=True), align="center"), no_w, SHADE_HEAD)
    head += "".join(cell(para(runs(c, 22, bold=True), align="center", line=264), col_w, SHADE_HEAD)
                    for c, _, _ in isi.BACAAN)
    rows = [head]
    kana = [c[1].split() for c in isi.BACAAN]
    roma = [c[2].split() for c in isi.BACAAN]
    for i in range(10):
        r = cell(para(run(str(i + 1), size=19, bold=True), align="center"), no_w, SHADE_HEAD, valign="center")
        for k in range(n):
            r += cell(para(run(kana[k][i], size=19), align="center")
                      + para(run(roma[k][i], size=15, italic=True, color=C_ROMAJI), align="center"), col_w)
        rows.append(r)
    return table(widths, rows, header=True, inside_v=True)


def bagian_houkoku():
    s = h1(2, "{報告|ほうこく}", "Hōkoku", "Laporan")
    s += h2("2.1  Pola Pembuka Laporan", "{報告|ほうこく}の{始|はじ}め{方|かた}", "Hōkoku no hajimekata")
    s += catatan("Hampir semua laporan ke sensei dimulai dengan pola ini. Setelah itu, siswa memperkenalkan "
                 "diri dan menyebut tugasnya (係).")
    s += dialog(isi.PEMBUKA + [("Siswa",) + isi.PERKENALAN])

    s += h2("2.2  Cara Menghitung Benda dan Orang", "{数|かぞ}え{方|かた}", "Kazoekata")
    s += catatan("Dipakai saat melapor jumlah barang, buku, HP, atau siswa. Pola: benda は/が + jumlah + "
                 "counter + あります. Untuk orang: jumlah + 人 + います.")
    s += tabel_counter()
    s += para(run("Bacaan yang perlu dihafal", size=22, bold=True, color=C_ACCENT), before=120, after=80, keep_next=True)
    s += tabel_bacaan()
    for t in [
        "7人 bisa dibaca ななにん atau しちにん.",
        "回: 1回 いっかい, 6回 ろっかい, 8回 はっかい, 10回 じゅっかい; lainnya angka + かい.",
        "Di atas 10, gabungkan puluhan dan satuan: 12本 じゅうにほん, 23冊 にじゅうさんさつ. "
        "Kelipatan 10: 20本 にじゅっぽん, 20冊 にじゅっさつ, 20個 にじゅっこ.",
        "つ hanya sampai 10. Untuk 11 ke atas, pakai counter yang sesuai, misalnya 個.",
    ]:
        s += bullet(t)
    s += para(run("Contoh laporan:", size=19, bold=True), before=80, after=40, keep_next=True)
    s += kotak(
        blok_bahasa("{雑巾|ぞうきん}は{三枚|さんまい}あります。", "Zōkin wa sanmai arimasu.", "Ada 3 lap.")
        + para("", after=40)
        + blok_bahasa("ほうきは{二本|にほん}あります。", "Hōki wa nihon arimasu.", "Ada 2 sapu.")
        + para("", after=40)
        + blok_bahasa("{学生|がくせい}は{二十人|にじゅうにん}います。", "Gakusei wa nijūnin imasu.", "Ada 20 siswa.")
    )

    for i, sesi in enumerate(isi.HOUKOKU, 3):
        s += h2(f"2.{i}  {sesi['judul']}", sesi["jp"], sesi["romaji"])
        s += dialog([("*", "Mulai dengan Pola Pembuka (2.1).")] + sesi["baris"])
    return s


def bagian_souji():
    s = h1(3, "{掃除|そうじ}", "Sōji", "Bersih-bersih")
    s += h2("3.1  Nama Alat Kebersihan", "{掃除|そうじ}{道具|どうぐ}", "Sōji dōgu")
    widths = [600, 2600, 2400, 2338, 1700]
    head = "".join(cell(para(run(t, size=19, bold=True)), w, SHADE_HEAD)
                   for t, w in zip(["No.", "Bahasa Indonesia", "Bahasa Jepang", "Romaji", "Counter"], widths))
    rows = [head]
    for n, (indo, jp, rom, ctr) in enumerate(isi.ALAT_SOUJI, 1):
        rows.append(
            cell(para(run(str(n), size=19)), widths[0])
            + cell(para(run(indo, size=20)), widths[1])
            + cell(para(runs(jp, 24), line=264), widths[2])
            + cell(para(run(rom, size=19, italic=True, color=C_ROMAJI)), widths[3])
            + cell(para(runs(ctr, 22), line=264), widths[4])
        )
    s += table(widths, rows, header=True)

    for i, sesi in enumerate(isi.SOUJI, 2):
        s += h2(f"3.{i}  {sesi['judul']}", sesi["jp"], sesi["romaji"])
        baris = sesi["baris"]
        if sesi.get("pembuka"):
            baris = [("*", "Mulai dengan Pola Pembuka (2.1).")] + baris
        s += dialog(baris)
    return s


def bagian_penalti():
    s = h1(4, "ペナルティ", "Penaruti", "Penalti")
    for i, sesi in enumerate(isi.PENALTI, 1):
        s += h2(f"4.{i}  {sesi['judul']}", sesi["jp"], sesi["romaji"])
        s += dialog(sesi["baris"])
    return s


def bagian_kokorogamae():
    s = h1(5, "{実習生|じっしゅうせい}の{心構|こころがま}え", "Jisshūsei no Kokorogamae",
           "Sikap Peserta Praktik Kerja")
    widths = [600, TEXT_W - 600]
    rows = []
    for n, (jp, rom, arti) in enumerate(isi.KOKOROGAMAE, 1):
        rows.append(cell(para(run(f"{n}.", size=22, bold=True, color=C_ACCENT), line=264), widths[0])
                    + cell(blok_bahasa(jp, rom, arti), widths[1]))
    s += table(widths, rows)
    return s


# ---------- paket docx ----------

STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults>
<w:rPrDefault><w:rPr><w:rFonts w:ascii="{FONT_LATIN}" w:hAnsi="{FONT_LATIN}" w:eastAsia="{FONT_JP}" w:cs="{FONT_LATIN}"/>
<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="id-ID" w:eastAsia="ja-JP"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
<w:qFormat/><w:pPr><w:keepNext/><w:outlineLvl w:val="0"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>
<w:qFormat/><w:pPr><w:keepNext/><w:outlineLvl w:val="1"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Footer"><w:name w:val="footer"/><w:basedOn w:val="Normal"/></w:style>
<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>
<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>
<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""

NUMBERING = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="singleLevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/>
<w:pPr><w:ind w:left="400" w:hanging="260"/></w:pPr></w:lvl></w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>"""

FOOTER = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:p><w:pPr><w:pStyle w:val="Footer"/><w:jc w:val="center"/></w:pPr>
{run("Aisatsu & Hōkoku  ·  ", size=16, color=C_ARTI)}
<w:r>{rpr(size=16, color=C_ARTI)}<w:fldChar w:fldCharType="begin"/></w:r>
<w:r>{rpr(size=16, color=C_ARTI)}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>
<w:r>{rpr(size=16, color=C_ARTI)}<w:fldChar w:fldCharType="separate"/></w:r>
<w:r>{rpr(size=16, color=C_ARTI)}<w:t>1</w:t></w:r>
<w:r>{rpr(size=16, color=C_ARTI)}<w:fldChar w:fldCharType="end"/></w:r>
</w:p></w:ftr>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>"""

CORE = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>Aisatsu &amp; Houkoku — Pegangan Siswa</dc:title><dc:language>id-ID</dc:language>
</cp:coreProperties>"""


def document():
    body = judul() + bagian_aisatsu() + bagian_houkoku() + bagian_souji() + bagian_penalti() + bagian_kokorogamae()
    sect = (
        '<w:sectPr><w:footerReference w:type="default" r:id="rId3"/>'
        '<w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1000" w:right="1134" w:bottom="1000" w:left="1134" w:header="500" w:footer="500" w:gutter="0"/>'
        "</w:sectPr>"
    )
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        f"<w:body>{body}{sect}</w:body></w:document>"
    )


def main():
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("docProps/core.xml", CORE)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", document())
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)
        z.writestr("word/footer1.xml", FOOTER)
    print(OUT)


if __name__ == "__main__":
    main()
