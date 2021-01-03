#!/bin/sh
indigo_head=`cat HEAD`

wget https://github.com/epam/Indigo/raw/$indigo_head/api/indigo.h
wget https://github.com/epam/Indigo/raw/$indigo_head/api/python/indigo.py
wget https://github.com/epam/Indigo/raw/$indigo_head/api/plugins/renderer/python/indigo_renderer.py
wget https://github.com/epam/Indigo/raw/$indigo_head/api/plugins/inchi/python/indigo_inchi.py
