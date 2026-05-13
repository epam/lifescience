# Indigo 1.43.0
Released 2026-05-13

## Features
* [3526](https://github.com/epam/Indigo/issues/3526) Update SDF and KET format to include information about preset phosphate position
* [3525](https://github.com/epam/Indigo/issues/3525) Expose ability to calculate fully expanded large molecule into chemical structures
* [3562](https://github.com/epam/Indigo/issues/3562) Add api to iterate through attachments points of S-groups of 'SUP' type
* [3554](https://github.com/epam/Indigo/issues/3554) Implement multi-threading in Bingo NoSQL substructure search

## Bugfixes and improvements
* [3307](https://github.com/epam/Indigo/issues/3307) If the selected group is forming an n-agon with 6 or more than 6 points, then the bases should be located inside of the circular structure
* [3308](https://github.com/epam/Indigo/issues/3308) If the selected group is forming an n-agon with 12 or more than 12 points, the bases should be located inside of the circular structure
* [3304](https://github.com/epam/Indigo/issues/3304) Fixed monomer of cycle on layout should be top left monomer
* [3305](https://github.com/epam/Indigo/issues/3305) The "center" of the n-agon should be positioned to the right of the fixed monomer
* [3496](https://github.com/epam/Indigo/issues/3496) Fixing the issue during reading of the molecule data and parse it.
* [3301](https://github.com/epam/Indigo/issues/3301) System provides invalid SDF content (missing semicolon) on mono…
* [3449](https://github.com/epam/Indigo/issues/3449) Bond length become wrong after Arrange as a Ring option applied
* [3329](https://github.com/epam/Indigo/issues/3329) Sequential application of “Create cyclic structure” to different segments of one chain leads to overlapping and distorted topology
* [3584](https://github.com/epam/Indigo/issues/3584) Deadlock in multithread subsearch.
* [3622](https://github.com/epam/Indigo/issues/3622) Fix Bingo-nosql matcher sub tau speed issue
* [3268](https://github.com/epam/Indigo/issues/3268) Cyclic layout issues
* [3353](https://github.com/epam/Indigo/issues/3353) System ignores Implicit H count value in export to SVG/PNG
* [3303](https://github.com/epam/Indigo/issues/3303) Wrong monomer re-layout


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.42.0-rc.1...indigo-1.43.0