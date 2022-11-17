# Indigo 1.8.0

*17 Nov. 2022*

## Features
* Core: Added indigo option "smiles-saving-format" to save daylight smiles (#876)
* Core: Support for generic and polymer s-groups for extended SMILES (#874)
* Core: Added dearomatize on load option "dearomatize-on-load" (#868)
* Core: Reagents support for miscellaneous cases: SMILES, SMARTS, SVG and PNG rendering. (#837,#836,#835,#834)
* Core: Reagents and conditions support in CDXML format (#832)
* Core: Reagents support for RXN (#830)
* Core: Added equilibrium arrows rendering (#808, #801)
* Core: Add support for Lee-Crippen SMARTS pKa calculation method (#791)
* Core: Query features support for KET (#303) 
* API: Support for CDXML format (#853)
* Implement version update script and specify versioning policy (#794)
* Utils: indigo-service: Configuration refactoring and simplification (#777)
* API: add hash calculation for molecules and reactions (#768,#769)

## Improvements
* API: python: reorganize codebase, drop support of Python 2 (#798)
* API: salt checking implemented (#537)
* Core: Simple objects rendering (#309)

## Bugfixes
* API: Versions 1.5 and later conflict with xgboost (#770)
* Core: Calculate CIP function - atom list issue (#736)
* Core: KET format: Issues with plus and arrow signs for reactions. (#733, #732)
* Core: KET format: R-Groups generation bug (#711)
* Core: Text objects rendering issue (#706)
* Core: Dative and hydrogen bonds issue (#654)
* Core: loadMolecule segfault for certain inputs (#545)
* Core: Empty molecule with R-Group is not rendered (#356)
* Core: Generic S-Group is not rendered (#355)
* Core: Calling molecularWeight() on an invalid isotope kills the JVM when called from Java (#641)
