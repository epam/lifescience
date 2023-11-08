# Indigo 1.14.0
Released 2023-11-07

## Features
* [#1217](https://github.com/epam/Indigo/issues/1217) Support SDF-format for Indigo-Ketcher API
* [#1257](https://github.com/epam/Indigo/issues/1257) Enhanced stereo labels on atropisomers are lost when opening saved Extended SMILES

## Bugs
* [#887](https://github.com/epam/Indigo/issues/887) When saving in PNG and SVG format, files have low resolution when opened (Ketcher Remote)
* [#1200](https://github.com/epam/Indigo/issues/1200) MolfileSaver add Data S-Groups to molecule at saveMolecule()
* [#1199](https://github.com/epam/Indigo/issues/1199) CanonicalSmiles saver contains extended part.
* [#1161](https://github.com/epam/Indigo/issues/1161) Bingo unable to index on SQL Server
* [#1040](https://github.com/epam/Indigo/issues/1040) SMILES/SMARTS import: Files with S-Group Properties cause an error 
* [#1145](https://github.com/epam/Indigo/issues/1145) CDX import: letter is duplicate and 'superscript' and 'subscript' become the same size as the letter
* [#1191](https://github.com/epam/Indigo/issues/1191) Bingo-elastic: Cannot search at elastic using custom-index
* [#731](https://github.com/epam/Indigo/issues/731) Warnings in the Structure Check window doesn't display for molecules with R-Groups
* [#1230](https://github.com/epam/Indigo/issues/1230) Unable to save file if the canvas has a reaction arrow and a Functional Group
* [#1249](https://github.com/epam/Indigo/issues/1249) Incorrect order of aliases in SMILES saver
* [#1240](https://github.com/epam/Indigo/issues/1240) Unable to open the CDX file with an R-Group added to the whole structure
* [#1239](https://github.com/epam/Indigo/issues/1239) CDX: An abbreviation appears in the upper left corner of a Function Group or Salt when opening a saved file
* [#1287](https://github.com/epam/Indigo/issues/1287) New S-Group type Query component level grouping
* [#1260](https://github.com/epam/Indigo/issues/1260) SMARTS saver works incorrectly for non-query entities if atom valence or radical present
* [#1300](https://github.com/epam/Indigo/issues/1300) Stereobond is not preserved after pasting a SMILES structure
* [#1277](https://github.com/epam/Indigo/issues/1277) Atropisomer centers support
* [#1347](https://github.com/epam/Indigo/issues/1347) When pasting Extended SMILES with coordinates enhanced stereochemistry is lost

## Improvements
* [#1037](https://github.com/epam/Indigo/issues/1037) Indigo Toolkit information in the 'About' section that is not relevant for the users
* [#1197](https://github.com/epam/Indigo/issues/1197) Migrate indigo-knime nodes to KNIME Analytics Platform 5.1

 
**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.13.0...indigo-1.14.0