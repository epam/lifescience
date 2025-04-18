
# Ketcher 3.2.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
- [#6215](https://github.com/epam/ketcher/issues/6215) – Introducing the snap to angle and standard bond length for monomers connected via bonds
- [#6252](https://github.com/epam/ketcher/issues/6252) – Allow creation of antisense chains in sequence mode
- [#6383](https://github.com/epam/ketcher/issues/6383) – Introduce the creation of DNA antisense chains
- [#6355](https://github.com/epam/ketcher/issues/6355) – Change attachment points of backbone monomers in automatically created antisense chains
- [#6254](https://github.com/epam/ketcher/issues/6254) – Update the representation of sense and antisense chains in sequence mode (2/2)
- [#6284](https://github.com/epam/ketcher/issues/6284) – Long bonds for uneven double stranded sequences in snake and flex modes
- [#6527](https://github.com/epam/ketcher/issues/6527) – Add ability to pass coordinates to Ketcher addFragment and setMolecule API to position provided structure
- [#6357](https://github.com/epam/ketcher/issues/6357) – Allow insertion of phosphates (p) from the keyboard in sequence mode
- [#6596](https://github.com/epam/ketcher/issues/6596) – Update Indigo to 1.30.0 in browser module

### Bugfixes and improvements
- [#6219](https://github.com/epam/ketcher/issues/6219) – Unable to save to HELM hydrogen connection between micromolecule (with AP) and monomer
- [#6005](https://github.com/epam/ketcher/issues/6005) – Move the dot indicating a modified phosphate in sequence mode
- [#4145](https://github.com/epam/ketcher/issues/4145) – Implement popup versions of Ketcher (and routing)
- [#5700](https://github.com/epam/ketcher/issues/5700) – System allow to establish infinit number of bonds from monomer to microstructure
- [#6534](https://github.com/epam/ketcher/issues/6534) – Adding nucleotide to the last position having phosphate in antisense causes exception: ReferenceError: process is not defined
- [#6402](https://github.com/epam/ketcher/issues/6402) – Hydrogen bonds misaligned due to antisense strand direction change when opening or pasting a structure in Macro Mode
- [#6464](https://github.com/epam/ketcher/issues/6464) – Splitting chain with Enter key doesn't work
- [#6425](https://github.com/epam/ketcher/issues/6425) – Hiding of number indicators while in sync editing mode when the triangle overlaps with the number
- [#6535](https://github.com/epam/ketcher/issues/6535) – Unable to add nucleoside to the end of sequence if hanging antisense monomer present
- [#6561](https://github.com/epam/ketcher/issues/6561) – Switching to macromolecules changes CSS in the page
- [#6369](https://github.com/epam/ketcher/issues/6369) – System doesn't switch Library tab to proper one if user changes typing type using keboard shortcuts
- [#6627](https://github.com/epam/ketcher/issues/6627) – Fix invisible snapping drawings after switching to micro mode
- [#6621](https://github.com/epam/ketcher/issues/6621) – Fix monomer snapping wiping monomer labels
- [#6608](https://github.com/epam/ketcher/issues/6608) – API setMolecule moves molecule off-canvas on second call
- [#6607](https://github.com/epam/ketcher/issues/6607) – README missing coordinate units for setMolecule and addFragment API methods
- [#6539](https://github.com/epam/ketcher/issues/6539) – System should add same thing in antisense chain but not connect it with H-bond if it is not nucleotide/nucleoside
- [#6624](https://github.com/epam/ketcher/issues/6624) – Enter key in single-strand edit mode incorrectly breaks both chains instead of only one
- [#6632](https://github.com/epam/ketcher/issues/6632) – New sequence appears gray after clearing the canvas in non-sync mode
- [#6631](https://github.com/epam/ketcher/issues/6631) – Sync mode causes incorrect letter input after adding a monomer in non-sync mode
- [#6606](https://github.com/epam/ketcher/issues/6606) – Adding nucleotide to the last position having phosphate in antisense works wrong
- [#6531](https://github.com/epam/ketcher/issues/6531) – System can't add nucleotide between phosphate and nucleotide in antisence chain
- [#6617](https://github.com/epam/ketcher/issues/6617) – Empty element appears after undoing line deletion in Sequence mode and switching to Flex/Snake mode
- [#6609](https://github.com/epam/ketcher/issues/6609) – System creates ambiguous RNA nucleotides instead of DNA ones in case of DNA antisense stand creation
- [#6615](https://github.com/epam/ketcher/issues/6615) – Missing warning message when deleting all hydrogen bonds between two chains
- [#6619](https://github.com/epam/ketcher/issues/6619) – System doesn't create antisense phosphate if it sistuated to the left from nubleotide
- [#6623](https://github.com/epam/ketcher/issues/6623) – Sense and antisense chains switch places during editing based on monomer count
- [#6443](https://github.com/epam/ketcher/issues/6443) – System allow to select single antisense symbol that causes an error if it got deleted
- [#4002](https://github.com/epam/ketcher/issues/4002) – getSmiles and getSmarts on query feature containing aromatic ring raises an error
- [#6709](https://github.com/epam/ketcher/issues/6709) – Unable to paste HELM from clipboard to the canvas. System throws an error: Convert error! option manager: Property "sequence-type" not defined
- [#6723](https://github.com/epam/ketcher/issues/6723) – Forbid moving sequence nodes and snapping by select rectangle tool
- [#6729](https://github.com/epam/ketcher/issues/6729) – Create RNA/DNA Strand doesn't work for B, K, Y and S ambiguous bases
- [#6750](https://github.com/epam/ketcher/issues/6750) – Incorrect R1 attachment atom for natural Ribose (R) in the library
- [#6759](https://github.com/epam/ketcher/issues/6759) – Add pruning of the remaining transient views on clear canvas button click
- [#6795](https://github.com/epam/ketcher/issues/6795) – Incorrect properties of some monomers in the library
- [#6829](https://github.com/epam/ketcher/issues/6829) – Add monomers to the library
- [#6786](https://github.com/epam/ketcher/issues/6786) – Add monomers from HELM Core Library to Ketcher Library

---

### Additional notes:
- Ketcher 3.2.0 has been built and tested with Indigo version 1.30 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.30.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.30.0/images/sha256-ec74234c98bbecdab2134efcd04248efa8e69f398991ba29f33c51327c815433)).

