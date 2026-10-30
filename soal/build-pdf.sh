#!/bin/bash
# Ubah file soal Markdown menjadi PDF A4 siap cetak.
# Pakai: soal/build-pdf.sh soal/bab-15        (semua .md di folder itu)
#        soal/build-pdf.sh soal/bab-15/tes-kotoba-bab-15.md
# Furigana ditulis {漢字|かんじ} dan diubah menjadi <ruby> sebelum dikonversi.
# Butuh: Node.js (npx) dan Google Chrome (path lain bisa lewat variabel CHROME).
set -euo pipefail

CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
DIR="$(cd "$(dirname "$0")" && pwd)"
CSS="$DIR/style.css"

if [ $# -eq 0 ]; then
  echo "Pakai: $0 <folder-bab atau file.md>" >&2
  exit 1
fi

if [ -d "$1" ]; then
  FILES=("$1"/*.md)
else
  FILES=("$1")
fi

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for MD in "${FILES[@]}"; do
  NAME="$(basename "$MD" .md)"
  OUT="$(cd "$(dirname "$MD")" && pwd)/$NAME.pdf"
  HTML="$TMP/$NAME.html"
  TITLE="$(grep -m1 '^# ' "$MD" | sed 's/^# //')"

  {
    echo "<!doctype html><html lang=\"id\"><head><meta charset=\"utf-8\">"
    echo "<title>$TITLE</title><style>"
    cat "$CSS"
    echo "</style></head><body>"
    sed -E 's/\{([^{}|]+)\|([^{}|]+)\}/<ruby>\1<rt>\2<\/rt><\/ruby>/g' "$MD" \
      | npx --yes marked@12.0.2 --gfm
    echo "</body></html>"
  } > "$HTML"

  # Chrome kadang tidak menutup sendiri setelah mencetak; tunggu PDF lalu hentikan.
  rm -f "$OUT"
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --no-first-run --no-default-browser-check --disable-extensions \
    --user-data-dir="$TMP/chrome" \
    --print-to-pdf="$OUT" "file://$HTML" >/dev/null 2>&1 &
  PID=$!
  for _ in $(seq 1 60); do
    if ! kill -0 "$PID" 2>/dev/null; then break; fi
    if [ -s "$OUT" ]; then sleep 1; break; fi
    sleep 0.5
  done
  kill "$PID" 2>/dev/null || true
  wait "$PID" 2>/dev/null || true

  if [ -s "$OUT" ]; then
    echo "PDF: $OUT"
  else
    echo "Gagal membuat PDF: $MD" >&2
    exit 1
  fi
done
