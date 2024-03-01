# Indigo 1.18.0
Released 2024-02-29

## Features
* [#1412](https://github.com/epam/Indigo/issues/1412) Nucleotide splitting for V3000 molfile SCSR  
* [#1450](https://github.com/epam/Indigo/issues/1450) No naturalAnalogShort in KET for basic aminoacids during conversion MOLV3000 -> KET 
* [#1436](https://github.com/epam/Indigo/issues/1436) Expose Fold/Unfold hydrogens function in indigo API
* [#1440](https://github.com/epam/Indigo/issues/1440) Add support for query features in MOL, SDF and RXN formats (Marvin extension)
* [#1426](https://github.com/epam/Indigo/issues/1426) Import sequence format for RNA, DNA and PEPTIDES 
* [#1589](https://github.com/epam/Indigo/issues/1589) Apply hydrogens folding/unfolding with respect to selected atoms 
## Bugs
* [#1307](https://github.com/epam/Indigo/issues/1307) Error in DevTool console about memory access out of bound when call 'ketcher.getRxn()' 
* [#1431](https://github.com/epam/Indigo/issues/1431) Crash during parsing query mol-file
* [#1439](https://github.com/epam/Indigo/issues/1439) Indigo can't parse KET with R-Site as a leaving group 
* [#1232](https://github.com/epam/Indigo/issues/1232) Multi-line reaction cause access violationg exception.
* [#1423](https://github.com/epam/Indigo/issues/1423) Common atoms loaded as aliphatic in SMARTS mode
* Update bug_report.md
* [#1458](https://github.com/epam/Indigo/issues/1458) Failed UT api\indigo_test.py:test_convert_smarts 
* [#1460](https://github.com/epam/Indigo/issues/1460) ImplicitH set to zero casue error loading query molecule from ket 
* [#1446](https://github.com/epam/Indigo/issues/1446) Dearomatization does not work with query features
* PostgreSQL 11 EOL support 
* [#1465](https://github.com/epam/Indigo/issues/1465) Unable to load specific mol-file
* [#1484](https://github.com/epam/Indigo/issues/1484) Query molecule convert implicit/explicit hydrogens cause error 
* [#1512](https://github.com/epam/Indigo/issues/1512) Broken string-formats support for wasm 
* [#1452](https://github.com/epam/Indigo/issues/1452) Convert from implicit hydrogens change layout 
* [#1463](https://github.com/epam/Indigo/issues/1463) Macro: Some molecules are not perfect on preview tooltip 
* [#1524](https://github.com/epam/Indigo/issues/1524) Dearomatizing doesn't work for molecula with custom query fetures 
* [#1568](https://github.com/epam/Indigo/issues/1568) Wrong molecule nodes enumeration in KET-file 
* [#1476](https://github.com/epam/Indigo/issues/1476) Aromatization/Dearomatization wipes out SOME Ring bond count values 
* [#1478](https://github.com/epam/Indigo/issues/1478) Dearomatization causes exception in case of Implicit H count query feature set to 4 (i.e. more than 2) 
* [#1525](https://github.com/epam/Indigo/issues/1525) System attach two explicit hydrogens to aromatized ring 
* [#1573](https://github.com/epam/Indigo/issues/1573) Add/Remove explicit hydrogens can't be applied to fullerene C60 - system throws exception 
* [#1567](https://github.com/epam/Indigo/issues/1567) System can't copy atom with custom query feature to clipboard 
* [#1534](https://github.com/epam/Indigo/issues/1534) Presence of stand alone H2 molecule on the canvas breaks Add explicit hydrogens feature (it stops working) 
* [#1468](https://github.com/epam/Indigo/issues/1468) Valence lost on loading molfile with MRV extension.
* [#1472](https://github.com/epam/Indigo/issues/1472) Dearomatization wipes out Aromaticity query property
* [#1504](https://github.com/epam/Indigo/issues/1504) Molfile MRV extension generated for "H count"
* [#1500](https://github.com/epam/Indigo/issues/1500) Atom Query feature export: System replace "Ring membership" values with "Ring Bond Count" ones for value 0 - export to SDF V2000 file 
* [#1564](https://github.com/epam/Indigo/issues/1564) Add/Remove explicit hydrogens wanishes "Chirality" value 
* [#1598](https://github.com/epam/Indigo/issues/1598) Macro: V3000 export: leaving groups are displayed as side chain connections for standard presets added to canvas 
* [#1533](https://github.com/epam/Indigo/issues/1533) System attach two explicit hydrogens to atoms connected to "any type" bonds 
* [#1608](https://github.com/epam/Indigo/issues/1608) convert_explicit_hydrogens response doesn't comply with the ket schema 
* [#1538](https://github.com/epam/Indigo/issues/1538) Add/Remove explicit hydrogens feature doesn't work if atom with problem valence present on canvas (crash happens) 
* [#1614](https://github.com/epam/Indigo/issues/1614) Adding hydrogens doesn't work for bonds with No center value of Reacting Center 
* [#1550](https://github.com/epam/Indigo/issues/1550) Add/Remove explicit hydrogens feature doesn't work for "Any Atom" molecule with valence value set
* [#1593](https://github.com/epam/Indigo/issues/1593) Macro: V3000 import: removed 5' phosphate is displayed in Ketcher
* [#1483](https://github.com/epam/Indigo/issues/1483) Unable to past empty reaction (arrow only) from clipboard to canvas
* [#1607](https://github.com/epam/Indigo/issues/1607) Unable to load large base64 CDX content to canvas if remote indigo used`
* [#1536](https://github.com/epam/Indigo/issues/1536) Add/Remove explicit hydrogens feature doesn't work for reactions on canvas (crash happens)
* [#1652](https://github.com/epam/Indigo/issues/1652) Unfold hydrogens does not select added bonds 
* [#1640](https://github.com/epam/Indigo/issues/1640) System adds hydrogens for only one atom among many selected by 
* [#1634](https://github.com/epam/Indigo/issues/1634) Add/Remove hydrogens doesn't work for atoms with Radical=Triplete if atom with query feature present on the canvas
* [#1629](https://github.com/epam/Indigo/issues/1629) Add/Rmove hydrogens process should count R-Group attachment point as hydrogen
* [#1695](https://github.com/epam/Indigo/issues/1695) CDX loader failed if object with zero id follow by reaction 
* [#1697](https://github.com/epam/Indigo/issues/1697) CDX loader crashed on some files with abbreviations by 
* [#1684](https://github.com/epam/Indigo/issues/1684) System put on the canvas two arrows (one above other) per each arrow on target CDX 
* [#1724](https://github.com/epam/Indigo/issues/1724) Fold hydrogen in reaction with selection works wrong by 
* [#1730](https://github.com/epam/Indigo/issues/1730) UT cano/permutations is too slow by 
* [#1576](https://github.com/epam/Indigo/issues/1576) Bad molecule layout after adding hydrogens (Chlorophyll A) 
* [#1685](https://github.com/epam/Indigo/issues/1685) System shows attached abbreviation group in wrong position 

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.16.0...indigo-1.18.0

