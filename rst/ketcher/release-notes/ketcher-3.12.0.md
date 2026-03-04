
# Ketcher 3.12.0

## What's Changed

### New features
- [#8777](https://github.com/epam/ketcher/issues/8777) – Change the logic for activation of 'Arrange as a Ring' tool and context menu item
- [#8781](https://github.com/epam/ketcher/issues/8781) – Change the logic for attachment points editing drop-down in the monomer creation wizard
- [#8857](https://github.com/epam/ketcher/issues/8857) – Monomer saving - presets in the monomer creation wizard
- [#8856](https://github.com/epam/ketcher/issues/8856) – Defining other monomer properties - presets in the monomer creation wizard
- [#8866](https://github.com/epam/ketcher/issues/8866) – Defining the preset - presets in the monomer creation wizard
- [#8851](https://github.com/epam/ketcher/issues/8851) – Highlighting presets in the monomer creation wizard
- [#8854](https://github.com/epam/ketcher/issues/8854) – Defining the preset - presets in the monomer creation wizard
- [#8849](https://github.com/epam/ketcher/issues/8849) – Entering the wizard - presets in the monomer creation wizard
- [#8852](https://github.com/epam/ketcher/issues/8852) – Additions to the structure - presets in the monomer creation wizard
- [#8850](https://github.com/epam/ketcher/issues/8850) – Add "Mark as a..." context menu option for Nucleotide (preset) in monomer creation wizard
- [#8008](https://github.com/epam/ketcher/issues/8008) – Implementation of Copolymer S-Group type

### Bugfixes and improvements
- [#8437](https://github.com/epam/ketcher/issues/8437) – If no selection made, system doesn't define attachment points for monomer
- [#5701](https://github.com/epam/ketcher/issues/5701) – It is possible to connect all APs to same atom
- [#8800](https://github.com/epam/ketcher/issues/8800) – The hover on a selected atom differs in micro mode and in macro mode
- [#7797](https://github.com/epam/ketcher/issues/7797) – Underline colour for the base counter in the Calculate Properties window doesn't fit the requirement
- [#7789](https://github.com/epam/ketcher/issues/7789) – Fragment selection highlighting inconsistent between Micro and Macro modes
- [#7325](https://github.com/epam/ketcher/issues/7325) – Right-click copy option does not work for microstructures on macro canvas
- [#8837](https://github.com/epam/ketcher/issues/8837) – No bad valence indication on Macromolecules canvas
- [#8792](https://github.com/epam/ketcher/issues/8792) – Rename monomer symbol to monomer code in the monomer creation wizard.
- [#8898](https://github.com/epam/ketcher/issues/8898) – Selection ignored in Ketcher API calls
- [#7128](https://github.com/epam/ketcher/issues/7128) – Molecular formula letters are not on the same level
- [#8641](https://github.com/epam/ketcher/issues/8641) – Tooltip in popup Ketcher sequence mode appears beyond view area for sequences at the top
- [#4724](https://github.com/epam/ketcher/issues/4724) – After clicking the "Clear Canvas" button multiple times, a user has to click the "Undo" button multiple times to return the structure
- [#6071](https://github.com/epam/ketcher/issues/6071) – Change event does not trigger after switching to Micro mode
- [#6236](https://github.com/epam/ketcher/issues/6236) – Cycled aromatic bond looks wrong on Macro canvas
- [#7123](https://github.com/epam/ketcher/issues/7123) – Deleting one of multiple monomers does not trigger recalculation in Calculate Properties window
- [#5170](https://github.com/epam/ketcher/issues/5170) – Fixed "Process is not defined" error is displayed in console after Clearing Canvas in Macro Mode with the element with an attachment point and switching to Micro
- [#5125](https://github.com/epam/ketcher/issues/5125) – Fixed after copying and pasting, structure under cursor causes Uncaught TypeErrors in DevTool console when approaching the edges of canvas
- [#8205](https://github.com/epam/ketcher/issues/8205) – System shouldn't allow to upload monomers with no base IDT alias defined
- [#5656](https://github.com/epam/ketcher/issues/5656) – Bond properties are not implemented
- [#8954](https://github.com/epam/ketcher/issues/8954) – Undo/redo operations doesn't work for atoms, arrows and pluses after changing their positions in Macro mode
- [#7188](https://github.com/epam/ketcher/issues/7188) [#7190](https://github.com/epam/ketcher/issues/7190) [#7255](https://github.com/epam/ketcher/issues/7255) – Unknown peptide, sugar, unknown base and unknown phosphate looks like chems (in addition ketcher wrongly considers R3-R1 connection between unknown sugar and/or unknown base as side chain connection)
- [#9047](https://github.com/epam/ketcher/issues/9047) – Leaving group atom position is incorrect for nucleotides created in monomer wizard
- [#9032](https://github.com/epam/ketcher/issues/9032) – Flex mode icon is active after ketcher close and open again
- [#8965](https://github.com/epam/ketcher/issues/8965) – Migrate to Indigo v1.40.0 in-browser module
- [#8918](https://github.com/epam/ketcher/issues/8918) – Update the help document (3.11.)

---

### Additional notes:
- Ketcher 3.12.0 has been built and tested with Indigo version 1.40 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.40.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.40.0/images/sha256-865dd73f1ee9c49bcde04f6529ec6f16a3943a7985aa31df691378a27cb98056)).
