#!/bin/sh
indigo_head=`cat HEAD`

wget https://github.com/epam/Indigo/raw/$indigo_head/api/c/indigo/indigo.h
wget https://github.com/epam/Indigo/raw/$indigo_head/api/python/indigo/__init__.py -O indigo.py
wget https://github.com/epam/Indigo/raw/$indigo_head/api/python/indigo/renderer.py -O indigo_renderer.py
wget https://github.com/epam/Indigo/raw/$indigo_head/api/python/indigo/inchi.py -O indigo_inchi.py
