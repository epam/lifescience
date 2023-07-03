# Indigo 1.11.0
Released 2023-06-19

## What's Changed

## Features
* [#1053](https://github.com/epam/Indigo/issues/1053) Split publish job in "Indigo CI" GitHub Action
* [#310](https://github.com/epam/Indigo/issues/310) Support stereo CIP calculation in Ket format
* [#957](https://github.com/epam/Indigo/issues/957) Support of Korean, Chinese and Japanese characters in Standalone.
* [#995](https://github.com/epam/Indigo/issues/995) Automated memory leaks testing

## Bugfixes
* [#1044](https://github.com/epam/Indigo/issues/1044)  SVG/PNG: Reaction arrows are not visible without structures at preview and in saved files
* [#932](https://github.com/epam/Indigo/issues/932) Reagents: When opening Daylight SMILES and Extended SMILES files with reagent the original structure is distorted
* [#1084](https://github.com/epam/Indigo/issues/1084) Can't open mol v3000 files with 'S-Group Properties Type = Generic' and 'S-Group Properties Type = Multiple'
* [#1083](https://github.com/epam/Indigo/issues/1083)  Indigo Service: enable of using Indigo Options
* [#910](https://github.com/epam/Indigo/issues/910)  MDL Molfile v3000 encoding: Automatic selection of MDL Molfile v3000 encoding doesn't work if the number of atoms (or bonds) exceeds 999
* [#956](https://github.com/epam/Indigo/issues/956)  Copy Image: When inversion type is chosen in the atom's properties, it is not saved
* [#955](https://github.com/epam/Indigo/issues/955) Copy Image: Saved bonds does not have Reacting Center marks
* [#1052](https://github.com/epam/Indigo/issues/1052) Set "Indigo Docker images preparation" GItHub Action to start manually only add version tag to Docker images
* [#1064](https://github.com/epam/Indigo/issues/1064) Keep implicit hydrogens information in KET-format
* [#1048](https://github.com/epam/Indigo/issues/1048) Memory leak in 3rd party library
* [#1056](https://github.com/epam/Indigo/issues/1056) RXN2000/3000 should not serialize INDIGO_DESC fields for s-groups
* [#1050](https://github.com/epam/Indigo/issues/1050) Memory leak in StringPool code
* [#1031](https://github.com/epam/Indigo/issues/1031) Calculate CIP: Hovering over the label R/S displays Indigo system information
* [#1049](https://github.com/epam/Indigo/issues/1049) Memory leak in the SMILES loader code
* [#973](https://github.com/epam/Indigo/issues/973) Daylight SMARTS: Error when save file in SMART format with reaction arrow and reagent
* [#1017](https://github.com/epam/Indigo/issues/1017) imagoVersions is undefined
* [#899](https://github.com/epam/Indigo/issues/899) Add restrictions on size to be less than 1000
* [#1015](https://github.com/epam/Indigo/issues/1015) Cannot test CDX export with certain files
* [#944](https://github.com/epam/Indigo/issues/544) CDX import: Greek letters, Celsius and Fahrenheit signs are replaced with question marks
* [#1093](https://github.com/epam/Indigo/issues/1093) python binding memory leak from 1.8.0 (and still present in 1.10.0)

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.10.0...indigo-1.11.0
