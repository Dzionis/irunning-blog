#!/bin/bash
# Builds the 720px WebP card thumbnails in assets/images/blog/thumbs/ for every
# post's front-matter `image.path`. Cards (homepage, blog listing, "Keep reading")
# use the thumb when it exists and fall back to the full image otherwise.
# Needs cwebp (Homebrew `webp`).
# Usage: scripts/make-blog-thumbs.sh            # only missing thumbs
#        scripts/make-blog-thumbs.sh --force    # rebuild all
set -e
cd "$(dirname "$0")/.."
out=assets/images/blog/thumbs
mkdir -p "$out"
for post in _posts/*.md; do
  src=$(awk 'NR>1 && /^---$/{exit} NR>1' "$post" | grep -A2 '^image:' | grep 'path:' | sed 's/.*path: *//; s/"//g')
  [ -z "$src" ] && continue
  name=$(basename "$src"); name="${name%.*}"
  dst="$out/$name.webp"
  if [ -f "$dst" ] && [ "$1" != "--force" ]; then continue; fi
  cwebp -quiet -q 70 -resize 720 0 ".$src" -o "$dst"
  echo "thumb: $dst ($(( $(stat -f%z "$dst") / 1024 )) KB)"
done
