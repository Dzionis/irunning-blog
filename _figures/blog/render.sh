#!/bin/bash
# Renders a figure page to a 2x PNG and copies it into assets/images/blog.
# Usage: _figures/blog/render.sh <name>        (desktop, 720px wide)
#        _figures/blog/render.sh <name>-mobile (mobile, 400px wide)
# Height comes from the page's .canvas height.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
NAME="$1"
W=720; [[ "$NAME" == *-mobile ]] && W=400
H=$(grep -o '\.canvas { height: [0-9]*px' "$DIR/$NAME.html" | grep -o '[0-9]*' | head -1)
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=$W,$H --allow-file-access-from-files \
  --screenshot="$DIR/../../assets/images/blog/$NAME.png" "file://$DIR/$NAME.html" >/dev/null 2>&1
OUT="$DIR/../../assets/images/blog/$NAME.png"
# Photo-heavy figures opt into JPEG with <html data-format="jpg">.
if grep -q 'data-format="jpg"' "$DIR/$NAME.html"; then
  sips -s format jpeg -s formatOptions 82 "$OUT" --out "${OUT%.png}.jpg" >/dev/null && rm "$OUT"
  OUT="${OUT%.png}.jpg"
fi
echo "${OUT#$DIR/../../} (${W}x${H} @2x, $(du -h "$OUT" | cut -f1))"
