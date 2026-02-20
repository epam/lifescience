# Indigo 1.38.0
Released 2026-02-20

## Features
* [3227](https://github.com/epam/Indigo/issues/3227) Introducing Copolymer S-group type
* [3272](https://github.com/epam/Indigo/issues/3272) SDF files for library/monomer information
* [3196](https://github.com/epam/Indigo/issues/3196) Support formation of circular structures in flex mode - PoC

## Bugfixes and improvements
* [3239](https://github.com/epam/Indigo/issues/3239) System doesn't save monomer expand/collapse state in Mol v3000 for user created monomers (they always come in collapsed state)
* [3261](https://github.com/epam/Indigo/issues/3261) indigoSaveCdxml doesn't support reaction molecules
* [3269](https://github.com/epam/Indigo/issues/3269) System ignored HELM alias for bases on monomer load to Library
* [3256](https://github.com/epam/Indigo/issues/3256) Metals loaded from cdxml are always represented with hydrogens
* [3237](https://github.com/epam/Indigo/issues/3237) Stackoverflow iterate components
* [3277](https://github.com/epam/Indigo/issues/3277) System adds broken Preset to the library (part2)
* [3278](https://github.com/epam/Indigo/issues/3278) System doesn't allow to add monomers with the same structure but different names (part2)
* [3286](https://github.com/epam/Indigo/issues/3286) CHEMBUGS-64 Automapping fails to guard against contradictory reaction center annotation, corrupts future structure export data
* [3297](https://github.com/epam/Indigo/issues/3297) Random '$$$$V2.0' empty return from conversion to HELM
* [3293](https://github.com/epam/Indigo/issues/3293) Library update works wrong if we use empty SDF file
* [3292](https://github.com/epam/Indigo/issues/3292) Save to SDF v2000 works wrong for created monomers
* [3291](https://github.com/epam/Indigo/issues/3291) Layout works wrong 
* [3267](https://github.com/epam/Indigo/issues/3267) Export to sugar monomer to AxoLabs error message is wrong
* [3265](https://github.com/epam/Indigo/issues/3265) System should be able to load unknown monomer on any position
* [3338](https://github.com/epam/Indigo/issues/3338) System losts stereo bonds on monomer load to Library
* [3247](https://github.com/epam/Indigo/issues/3247) SVG/PNG: Export of any atom with Isotope (atomic mass) value set doesn't work


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.37.0-rc.1...indigo-1.38.0