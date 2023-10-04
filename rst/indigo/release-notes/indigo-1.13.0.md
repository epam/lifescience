# Indigo 1.13.0
Released 2023-10-04

## What's Changed

## Bugfixes
* [#1205](https://github.com/epam/Indigo/issues/1205) Reagent located at the bottom of the arrow when opening the RXN V2000 and V3000 files are located on top of the arrow
* [#1168](https://github.com/epam/Indigo/issues/1168) Error message when trying to save structure with Multiple Group type applied to entire structure
* [#1166](https://github.com/epam/Indigo/issues/1166) CDX: file with R-Group label saved in Ketcher opens without part of structure
* [#1159](https://github.com/epam/Indigo/issues/1159) [CDX] IndigoException: stoi when reading USPTO CDX file
* [#1155](https://github.com/epam/Indigo/issues/1155) [CDX] Indigo header files doesn't appear in msvc solution.
* [#1152](https://github.com/epam/Indigo/issues/1152) No module named tzdata while running indigo service
* [#1139](https://github.com/epam/Indigo/issues/1139) core dumped when reading CDX file downloaded from USPTO
* [#1113](https://github.com/epam/Indigo/issues/1113) RXN 3000 import: When importing, the structure becomes unreadable
* [#1094](https://github.com/epam/Indigo/issues/1094) Structure with R-Group isn't opened correctly from v3000 mol file
* [#1061](https://github.com/epam/Indigo/issues/1061) [Bingo-Elastic] Cannot create custom index in python bingo-elastic
* [#1026](https://github.com/epam/Indigo/issues/1026) [Bingo-Elastic] SVG/PNG: Contracted 'Functional Groups' and 'Salts and Solvents' are rendered expanded when saved
* [#926](https://github.com/epam/Indigo/issues/926) CDXML import: 'superscript' and 'subscript' appears below the letter

## Features
* [#1182 ](https://github.com/epam/Indigo/issues/1182) Enhanced stereo labels on atropisomers are lost when opening molfiles
* [#1158](https://github.com/epam/Indigo/issues/1158) Ketcher needs to correctly serialize/deserialize attachment point information for super atoms for mol v3000 & ket format

## Improvements
* [#1111](https://github.com/epam/Indigo/issues/1111) api: add method for copying RGroups for Java and .NET
* [#1124](https://github.com/epam/Indigo/issues/1124) SMILES format does not store alias information

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.12.0...indigo-1.13.0