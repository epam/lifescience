# Indigo 1.32.0
Released 2025-06-18

## Features
* [2767](https://github.com/epam/Indigo/issues/2767) Add support for Postgres 17
* [1970](https://github.com/epam/Indigo/issues/1970) New text entities in KET-format
* [2843](https://github.com/epam/Indigo/issues/2843) Support of "HELM alias" property for monomers
* [2844](https://github.com/epam/Indigo/issues/2844) Support for "Modification Type" property of monomers
* [2870](https://github.com/epam/Indigo/issues/2870) Add suuport for flip expanded monomer
* [2840](https://github.com/epam/Indigo/issues/2840) Add InChI key method to cpp api

## Bugfixes and improvements
* [2805](https://github.com/epam/Indigo/issues/2805) Saving of 3:3 reaction to SDF v2000 causes exception: Convert error! core: \<reaction\> is not a base molecule
* [2781](https://github.com/epam/Indigo/issues/2781) Ketcher fails to save structure in MOL V3000 format when encountering custom attachment labels like “Ch”
* [2851](https://github.com/epam/Indigo/issues/2851) Macromolecule property Molecular mass wrong calculation
* [2772](https://github.com/epam/Indigo/issues/2772) Saving monomers to SDF v3000 works wrong - system saves every monomer template for every monomer on the canvas 
* [2860](https://github.com/epam/Indigo/issues/2860) Copy to clipboard doesn't work if Multi-Tailed Arrow present on the canvas
* [2858](https://github.com/epam/Indigo/issues/2858) Export to any format doesn't work. System throw exception
* [2047](https://github.com/epam/Indigo/issues/2047) Saved Ellipse and Line Shapes in CDX, CDXML, Base 64 CDX formats are not correctly displayed after opening
* [2868](https://github.com/epam/Indigo/issues/2868) Indigo use wrong rotate parameter name KET files
* [2867](https://github.com/epam/Indigo/issues/2867) API calculateMacroProperties does not allow to pass parameters for UPC and NAC
* [2859](https://github.com/epam/Indigo/issues/2859) System wrongly reverse reaction order on Calculated Values dialog (and thus - values are wrong)
* [2462](https://github.com/epam/Indigo/issues/2462) Can't save a reaction with Multi-Tailed Arrow to Daylight SMARTS format
* [2892](https://github.com/epam/Indigo/issues/2892) API calculateMacroProperties does not work if only molecule passed as a parameter without monomers
* [2888](https://github.com/epam/Indigo/issues/2888) Unable to export single expanded monomer to SVG Image, system throws error: array: invalid index 0
* [1679](https://github.com/epam/Indigo/issues/1679) System ignores carrige return in text blocks in loaded CDX
* [1683](https://github.com/epam/Indigo/issues/1683) System shifts text label to the right
* [2897](https://github.com/epam/Indigo/issues/2897) Calculated Values doesn't work if reaction arrow overlaps reactant bounding box
* [2931](https://github.com/epam/Indigo/issues/2931) Calculated values doesn't work for "rich" monomer chain
* [2917](https://github.com/epam/Indigo/issues/2917) Molecular mass and Molecular formula are not calculated for Molecule (custom CHEM)
* [2939](https://github.com/epam/Indigo/issues/2939) System doesn't calculate melting temperature for GC nucleotides pair
* [2930](https://github.com/epam/Indigo/issues/2930) System shouldn't count bases that are not part of a nucleotide/nucleoside as RNA/DNA
* [2947](https://github.com/epam/Indigo/issues/2947) System "caches" PNG/SVG of canvas and stops reflect rotation/flip chanages if any
* [2987](https://github.com/epam/Indigo/issues/2987) Melting temperature value missed if UPC or NAC value set to zero
* [2946](https://github.com/epam/Indigo/issues/2946) Non-standard connections cause chain break in macromolecule properties calculation
* [2902](https://github.com/epam/Indigo/issues/2902) Indigo does not calculate properties for Peptides tab if Phosphate is missing in mixed chain
* [2903](https://github.com/epam/Indigo/issues/2903) Indigo fails to calculate properties when two chains are connected via a microstructure
* [2904](https://github.com/epam/Indigo/issues/2904) Indigo fails to calculate properties when two chains are connected via a CHEM
* [2905](https://github.com/epam/Indigo/issues/2905) Incorrect Calculate Properties result when monomers are connected via not a R2-R1


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.31.0-rc.1...indigo-1.32.0