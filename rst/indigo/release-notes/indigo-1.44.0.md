# Indigo 1.44.0
Released 2026-07-10

## Features
* [3541](https://github.com/epam/Indigo/issues/3541) Support for BILN
* [3636](https://github.com/epam/Indigo/issues/3636) Add coordinates support in bingo-nosql
* #3524 – Support default InChI (Key) generation
* [3598](https://github.com/epam/Indigo/issues/3598) Add cross bonds related api methods for superatoms and remove type based restriction from generic sgroups methods
* [3536](https://github.com/epam/Indigo/issues/3536) Implement update mode for integration tests

## Bugfixes and improvements
* [3333](https://github.com/epam/Indigo/issues/3333) Adding missing elements and test to fix the current workflow
* [3544](https://github.com/epam/Indigo/issues/3544) Indexing issues in Sgroups created as match to query molecule with unfolded hydrogens
* [3577](https://github.com/epam/Indigo/issues/3577) Arrange as a Ring doesn't work if circular structure has tails that has connection between each other
* [3545](https://github.com/epam/Indigo/issues/3545) Error on attempt to get 'SRU' sgroup name contradicts API documentation
* [3215](https://github.com/epam/Indigo/issues/3215) Export to SMARTS works wrong for R-Groups
* [3249](https://github.com/epam/Indigo/issues/3249) Unable to load Mol v3000 file with R-group fragment inside - system throws exception
* [3595](https://github.com/epam/Indigo/issues/3595) Pasting a large molecule doesn't work in Ketcher (works slow)
* [3600](https://github.com/epam/Indigo/issues/3600) Layout is wrong while open HELM file in the Flex mode of Macromolecules mode
* [3220](https://github.com/epam/Indigo/issues/3220) System ignores implicitly provided file format on load content thru Paste From Clipboard way
* [3606](https://github.com/epam/Indigo/issues/3606) Bond length between the base and the sugar is not standart if the selected group is forming an n-agon with 12 or more than 12 points
* #3641, [3642](https://github.com/epam/Indigo/issues/3642) Add/Remove explicit hydrogens operation causes Error: array: invalid index 2 (size=2) exception
* [3661](https://github.com/epam/Indigo/issues/3661) BILN import/export special cases

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.43.0-rc.1...indigo-1.44.0