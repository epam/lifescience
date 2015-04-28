#!/bin/sh

echo "Run cross-reference verify"

cd build/html

linkchecker --ignore-url=^http --ignore-url=^todo -t 100 -F html index.html
