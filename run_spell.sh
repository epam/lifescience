#!/bin/sh

echo " " > aspell_output.txt

for f in rst/*/*.rst 
do
   echo $f
   echo "******************************************************************************************************************************" >> aspell_output.txt
   echo $f >> aspell_output.txt
   echo "******************************************************************************************************************************" >> aspell_output.txt
   cat $f | aspell  pipe list -d en_GB  ignore,-W 4 --encoding=utf-8 --mode=tex --personal=./aspell.ignore.txt  | grep -E "\&.*|\# .*" >> aspell_output.txt
done
