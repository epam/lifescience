#!/bin/sh

echo "Run cross-reference verify"

cd build/html

linkchecker --ignore-url=^http -t 100 -F html index.html
