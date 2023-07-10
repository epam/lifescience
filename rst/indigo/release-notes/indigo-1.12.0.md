# Indigo 1.12.0
Released 2023-07-09

## What's Changed

## Bugfixes
* [#965](https://github.com/epam/Indigo/issues/965) MDL Molfile v3000: when opening files containing 'Salts an Solvents', names are truncated and abbreviation is expanded
* [#1036](https://github.com/epam/Indigo/issues/1036) SMILES import: general chiral specification labels (TH, AL, SP, TB, OH ) don't work
* [#1051](https://github.com/epam/Indigo/issues/1051) Opening file with a superatom label saved in RXN v3000 format only the first part of the label is displayed
* [#1114](https://github.com/epam/Indigo/issues/1114) Atoms of Benzene ring become Monoradicals when opened from file saved in Daylight SMARTS
* [#1132](https://github.com/epam/Indigo/issues/1132) SMILES loader uninitialized heap fix
* [#1102](https://github.com/epam/Indigo/issues/1102) When pasting Extended SMILES structure with stereochemistry there are two &1 centers instead of an ABS and an &1
* [#1135](https://github.com/epam/Indigo/issues/1135) C library macro - va_end() is missing before return statement.
* [#1126](https://github.com/epam/Indigo/issues/1126) Segfault when iterating CDX file from USPTO downloads
* [#1144](https://github.com/epam/Indigo/issues/1144) Unable to save the structure after clicking 'Save', an error appears

## Improvements
* [#1098](https://github.com/epam/Indigo/issues/1098) api: add method for copying RGroups

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.11.0...indigo-1.12.0