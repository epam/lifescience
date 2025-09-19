
# Ketcher 3.5.0

## What's Changed

### New features
- [#6738](https://github.com/epam/ketcher/issues/6738) – Ability to change the number of monomers in a line
- [#5208](https://github.com/epam/ketcher/issues/5208) – Allow modifying amino acids on canvas
- [#6995](https://github.com/epam/ketcher/issues/6995) – Smart positioning of CIP stereo labels for atoms
- [#6852](https://github.com/epam/ketcher/issues/6852) – Improve the hydrophobicity graph in the "Calculate Properties" window
- [#6589](https://github.com/epam/ketcher/issues/6589) – API lacks support for 3 letter code sequence export in macro mode
- [#7070](https://github.com/epam/ketcher/issues/7070) – Include the removed versions of some 3D templates in the templates library in addition to the corrected ones
- [#7224](https://github.com/epam/ketcher/issues/7224) – Migrate to Indigo v1.33.0 in-browser module

### Bugfixes and improvements
- [#7094](https://github.com/epam/ketcher/issues/7094) – Update the help document (3.4.)
- [#6294](https://github.com/epam/ketcher/issues/6294) – Hiding toolbar buttons doesn't also hide disable the corresponding keyboard shortcut
- [#6930](https://github.com/epam/ketcher/issues/6930) – Replace File comparison (for MOL files ONLY!) operations with valid helper function - verifyFileExport
- [#7032](https://github.com/epam/ketcher/issues/7032) – Ketcher allows to make changes in sequence while being in nucleotide modification mode
- [#5971](https://github.com/epam/ketcher/issues/5971) – Inconsistent selection sensitivity when highlighting sequences
- [#7023](https://github.com/epam/ketcher/issues/7023) – Hydrophobicity section is missing tooltip icon and description
- [#6834](https://github.com/epam/ketcher/issues/6834) – Clicking on base card in RNA Builder does not scroll to selected base if multiple bases from the same section are selected
- [#7031](https://github.com/epam/ketcher/issues/7031) – Layout shift when entering symbol in sequence mode upon first macromolecules mode initialization
- [#6958](https://github.com/epam/ketcher/issues/6958) – Monomers positions are not preserved when pasting macromolecule in MOL format
- [#7200](https://github.com/epam/ketcher/issues/7200) – App crashes after modifying amino acids and switching to Micro mode
- [#7203](https://github.com/epam/ketcher/issues/7203) – N-methylation is shown as available for Hyp even though it shouldn't be
- [#7142](https://github.com/epam/ketcher/issues/7142) – Monomer selection without bonds should work the same as with bonds
- [#7251](https://github.com/epam/ketcher/issues/7251) – Incorrect tooltips for properties and logic for the hydrophobicity graph in the "Calculate properties" window
- [#7130](https://github.com/epam/ketcher/issues/7130) – Incorrect calculation when part of a microstructure is selected - full structure is sent to Indigo
- [#7150](https://github.com/epam/ketcher/issues/7150) – Molecule mass should be calculated for partial selected micromolecule (ketcher part)
- [#7202](https://github.com/epam/ketcher/issues/7202) – Incorrect order of amino acid modification options in context menu
- [#7281](https://github.com/epam/ketcher/issues/7281) – App crashes when closing Ketcher
- [#6985](https://github.com/epam/ketcher/issues/6985) – Structure appears on incorrect canvas in molecules mode for several ketcher instances on same page
- [#7288](https://github.com/epam/ketcher/issues/7288) – Monomers shifts out of visible area when adjusting layout with ruler in sequence edit mode
- [#7318](https://github.com/epam/ketcher/issues/7318) – Bonds are overlapped by CIP labels when moving the structure or when the structure has small bond angles

---

### Additional notes:
- Ketcher 3.5.0 has been built and tested with Indigo version 1.33 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.33.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.33.0/images/sha256-e6c8cb1bbede651471b905c927dd1743819ef3025f7c86db13c4aa7db560dc36)).
