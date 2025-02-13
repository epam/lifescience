# Indigo 1.28.0
Released 2025-02-13

## Bugfixes 
* [#2313](https://github.com/epam/Indigo/issues/2313) Indigo functions doesn't work if ambiguous monomer present on the canvas 
* [#2435](https://github.com/epam/Indigo/issues/2435) Export of ambiguous monomers to Sequence/FASTA doesn't work for mixed ambiguous monomers
* [#2324](https://github.com/epam/Indigo/issues/2324) System loads DNA bases instead of RNA ones during IDT import
* [#2387](https://github.com/epam/Indigo/issues/2387) After opening a saved HELM file, microstructure name F1 turns into Mod0
* [#2062](https://github.com/epam/Indigo/issues/2062) HELM loader ignores repeating token
* [#2332](https://github.com/epam/Indigo/issues/2332) Error message should use "ambiguous monomer" instead of "variant monomer" 
* [#2338](https://github.com/epam/Indigo/issues/2338) System loads HELM inline SMILES phosphate as base (RNA1{R[P%91(O)(O)=O.[*:1]%91 |$;;;;_R1$|]}$$$$V2.0)
* [#2436](https://github.com/epam/Indigo/issues/2436) System should report an error if we have one or more monomers on the canvas don't have mapping for them in case of export to Sequence/FASTA
* [#2427](https://github.com/epam/Indigo/issues/2427) Import of unsplit monomers from HELM doesn't work 
* [#2041](https://github.com/epam/Indigo/issues/2041) Monomer could be saved to RXN V3000 format but can't be loaded back - exception
* [#2137](https://github.com/epam/Indigo/issues/2137) An error occurred while saving the unresolved nucleotides and arrow in the RXN3000 format
* [#2195](https://github.com/epam/Indigo/issues/2195) Indigo functions doesn't work if query atom and monomer on the canvas at the same time
* [#2126](https://github.com/epam/Indigo/issues/2126) An error occurred while saving the nucleotide and arrow in the RXN2000 format
* [#2330](https://github.com/epam/Indigo/issues/2330) Error diagnostic is not clear in case of wrong percent value type
* [#2622](https://github.com/epam/Indigo/issues/2622) Saving to MOL 3000 cause template data loss that causes wrong export to HELM
* [#2361](https://github.com/epam/Indigo/issues/2361) Wrong error message if SMILES phosphate has lack of attachemt point 
* [#2359](https://github.com/epam/Indigo/issues/2359) System loads HELM even it it has wrong connection section (PEPTIDE1{[DACys]}|PEPTIDE2{C}$PEPTIDE1,PEPTIDE2,1:R1-1:R2$$$V2.0)
* [#2539](https://github.com/epam/Indigo/issues/2539) Export of unknown monomer to HELM doesn't work
* Revert "[#2657](https://github.com/epam/Indigo/issues/2657)  - Add ES6 options for WASM build ([#2658](https://github.com/epam/Indigo/issues/2658))"

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.26.0-rc.1...indigo-1.27.0

