
# Ketcher 3.0.0

## What's Changed
🎉  We’re excited to introduce Ketcher 3.0, featuring the newly available Macromolecules mode!

This mode enables users to work with monomers and RNA presets, combine them into polymer chains, create antisense chains, import/export of different formats (HELM, SCSR/MOL V3000, Sequence, FASTA, IDT, Ket). More information provided in [User manual for Macromolecules mode](https://github.com/epam/ketcher?tab=readme-ov-file#macromolecules-mode)

Along with this major enhancement, we've included various improvements and bug fixes to enhance performance and usability.

Here are the updated release notes with links to the corresponding issues:

### New features
- [#6034](https://github.com/epam/ketcher/issues/6034) – Make macromolecules switcher enabled by default
- [#6029](https://github.com/epam/ketcher/issues/6029) – Enter flex mode when macromolecules mode was not entered in before and there is a drawing on canvas
- [#6027](https://github.com/epam/ketcher/issues/6027) – Support for single atom properties in macromolecules mode
- [#6028](https://github.com/epam/ketcher/issues/6028) – Support all remaining types of bonds from small molecules mode in macro molecules mode
- [#6227](https://github.com/epam/ketcher/issues/6227) – Update indigo to 1.28.0 in browser module


### Bugfixes and improvements
- [#5978](https://github.com/epam/ketcher/issues/5978) – Entire element bounding box should be clickable, not only black dots
- [#6127](https://github.com/epam/ketcher/issues/6127) – Hover mouse over ambiguous monomer on Micromolecules canvas causes app crash
- [#5476](https://github.com/epam/ketcher/issues/5476) – Copy/Cut and Paste using Ctrl+C/X and Ctrl+V doesn't work for static elements in Mozilla Firefox
- [#5317](https://github.com/epam/ketcher/issues/5317) – Some side chain bonds are not shown in Sequence mode for bases, CHEMs, phosphates and sugars
- [#5796](https://github.com/epam/ketcher/issues/5796) – Indigo functions doesn't work if monomer on micro canvas - system throws an error: Error: Cannot deserialize input JSON.
- [#5032](https://github.com/epam/ketcher/issues/5032) – Selection of monomers should disappear when the user moves the cursor
- [#5139](https://github.com/epam/ketcher/issues/5139) – After pressing the Clear Canvas button in sequence-editing view, the Enter button does not start a new sequence but erases it
- [#5231](https://github.com/epam/ketcher/issues/5231) – Canvas should remain in edit mode if we insert monomer from the library
- [#5795](https://github.com/epam/ketcher/issues/5795) – Undo operation doesn't work for monomer at micro mode if it was deleted - system throws exception in console
- [#6112](https://github.com/epam/ketcher/issues/6112) – System opens "intellisence"-like dropdown control in unnecessary case
- [#5663](https://github.com/epam/ketcher/issues/5663) – Movement of microstructures on Sequence mode doesn't work
- [#4533](https://github.com/epam/ketcher/issues/4533) – After inserting a nucleotide in the Text-editing mode, the cursor blinks in the wrong place
- [#6026](https://github.com/epam/ketcher/issues/6026) – Bond length is different for monomers loaded from HELM and from the library
- [#4723](https://github.com/epam/ketcher/issues/4723) – When pressing Enter, a user can create new sequences in the “Modify RNA Builder” mode
- [#6022](https://github.com/epam/ketcher/issues/6022) – Side chain attachment point shown in wrong place in Snake mode
- [#5341](https://github.com/epam/ketcher/issues/5341) – Replacing all monomers (or part of them) in edit mode - works wrong - system cuts sequence on two
- [#5670](https://github.com/epam/ketcher/issues/5670) – Structural distortion occurs during multi expand and multi collapse of macromolecule abbreviations in micro mode
- [#6021](https://github.com/epam/ketcher/issues/6021) – Connection between molecule and monomer does not affect an amount of implicit hydrogens
- [#5115](https://github.com/epam/ketcher/issues/5115) – Switching from Sequence mode to Flex mode and back shifts visible area of canvas beyond visible frame.
- [#4526](https://github.com/epam/ketcher/issues/4526) – In the Text-editing mode, the canvas is not moved to make the newly added sequence visible
- [#6240](https://github.com/epam/ketcher/issues/6240) – Export to 3-letter sequence doesn't work
- [#6235](https://github.com/epam/ketcher/issues/6235) – Incorrect representation of hydrogens for alias charge valence and radical properties in macro mode
- [#6034](https://github.com/epam/ketcher/issues/6034) – Combine two editors in ketcher-react package in order to make macro switcher enabled by default
- [#6247](https://github.com/epam/ketcher/issues/6247) – Update the help document
- [#3627](https://github.com/epam/ketcher/issues/3627) – Ketcher requires unsafe-eval in order to run, which contradicts content security policy best practices
- [#6344](https://github.com/epam/ketcher/issues/6344) - Excessive scroll appears in macromolecules mode in canvas if Ketcher is inside dialog window
- [#6291](https://github.com/epam/ketcher/issues/6291) - Super G and Super T monomers do not load from a saved RXN V3000 file
- [#6370](https://github.com/epam/ketcher/issues/6370) - Inconsistent zoom behavior when inserting a molecule via setMolecule and Paste from Clipboard/Open from File
- [#6375](https://github.com/epam/ketcher/issues/6375) - Ketcher renders editor twice in dev mode
- [#6379](https://github.com/epam/ketcher/issues/6379) - Ketcher does not respond if switch to macromolecules, close popup with ketcher and open again
- [#6411](https://github.com/epam/ketcher/issues/6411) - Ketcher structure copy-paste in KET instead of MOL
- [#6196](https://github.com/epam/ketcher/issues/6196) - Ambiguous DNA bases (N, D, H, W) wrongly converted to DNA bases on antisense creation
- [#6106](https://github.com/epam/ketcher/issues/6106) - Two sense chain to one antisense connection render
- [#6272](https://github.com/epam/ketcher/issues/6272) - Cursor position after adding preset in sequence mode causes an incorrect sequence formation
- [#6132](https://github.com/epam/ketcher/issues/6132) - System should not re-layout canvas in case of antisense creation

---

### Additional notes:
- Ketcher 3.0 has been built and tested with Indigo version 1.28 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.28.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.28.0/images/sha256-5ac5b4e4b09cc8473ffa7690a412c3cae95bf144521449fac4b296c82b20d028)).
- [How to hide Macromolecules mode](https://github.com/epam/ketcher?tab=readme-ov-file#macromolecules-mode)