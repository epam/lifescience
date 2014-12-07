#!/bin/bash

for f in $(find source -name '*.html') ; do
    o="${f/#source/dest}"
    o="${o%.html}".rst
    mkdir -p "$(dirname "$o")"
    echo "$f -> $o"
    pandoc -f html -t rst "$f" -o "$o"
done

mv source/assets dest
ln -s ../dest/assets source/assets
