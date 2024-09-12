
# Ketcher 2.23.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#4852](https://github.com/epam/ketcher/issues/4852) – UX support for HELM import/export
* [#4846](https://github.com/epam/ketcher/issues/4846) – Make Sequence view default in Macromolecules mode
* [#4431](https://github.com/epam/ketcher/issues/4431) – Implement support of unresolved IDT monomers
* [#4382](https://github.com/epam/ketcher/issues/4382) – Implement support of unsplit nucleotides
* [#3532](https://github.com/epam/ketcher/issues/3532) – Displaying side chain connections in snake-like mode
* [#4856](https://github.com/epam/ketcher/issues/4856) – Add new CHEM monomers to the library
* [#2654](https://github.com/epam/ketcher/issues/2654) – Improve WASM loading performance
* [#5083](https://github.com/epam/ketcher/issues/5083) – Update indigo to 1.22.0 in browser module

### Bugfixes and improvements
* [#4660](https://github.com/epam/ketcher/issues/4660) – Zero charge shows explicit 0 instead of blank after using A+/A- Tools
* [#4801](https://github.com/epam/ketcher/issues/4801) – Cut operation for attachment points makes canvas inaccessible/unoperational and delete entire molecule
* [#4636](https://github.com/epam/ketcher/issues/4636) – In the Sequence mode, when selecting elements on the canvas, the total number of elements is not displayed in the Right-click menu
* [#4686](https://github.com/epam/ketcher/issues/4686) – After moving the structure in the Macro mode, in the Micro mode the S-group value is displayed separately from the structure
* [#4823](https://github.com/epam/ketcher/issues/4823) – In sequence mode, each press adds two characters and when deleted, also removes two
* [#4793](https://github.com/epam/ketcher/issues/4793) – Context menu for attachment point labels should contain only Delete option
* [#4784](https://github.com/epam/ketcher/issues/4784) – Attachment point enumeration logic works wrong
* [#4786](https://github.com/epam/ketcher/issues/4786) – Keyboard shortcut stops working after adding/removing attachment point
* [#4607](https://github.com/epam/ketcher/issues/4607) – Inconsistent display of a separate phosphate in the sequence representation in the Sequence mode
* [#4782](https://github.com/epam/ketcher/issues/4782) – It is possible to attach bond to attachment point label
* [#4791](https://github.com/epam/ketcher/issues/4791) – System saves selection states of attachment point labels to KET file (it should not)
* [#4837](https://github.com/epam/ketcher/issues/4837) – Library filter does not reset when switching between Micro and Macro mode
* [#4833](https://github.com/epam/ketcher/issues/4833) – Support rendering multiple Ketcher editors on a page without an iframe
* [#4773](https://github.com/epam/ketcher/issues/4773) – It is impossible to apply R-group to atom with attachment point attached
* [#4927](https://github.com/epam/ketcher/issues/4927) – Able to change attachment point label to an atom if it is selected first
* [#4925](https://github.com/epam/ketcher/issues/4925) – Unable to change atom to another if molecule has attachment point
* [#4929](https://github.com/epam/ketcher/issues/4929) – System allow to change atoms inside S-group without removing abbreviation
* [#4930](https://github.com/epam/ketcher/issues/4930) – Fix missing IDT aliases and label positioning for unsplit nucleotides
* [#4889](https://github.com/epam/ketcher/issues/4889) – After using "Clear Canvas" in the Sequence mode and entering new sequence, extra structures are shown in Flex and Snake modes
* [#4924](https://github.com/epam/ketcher/issues/4924) – RNA Preset without Base causes constant crash after switching to Macromolecules mode
* [#4977](https://github.com/epam/ketcher/issues/4977) – System doesn't show side chain bonds if chain loaded directly to Snake-mode canvas
* [#4997](https://github.com/epam/ketcher/issues/4997) – The second of three horizontal bond overlaps backbone connection line
* [#4975](https://github.com/epam/ketcher/issues/4975) – Connection is displayed at the bottom of the row, if drag a horizontal side-chain connection between the extreme nucleotides of a row
* [#5035](https://github.com/epam/ketcher/issues/5035) – Bonds in the snake chain are displayed differently after saving in ket format
* [#5034](https://github.com/epam/ketcher/issues/5034) – When dragging the side chain connections between CHEM, all these connections pass exclusively from the left, and not the shortest path
* [#4881](https://github.com/epam/ketcher/issues/4881) – When switching from Sequence mode to Flex mode, RNA abbreviations remain
* [#4995](https://github.com/epam/ketcher/issues/4995) – The bottom horizontal bonds does not shift if there is an overlap
* [#5074](https://github.com/epam/ketcher/issues/5074) – Switching from Sequence mode to Snake mode and back shifts visible area of canvas beyond visible frame. Forever.
* [#5121](https://github.com/epam/ketcher/issues/5121) – Copy does not work in the Firefox browser
* [#5335](https://github.com/epam/ketcher/issues/5335) - The application crashes when selecting Enhanced Stereochemistry from the right-click menu
