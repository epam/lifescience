# Indigo 1.9.0

*31 January 2023*
 
## Features
* Add support of R-groups to the CDX loader. by @even1024 [#36](https://github.com/epam/Indigo/issues/36)
* cdx import in scope of current KET/CDXML features support by @even1024 [#885](https://github.com/epam/Indigo/issues/885)
* core: replace MultiMap in MoleculeRGroupsComposition class by @loimu [#521](https://github.com/epam/Indigo/issues/521)
* core: replace MultiMap in MolfileLoader class by @loimu [#521](https://github.com/epam/Indigo/issues/521)

## Bugfixes
* MDL Molfile v3000 encoding: Automatic selection of MDL Molfile v3000 encoding doesn't work if the structure contains Enhanced stereochemistry by @mkviatkovskii [#924](https://github.com/epam/Indigo/issues/924)
* Structures with the arrow lose their integrity when pressing 'Layout' by @even1024 [#938](https://github.com/epam/Indigo/issues/938)
* Abbreviations are not supported by @even1024 [#685](https://github.com/epam/Indigo/issues/685)
* api: tests: IronPython update to 3.4.0, fix tests by @mkviatkovskii [#934](https://github.com/epam/Indigo/issues/934)
* CDX import: Reaction arrows disappear when opening a file by @even1024 [#943](https://github.com/epam/Indigo/issues/943)
* CDX import: Aromatized structures are not recognized when Pasting from Clipboard by @even1024 [#950](https://github.com/epam/Indigo/issues/950)
* CDXML parser memory leak by @even1024 [#966](https://github.com/epam/Indigo/issues/966)
* Error opening MOL and RXN files with RBC/SUB/UNC queries by @even1024 [#928](https://github.com/epam/Indigo/issues/928)
* CDX Import, CDXML Import: parsing error when superatom starts with 'R' symbol by @even1024 [#960](https://github.com/epam/Indigo/issues/960)
* CDXML: When opening a saved file with text, the Font size enlarges by @even1024 [#961](https://github.com/epam/Indigo/issues/961)
* CDXML: When opening a file saved with 'Any atom', 'Atom Generics' or 'Group Generics' structure loses its integrity by @even1024 [#968](https://github.com/epam/Indigo/issues/968)
* CDXML import fails to load rectangle primitives by @even1024 in [#979](https://github.com/epam/Indigo/issues/979)
* CDXML: File containing Functional Groups or Salts and Solvents cannot be opened and causes a convert error by @even1024 in [#963](https://github.com/epam/Indigo/issues/963)
* CDXML import: nodes with radicals are not getting parsed by @even1024 [#990](https://github.com/epam/Indigo/issues/990)
* CDXML import: fails to import some cdxml files with multiple text objects related to different fragments by @even1024 [#992](https://github.com/epam/Indigo/issues/992)
* CDXML import: 'superscript' and 'subscript' is not displayed correctly [#962](https://github.com/epam/Indigo/issues/962)
* Improve ssl bingo elastic by @MysterionRise [#863](https://github.com/epam/Indigo/issues/863)
* bingo: postgres: add support for Postgres 15, drop support for Postgres 10 by @mkviatkovskii
* fix auto-saving to CTAB v3000 by @mkviatkovskii [#929](https://github.com/epam/Indigo/issues/929)
