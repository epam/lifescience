
# Ketcher 3.1.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
- [#6167](https://github.com/epam/ketcher/issues/6167) – Long bonds for linearly displayed circular structures
- [#5942](https://github.com/epam/ketcher/issues/5942) – Update the representation of sense and antisense chains in sequence mode (1/2)
- [#5995](https://github.com/epam/ketcher/issues/5995) – Synchronize the library tab with typing type switcher in sequence mode
- [#6222](https://github.com/epam/ketcher/issues/6222) – New chain tool behavior
- [#6246](https://github.com/epam/ketcher/issues/6246) – Import indigo with EXPORT_ES6 & USE_ES6_IMPORT_META options
- [#6417](https://github.com/epam/ketcher/issues/6417) – Update Indigo to 1.29.0 in browser module

### Bugfixes and improvements
- [#6164](https://github.com/epam/ketcher/issues/6164) – Changing any parameter at Settings cause Undo/Redo work wrong (or delete undo history)
- [#6166](https://github.com/epam/ketcher/issues/6166) – Color schema for Favorites tab at RNA Library is wrong for Peptides
- [#6088](https://github.com/epam/ketcher/issues/6088) – Disable create antisense strand option if antisense-less base present in chain selection
- [#5696](https://github.com/epam/ketcher/issues/5696) – Adding Attachment point to microstructure already connected to monomer - causes problems
- [#6201](https://github.com/epam/ketcher/issues/6201) – Circular hydrogen bond connection between three (or more) chains, those hydrogen bonds isn't considered as side chain connection for layout purposes
- [#6195](https://github.com/epam/ketcher/issues/6195) – Nucleotide wrongly become antisense oriented if have hydrogen connection to sugar
- [#6194](https://github.com/epam/ketcher/issues/6194) – Unknown monomer and CHEM overlap to each other if both are the side chain for same chain
- [#6422](https://github.com/epam/ketcher/issues/6422) – Long bond appears behind monomers when using attachment points
- [#6084](https://github.com/epam/ketcher/issues/6084) – System doesn't allow select ambiguous monomers from the library
- [#6085](https://github.com/epam/ketcher/issues/6085) – Changing of ambiguous base via RNA Builder on Sequence mode causes sequence corruption
- [#6098](https://github.com/epam/ketcher/issues/6098) – Adding second chain with antisense chain to the canvas cause layout problem
- [#6446](https://github.com/epam/ketcher/issues/6446) – System shouldn't merge two antisense chains if separator monomer got deleted
- [#6447](https://github.com/epam/ketcher/issues/6447) – System doesn't split chain pair on two if - symbol deleted
- [#6460](https://github.com/epam/ketcher/issues/6460) – Troubles with switching to Edit mode if - symbol present in sequence
- [#5780](https://github.com/epam/ketcher/issues/5780) – Connection points appear visually disconnected when moving monomers in Flex and Snake mode
- [#6462](https://github.com/epam/ketcher/issues/6462) – Adding peptide between RNA and - symbol breaks sense/antisense chain
- [#6456](https://github.com/epam/ketcher/issues/6456) – Long bond appears behind the structure after Copy-Paste in Flex Mode
- [#6471](https://github.com/epam/ketcher/issues/6471) – Removing peptide from sense/antisense chain cause unnecessary phosphate removal
- [#6493](https://github.com/epam/ketcher/issues/6493) – Undo of deleted bond on sequence mode causes "ghost" monomer appearance on the canvas
- [#6505](https://github.com/epam/ketcher/issues/6505) – Hotkey CTRL+ALT+P does not switch library to Peptides
- [#6628](https://github.com/epam/ketcher/issues/6628) – Add export of ketcher-standalone esm module as cjs
- [#6159](https://github.com/epam/ketcher/issues/6159) – Aromatizing doesn't work for Pyridone and Pyrone (molecules from Template library)
- [#6588](https://github.com/epam/ketcher/issues/6588) – Peptide sequence not pasting directly on canvas
- [#6661](https://github.com/epam/ketcher/issues/6661) – Adjust ketcher-standalone entrypoints to work for all builders

---

### Additional notes:
- Ketcher 3.1.0 has been built and tested with Indigo version 1.29 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.29.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.29.0/images/sha256-e79143bab1b5b96dc8b7b1e10d62612f89e59399c16dba4ecfa56f11fe8fb118)).

