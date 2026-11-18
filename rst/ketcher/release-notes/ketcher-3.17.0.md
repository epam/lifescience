
# Ketcher 3.17.0

## What's Changed

### New features
- [#8855](https://github.com/epam/ketcher/issues/8855) – Add preset-specific error messages in monomer creation wizard
- [#8922](https://github.com/epam/ketcher/issues/8922) – Add Edit Instance prefill for monomer creation wizard
- [#9456](https://github.com/epam/ketcher/issues/9456) – Add BILN format and monomer alias support
- [#6784](https://github.com/epam/ketcher/issues/6784) – Home and End keys support in Sequence mode

### Bugfixes and improvements
- [#8779](https://github.com/epam/ketcher/issues/8779) – Allow moving selected S-groups and monomers in molecules mode
- [#9779](https://github.com/epam/ketcher/issues/9779) – Add an additional amino acid (E*) and assign it and D* a new modification type
- [#9757](https://github.com/epam/ketcher/issues/9757) – App crashes while editing sequence containing particular ambiguous monomers
- [#7726](https://github.com/epam/ketcher/issues/7726) – Bond thickness is less than others on monomer preview
- [#8006](https://github.com/epam/ketcher/issues/8006) – LGAs label numerals are not subscripted
- [#9820](https://github.com/epam/ketcher/issues/9820) – Adding bond to atom could ended with wrong bond angle if user slightly moved mouse during click
- [#9692](https://github.com/epam/ketcher/issues/9692) – RNA Builder: Impossible to specify the phosphate position before any preset components are added
- [#9990](https://github.com/epam/ketcher/issues/9990) – Undo has no effect on bond type changes
- [#9738](https://github.com/epam/ketcher/issues/9738) – Swap stereo labels and stereo atoms when bond is flipped
- [#8251](https://github.com/epam/ketcher/issues/8251) – Monomer should be selected on the canvas after creation
- [#9489](https://github.com/epam/ketcher/issues/9489) – Nucleotide presets: Creating preset with the same component codes replaces properties of the existing preset
- [#7546](https://github.com/epam/ketcher/issues/7546) – Canvas does not reset scroll position after using “Clear canvas” - added monomers appear offset
- [#9751](https://github.com/epam/ketcher/issues/9751) – RNA Builder: Missing "Switch to right/left" tooltips when hovering over the phosphate position picker options
- [#9731](https://github.com/epam/ketcher/issues/9731) – Rotation tool: Rotation center of partially selected structure changes color when hovering over
- [#9383](https://github.com/epam/ketcher/issues/9383) – Rotation tool: After moving the rotation center the rotation handle is not set to the starting position and rotation circle does not cross the dashed line
- [#8181](https://github.com/epam/ketcher/issues/8181) – It is possible to define preset (group) name more than 200 symbols
- [#6273](https://github.com/epam/ketcher/issues/6273) – Thick foreground bonds do not work if the atoms are not carbons
- [#9837](https://github.com/epam/ketcher/issues/9837) – Correct the warning message for unusual base leaving group
- [#8199](https://github.com/epam/ketcher/issues/8199) – System allow to upload monomer that has IDT alises that is longer than allowed (it shouldn't!)
- [#4309](https://github.com/epam/ketcher/issues/4309) – Delete and Backspace hotkeys deletes elements under mouse cursor (hover), but not selected ones
- [#8198](https://github.com/epam/ketcher/issues/8198) – It is possible to add monomer with HELM alias is too long
- [#5849](https://github.com/epam/ketcher/issues/5849) – Expanded monomer inconsistent behaviour
- [#8600](https://github.com/epam/ketcher/issues/8600) – Single Up bond between two monomers painted wrong
- [#4093](https://github.com/epam/ketcher/issues/4093) – Keep loading indicator visible until paste completes
- [#9349](https://github.com/epam/ketcher/issues/9349) – Stereo group labels are overlapped
- [#5468](https://github.com/epam/ketcher/issues/5468) – Multi-Tailed Arrow can't be selected if Structure Selection Tool is used and clicking on tails or head
- [#8778](https://github.com/epam/ketcher/issues/8778) – Only show the possible monomer properties in the attributes panel in the monomer creation wizard
- [#8173](https://github.com/epam/ketcher/issues/8173) – IDT alias could be longer than 10 symbols without slashes
- [#10134](https://github.com/epam/ketcher/issues/10134) – Update the help document (3.16.)
- [#9991](https://github.com/epam/ketcher/issues/9991) – Remove "Highlight" checkbox from monomer creation wizard
- [#10054](https://github.com/epam/ketcher/issues/10054) – Nucleotide preset: R-group labels disappear when switching component tabs
- [#9299](https://github.com/epam/ketcher/issues/9299) – Fixes on new lexical library
- [#10102](https://github.com/epam/ketcher/issues/10102) – Type combobox is empty if S-Group Properties` dialog opened for Copolymer s-group for edit
- [#7940](https://github.com/epam/ketcher/issues/7940) – Export to HELM of monomer with attached micromolecule should cause warning message: The molecule will be exported using inline SMILES, and on load will appear as a CHEM monomer
- [#10260](https://github.com/epam/ketcher/issues/10260) – Warning message for unusual base leaving group incorrectly refers to "hydroxyl" instead of "hydrogen"
- [#10146](https://github.com/epam/ketcher/issues/10146) – Migrate to Indigo v1.45.0 in-browser module

---

### Additional notes:
- Ketcher 3.17.0 has been built and tested with Indigo version 1.45 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.45.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.45.0/images/sha256-076c00b594da13e5390b5d72f645d27edb53f39aabed43d3273ed501098d6152)).
