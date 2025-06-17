# Indigo 1.31.0
Released 2025-06-17

## Features
* [2788](https://github.com/epam/Indigo/issues/2788) Support for PNG/SVG export of expanded monomers

## Bugfixes and improvements
* [2150](https://github.com/epam/Indigo/issues/2150) Can't save a schema with some elements from Periodic Table in PNG and SVG format
* [425](https://github.com/epam/Indigo/issues/425) Smiles with attachment points is not read correctly (valences are wrong)
* [2747](https://github.com/epam/Indigo/issues/2747) Incorrect substituent position
* [1680](https://github.com/epam/Indigo/issues/1680) System can't load CDX with (unsupported) brackets inside
* [1631](https://github.com/epam/Indigo/issues/1631) Add/Remove hydrogens changes Radical value from Diradical (triplet) to Diradical (singlet)
* [2755](https://github.com/epam/Indigo/issues/2755) Error occurs on click of "Remove Explicit Hydrogens" in reaction
* [1686](https://github.com/epam/Indigo/issues/1686) System shows positive charge modificator as extra + in addition to charge modified molecule 
* [2810](https://github.com/epam/Indigo/issues/2810) Unnecessary rearrangment of cdxml reaction
* [2807](https://github.com/epam/Indigo/issues/2807) Missing label from cdxml
* [2801](https://github.com/epam/Indigo/issues/2801) Can't render reactions which contain brackets
* [2778](https://github.com/epam/Indigo/issues/2778) Can't render fragments with multiple external connections
* [2815](https://github.com/epam/Indigo/issues/2815) CIP labels are not rendered
* [2591](https://github.com/epam/Indigo/issues/2591) Reagents are repositioned above the reaction arrow after saving and loading RXN V2000/V3000 files
* [2832](https://github.com/epam/Indigo/issues/2832) Load from clipboard ignores RNA/DNA/PEP switcher and always loads DNA ambiguous bases even if RNA mode switched on
* [2845](https://github.com/epam/Indigo/issues/2845) Export to PNG/SVG works wrong for labels
* [2722](https://github.com/epam/Indigo/issues/2722) Monomer could be saved to RDF V3000 format but can't be loaded back - exception

**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.30.0-rc.1...indigo-1.31.0