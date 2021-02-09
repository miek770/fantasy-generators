#!/usr/bin/bash

# Get project title and version from main.py
TITLE=$(grep -n "__title__ = " main.py | tr '"' '\n' | sed '2q;d' | tr ' ' '_')
VERSION=$(grep -n "__version__ = " main.py | tr '"' '\n' | sed '2q;d' | tr ' ' '_')

# Remove previous distribution
rm -rf main.dist
rm -rf "$TITLE-$VERSION"
rm -rf "$TITLE-$VERSION.zip"

# Compile using Nuitka
python -m nuitka --standalone --plugin-enable=numpy --mingw64 --assume-yes-for-downloads --remove-output main.py

# Rename and compress release
sleep 5
mkdir main.dist/names
cp names/*.txt main.dist/names
mv main.dist/main.exe "main.dist/$TITLE-$VERSION.exe"
mv main.dist "$TITLE-$VERSION"
zip -r "$TITLE-$VERSION.zip" "$TITLE-$VERSION"