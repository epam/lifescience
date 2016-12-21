#!/bin/sh
indigo_head=`cat HEAD`
wget http://github.com/epam/Indigo/archive/$indigo_head.zip -O indigo.zip 
