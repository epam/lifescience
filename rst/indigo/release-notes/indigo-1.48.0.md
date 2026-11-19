# Indigo 1.48.0
Released 2026-11-18

## New features
* #3685 - Support BILN aliases as a monomer property in the library
* #3837 - Provide a support for Haptic Bond: Introduce models and data structures according to a contract.
* #3838 - introduce to ket format haptic bond support
* #3840 - haptic bonds in mol v3000
* #3841 - Introduce support to correctly render haptic bonds within PNG/SVG

## Bugfixes and improvements
* #108 - Fix Bingo PostgreSQL index corruption during concurrent writes and crash recovery
* #317 - making a fix for smiles to support stereochemistry information
* #3635 - Monomer recognition fails when loading a molecule with aromatic bonds from a 'mol v3000' file using a monomer library
* #3776 - Export to HELM method throws allowRGroupOnRSite error
* #3803 - Enhanced stereochemistry is deleted when creating S-groups
* #3834 - expandedMonomersToAtoms throw IndigoException
* #3847 - Monomers in generated HELM strings are disconnected
* #3854 - addCIPStereoDescriptors throws exception "array: invalid index N (size=M)"


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.47.0-rc.1...indigo-1.48.0