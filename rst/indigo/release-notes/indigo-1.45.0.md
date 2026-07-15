# Indigo 1.45.0
Released 2026-07-10

## Features
* [3333](https://github.com/epam/Indigo/issues/3333) Use BIOVIA post 2014 valence table to calculate atomic valences from molfiles

## Bugfixes and improvements
* [3599](https://github.com/epam/Indigo/issues/3599) Bond length become wrong after Arrange as a Ring option applied
* [3648](https://github.com/epam/Indigo/issues/3648) Integration tests may fails in MT mode
* [3283](https://github.com/epam/Indigo/issues/3283) SVG export fails, with S-Groups
* [1937](https://github.com/epam/Indigo/issues/1937) Add tests for Bingo Oracle
* [3606](https://github.com/epam/Indigo/issues/3606) Bond length between the base and the sugar is not standart if the selected group is forming an n-agon with 12 or more than 12 points
* [3683](https://github.com/epam/Indigo/issues/3683) SMARTS search crashes in the Postgres
* [235](https://github.com/epam/Indigo/issues/235) Add Tautomer support in Bingo Elastic Python
* [3688](https://github.com/epam/Indigo/issues/3688) `Add explicit hydrogens` operation causes unfolded hydrogen out of query component
* [3702](https://github.com/epam/Indigo/issues/3702) Unfold hydrogens makes monoradical from Helium with odd valence
* [3359](https://github.com/epam/Indigo/issues/3359) Atoms with invalid valence loaded with explicitly defined valence from CDX
* [3691](https://github.com/epam/Indigo/issues/3691) Refactoring PtrArray<T>

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.44.0-rc.1...indigo-1.45.0