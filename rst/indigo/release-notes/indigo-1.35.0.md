# Indigo 1.35.0
Released 2025-09-19

## Features
* [2894](https://github.com/epam/Indigo/issues/2894) Saving expanded monomers into MOL-files 
* Update monomer expand to follow Indigo structure

## Bugfixes and improvements
* [2900](https://github.com/epam/Indigo/issues/2900) CIP labels are always rendered from cdxml
* [3012](https://github.com/epam/Indigo/issues/3012) Create IUPAC Compliant Chemical Formula
* [3050](https://github.com/epam/Indigo/issues/3050), [3047](https://github.com/epam/Indigo/issues/3047), [3048](https://github.com/epam/Indigo/issues/3048), [3054](https://github.com/epam/Indigo/issues/3054), [3051](https://github.com/epam/Indigo/issues/3051) Loading monomer chain from SDF file works wrong - bonds between monomers got lost/Export RNA monomers from MOLv3000 doesn't work for ACCLDraw export
* [2928](https://github.com/epam/Indigo/issues/2928) Isoelectric Point calculation should take into account occupied leaving groups (exclude them)
* [3053](https://github.com/epam/Indigo/issues/3053) Calculate properties doesn't work for "rich" sequences
* [3049](https://github.com/epam/Indigo/issues/3049) Stereo labels got missied on export to SVG result
* [3056](https://github.com/epam/Indigo/issues/3056) HELM load fails if it contains more than one instance of monomers with aliasHELM property
* [3045](https://github.com/epam/Indigo/issues/3045) Adding substituents to reactants breaks chemical property calculations
* [3061](https://github.com/epam/Indigo/issues/3061), [3062](https://github.com/epam/Indigo/issues/3062) System can't recognize single rebose or phosphate if loaded from HELM
* [3069](https://github.com/epam/Indigo/issues/3069) Export to RXN doesn't work, system throws exception: Error: memory access out of bounds
* [3094](https://github.com/epam/Indigo/issues/3094) Export of expanded CHEMs works wrong (system losts CHEM type)


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.33.0-rc.1...indigo-1.34.0