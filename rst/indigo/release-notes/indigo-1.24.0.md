# Indigo 1.24.0
Released 2024-10-04

## Features
* [2096](https://github.com/epam/Indigo/issues/2096) Support retrosynthetic arrows - PNG/SVG rendering
* [2097](https://github.com/epam/Indigo/issues/2097) Add retrosynthetic arrow import/export for cdx/cdxml formats
* [2031](https://github.com/epam/Indigo/issues/2031) Build a data structure for a reaction tree
* [1619](https://github.com/epam/Indigo/issues/1619) Import/export of variant monomers from IDT
* [2052](https://github.com/epam/Indigo/issues/2052) Position pathway reaction on canvas
* [2015](https://github.com/epam/Indigo/issues/2015) Import/Export of variant monomers from Fasta/Sequence
* [2028](https://github.com/epam/Indigo/issues/2028) PNG image support in CDX/CDXML
* [2128](https://github.com/epam/Indigo/issues/2128) Add Multi-tail Arrows to Pathway Reactions Loaded from RDF
* [2188](https://github.com/epam/Indigo/issues/2188) HELM 2 support: variant monomers
* [2189](https://github.com/epam/Indigo/issues/2189) HELM 2 support: support for SMILES 

## Bugfixes
* [2232](https://github.com/epam/Indigo/issues/2232) System replace arrows of diffrent types with Open Arrow type while loading from PPTX(CDX)
* [2249](https://github.com/epam/Indigo/issues/2249) Arrow Open Angle changes to Arrow Filled Triangle after saving and opening in CDX/CDXML
* [2120](https://github.com/epam/Indigo/issues/2120) Export the structure for nucleotides 2-Amino-dA does not work correctly
* [2266](https://github.com/epam/Indigo/issues/2266) Error message is wrong for missing ratio number (PEPTIDE1{(A:+C:0.1)}$$$$V2.0)
* [2300](https://github.com/epam/Indigo/issues/2300) HELM loading doesn't work in remote version
* [2293](https://github.com/epam/Indigo/issues/2293) Export IDT doesn't work for natural ambiguous monomers
* [2336](https://github.com/epam/Indigo/issues/2336) Ribose sugar doesn't allow to load IDT custom mixed bases
* [2358](https://github.com/epam/Indigo/issues/2358) Import of monomer with only one connection point (R2) doesn't work
* [2321](https://github.com/epam/Indigo/issues/2321) Export of multi-character monomer IDs inside ambiguous monomer works wrong
* [2375](https://github.com/epam/Indigo/issues/2375) Export to IDT doesn't work at all for mixed bases
* [2356](https://github.com/epam/Indigo/issues/2356) Library ambiguous peptides loaded as mixtures from FASTA
* [2357](https://github.com/epam/Indigo/issues/2357) Export to HELM doesn't work if we connect peptide TO molecule
* [2303](https://github.com/epam/Indigo/issues/2303) Import of variant monomers from Sequence doesn't work for RNA and FASTA for RNA/DNA
* [2355](https://github.com/epam/Indigo/issues/2355) Import of HELM with fractional ratio mixture values doesn't work - system expects integer
* [2421](https://github.com/epam/Indigo/issues/2421) Incorrect stereo-label placement for (E) and (Z) (indigo part)
* [2417](https://github.com/epam/Indigo/issues/2417) The layout is incorrect with retrosynthetic arrow

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.24.0...indigo-1.23.0
