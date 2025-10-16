# Indigo 1.36.0
Released 2025-10-16

## Features
* [905](https://github.com/epam/Indigo/issues/905) Support for pagination in Bingo Elastic
* [3092](https://github.com/epam/Indigo/issues/3092) Avoid overwriting cmake output directories variables
* [3099](https://github.com/epam/Indigo/issues/3099) Support dev container
* [2893](https://github.com/epam/Indigo/issues/2893) Reaction data support in KET-format 
* [3136](https://github.com/epam/Indigo/issues/3136) No attachment points check should be performed for terminal CHEMs on IDT import/export
* [3135](https://github.com/epam/Indigo/issues/3135) Mark undefined stereocenters using the standardize function
* [3085](https://github.com/epam/Indigo/issues/3085) HELM annotations support

## Bugfixes and improvements
* [3065](https://github.com/epam/Indigo/issues/3065) Indigo build fails when trying to build indigo-depict
* [3060](https://github.com/epam/Indigo/issues/3060) CH labels are recognised as pseudo-atoms when parsing cdxml
* [3096](https://github.com/epam/Indigo/issues/3096) Expand monomer works wrong with selection
* [3105](https://github.com/epam/Indigo/issues/3105) bingo-elastic-python filter broken for exact/substructure
* [3130](https://github.com/epam/Indigo/issues/3130) Bingo-postrgress-fingerprints tests are failing
* [3071](https://github.com/epam/Indigo/issues/3071) Export to RDF V2000 doesn't work if "star" atom on the canvas. System throws exception: Convert error! std::bad_cast
* [3067](https://github.com/epam/Indigo/issues/3067) System can't load HELM with inline SMILES if it has r-site star atom without square brackets
* [3120](https://github.com/epam/Indigo/issues/3120) bingo-elastic-python reaction exact search do not use postprocess actions
* [3150](https://github.com/epam/Indigo/issues/3150) Exception during molecules loading in test fixture
* [3123](https://github.com/epam/Indigo/issues/3123) Unable to paste FASTA content from clipcoard
* [3159](https://github.com/epam/Indigo/issues/3159) Export to HELM works wrong for custom monomers imported from HELM with inline SMILES
* [3068](https://github.com/epam/Indigo/issues/3068), [3080](https://github.com/epam/Indigo/issues/3080), [3082](https://github.com/epam/Indigo/issues/3082), [3086](https://github.com/epam/Indigo/issues/3086), [3087](https://github.com/epam/Indigo/issues/3087), [3088](https://github.com/epam/Indigo/issues/3088), [3090](https://github.com/epam/Indigo/issues/3090), [3084](https://github.com/epam/Indigo/issues/3084) System can't load atom properties (Charge, Isotope and Valence) in SMARTS with "star" atom. System throws exception. 
* [3144](https://github.com/epam/Indigo/issues/3144), [3147](https://github.com/epam/Indigo/issues/3147) Export to IDT baseless preset and modified phosphate
* [3148](https://github.com/epam/Indigo/issues/3148) Export to IDT shouldn't work if monomer at the end has no 3' position IDT code
* [3169](https://github.com/epam/Indigo/issues/3169) Export to IDT doesn't work if R1-only CHEM stays on five prime position


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.35.0-rc.1...indigo-1.36.0