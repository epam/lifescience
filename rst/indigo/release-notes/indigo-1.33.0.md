# Indigo 1.33.0
Released 2025-08-14

## Features
* [2890](https://github.com/epam/Indigo/issues/2890) Conda support
* [2835](https://github.com/epam/Indigo/issues/2835) Loading HELM with monomers with multi-character IDs without brackets
* [2836](https://github.com/epam/Indigo/issues/2836) Loading monomer NOT from the library as Unknown monomers (in the same manner as it works in IDT)

## Bugfixes and improvements
* [2933](https://github.com/epam/Indigo/issues/2933) Melting temperature calculation works wrong
* [2748](https://github.com/epam/Indigo/issues/2748) Substituents are displayed backwards if appearing on the left of the molecule
* [2934](https://github.com/epam/Indigo/issues/2934) Melting temperature should not be defined for one RNA/DNA nucleotide chain lenght
* [2927](https://github.com/epam/Indigo/issues/2927) Molecule formula atom order wrong
* [522](https://github.com/epam/Indigo/issues/522) core: replace Obj with standard smart pointer
* [2937](https://github.com/epam/Indigo/issues/2937) System doesn't calculate melting temperature for mix of nucleotides/nucleosides and phosphates
* [2720](https://github.com/epam/Indigo/issues/2720) Reaction SMILES lossily handles enhanced stereochemistry
* [2968](https://github.com/epam/Indigo/issues/2968) Melting temperature calculation works wrong
* [2969](https://github.com/epam/Indigo/issues/2969) Export of unknown for Ketcher monomers works wrong
* [2923](https://github.com/epam/Indigo/issues/2923) System doesn't substract from mass of monomer mass of leaving group atom(s) if an attachment point is occupied
* [2966](https://github.com/epam/Indigo/issues/2966) Load from HELM doesn't work for two side chain connected sequences
* [2986](https://github.com/epam/Indigo/issues/2986) Don't calculate Melting temperature for one pair of double stranded DNA/RNA nucleotides


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.32.0-rc.1...indigo-1.33.0