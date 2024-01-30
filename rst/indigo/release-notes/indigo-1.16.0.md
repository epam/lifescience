# Indigo 1.16.0
Released 2024-01-30

## Features
* [#1185](https://github.com/epam/Indigo/issues/1185) Macromolecules export from MolV3000 to KET
* [#1381](https://github.com/epam/Indigo/issues/1381) Macromolecules import from KET

## Bugs
* [#1395](https://github.com/epam/Indigo/issues/1395) Class and naturalAnalog of KET monomerTemplate should be optional
* [#1405](https://github.com/epam/Indigo/issues/1405) Valence is lost for Mol and Rxn files
* [#1415](https://github.com/epam/Indigo/issues/1415) Incorrect S-Group count in MOL V3000 header if ImplicitH is set
* [#1346](https://github.com/epam/Indigo/issues/1346) Extended SMILES: Atropisomer is displayed incorrectly
* [#1304](https://github.com/epam/Indigo/issues/1304) Indigo accepts `[#6]` notation in SMILES mode
* [#1355](https://github.com/epam/Indigo/issues/1355) Error appears when pressing 'Layout'
* [#1330](https://github.com/epam/Indigo/issues/1330) Implicit H count is not added to the SMARTS file
* [#1358](https://github.com/epam/Indigo/issues/1358) Error while loading `[!#6,!#7,!#8]` smarts
* [#1357](https://github.com/epam/Indigo/issues/1357) Wrong atom list when paste structure as SMARTS
* [#1292](https://github.com/epam/Indigo/issues/1292) valid SMARTS with cycles cause error in loader
* [#1349](https://github.com/epam/Indigo/issues/1349) Symbol for topology chain is missing in SMARTS file
* [#1351](https://github.com/epam/Indigo/issues/1351) Error returned when try to convert structure with custom query for bond into SMARTS format
* [#1283](https://github.com/epam/Indigo/issues/1283) wrong chirality generated by SMARTS load/save
* [#1329](https://github.com/epam/Indigo/issues/1329) Aromacity is incorrectly marked in the SMARTS file
* [#1325](https://github.com/epam/Indigo/issues/1325) Indigo should return warning for some attributes
* [#1328](https://github.com/epam/Indigo/issues/1328) Chirality is not added to the SMARTS file
* [#1281](https://github.com/epam/Indigo/issues/1281) Support SMARTS "or unspecified" bond property in custom queries
* [#1321](https://github.com/epam/Indigo/issues/1321) When saving a structure with set up Implicit H count and any other atom attribute then an error appears
* [#1309](https://github.com/epam/Indigo/issues/1309) Error appears while trying to save some element with set up H count and implicit H count
* [#1319](https://github.com/epam/Indigo/issues/1319) Directional bonds are encoded incorrectly in SMARTS
* [#1183](https://github.com/epam/Indigo/issues/1183) Support monomer templates import from KET-format
* [#1184](https://github.com/epam/Indigo/issues/1184) Support monomer templates export into KET-format
* [#1310](https://github.com/epam/Indigo/issues/1310) Error appears while opening SMARTS file with query which contains comma
* [#1322](https://github.com/epam/Indigo/issues/1322) Reaction cannon be saved in convert function
* [#1303](https://github.com/epam/Indigo/issues/1303) Return original format from convert and layout function
* [#1316](https://github.com/epam/Indigo/issues/1316) SMARTS saver miss component level grouping
* [#1254](https://github.com/epam/Indigo/issues/1254) SMARTS with component-level grouping saved without '()'
* [#1252](https://github.com/epam/Indigo/issues/1252) SMARTS loader load grouped components as separate molecules
* [#1245](https://github.com/epam/Indigo/issues/1245) Reaction/Molecule autoloaders don't load SMARTS
* [#914](https://github.com/epam/Indigo/issues/914) Why is the code InChI=123 valid?
* [#1224](https://github.com/epam/Indigo/issues/1224) Different indent after loading reaction from file and after layout it.
* [#1221](https://github.com/epam/Indigo/issues/1221) An empty structure is returned given incorrect InChi string

## Improvements
* [#1338](https://github.com/epam/Indigo/issues/1338) Use docker image for building npm packages and apply tags while publish

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.14.0...indigo-1.16.0