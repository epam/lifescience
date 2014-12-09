#!/bin/bash

DEST=$1
[ -z "$DEST" ] && DEST=rst
[ -z "$pandoc" ] && pandoc=pandoc

for f in $(find source -name '*.html') ; do
    o="${f/#source/$DEST}"
    o="${o%.html}".rst
    mkdir -p "$(dirname "$o")"
    echo "$f -> $o"
    $pandoc -f html -t rst "$f" -o "$o"
done

ln -fs $(realpath source/assets) $DEST/assets
