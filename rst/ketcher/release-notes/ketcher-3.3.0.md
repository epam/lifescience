
# Ketcher 3.3.0

## What's Changed

### New features
- [#6508](https://github.com/epam/ketcher/issues/6508) – Update the logic for recognizing sense and antisense chains
- [#6435](https://github.com/epam/ketcher/issues/6435) – Do not retain snake mode layout when passing though snake mode
- [#6519](https://github.com/epam/ketcher/issues/6519) – Implement the library redesign and modify the RNA builder behavior
- [#6620](https://github.com/epam/ketcher/issues/6620) – Add salts to the "Salts and Solvents" tab in the monomer library
- [#6472](https://github.com/epam/ketcher/issues/6472) – Add "Copy", "Paste", and "Delete" to the r-click drop down menu in sequence mode
- [#5999](https://github.com/epam/ketcher/issues/5999) – Added "Create Antisense Strand" icon on the toolbar
- [#6317](https://github.com/epam/ketcher/issues/6317) – Introducing the snap to distance functionality for monomers connected via bonds
- [#6612](https://github.com/epam/ketcher/issues/6612) – Update the help documentation (3.2)
- [#6987](https://github.com/epam/ketcher/issues/6987) – Migrate to Indigo v1.31.0 in-browser module

### Bugfixes and improvements
- [#6293](https://github.com/epam/ketcher/issues/6293) – Remove base monomer border after selection
- [#6573](https://github.com/epam/ketcher/issues/6573) – Incorrect bond length and angle for non-natural monomers in the library
- [#6695](https://github.com/epam/ketcher/issues/6695) – Unable to create antisense RNA/DNA chain in case of multiple сhain selection (if not eligible for antisense chain selected)
- [#6842](https://github.com/epam/ketcher/issues/6842) – Single click on already selected monomer cause monomer sticks to mouse cursor and snapping elements appear on the canvas forever
- [#6813](https://github.com/epam/ketcher/issues/6813) – Click on monomer selection area causes an exception Uncaught TypeError: Cannot read properties of undefined (reading 'drawingEntity')
- [#6774](https://github.com/epam/ketcher/issues/6774) – Modified bases selected via RNA Builder revert to natural analogs in all modes
- [#6495](https://github.com/epam/ketcher/issues/6495) – System replaces A base with always RNA N base (alternatives of A,C,G,U) even if user selected DNA N base (alternatives of A,C,G,T)
- [#6716](https://github.com/epam/ketcher/issues/6716) – Cursor can escape to the void after same actions and broke canvas
- [#6671](https://github.com/epam/ketcher/issues/6671) – Removing dash should turn aligned nucleotide to nucleoside
- [#6541](https://github.com/epam/ketcher/issues/6541) – Undo of clear canvas operation causes molecules bonds overlap atom labels
- [#6712](https://github.com/epam/ketcher/issues/6712) – Adding RNA/DNA before empty space in sense sequence causes exception and broken canvas
- [#6776](https://github.com/epam/ketcher/issues/6776) – Phosphate does not appear immediately when added via keyboard in SYNC mode
- [#6780](https://github.com/epam/ketcher/issues/6780) – Phosphate always added to sense strand in non-SYNC mode when targeting antisense strand
- [#6781](https://github.com/epam/ketcher/issues/6781) – Phosphates added via keyboard in SYNC mode are not reverted by Undo and cause console errors on hover
- [#6779](https://github.com/epam/ketcher/issues/6779) – Unable to add phosphate to antisense strand in SYNC mode via keyboard
- [#6775](https://github.com/epam/ketcher/issues/6775) – Adding monomer to first from the left position of antisense chain works wrong and causes exception: Uncaught TypeError: Cannot read properties of undefined (reading 'chain')
- [#6863](https://github.com/epam/ketcher/issues/6863) – Horizontal/Vertical snap to distance doesn't work for hydrogen bonds
- [#6814](https://github.com/epam/ketcher/issues/6814) – System should turn nucleotide to nucleoside on sequence break by Enter
- [#6783](https://github.com/epam/ketcher/issues/6783) – Incorrect cursor jumps after phosphate insertion in middle or at end of sequence
- [#6824](https://github.com/epam/ketcher/issues/6824) – Unable to delete multiple sequences at once via right-click menu in Sequence mode
- [#6705](https://github.com/epam/ketcher/issues/6705) – Antisense complement is not skipped when terminal monomer lacks an attachment point (R1/R2), causing incorrect structure on canvas
- [#6833](https://github.com/epam/ketcher/issues/6833) – Tooltips on monomer cards in all sections instantly disappear on hover in popup Ketcher
- [#6830](https://github.com/epam/ketcher/issues/6830) – RNA Builder section do not highlight corresponding monomer in library on first click
- [#6828](https://github.com/epam/ketcher/issues/6828) – Star icon for Favorites tab in monomer library is too small compared to design specification
- [#6831](https://github.com/epam/ketcher/issues/6831) – Last row of monomers in Sugars, Bases, and Phosphates sections is not visible in popup Ketcher
- [#6834](https://github.com/epam/ketcher/issues/6834) – Clicking on base card in RNA Builder does not scroll to selected base if multiple bases from the same section are selected
- [#6816](https://github.com/epam/ketcher/issues/6816) – Incorrect hotkeys are displayed and triggered for RNA and DNA Antisense strand creation

---

### Additional notes:
- Ketcher 3.3.0 has been built and tested with Indigo version 1.31 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.31.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.31.0/images/sha256-ca9addbfebcee2ddc858362ce4020f59fd180d4de8a97af1609389e6e9106cdf)).
