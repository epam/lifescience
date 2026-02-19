# Indigo 1.37.0
Released 2026-02-19

## Features
* [3161](https://github.com/epam/Indigo/issues/3161) SDF files for library/monomer information
* [3152](https://github.com/epam/Indigo/issues/3152) AxoLabs format support
* [3146](https://github.com/epam/Indigo/issues/3146) IDT export: use hardcorded nucleotides instead of standard ones

## Bugfixes and improvements
* [2922](https://github.com/epam/Indigo/issues/2922) Performing an exact match search results in PostgreSQL termination
* [3193](https://github.com/epam/Indigo/issues/3193) Missing valence of 0 in mol file
* [3016](https://github.com/epam/Indigo/issues/3016) Valence 0 is not taken into account by Molfile export via API
* [3079](https://github.com/epam/Indigo/issues/3079) Export to SVG/PNG doesn't work for molecules with "star" atom. System throws an error: molecule render internal: Query atom type 4 not supported
* [3141](https://github.com/epam/Indigo/issues/3141) One time exception on export to RXN: molecule: casting to molecule is invalid
* [3178](https://github.com/epam/Indigo/issues/3178) Unable to copy user created monomer, exception: Convert error! molecule: casting to molecule is invalid
* [3070](https://github.com/epam/Indigo/issues/3070) Saving to RXN v2000 encloses Polymer labels into double quotes
* [3206](https://github.com/epam/Indigo/issues/3206) Export (or import) to (from) Mol v3000 works wrong for CHEM monomers
* [3200](https://github.com/epam/Indigo/issues/3200) System allows to export not a purely amino acid to Sequence (3-letter code)
* [3210](https://github.com/epam/Indigo/issues/3210) System loads Sequence with numbers in middle
* [3102](https://github.com/epam/Indigo/issues/3102) System can't load sugar-phosphate preset from HELM if sugar provided with HELMAlias name
* [3220](https://github.com/epam/Indigo/issues/3220) System ignores implicitly provided file format on load content thru Paste From Clipboard way
* [3187](https://github.com/epam/Indigo/issues/3187) Export to HELM works wrong for custom monomers imported from HELM with inline SMILES (part 2)
* [3228](https://github.com/epam/Indigo/issues/3228) Loading of AxoLabs with last monomer in brackets doesn't work
* [3234](https://github.com/epam/Indigo/issues/3234) Unable to add user`s peptide, nucleotide and CHEM to the library
* [3235](https://github.com/epam/Indigo/issues/3235) System adds broken Preset to the library
* [3238](https://github.com/epam/Indigo/issues/3238) Monomer name is missed if updated from the API
* [3212](https://github.com/epam/Indigo/issues/3212) Export to RXN disorganize the reaction


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.36.0-rc.1...indigo-1.37.0