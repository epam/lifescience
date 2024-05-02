# Indigo 1.19.0
Released 2024-05-02

## Features
* [#1755](https://github.com/epam/Indigo/issues/1755) Import and export fasta format for RNA, DNA and PEPTIDES
* [#1466](https://github.com/epam/Indigo/issues/1466) Export as sequence string for RNA, DNA and PEPTIDEs

## Bugs
* [#1787](https://github.com/epam/Indigo/issues/1787) Some Bonds from ChemDraw don't open in the Ketcher
* [#1776](https://github.com/epam/Indigo/issues/1776) Cannot add to Canvas saved in the Ketcher CDX file with Bond structures
* [#1775](https://github.com/epam/Indigo/issues/1775) Save to CDX converts triple bond to Single/Double Aromatic bond
* [#1774](https://github.com/epam/Indigo/issues/1774) Save to CDX converts aromatic benzene ring to dashed ring
* [#1425](https://github.com/epam/Indigo/issues/1425) Indexing of a substantial quantity of molecules instigates the indexing process for the entire file.
* [#1575](https://github.com/epam/Indigo/issues/1575) Basic hydrogen layout problem - angles of hydrogens are not perfect
* [#1771](https://github.com/epam/Indigo/issues/1771) Bingo version does not return current tag
* [#1761](https://github.com/epam/Indigo/issues/1761) Can't export sequence with 1 monomer to molv3000
* [#1598](https://github.com/epam/Indigo/issues/1598) Macro: V3000 export: leaving groups are displayed as side chain connections for standard presets added to canvas
* [#1477](https://github.com/epam/Indigo/issues/1477) sequence id calculation for molv3000
* [#1563](https://github.com/epam/Indigo/issues/1563) Unable to load mol file: System throws exception: Convert error! Unexpected token '<', "<!DOCTYPE "... is not valid JSON
* [#1852](https://github.com/epam/Indigo/issues/1852) Macro(Export FASTA): The header 'Sequence N' is missing, and '>' symbol is located at end of the first sequence
* [#1822](https://github.com/epam/Indigo/issues/1822) Fasta: All Peptides should be saved to FASTA format and (use N/X symbol as well).
* [#1851](https://github.com/epam/Indigo/issues/1851) Macro(Import FASTA): The ';' symbol is not recognized as a comment
* [#1786](https://github.com/epam/Indigo/issues/1786) Some bonds from Ketcher don't display correctly in the Ketcher and the ChemDraw for CDXML format. 
* [#1777](https://github.com/epam/Indigo/issues/1777) Some bonds don't display correctly in ChemDraw when opening a saved Ketcher CDX file.
* [#1849](https://github.com/epam/Indigo/issues/1849) Macro(Import FASTA): The ' * ' symbol occurring between two letters is not recognized as a break in peptide chain
* [#1850](https://github.com/epam/Indigo/issues/1850) Macro(Import FASTA): The '>' symbol is not recognized as indicating a new sequence
* [#1802](https://github.com/epam/Indigo/issues/1802) bad performance in WASM during the parsing of large sequences
* [#1848](https://github.com/epam/Indigo/issues/1848) Cannot save FASTA using the Remote mode
* [#1791](https://github.com/epam/Indigo/issues/1791) Aromatic is lost from Benzene while save to CDX/base64 CDX formats
* [#1774](https://github.com/epam/Indigo/issues/1774) Save to CDX converts aromatic benzene ring to dashed ring
* [#1773](https://github.com/epam/Indigo/issues/1773) Save to CDX converts plus and arrow into lone pair and line
* [#1796](https://github.com/epam/Indigo/issues/1796) Some bonds from ChemDraw don't display correctly in the Ketcher.
* [#1814](https://github.com/epam/Indigo/issues/1814) Macro: System ignore spaces and line breaks when importing a sequence through Paste from Clipboard
* [#1801](https://github.com/epam/Indigo/issues/1791) No monomer full name when import from a sequence
* [#1161](https://github.com/epam/Indigo/issues/1161) bingo unable to index on sql server
* [#1773](https://github.com/epam/Indigo/issues/1773) Save to CDX converts plus and arrow into lone pair and line
* [#1774](https://github.com/epam/Indigo/issues/1774) Save to CDX converts aromatic benzene ring to dashed ring 
* [#1796](https://github.com/epam/Indigo/issues/1796) Some bonds from ChemDraw don't display correctly in the Ketcher. 
* [#1881](https://github.com/epam/Indigo/issues/1881) Macro: Cannot load Peptides from our Library that are not connected by bonds using FASTA file 

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.18.0...indigo-1.19.0