# Indigo 1.25.0
Released 2024-11-18

## Features
* [2236](https://github.com/epam/Indigo/issues/2236) Import/export multi-tails in KET
* [2162](https://github.com/epam/Indigo/issues/2162) Add support for rendering embedded SVGs while exporting to PNG 
* [2129](https://github.com/epam/Indigo/issues/2129) Render Multi-tail Arrows for Pathway Reactions in PNG and SVG
* [2176](https://github.com/epam/Indigo/issues/2176) add ACS style reaction layout
* [2209](https://github.com/epam/Indigo/issues/2209) SVG image support in CDX/CDXML
* [2237](https://github.com/epam/Indigo/issues/2237) Save multi reactions (pathway, single, edge cases) to RDF
* [2175](https://github.com/epam/Indigo/issues/2175) Adjust the rendering of PNG and SVG formats for ACS style

## Bugfixes and improvements
* [2293](https://github.com/epam/Indigo/issues/2293) Export IDT doesn't work for natural ambiguous monomers
* [2383](https://github.com/epam/Indigo/issues/2383) update lunasvg
* [2309](https://github.com/epam/Indigo/issues/2309) Update layout for pathway reaction on canvas
* [1989](https://github.com/epam/Indigo/issues/1989) Convert api does not recognise format during autodetection
* [2070](https://github.com/epam/Indigo/issues/2070) Settings for the "attachment point tool" don't update with changed pixel settings
* [2457](https://github.com/epam/Indigo/issues/2457) The reaction is not in the center of the picture after saved in png (svg)
* [2444](https://github.com/epam/Indigo/issues/2444) The thickness of the arrow is incorrect when saving to png(svg)
* [2447](https://github.com/epam/Indigo/issues/2447) single up and single down bonds are displayed incorrect when save to PNG(svg)
* [2257](https://github.com/epam/Indigo/issues/2257) Unable to save CHEM SS3 to IDT format
* [2312](https://github.com/epam/Indigo/issues/2312) Export of ambiguous monomers doesn't work (error appears) to any export format (even to SVG/PNG) except KET
* [2433](https://github.com/epam/Indigo/issues/2433) Issues with Saving and Opening Structures with Multi-Tailed Arrow in CDX and CDXML Formats
* [2512](https://github.com/epam/Indigo/issues/2512) Equilibrium Half Arrows are displayed incorrect when saved to PNG (svg) by default size
* [2217](https://github.com/epam/Indigo/issues/2217) The wrong direction of the arrows when exporting from CDXML (or CDX, base64 cdx) format and two retrosynthetic arrows
* [2422](https://github.com/epam/Indigo/issues/2422) Indigo functions doesn't work prorerly: Aromatize, Dearomatize, Layout, Clean Up, Hydrogens, Auto-Mapping Tool
* [2458](https://github.com/epam/Indigo/issues/2458) The reaction with catalysts is displayed incorrect with ACS style setting and after layout
* [2440](https://github.com/epam/Indigo/issues/2440) System shouldn't allow user to export alternatives ambiguous monomers to IDT (since only mixtures are supported)
* [2331](https://github.com/epam/Indigo/issues/2331) System should throw an error in case of wrong IUBcode
* [2122](https://github.com/epam/Indigo/issues/2122) Sugar R should not save in the IDT format
* [2446](https://github.com/epam/Indigo/issues/2446) Sub font size is incorrect when save to png (svg)
* [2407](https://github.com/epam/Indigo/issues/2407) The ordering of branches of cascade reactions and reactions themselves should be the same on Load/Save from/to RDF
* [2478](https://github.com/epam/Indigo/issues/2478) The arrow is displayed incorrect when import from rxn file
* [2603](https://github.com/epam/Indigo/issues/2603) Unknown 'a' CIP stereochemistry cause error in CDXML parser


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.24.0-rc.1...indigo-1.25.0
