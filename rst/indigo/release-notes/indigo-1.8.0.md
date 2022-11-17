# Indigo 1.8.0

*17 Nov. 2022*

## Features
* Core: Added indigo option "smiles-saving-format" to save daylight smiles [#876](https://github.com/epam/Indigo/issues/876)
* Core: Support for generic and polymer s-groups for extended SMILES [#874](https://github.com/epam/Indigo/issues/874)
* Core: Added dearomatize on load option "dearomatize-on-load" [#868](https://github.com/epam/Indigo/issues/868)
* Core: Reagents support for miscellaneous cases: SMILES, SMARTS, SVG and PNG rendering. [#837](https://github.com/epam/Indigo/issues/837),[#836](https://github.com/epam/Indigo/issues/836),[#835](https://github.com/epam/Indigo/issues/835),[#834](https://github.com/epam/Indigo/issues/834)
* Core: Reagents and conditions support in CDXML format (#832) [#832](https://github.com/epam/Indigo/issues/832)
* Core: Reagents support for RXN [#830](https://github.com/epam/Indigo/issues/832)
* Core: Added equilibrium arrows rendering [#808](https://github.com/epam/Indigo/issues/832), [#801](https://github.com/epam/Indigo/issues/801)
* Core: Add support for Lee-Crippen SMARTS pKa calculation method [#791](https://github.com/epam/Indigo/issues/791)
* Core: Query features support for KET [#303](https://github.com/epam/Indigo/issues/303) 
* API: Support for CDXML format [#853](https://github.com/epam/Indigo/issues/853)
* Implement version update script and specify versioning policy [#794](https://github.com/epam/Indigo/issues/794)
* Utils: indigo-service: Configuration refactoring and simplification [#777](https://github.com/epam/Indigo/issues/777)
* API: add hash calculation for molecules and reactions [#768](https://github.com/epam/Indigo/issues/768),[#769](https://github.com/epam/Indigo/issues/769)

## Improvements
* API: python: reorganize codebase, drop support of Python 2 [#798](https://github.com/epam/Indigo/issues/798)
* API: salt checking implemented [#537](https://github.com/epam/Indigo/issues/537)
* Core: Simple objects rendering [#309](https://github.com/epam/Indigo/issues/309)

## Bugfixes
* API: Versions 1.5 and later conflict with xgboost [#770](https://github.com/epam/Indigo/issues/778)
* Core: Calculate CIP function - atom list issue [#736](https://github.com/epam/Indigo/issues/736)
* Core: KET format: Issues with plus and arrow signs for reactions. [#733](https://github.com/epam/Indigo/issues/733), [#732](https://github.com/epam/Indigo/issues/732)
* Core: KET format: R-Groups generation bug [#711](https://github.com/epam/Indigo/issues/711)
* Core: Text objects rendering issue [#706](https://github.com/epam/Indigo/issues/706)
* Core: Dative and hydrogen bonds issue [#654](https://github.com/epam/Indigo/issues/654)
* Core: loadMolecule segfault for certain inputs [#545](https://github.com/epam/Indigo/issues/545)
* Core: Empty molecule with R-Group is not rendered [#356](https://github.com/epam/Indigo/issues/356)
* Core: Generic S-Group is not rendered [#355](https://github.com/epam/Indigo/issues/355)
* Core: Calling molecularWeight() on an invalid isotope kills the JVM when called from Java [#641](https://github.com/epam/Indigo/issues/641)
