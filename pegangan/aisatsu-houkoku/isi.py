# Isi pegangan Aisatsu & Houkoku.
#
# Notasi:
#   {漢字|かんじ}  -> kanji dengan furigana
#   [teks]         -> isian/placeholder, ditampilkan sebagai （teks） berwarna
#
# Baris dialog: (pembicara, jepang, romaji, arti)
# Baris catatan: ("*", "teks catatan bahasa Indonesia")

PEMBUKA = [
    ("Siswa", "{失礼|しつれい}します。{入|はい}ってもいいですか。",
     "Shitsurei shimasu. Haitte mo ii desu ka.",
     "Permisi. Bolehkah saya masuk?"),
    ("Sensei", "はい。", "Hai.", "Ya."),
    ("Siswa", "[salam]。すみません、[nama]{先生|せんせい}。{今|いま}よろしいですか。",
     "[salam]. Sumimasen, [nama] sensei. Ima yoroshii desu ka.",
     "[salam]. Maaf, [nama] Sensei. Apakah sekarang ada waktu?"),
    ("Sensei", "はい。", "Hai.", "Ya."),
]

PERKENALAN = ("{私|わたし}は[nama kelas]クラスの[nama]です。",
              "Watashi wa [nama kelas] kurasu no [nama] desu.",
              "Saya [nama] dari kelas [nama kelas].")

HAI = ("Sensei", "はい。", "Hai.", "Ya.")


def kenalan(jp, romaji, arti, pembicara="Siswa"):
    """Baris perkenalan diri + kalimat tugas, setelah pola pembuka."""
    return (pembicara, PERKENALAN[0] + jp, PERKENALAN[1] + " " + romaji,
            PERKENALAN[2] + " " + arti)


AISATSU = [
    {
        "judul": "Mulai Belajar",
        "jp": "{勉強|べんきょう}を{始|はじ}めるとき",
        "baris": [
            ("Leader", "{皆|みな}さん、{立|た}ってください。", "Minasan, tatte kudasai.",
             "Semuanya, silakan berdiri."),
            ("Semua", "はい。", "Hai.", "Ya."),
            ("Leader", "{気|き}をつけ。{礼|れい}。", "Ki o tsuke. Rei.",
             "Siap. Beri hormat."),
            ("Semua", "おはようございます。／こんにちは。",
             "Ohayō gozaimasu. / Konnichiwa.",
             "Selamat pagi. / Selamat siang. (sesuaikan dengan waktu)"),
            ("Sensei", "おはようございます。／こんにちは。",
             "Ohayō gozaimasu. / Konnichiwa.",
             "Selamat pagi. / Selamat siang."),
            ("Leader", "{礼|れい}！", "Rei!", "Membungkuk!"),
            ("Semua", "どうぞよろしくお{願|ねが}いします。",
             "Dōzo yoroshiku onegai shimasu.", "Mohon bimbingannya."),
            ("Sensei", "こちらこそ、よろしくお{願|ねが}いします。",
             "Kochira koso, yoroshiku onegai shimasu.", "Saya juga, mohon kerja samanya."),
            ("Leader", "{座|すわ}ってください。", "Suwatte kudasai.", "Silakan duduk."),
            ("Semua", "はい。", "Hai.", "Ya."),
            ("Leader", "{勉強|べんきょう}する{前|まえ}に、{一緒|いっしょ}にお{祈|いの}りしましょう。",
             "Benkyō suru mae ni, issho ni oinori shimashō.",
             "Sebelum belajar, mari kita berdoa bersama."),
            ("Semua", "はい、そうしましょう。", "Hai, sō shimashō.", "Ya, mari."),
            ("Leader", "{始|はじ}めてください。", "Hajimete kudasai.",
             "Silakan dimulai. (Al-Fatihah)"),
            ("*", "Berdoa masing-masing, lalu Asmaul Husna."),
            ("Leader", "{終|お}わります。", "Owarimasu.", "Selesai."),
            ("Semua", "{終|お}わりました。", "Owarimashita.", "Sudah selesai."),
        ],
    },
    {
        "judul": "Selesai Belajar",
        "jp": "{勉強|べんきょう}が{終|お}わるとき",
        "baris": [
            ("Leader", "{皆|みな}さん、{立|た}ってください。", "Minasan, tatte kudasai.",
             "Semuanya, silakan berdiri."),
            ("Semua", "はい。", "Hai.", "Ya."),
            ("Leader", "{気|き}をつけ。{礼|れい}。", "Ki o tsuke. Rei.",
             "Siap. Beri hormat."),
            ("Semua", "こんにちは。／こんばんは。", "Konnichiwa. / Konbanwa.",
             "Selamat siang. / Selamat malam. (sesuaikan dengan waktu)"),
            ("Sensei", "こんにちは。／こんばんは。", "Konnichiwa. / Konbanwa.",
             "Selamat siang. / Selamat malam."),
            ("Leader", "{礼|れい}！", "Rei!", "Membungkuk!"),
            ("Semua", "どうもありがとうございました。", "Dōmo arigatō gozaimashita.",
             "Terima kasih banyak."),
            ("Sensei", "どういたしまして。", "Dō itashimashite.", "Sama-sama."),
            ("Leader", "{勉強|べんきょう}が{終|お}わってから、{一緒|いっしょ}にお{祈|いの}りしましょう。",
             "Benkyō ga owatte kara, issho ni oinori shimashō.",
             "Setelah belajar selesai, mari kita berdoa bersama."),
            ("Semua", "はい、そうしましょう。", "Hai, sō shimashō.", "Ya, mari."),
            ("Leader", "{始|はじ}めてください。", "Hajimete kudasai.",
             "Silakan dimulai. (Al-Fatihah)"),
            ("*", "Berdoa masing-masing."),
            ("Leader", "{終|お}わります。{礼|れい}。", "Owarimasu. Rei.",
             "Selesai. Beri hormat."),
            ("Semua", "お{先|さき}に{失礼|しつれい}します。", "Osaki ni shitsurei shimasu.",
             "Saya permisi pulang duluan."),
            ("Sensei", "はい、お{疲|つか}れさまでした。", "Hai, otsukaresama deshita.",
             "Ya, terima kasih atas kerja kerasnya."),
            ("Semua", "お{疲|つか}れさまでした。", "Otsukaresama deshita.",
             "Terima kasih atas kerja kerasnya."),
        ],
    },
]

# (Indonesia, jepang, romaji, counter)
ALAT_SOUJI = [
    ("Lap", "{雑巾|ぞうきん}", "zōkin", "{枚|まい}"),
    ("Kemoceng / sulak", "{羽|はね}ぼうき", "hanebōki", "{本|ほん}"),
    ("Ember", "バケツ", "baketsu", "{個|こ}"),
    ("Cairan pembersih", "{洗剤|せんざい}", "senzai", "{本|ほん}"),
    ("Sapu", "ほうき", "hōki", "{本|ほん}"),
    ("Pengki / serok", "ちりとり", "chiritori", "{個|こ}"),
    ("Pel", "モップ", "moppu", "{本|ほん}"),
]

# (counter, dipakai untuk, pertanyaan, romaji pertanyaan)
COUNTER = [
    ("{枚|まい}", "mai", "Benda tipis: lap, kertas, formulir", "{何枚|なんまい}", "nanmai"),
    ("{本|ほん}", "hon", "Benda panjang: spidol, sapu, pel, kemoceng, botol", "{何本|なんぼん}", "nanbon"),
    ("{冊|さつ}", "satsu", "Buku, buku PR", "{何冊|なんさつ}", "nansatsu"),
    ("{台|だい}", "dai", "Mesin/perangkat: HP, komputer", "{何台|なんだい}", "nandai"),
    ("{個|こ}", "ko", "Benda satuan: penghapus, ember, kotak alat, tempat sampah", "{何個|なんこ}", "nanko"),
    ("{人|にん}", "nin", "Orang, siswa", "{何人|なんにん}", "nannin"),
    ("つ", "tsu", "Hitungan umum benda, 1–10 saja", "いくつ", "ikutsu"),
    ("{回|かい}", "kai", "Berapa kali (tindakan)", "{何回|なんかい}", "nankai"),
]

# Kolom tabel bacaan: (counter, [10 bacaan hiragana], [10 romaji])
BACAAN = [
    ("{枚|まい}",
     "いちまい にまい さんまい よんまい ごまい ろくまい ななまい はちまい きゅうまい じゅうまい",
     "ichimai nimai sanmai yonmai gomai rokumai nanamai hachimai kyūmai jūmai"),
    ("{本|ほん}",
     "いっぽん にほん さんぼん よんほん ごほん ろっぽん ななほん はっぽん きゅうほん じゅっぽん",
     "ippon nihon sanbon yonhon gohon roppon nanahon happon kyūhon juppon"),
    ("{冊|さつ}",
     "いっさつ にさつ さんさつ よんさつ ごさつ ろくさつ ななさつ はっさつ きゅうさつ じゅっさつ",
     "issatsu nisatsu sansatsu yonsatsu gosatsu rokusatsu nanasatsu hassatsu kyūsatsu jussatsu"),
    ("{台|だい}",
     "いちだい にだい さんだい よんだい ごだい ろくだい ななだい はちだい きゅうだい じゅうだい",
     "ichidai nidai sandai yondai godai rokudai nanadai hachidai kyūdai jūdai"),
    ("{個|こ}",
     "いっこ にこ さんこ よんこ ごこ ろっこ ななこ はっこ きゅうこ じゅっこ",
     "ikko niko sanko yonko goko rokko nanako hakko kyūko jukko"),
    ("{人|にん}",
     "ひとり ふたり さんにん よにん ごにん ろくにん ななにん はちにん きゅうにん じゅうにん",
     "hitori futari sannin yonin gonin rokunin nananin hachinin kyūnin jūnin"),
    ("つ",
     "ひとつ ふたつ みっつ よっつ いつつ むっつ ななつ やっつ ここのつ とお",
     "hitotsu futatsu mittsu yottsu itsutsu muttsu nanatsu yattsu kokonotsu tō"),
]

CEK_ALAT_JP = [
    ("マーカーが[　]{本|ほん}あります。", "Māka ga [ ] hon arimasu.", "Ada [ ] spidol."),
    ("{赤|あか}いマーカーが[　]{本|ほん}あります。", "Akai māka ga [ ] hon arimasu.", "Ada [ ] spidol merah."),
    ("{青|あお}いマーカーが[　]{本|ほん}あります。", "Aoi māka ga [ ] hon arimasu.", "Ada [ ] spidol biru."),
    ("{黒|くろ}いマーカーが[　]{本|ほん}あります。", "Kuroi māka ga [ ] hon arimasu.", "Ada [ ] spidol hitam."),
    ("イレーザーが[　]{個|こ}あります。", "Irēzā ga [ ] ko arimasu.", "Ada [ ] penghapus papan."),
    ("{道具箱|どうぐばこ}が[　]{個|こ}あります。", "Dōgubako ga [ ] ko arimasu.", "Ada [ ] kotak alat."),
    ("ごみ{箱|ばこ}が[　]{個|こ}あります。", "Gomibako ga [ ] ko arimasu.", "Ada [ ] tempat sampah."),
]


def cek_alat(penutup_jp, penutup_romaji, penutup_arti):
    jp = "".join(x[0] for x in CEK_ALAT_JP)
    return ("Siswa", jp + "{授業|じゅぎょう}{道具|どうぐ}のチェックが{終|お}わりました。" + penutup_jp,
            " ".join(x[1] for x in CEK_ALAT_JP) + " Jugyō dōgu no chekku ga owarimashita. " + penutup_romaji,
            "Ada [ ] spidol, [ ] spidol merah, [ ] spidol biru, [ ] spidol hitam, [ ] penghapus, "
            "[ ] kotak alat, [ ] tempat sampah. Pengecekan alat pelajaran sudah selesai. " + penutup_arti)


HOUKOKU = [
    {
        "judul": "Kelas Sudah Siap",
        "jp": "{準備|じゅんび}の{報告|ほうこく}の{係|かかり}",
        "romaji": "Junbi no hōkoku no kakari",
        "baris": [
            kenalan("{準備|じゅんび}の{報告|ほうこく}の{係|かかり}です。クラスは[　]{人|にん}います。",
                    "Junbi no hōkoku no kakari desu. Kurasu wa [ ] nin imasu.",
                    "Saya petugas laporan persiapan. Di kelas ada [ ] orang."),
            ("*", "Jika semua hadir:"),
            ("Siswa", "みんないます。", "Minna imasu.", "Semua hadir."),
            ("*", "Jika ada yang tidak hadir:"),
            ("Siswa", "[　]{人|にん}いません。{名前|なまえ}は[nama]さんと[nama]さんです。",
             "[ ] nin imasen. Namae wa [nama]-san to [nama]-san desu.",
             "[ ] orang tidak hadir. Namanya [nama] dan [nama]."),
            ("Siswa", "{勉強|べんきょう}の{準備|じゅんび}ができました。お{願|ねが}いします。",
             "Benkyō no junbi ga dekimashita. Onegai shimasu.",
             "Persiapan belajar sudah siap. Mohon bimbingannya."),
            ("Sensei", "[menyebut satu kosakata]", "", "Sensei menyebut satu kosakata yang sudah dipelajari."),
            ("Siswa", "[kosakata]ですね。はい、わかりました。{失礼|しつれい}します。",
             "[kosakata] desu ne. Hai, wakarimashita. Shitsurei shimasu.",
             "[kosakata], ya. Baik, saya mengerti. Permisi."),
        ],
    },
    {
        "judul": "Meminta PR",
        "jp": "{宿題|しゅくだい}をお{願|ねが}いする{係|かかり}",
        "romaji": "Shukudai o onegai suru kakari",
        "baris": [
            kenalan("{宿題|しゅくだい}をお{願|ねが}いする{係|かかり}です。{宿題|しゅくだい}をお{願|ねが}いします。",
                    "Shukudai o onegai suru kakari desu. Shukudai o onegai shimasu.",
                    "Saya petugas meminta PR. Mohon PR-nya."),
            ("Sensei", "はい。", "Hai.", "Ya. (memberikan PR)"),
            ("Siswa", "はい、わかりました。{失礼|しつれい}します。",
             "Hai, wakarimashita. Shitsurei shimasu.", "Baik, saya mengerti. Permisi."),
        ],
    },
    {
        "judul": "Meminjam Alat Pelajaran",
        "jp": "{授業|じゅぎょう}{道具|どうぐ}を{借|か}りる{係|かかり}",
        "romaji": "Jugyō dōgu o kariru kakari",
        "baris": [
            kenalan("{授業|じゅぎょう}{道具|どうぐ}を{借|か}りる{係|かかり}です。{授業|じゅぎょう}{道具|どうぐ}を{借|か}りてもいいですか。",
                    "Jugyō dōgu o kariru kakari desu. Jugyō dōgu o karite mo ii desu ka.",
                    "Saya petugas meminjam alat pelajaran. Bolehkah saya meminjam alat pelajaran?"),
            HAI,
            ("Siswa", "{失礼|しつれい}します。", "Shitsurei shimasu.", "Permisi. (mengambil alat)"),
            ("Siswa", "{授業|じゅぎょう}{道具|どうぐ}を{持|も}ってきました。チェックをお{願|ねが}いします。",
             "Jugyō dōgu o motte kimashita. Chekku o onegai shimasu.",
             "Saya sudah membawa alat pelajaran. Mohon dicek."),
            HAI,
            cek_alat("{授業|じゅぎょう}{道具|どうぐ}を{教室|きょうしつ}に{持|も}っていってもいいですか。",
                     "Jugyō dōgu o kyōshitsu ni motte itte mo ii desu ka.",
                     "Bolehkah saya membawa alat pelajaran ke kelas?"),
            HAI,
            ("Siswa", "{以上|いじょう}です。{失礼|しつれい}します。", "Ijō desu. Shitsurei shimasu.",
             "Sekian. Permisi."),
        ],
    },
    {
        "judul": "Mengembalikan Alat Pelajaran",
        "jp": "{授業|じゅぎょう}{道具|どうぐ}を{返|かえ}す{係|かかり}",
        "romaji": "Jugyō dōgu o kaesu kakari",
        "baris": [
            kenalan("{授業|じゅぎょう}{道具|どうぐ}を{返|かえ}す{係|かかり}です。{授業|じゅぎょう}{道具|どうぐ}を{返|かえ}します。チェックをお{願|ねが}いします。",
                    "Jugyō dōgu o kaesu kakari desu. Jugyō dōgu o kaeshimasu. Chekku o onegai shimasu.",
                    "Saya petugas mengembalikan alat pelajaran. Saya kembalikan alat pelajaran. Mohon dicek."),
            HAI,
            cek_alat("{授業|じゅぎょう}{道具|どうぐ}をどこに{置|お}きますか。",
                     "Jugyō dōgu o doko ni okimasu ka.",
                     "Alat pelajaran diletakkan di mana?"),
            ("Sensei", "{元|もと}の{所|ところ}に{戻|もど}してください。", "Moto no tokoro ni modoshite kudasai.",
             "Tolong kembalikan ke tempat semula. (bisa juga: {置|お}いてください)"),
            ("Siswa", "{元|もと}の{所|ところ}に{戻|もど}しますね。はい、わかりました。{失礼|しつれい}します。",
             "Moto no tokoro ni modoshimasu ne. Hai, wakarimashita. Shitsurei shimasu.",
             "Dikembalikan ke tempat semula, ya. Baik, saya mengerti. Permisi."),
            ("*", "Mengembalikan alat ke tempat semula, lalu kembali ke sensei."),
            ("Siswa", "{失礼|しつれい}します。{授業|じゅぎょう}{道具|どうぐ}を{元|もと}の{所|ところ}に{戻|もど}しました。{以上|いじょう}です。{失礼|しつれい}します。",
             "Shitsurei shimasu. Jugyō dōgu o moto no tokoro ni modoshimashita. Ijō desu. Shitsurei shimasu.",
             "Permisi. Alat pelajaran sudah saya kembalikan ke tempat semula. Sekian. Permisi."),
        ],
    },
    {
        "judul": "Mengumpulkan PR",
        "jp": "{宿題|しゅくだい}を{集|あつ}める{係|かかり}",
        "romaji": "Shukudai o atsumeru kakari",
        "baris": [
            kenalan("{宿題|しゅくだい}を{集|あつ}める{係|かかり}です。みんなの{宿題|しゅくだい}を{集|あつ}めてもいいですか。",
                    "Shukudai o atsumeru kakari desu. Minna no shukudai o atsumete mo ii desu ka.",
                    "Saya petugas mengumpulkan PR. Bolehkah saya mengumpulkan PR semua siswa?"),
            HAI,
            ("*", "Mengumpulkan buku PR, lalu kembali ke sensei."),
            ("Siswa", "チェックをお{願|ねが}いします。", "Chekku o onegai shimasu.", "Mohon dicek."),
            HAI,
            ("Siswa", "クラスは[　]{人|にん}います。{宿題|しゅくだい}は{一冊|いっさつ}、{二冊|にさつ}、…。"
                      "みんなの{宿題|しゅくだい}は[　]{冊|さつ}あります。チェックが{終|お}わりました。"
                      "みんなの{宿題|しゅくだい}をどこに{置|お}きますか。",
             "Kurasu wa [ ] nin imasu. Shukudai wa issatsu, nisatsu, … . "
             "Minna no shukudai wa [ ] satsu arimasu. Chekku ga owarimashita. "
             "Minna no shukudai o doko ni okimasu ka.",
             "Di kelas ada [ ] orang. PR-nya satu, dua, … (hitung sampai buku terakhir). "
             "PR semua siswa ada [ ] buku. Pengecekan selesai. PR-nya diletakkan di mana?"),
            ("Sensei", "{教室|きょうしつ}の{先生|せんせい}の{机|つくえ}の{上|うえ}に{置|お}いてください。",
             "Kyōshitsu no sensei no tsukue no ue ni oite kudasai.",
             "Tolong letakkan di atas meja sensei di kelas."),
            ("Siswa", "{教室|きょうしつ}の{先生|せんせい}の{机|つくえ}の{上|うえ}に{置|お}きますね。"
                      "はい、わかりました。{以上|いじょう}です。{失礼|しつれい}します。",
             "Kyōshitsu no sensei no tsukue no ue ni okimasu ne. Hai, wakarimashita. Ijō desu. Shitsurei shimasu.",
             "Diletakkan di atas meja sensei di kelas, ya. Baik, saya mengerti. Sekian. Permisi."),
        ],
    },
    {
        "judul": "Mengambil PR",
        "jp": "{宿題|しゅくだい}を{持|も}って{帰|かえ}る{係|かかり}",
        "romaji": "Shukudai o motte kaeru kakari",
        "baris": [
            kenalan("{宿題|しゅくだい}を{持|も}って{帰|かえ}る{係|かかり}です。みんなの{宿題|しゅくだい}を{持|も}って{帰|かえ}ってもいいですか。",
                    "Shukudai o motte kaeru kakari desu. Minna no shukudai o motte kaette mo ii desu ka.",
                    "Saya petugas mengambil PR. Bolehkah saya membawa kembali PR semua siswa?"),
            HAI,
            ("*", "Mengambil buku PR, lalu kembali ke sensei."),
            ("Siswa", "{失礼|しつれい}します。みんなの{宿題|しゅくだい}を{取|と}りました。チェックをお{願|ねが}いします。",
             "Shitsurei shimasu. Minna no shukudai o torimashita. Chekku o onegai shimasu.",
             "Permisi. PR semua siswa sudah saya ambil. Mohon dicek."),
            HAI,
            ("Siswa", "クラスは[　]{人|にん}います。{宿題|しゅくだい}は{一冊|いっさつ}、{二冊|にさつ}、…。"
                      "みんなの{宿題|しゅくだい}は[　]{冊|さつ}あります。チェックが{終|お}わりました。"
                      "みんなの{宿題|しゅくだい}を{持|も}って{帰|かえ}ってもいいですか。",
             "Kurasu wa [ ] nin imasu. Shukudai wa issatsu, nisatsu, … . "
             "Minna no shukudai wa [ ] satsu arimasu. Chekku ga owarimashita. "
             "Minna no shukudai o motte kaette mo ii desu ka.",
             "Di kelas ada [ ] orang. PR-nya satu, dua, … (hitung sampai buku terakhir). "
             "PR semua siswa ada [ ] buku. Pengecekan selesai. Bolehkah saya membawanya kembali?"),
            HAI,
            ("Siswa", "{以上|いじょう}です。{失礼|しつれい}します。", "Ijō desu. Shitsurei shimasu.",
             "Sekian. Permisi."),
        ],
    },
    {
        "judul": "Mengumpulkan HP",
        "jp": "{携帯電話|けいたいでんわ}を{集|あつ}める{係|かかり}",
        "romaji": "Keitai denwa o atsumeru kakari",
        "baris": [
            kenalan("{携帯電話|けいたいでんわ}を{集|あつ}める{係|かかり}です。みんなの{携帯電話|けいたいでんわ}を{集|あつ}めてもいいですか。",
                    "Keitai denwa o atsumeru kakari desu. Minna no keitai denwa o atsumete mo ii desu ka.",
                    "Saya petugas mengumpulkan HP. Bolehkah saya mengumpulkan HP semua siswa?"),
            HAI,
            ("*", "Mengumpulkan HP, lalu kembali ke sensei."),
            ("Siswa", "チェックをお{願|ねが}いします。", "Chekku o onegai shimasu.", "Mohon dicek."),
            HAI,
            ("Siswa", "クラスは[　]{人|にん}います。{携帯電話|けいたいでんわ}は{一台|いちだい}、{二台|にだい}、…。"
                      "みんなの{携帯電話|けいたいでんわ}は[　]{台|だい}あります。チェックが{終|お}わりました。"
                      "みんなの{携帯電話|けいたいでんわ}をどこに{置|お}きますか。",
             "Kurasu wa [ ] nin imasu. Keitai denwa wa ichidai, nidai, … . "
             "Minna no keitai denwa wa [ ] dai arimasu. Chekku ga owarimashita. "
             "Minna no keitai denwa o doko ni okimasu ka.",
             "Di kelas ada [ ] orang. HP-nya satu, dua, … (hitung sampai HP terakhir). "
             "HP semua siswa ada [ ] buah. Pengecekan selesai. HP-nya diletakkan di mana?"),
            ("Sensei", "{引|ひ}き{出|だ}しの{中|なか}に{置|お}いてください。",
             "Hikidashi no naka ni oite kudasai.", "Tolong letakkan di dalam laci."),
            ("*", "Dengarkan baik-baik kalimat sensei. Tempatnya bisa berbeda, misalnya {床|ゆか}に (di lantai)."),
            ("Siswa", "{引|ひ}き{出|だ}しの{中|なか}に{置|お}きますね。はい、わかりました。",
             "Hikidashi no naka ni okimasu ne. Hai, wakarimashita.",
             "Diletakkan di dalam laci, ya. Baik, saya mengerti. (meletakkan HP)"),
            ("Siswa", "みんなの{携帯電話|けいたいでんわ}を{引|ひ}き{出|だ}しの{中|なか}に{置|お}きました。"
                      "{以上|いじょう}です。{失礼|しつれい}します。",
             "Minna no keitai denwa o hikidashi no naka ni okimashita. Ijō desu. Shitsurei shimasu.",
             "HP semua siswa sudah saya letakkan di dalam laci. Sekian. Permisi."),
        ],
    },
    {
        "judul": "Mengambil HP",
        "jp": "{携帯電話|けいたいでんわ}を{持|も}って{帰|かえ}る{係|かかり}",
        "romaji": "Keitai denwa o motte kaeru kakari",
        "baris": [
            kenalan("{携帯電話|けいたいでんわ}を{持|も}って{帰|かえ}る{係|かかり}です。みんなの{携帯電話|けいたいでんわ}を{持|も}って{帰|かえ}ってもいいですか。",
                    "Keitai denwa o motte kaeru kakari desu. Minna no keitai denwa o motte kaette mo ii desu ka.",
                    "Saya petugas mengambil HP. Bolehkah saya membawa kembali HP semua siswa?"),
            HAI,
            ("Siswa", "{失礼|しつれい}します。", "Shitsurei shimasu.", "Permisi. (mengambil HP)"),
            ("Siswa", "みんなの{携帯電話|けいたいでんわ}を{取|と}りました。チェックをお{願|ねが}いします。",
             "Minna no keitai denwa o torimashita. Chekku o onegai shimasu.",
             "HP semua siswa sudah saya ambil. Mohon dicek."),
            HAI,
            ("Siswa", "クラスは[　]{人|にん}います。{携帯電話|けいたいでんわ}は{一台|いちだい}、{二台|にだい}、…。"
                      "みんなの{携帯電話|けいたいでんわ}は[　]{台|だい}あります。チェックが{終|お}わりました。"
                      "みんなの{携帯電話|けいたいでんわ}を{持|も}って{帰|かえ}ってもいいですか。",
             "Kurasu wa [ ] nin imasu. Keitai denwa wa ichidai, nidai, … . "
             "Minna no keitai denwa wa [ ] dai arimasu. Chekku ga owarimashita. "
             "Minna no keitai denwa o motte kaette mo ii desu ka.",
             "Di kelas ada [ ] orang. HP-nya satu, dua, … (hitung sampai HP terakhir). "
             "HP semua siswa ada [ ] buah. Pengecekan selesai. Bolehkah saya membawanya kembali?"),
            HAI,
            ("Siswa", "{以上|いじょう}です。{失礼|しつれい}します。", "Ijō desu. Shitsurei shimasu.",
             "Sekian. Permisi."),
        ],
    },
]

SOUJI = [
    {
        "judul": "Meminjam Alat Kebersihan",
        "jp": "{掃除|そうじ}{道具|どうぐ}を{借|か}りる",
        "romaji": "Sōji dōgu o kariru",
        "pembuka": True,
        "baris": [
            kenalan("{掃除|そうじ}{当番|とうばん}です。{掃除|そうじ}{道具|どうぐ}を{借|か}りてもいいですか。",
                    "Sōji tōban desu. Sōji dōgu o karite mo ii desu ka.",
                    "Saya petugas piket. Bolehkah saya meminjam alat kebersihan?"),
            HAI,
            ("Siswa", "{失礼|しつれい}します。", "Shitsurei shimasu.", "Permisi. (mengambil alat kebersihan)"),
            HAI,
            ("Siswa", "{掃除|そうじ}{道具|どうぐ}を{取|と}りました。チェックをお{願|ねが}いします。",
             "Sōji dōgu o torimashita. Chekku o onegai shimasu.",
             "Alat kebersihan sudah saya ambil. Mohon dicek. (sambil membungkuk)"),
            HAI,
        ],
    },
    {
        "judul": "Leader Mengecek Jumlah Alat",
        "jp": "{掃除|そうじ}{道具|どうぐ}のチェック",
        "romaji": "Sōji dōgu no chekku",
        "baris": [
            ("Leader", "{皆|みな}さん、{掃除|そうじ}{道具|どうぐ}をチェックしましょう。",
             "Minasan, sōji dōgu o chekku shimashō.", "Semuanya, mari kita cek alat kebersihan."),
            ("Petugas", "そうしましょう。", "Sō shimashō.", "Mari."),
            ("Leader", "[nama alat]は{何枚|なんまい}／{何本|なんぼん}／いくつありますか。",
             "[nama alat] wa nanmai / nanbon / ikutsu arimasu ka.",
             "[nama alat] ada berapa? (pakai counter yang sesuai)"),
            ("Petugas", "[jumlah + counter]あります。", "[jumlah + counter] arimasu.",
             "Ada [jumlah]. Contoh: {雑巾|ぞうきん}は{三枚|さんまい}あります。"),
            ("Leader", "[jumlah + counter]あるんですね。", "[jumlah + counter] aru n desu ne.",
             "Ada [jumlah], ya."),
            ("Petugas", "はい。", "Hai.", "Ya."),
            ("*", "Leader menghadap ke sensei."),
            ("Leader", "{失礼|しつれい}します。{掃除|そうじ}{道具|どうぐ}のチェックが{終|お}わりました。"
                       "{掃除|そうじ}を{始|はじ}めてもいいですか。",
             "Shitsurei shimasu. Sōji dōgu no chekku ga owarimashita. Sōji o hajimete mo ii desu ka.",
             "Permisi. Pengecekan alat kebersihan sudah selesai. Bolehkah kami mulai bersih-bersih?"),
            HAI,
            ("Leader", "{失礼|しつれい}します。", "Shitsurei shimasu.", "Permisi. (meninggalkan sensei)"),
            ("Leader", "じゃあ、{教室|きょうしつ}を{掃除|そうじ}しましょう。",
             "Jā, kyōshitsu o sōji shimashō.", "Nah, mari kita bersihkan kelas."),
            ("Petugas", "そうしましょう。", "Sō shimashō.", "Mari."),
        ],
    },
    {
        "judul": "Melapor Bersih-bersih Selesai",
        "jp": "{掃除|そうじ}が{終|お}わったときの{報告|ほうこく}",
        "romaji": "Sōji ga owatta toki no hōkoku",
        "pembuka": True,
        "baris": [
            kenalan("{掃除|そうじ}{当番|とうばん}です。{掃除|そうじ}が{終|お}わりました。チェックをお{願|ねが}いします。",
                    "Sōji tōban desu. Sōji ga owarimashita. Chekku o onegai shimasu.",
                    "Saya petugas piket. Bersih-bersih sudah selesai. Mohon dicek."),
            ("Sensei", "はい。", "Hai.", "Ya. (sensei mengecek hasil bersih-bersih di kelas)"),
        ],
    },
    {
        "judul": "Yubisashi Koshō",
        "jp": "{指差|ゆびさ}し{呼称|こしょう}",
        "romaji": "Yubisashi koshō — menunjuk sambil menyebut, di depan sensei",
        "baris": [
            ("Leader", "{指差|ゆびさ}し{呼称|こしょう}を{始|はじ}めましょう。",
             "Yubisashi koshō o hajimemashō.", "Mari mulai pengecekan dengan menunjuk."),
            ("Leader", "ホワイトボードはもう{消|け}しました。", "Howaito bōdo wa mō keshimashita.",
             "Papan tulis sudah dihapus."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk papan tulis)"),
            ("Leader", "{椅子|いす}はもう{片付|かたづ}けました。", "Isu wa mō katazukemashita.",
             "Kursi sudah dirapikan."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk kursi)"),
            ("Leader", "{扇風機|せんぷうき}はもう{消|け}しました。", "Senpūki wa mō keshimashita.",
             "Kipas angin sudah dimatikan."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk kipas angin)"),
            ("Leader", "{電気|でんき}はもう{消|け}しました。", "Denki wa mō keshimashita.",
             "Lampu sudah dimatikan."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk lampu)"),
            ("Leader", "{窓|まど}はもう{拭|ふ}きました。", "Mado wa mō fukimashita.",
             "Jendela sudah dilap."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk jendela)"),
            ("Leader", "{床|ゆか}はもう{掃|は}きました。", "Yuka wa mō hakimashita.",
             "Lantai sudah disapu."),
            ("Semua", "ヨシ！", "Yoshi!", "Oke! (menunjuk lantai)"),
            ("Leader", "{終|お}わりました。", "Owarimashita.", "Selesai. (membungkuk)"),
            ("Semua", "{終|お}わりました。", "Owarimashita.", "Selesai. (membungkuk)"),
            ("*", "Sesuaikan dengan bagian yang dibersihkan."),
        ],
    },
    {
        "judul": "Mengembalikan Alat Kebersihan",
        "jp": "{掃除|そうじ}{道具|どうぐ}を{返|かえ}す",
        "romaji": "Sōji dōgu o kaesu",
        "pembuka": True,
        "baris": [
            kenalan("{掃除|そうじ}{当番|とうばん}です。{掃除|そうじ}{道具|どうぐ}を{返|かえ}します。チェックをお{願|ねが}いします。",
                    "Sōji tōban desu. Sōji dōgu o kaeshimasu. Chekku o onegai shimasu.",
                    "Saya petugas piket. Saya kembalikan alat kebersihan. Mohon dicek. (membungkuk)"),
            HAI,
            ("Leader", "{皆|みな}さん、{掃除|そうじ}{道具|どうぐ}をチェックしましょう。",
             "Minasan, sōji dōgu o chekku shimashō.", "Semuanya, mari kita cek alat kebersihan."),
            ("Petugas", "そうしましょう。", "Sō shimashō.", "Mari."),
            ("*", "Cek alat dengan cara yang sama seperti saat meminjam."),
            ("Siswa", "{全部|ぜんぶ}あります。チェックが{終|お}わりました。{掃除|そうじ}{道具|どうぐ}をどこに{置|お}きますか。",
             "Zenbu arimasu. Chekku ga owarimashita. Sōji dōgu o doko ni okimasu ka.",
             "Semuanya ada. Pengecekan selesai. Alat kebersihan diletakkan di mana?"),
            ("Sensei", "{元|もと}の{所|ところ}に{置|お}いてください。", "Moto no tokoro ni oite kudasai.",
             "Tolong letakkan di tempat semula."),
            ("Siswa", "{元|もと}の{所|ところ}に{置|お}くんですね。はい、わかりました。{失礼|しつれい}します。",
             "Moto no tokoro ni oku n desu ne. Hai, wakarimashita. Shitsurei shimasu.",
             "Diletakkan di tempat semula, ya. Baik, saya mengerti. Permisi. (membungkuk)"),
            ("*", "Mengembalikan alat ke tempatnya, lalu kembali ke sensei."),
            ("Siswa", "{失礼|しつれい}します。{掃除|そうじ}{道具|どうぐ}を{元|もと}の{所|ところ}に{戻|もど}しました。"
                      "{以上|いじょう}です。{失礼|しつれい}します。",
             "Shitsurei shimasu. Sōji dōgu o moto no tokoro ni modoshimashita. Ijō desu. Shitsurei shimasu.",
             "Permisi. Alat kebersihan sudah saya kembalikan ke tempat semula. Sekian. Permisi. (membungkuk)"),
        ],
    },
]

PENALTI = [
    {
        "judul": "Laporan Penalti",
        "jp": "ペナルティの{報告|ほうこく}",
        "romaji": "Penaruti no hōkoku",
        "baris": [
            ("Siswa", "[salam]。すみません、[nama]{先生|せんせい}。{今|いま}よろしいですか。",
             "[salam]. Sumimasen, [nama] sensei. Ima yoroshii desu ka.",
             "[salam]. Maaf, [nama] Sensei. Apakah sekarang ada waktu?"),
            HAI,
            kenalan("{問題|もんだい}があります。どうもすみませんでした。これから{気|き}をつけます。"
                    "すみません、{先生|せんせい}。{問題|もんだい}を{解決|かいけつ}してもいいですか。",
                    "Mondai ga arimasu. Dōmo sumimasen deshita. Kore kara ki o tsukemasu. "
                    "Sumimasen, sensei. Mondai o kaiketsu shite mo ii desu ka.",
                    "Saya punya masalah. Mohon maaf. Mulai sekarang saya akan berhati-hati. "
                    "Maaf, Sensei. Bolehkah saya menyelesaikan masalah ini?"),
            ("Sensei", "はい。{問題|もんだい}は{何|なん}ですか。", "Hai. Mondai wa nan desu ka.",
             "Ya. Masalahnya apa?"),
            ("Siswa", "[masalah]。どうもすみませんでした。これから{気|き}をつけます。",
             "[masalah]. Dōmo sumimasen deshita. Kore kara ki o tsukemasu.",
             "[masalah]. Mohon maaf. Mulai sekarang saya akan berhati-hati. "
             "Contoh masalah: {時間|じかん}を{守|まも}りませんでした。(Jikan o mamorimasen deshita. = Saya tidak tepat waktu.)"),
            ("Sensei", "{心構|こころがま}え{七番|ななばん}を{五十回|ごじゅっかい}{書|か}いてください。{明日|あした}{出|だ}してください。",
             "Kokorogamae nana-ban o gojukkai kaite kudasai. Ashita dashite kudasai.",
             "Contoh penalti: tulis Kokorogamae nomor 7 sebanyak 50 kali. Serahkan besok."),
            ("Siswa", "ペナルティは{心構|こころがま}え{七番|ななばん}を{五十回|ごじゅっかい}{書|か}くんですね。"
                      "{明日|あした}{出|だ}すんですね。はい、わかりました。{失礼|しつれい}します。",
             "Penaruti wa kokorogamae nana-ban o gojukkai kaku n desu ne. "
             "Ashita dasu n desu ne. Hai, wakarimashita. Shitsurei shimasu.",
             "Penaltinya menulis Kokorogamae nomor 7 sebanyak 50 kali, ya. Diserahkan besok, ya. "
             "Baik, saya mengerti. Permisi."),
        ],
    },
    {
        "judul": "Laporan Penalti Selesai",
        "jp": "ペナルティが{終|お}わったときの{報告|ほうこく}",
        "romaji": "Penaruti ga owatta toki no hōkoku",
        "baris": [
            ("Siswa", "[salam]。すみません、[nama]{先生|せんせい}。{今|いま}よろしいですか。",
             "[salam]. Sumimasen, [nama] sensei. Ima yoroshii desu ka.",
             "[salam]. Maaf, [nama] Sensei. Apakah sekarang ada waktu?"),
            HAI,
            kenalan("{問題|もんだい}がありました。どうもすみませんでした。これから{気|き}をつけます。"
                    "すみません、{先生|せんせい}。ペナルティはもうやりました。チェックをお{願|ねが}いします。",
                    "Mondai ga arimashita. Dōmo sumimasen deshita. Kore kara ki o tsukemasu. "
                    "Sumimasen, sensei. Penaruti wa mō yarimashita. Chekku o onegai shimasu.",
                    "Saya punya masalah. Mohon maaf. Mulai sekarang saya akan berhati-hati. "
                    "Maaf, Sensei. Penaltinya sudah saya kerjakan. Mohon dicek. (sambil menyerahkan hasil penalti)"),
            ("Sensei", "はい。", "Hai.",
             "Ya. (sensei mengecek dan menandatangani; jika sudah beres, {名札|なふだ} dikembalikan)"),
            ("*", "Menerima {名札|なふだ} (nafuda, papan nama) dan hasil penalti."),
            ("Siswa", "どうもすみませんでした。これから{気|き}をつけます。"
                      "すみません、{先生|せんせい}。{座|すわ}って{勉強|べんきょう}してもいいですか。",
             "Dōmo sumimasen deshita. Kore kara ki o tsukemasu. "
             "Sumimasen, sensei. Suwatte benkyō shite mo ii desu ka.",
             "Mohon maaf. Mulai sekarang saya akan berhati-hati. Maaf, Sensei. Bolehkah saya duduk dan belajar?"),
            ("Sensei", "はい。／いいですよ。", "Hai. / Ii desu yo.", "Ya. / Boleh."),
            ("Siswa", "どうもありがとうございました。{以上|いじょう}です。{失礼|しつれい}します。",
             "Dōmo arigatō gozaimashita. Ijō desu. Shitsurei shimasu.",
             "Terima kasih banyak. Sekian. Permisi."),
        ],
    },
]

# (jepang, romaji, arti)
KOKOROGAMAE = [
    ("{規則|きそく}を{守|まも}ります。", "Kisoku o mamorimasu.", "Menaati peraturan."),
    ("{一生懸命|いっしょうけんめい}{頑張|がんば}ります。", "Isshōkenmei ganbarimasu.",
     "Berusaha keras dan bersungguh-sungguh."),
    ("{見|み}ます。{聞|き}きます。{考|かんが}えます。", "Mimasu. Kikimasu. Kangaemasu.",
     "Melihat. Mendengar. Berpikir."),
    ("{大切|たいせつ}なことをメモします。", "Taisetsu na koto o memo shimasu.",
     "Mencatat hal-hal yang penting."),
    ("{挨拶|あいさつ}します。", "Aisatsu shimasu.", "Memberi salam dengan riang dan bersemangat."),
    ("{返事|へんじ}をします。{黙|だま}りません。", "Henji o shimasu. Damarimasen.",
     "Menjawab/menyahut. Tidak diam saja."),
    ("{時間|じかん}を{守|まも}ります。", "Jikan o mamorimasu.", "Tepat waktu."),
    ("{協力|きょうりょく}します。", "Kyōryoku shimasu.", "Bekerja sama."),
    ("{感謝|かんしゃ}を{忘|わす}れません。「ありがとうございます」と{言|い}います。",
     "Kansha o wasuremasen. “Arigatō gozaimasu” to iimasu.",
     "Tidak lupa berterima kasih. Mengucapkan “Arigatō gozaimasu”."),
    ("わからないときは、{質問|しつもん}します。「はい」と{言|い}いません。{黙|だま}りません。{自分|じぶん}で{決|き}めません。",
     "Wakaranai toki wa, shitsumon shimasu. “Hai” to iimasen. Damarimasen. Jibun de kimemasen.",
     "Jika belum mengerti, bertanya; jangan menjawab “hai”. Tidak berdiam diri. Tidak memutuskan sendiri."),
    ("{間違|まちが}えたときは、すぐに{謝|あやま}ります。{言|い}い{訳|わけ}をしません。{反省|はんせい}します。",
     "Machigaeta toki wa, sugu ni ayamarimasu. Iiwake o shimasen. Hansei shimasu.",
     "Saat melakukan kesalahan, segera minta maaf. Tidak mencari alasan. Introspeksi diri."),
    ("{間違|まちが}えたときに、{笑|わら}いません。", "Machigaeta toki ni, waraimasen.",
     "Saat melakukan kesalahan, tidak tersenyum atau tertawa."),
    ("「{間違|まちが}いは{何|なに}か。」「どうして{間違|まちが}えたか。」と{考|かんが}えて、{同|おな}じ{間違|まちが}いはしません。",
     "“Machigai wa nani ka.” “Dōshite machigaeta ka.” to kangaete, onaji machigai wa shimasen.",
     "Memahami kesalahan yang dilakukan dan penyebabnya, supaya tidak mengulangi kesalahan yang sama."),
    ("{安全|あんぜん}に{気|き}をつけます。", "Anzen ni ki o tsukemasu.",
     "Berhati-hati dan mengutamakan keselamatan kerja."),
    ("{仕事|しごと}の{前|まえ}に{準備|じゅんび}をします。{仕事|しごと}の{後|あと}で{片付|かたづ}けます。",
     "Shigoto no mae ni junbi o shimasu. Shigoto no ato de katazukemasu.",
     "Bersiap sebelum mulai bekerja. Membereskan setelah selesai bekerja."),
    ("{仕事|しごと}の{時間|じかん}は{仕事|しごと}をします。", "Shigoto no jikan wa shigoto o shimasu.",
     "Bekerja pada jam kerja."),
    ("{自分|じぶん}で{仕事|しごと}を{探|さが}します。", "Jibun de shigoto o sagashimasu.",
     "Mencari pekerjaan sendiri (tidak menunggu disuruh)."),
    ("{仕事|しごと}を{速|はや}くします。{正確|せいかく}にします。{最後|さいご}にチェックします。",
     "Shigoto o hayaku shimasu. Seikaku ni shimasu. Saigo ni chekku shimasu.",
     "Bekerja dengan cepat dan tepat, lalu memeriksanya di akhir."),
    ("{道具|どうぐ}を{大切|たいせつ}に{使|つか}います。{壊|こわ}れたとき、なくなったとき、すぐに{報告|ほうこく}します。",
     "Dōgu o taisetsu ni tsukaimasu. Kowareta toki, nakunatta toki, sugu ni hōkoku shimasu.",
     "Menggunakan alat dengan baik. Jika rusak atau hilang, segera melapor."),
    ("{休|やす}む{前|まえ}に{許可|きょか}をもらいます。{休|やす}んだ{後|あと}で{謝|あやま}ります。{報告|ほうこく}します。",
     "Yasumu mae ni kyoka o moraimasu. Yasunda ato de ayamarimasu. Hōkoku shimasu.",
     "Meminta izin sebelum tidak hadir. Setelah hadir kembali, minta maaf dan melapor."),
    ("{健康|けんこう}に{気|き}をつけます。", "Kenkō ni ki o tsukemasu.", "Menjaga kesehatan."),
    ("{身|み}の{回|まわ}りを{清潔|せいけつ}にします。", "Mi no mawari o seiketsu ni shimasu.",
     "Menjaga kebersihan diri sendiri dan sekitarnya."),
    ("{毎日|まいにち}{着替|きが}えます。ハンカチを{持|も}ち{歩|ある}きます。",
     "Mainichi kigaemasu. Hankachi o mochiarukimasu.",
     "Setiap hari berganti pakaian. Selalu membawa saputangan."),
    ("{髪|かみ}を{切|き}ります。{爪|つめ}を{切|き}ります。ひげをそります。",
     "Kami o kirimasu. Tsume o kirimasu. Hige o sorimasu.",
     "Memangkas rambut. Memotong kuku. Mencukur kumis dan jenggot."),
    ("{鼻水|はなみず}はティッシュでかみます。つばを{道|みち}に{吐|は}きません。",
     "Hanamizu wa tisshu de kamimasu. Tsuba o michi ni hakimasen.",
     "Membuang ingus dengan tisu. Tidak meludah di jalan dan tempat umum."),
    ("{毎日|まいにち}{掃除|そうじ}をします。ごみはごみ{箱|ばこ}に{捨|す}てます。",
     "Mainichi sōji o shimasu. Gomi wa gomibako ni sutemasu.",
     "Setiap hari bersih-bersih. Membuang sampah pada tempatnya."),
    ("たばこを{吸|す}いません。", "Tabako o suimasen.", "Tidak merokok."),
    ("{洗濯|せんたく}や{掃除|そうじ}など、{自分|じぶん}のことは{自分|じぶん}でします。",
     "Sentaku ya sōji nado, jibun no koto wa jibun de shimasu.",
     "Mengurus diri sendiri, seperti mencuci dan bersih-bersih, untuk hidup mandiri di Jepang."),
    ("{電気|でんき}や{水|みず}などを{節約|せつやく}します。", "Denki ya mizu nado o setsuyaku shimasu.",
     "Menghemat listrik, air, dan sebagainya."),
    ("ご{飯|はん}を{残|のこ}しません。", "Gohan o nokoshimasen.",
     "Tidak menyisakan makanan (tidak boros)."),
]
