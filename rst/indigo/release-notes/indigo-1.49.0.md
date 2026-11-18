# Indigo 1.49.0
Released 2026-11-18

## New features
* #3617 - Valence as a function of dative bonds
* #3770 – Add support for custom fonts in SVG and PNG
* #3842 - Provide a support for attachment groups and haptic bonds in all wrappers available within Indigo.
* #3843 - Support haptic bonds in CDX/CDXMLload/save operations
* #3844 - Haptic bonds layout
* #3915 - Allow users to add custom abbreviations to indgio via the API

## Bugfixes and improvements
* Fix EPAM Indigo parsing so that the S groups needs to saved before collection block
* Add PostgreSQL 18 support
* #3870 - initialize claude settings for project
* #3863 – canonicalSmiles() fails with "SMILES saver: bad cycle number: 100" for highly cyclic valid SMILES
* #3882 – Generate unique glyph IDs at the SVG export


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.48.0-rc.1...indigo-1.49.0