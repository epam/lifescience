# Indigo 1.27.0
Released 2025-02-12

## Features
* [2559](https://github.com/epam/Indigo/issues/2559) Read Name and Reaction Conditions from RDF Metadata as a text
* [2404](https://github.com/epam/Indigo/issues/2404) Save Name and Reaction Conditions to RDF Metadata
* [2657](https://github.com/epam/Indigo/issues/2657) Add ES6 options for WASM build
* [2652](https://github.com/epam/Indigo/issues/2652) Skip Name and/or Reaction Conditions metadata fields on save to RDF if no data is available
* [2574](https://github.com/epam/Indigo/issues/2574) Support for Collapsed monomers

## Bugfixes 
indentation errors in docstring description
* [2654](https://github.com/epam/Indigo/issues/2654) Arrow size become 2 bonds length after indigo changed default arrow size to 1
* [2665](https://github.com/epam/Indigo/issues/2665) Margins are missing if no reaction result
* [2664](https://github.com/epam/Indigo/issues/2664) Vertical margin for catalyst is wrong
* [2662](https://github.com/epam/Indigo/issues/2662) Arrow size is wrong if reaction loaded from SMARTS
* [2653](https://github.com/epam/Indigo/issues/2653) Indigo should send to ketcher different bond size for macromolecules
* [2647](https://github.com/epam/Indigo/issues/2647) Reaction's name or conditions text wraps incorrectly in specific cases: the last line before truncating, removing of special symbols, empty line instead of "..."
* [2583](https://github.com/epam/Indigo/issues/2583) Not correct length of Multi-Tailed and Single arrows for reactions with atoms after loading from RDF or Layout actions 
* [2519](https://github.com/epam/Indigo/issues/2519) The length of the arrow becomes 2 bonds after layout but should be 1
* [2624](https://github.com/epam/Indigo/issues/2624) Elliptic arrow rendered wrong while expotring to PNG in remote mode
* [2497](https://github.com/epam/Indigo/issues/2497) Test fail on compare CML file for R-group

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.26.0-rc.1...indigo-1.27.0

