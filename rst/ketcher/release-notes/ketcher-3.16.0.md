
# Ketcher 3.16.0

## What's Changed

### New features
- [#8996](https://github.com/epam/ketcher/issues/8996) – Show attachment points in the attributes panel when defining presets
- [#9310](https://github.com/epam/ketcher/issues/9310) – Library and autochain support for presets with 5' phosphates

### Bugfixes and improvements
- [#6603](https://github.com/epam/ketcher/issues/6603) – Replace AJV with jsonschema in runtime to allow Ketcher work in CSP-strict environment
- [#6094](https://github.com/epam/ketcher/issues/6094) – It is possible to create antisense even if it is not allowed (when base has extra bond out of r1-r3 to sugar)
- [#8977](https://github.com/epam/ketcher/issues/8977) – No focus inside modal confirmation of type changing in monomer creation wizard
- [#6093](https://github.com/epam/ketcher/issues/6093) – Phosphate in antisense chain converted wrong
- [#7781](https://github.com/epam/ketcher/issues/7781) – Inconsistency in fragment selection hover behavior between Micro and Macro modes
- [#7204](https://github.com/epam/ketcher/issues/7204) – Long names and short names of 3D Templates in the Structure Library are swapped and short names are missed
- [#7278](https://github.com/epam/ketcher/issues/7278) – N-methylation option is missing even if monomer in selection is eligible for it
- [#5110](https://github.com/epam/ketcher/issues/5110) – Aromatize the molecules after drawing
- [#7083](https://github.com/epam/ketcher/issues/7083) – Delete operation on Sequence mode causes hanging bonds and undeletable monomers
- [#5480](https://github.com/epam/ketcher/issues/5480) – Ambiguous monomer tooltip covered
- [#5934](https://github.com/epam/ketcher/issues/5934) – Error message is wrong if user tries to establish hydrogen bond if it is already has single one
- [#5740](https://github.com/epam/ketcher/issues/5740) – Establishing connection between ambiguous phosphate and sugar works wrong
- [#6090](https://github.com/epam/ketcher/issues/6090) – Antisense creating doesn't work if ambiguous phosphate present in the chain selection
- [#4247](https://github.com/epam/ketcher/issues/4247) – When pressing the “Open from file” button, the full-screen mode closes
- [#9291](https://github.com/epam/ketcher/issues/9291) – Slow build problem (part 2): reduce circular imports with static-import rollback, mode initialization fixes, and lockfile reset
- [#9139](https://github.com/epam/ketcher/issues/9139) – Incorrect structure while press UNDO aftrer Create Monomer action on the Molecules Mode
- [#9730](https://github.com/epam/ketcher/issues/9730) – Rotation tool: Rotation-angle label overlaps 0° label in Macro mode
- [#8332](https://github.com/epam/ketcher/issues/8332) – cursor flickers between grabbing and pointing hand while dragging a monomer across the cards
- [#5543](https://github.com/epam/ketcher/issues/5543) – Styles from macromolecules mode break global styles
- [#9559](https://github.com/epam/ketcher/issues/9559) – S-Group: Subtype drop-down menu for Copolymer contains an extra option
- [#3951](https://github.com/epam/ketcher/issues/3951) – Aromatizing causes NULL in export to MDL Molfile V2000 format file
- [#9709](https://github.com/epam/ketcher/issues/9709) – It is not correct to have 5' indicator on an antisense chain.
- [#6314](https://github.com/epam/ketcher/issues/6314) – Export to Sequence (3-letter code) and export to IDT doesn't throws an error if user tries to save micromolecule structures
- [#8715](https://github.com/epam/ketcher/issues/8715) – File format dropdown height should be equal to File name edit box
- [#6091](https://github.com/epam/ketcher/issues/6091) – Antisense creating doesn't work if ambiguous sugar present in the chain selection
- [#6053](https://github.com/epam/ketcher/issues/6053) – D peptide with asterik is marked as modified
- [#9458](https://github.com/epam/ketcher/issues/9458) – Add validation for monomer name to ensure valid characters are used
- [#7745](https://github.com/epam/ketcher/issues/7745) – Preview tooltip doesn't appear on the canvas if monomer name too long
- [#6907](https://github.com/epam/ketcher/issues/6907) – Memory leaks for ketcher when it is opened inside modal
- [#8389](https://github.com/epam/ketcher/issues/8389) – Hanging bonds after sequence edit operation
- [#7574](https://github.com/epam/ketcher/issues/7574) – IDT code is missing from preview tooltip on sequence canvas
- [#7514](https://github.com/epam/ketcher/issues/7514) – IDT codes list is wrong for all presets
- [#7827](https://github.com/epam/ketcher/issues/7827) – Some bond types shouldn't be allowed in Create monomer wizard
- [#6234](https://github.com/epam/ketcher/issues/6234) – Thick foreground bond looks wrong on Macro canvas
- [#9817](https://github.com/epam/ketcher/issues/9817) – Double call of context menu for symbol on sequence canvas causes different menu to appear
- [#9622](https://github.com/epam/ketcher/issues/9622) – Update the help document (3.15.)
- [#9138](https://github.com/epam/ketcher/issues/9138) – Update the appearance of the monomer creation wizard
- [#9491](https://github.com/epam/ketcher/issues/9491) – Monomer Creation Wizard: Creating a Nucleotide (preset) allows empty mandatory field natural analogue
- [#8203](https://github.com/epam/ketcher/issues/8203) – System allow to define position IDT aliases with slashes inside
- [#8958](https://github.com/epam/ketcher/issues/8958) – Bond element stays after clear canvas is clicked in Macromolecules canvas
- [#8637](https://github.com/epam/ketcher/issues/8637) – Molecule structure chages made in monomer creation wizard doesn't appear at molecules canvas after monomer creation
- [#9887](https://github.com/epam/ketcher/issues/9887) – Copy paste does not work in Safari
- [#10123](https://github.com/epam/ketcher/issues/10123) – Migrate to Indigo v1.44.0 in-browser module

---

### Additional notes:
- Ketcher 3.16.0 has been built and tested with Indigo version 1.44 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.44.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.44.0/images/sha256-fb73144c4d21904e612d13829eae96745a60b8d990e59bbf9a1923a4ed05768d)).
