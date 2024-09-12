# Indigo 1.21.0
Released 2024-08-27

## Features
* [1903](https://github.com/epam/Indigo/issues/1903) Introduce IDT alias for monomers and RNA presets in Ket format
* [1901](https://github.com/epam/Indigo/issues/1901) Receive monomer library from Ketcher upon import/export IDT notation
* [1900](https://github.com/epam/Indigo/issues/1900) Export of modified RNA to IDT notation (modified IDT monomers)
* [1899](https://github.com/epam/Indigo/issues/1899) Import of modified IDT monomers

## Bugsfixes
* [1974](https://github.com/epam/Indigo/issues/1974) Preview: User can save IDT with 5' phosphate but cannot open this file again.
* [1972](https://github.com/epam/Indigo/issues/1972) Can't save KET with nameless superatom
* [1996](https://github.com/epam/Indigo/issues/1996) Cannot open IDT with MOE sugar.
* [1960](https://github.com/epam/Indigo/issues/1960) Fix error message in the SequenceLoader for an invalid sequence
* [1928](https://github.com/epam/Indigo/issues/1928) Support monomer to molecule connections type
* [1878](https://github.com/epam/Indigo/issues/1878) The structure saved in CML format does not open
* [1843](https://github.com/epam/Indigo/issues/1843) FASTA export: 80 chars limit
* [2000](https://github.com/epam/Indigo/issues/2000) Exporting a CDX file to ChemDraw loses information about charge on atoms
* [1997](https://github.com/epam/Indigo/issues/1997) Export to IDT doesn't work at all for remote indigo
* [1993](https://github.com/epam/Indigo/issues/1993) Micro and macro structures connected through attachment points cannot be opened after save in CDXML format in micro mode
* [2004](https://github.com/epam/Indigo/issues/2004) Errors occur when trying to save a macro structure connected to a micro structure to MOL V3000
* [1994](https://github.com/epam/Indigo/issues/1994) Micro and macro structures connected through attachment points cannot be opened after save in CDX and Base 64CDX format in micro mode
* [1992](https://github.com/epam/Indigo/issues/1992) Micro and macro structures connected through attachment points cannot be saved in Extended SMILES format in micro mode
* [1990](https://github.com/epam/Indigo/issues/1990) Micro and macro structures connected through attachment points cannot be saved in CML format in micro mode
* [1984](https://github.com/epam/Indigo/issues/1984) Error message is wrong if in case if position indicator in IDT code contradicts real position of the monomer in the chain
* [1982](https://github.com/epam/Indigo/issues/1982) Cannot open some expected IDT.

## Improvements
* [1976](https://github.com/epam/Indigo/issues/1976) Too slow monomer library load

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.21.0...indigo-1.20.0
