#!/bin/sh

echo " " > aspell_output.txt

FILES=$(find rst/ -type f -name '*.rst')

for f in $FILES
do
   echo $f
   echo "******************************************************************************************************************************" >> aspell_output.txt
   echo $f >> aspell_output.txt
   echo "******************************************************************************************************************************" >> aspell_output.txt
   cat $f | aspell  pipe list -d en_US  --ignore=4 --encoding=utf-8 --mode=tex --personal=./aspell.ignore.txt  | grep -E "\&.*|\# .*" >> aspell_output.txt
done
