#!/bin/sh
unzip indigo.zip
mv Indigo-*/ indigo-src/
cd indigo-src/
python build_scripts/indigo-release-libs.py --preset=linux64 
python build_scripts/indigo-make-by-libs.py --type=python
unzip dist/indigo-python-*
mv indigo-python-*/ ../indigo-python/