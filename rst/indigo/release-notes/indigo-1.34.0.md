# Indigo 1.34.0
Released 2025-08-21

## Features
* [2899](https://github.com/epam/Indigo/issues/2899) Peptide sequence should be auto-deceted at insert
* [2958](https://github.com/epam/Indigo/issues/2958) Map molfile monomers onto library monomers on import
* [2967](https://github.com/epam/Indigo/issues/2967) Support for marking of nucleotide components
* [2952](https://github.com/epam/Indigo/issues/2952) Expand c api to return CIP labels

## Bugfixes and improvements
* [2929](https://github.com/epam/Indigo/issues/2929) Isoelectric Point calculation formula seems to be wrong
* [2964](https://github.com/epam/Indigo/issues/2964) System loads base as sugar
* [2985](https://github.com/epam/Indigo/issues/2985) Incorrect Implementation of PKA calculation 
* [2926](https://github.com/epam/Indigo/issues/2926) Atom weights in indigo should be updated according to last IUPAC data
* [2936](https://github.com/epam/Indigo/issues/2936) System doesn't calculate melting temperature for mix of nucleotides/nucleosides and unsplit nucleotides/unsplit nucleosides
* [2965](https://github.com/epam/Indigo/issues/2965) System shouldn't allow to export molecules to 3-letter sequence format
* [2989](https://github.com/epam/Indigo/issues/2989) Export (and import) of sequence of nucleosides to HELM works wrong (doesn't work for import)
* [2993](https://github.com/epam/Indigo/issues/2993) System shouldn't consider closing bracket as part of name
* [2998](https://github.com/epam/Indigo/issues/2998) Input fields for ion concentration and oligonucleotides become inactive after entering excessively long number
* [2970](https://github.com/epam/Indigo/issues/2970) Rendering CIP labels breaks the generated svg for firefox
* [3014](https://github.com/epam/Indigo/issues/3014) Wrong bingo-postgres-linux version


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.33.0-rc.1...indigo-1.34.0