
# Ketcher 2.20.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#3650](https://github.com/epam/ketcher/issues/3650) - Remove and insert nucleotides in sequences (sequence representation)
* [#3861](https://github.com/epam/ketcher/issues/3861) - Insertion mode for nucleotide entry (switch RNA/DNA/Peptide)
* [#4146](https://github.com/epam/ketcher/issues/4146) - UI for Open/Save As FASTA
* [#4109](https://github.com/epam/ketcher/issues/4109) - UI for Save As Sequence
* [#3819](https://github.com/epam/ketcher/issues/3819) - Selection in sequence representation for view mode
* [#3819](https://github.com/epam/ketcher/issues/3819) - Selection in sequence representation edit mode
* [#3876](https://github.com/epam/ketcher/issues/3876) - Nucleotide preview in sequence representation

### Bugfixes and improvements
* [#3005](https://github.com/epam/ketcher/issues/3005) - Unable to 'undo' the paste action, if there is no reset to Select tool
* [#3902](https://github.com/epam/ketcher/issues/3902) - If open a macro file and put in center of canvas in micro mode then switch to macro, structure is not in center of canvas*
* [#3750](https://github.com/epam/ketcher/issues/3750) - Add search menu clear button
* [#4173](https://github.com/epam/ketcher/issues/4173) - the pop-up window does not appear in fullscreen mode after clicking the “Open” button and the “Save as” button
* [#4231](https://github.com/epam/ketcher/issues/4231) - Maximum call stack size exceeded error appears during snake layout for large chains
* [#3663](https://github.com/epam/ketcher/issues/3663) - After clicking the 'Duplicate and Edit' button and subsequently clicking 'Cancel,' the preset remains saved.
* [#4241](https://github.com/epam/ketcher/issues/4241) - Pasting large cyclodextrins structure cause Ketcher to freeze
* [#4271](https://github.com/epam/ketcher/issues/4271) - The Uncaught TypeError appears in the DevTool Console, when scrolling until it stops, using the Shift+Left arrow, in the Text-editing mode
* [#4295](https://github.com/epam/ketcher/issues/4295) - Cannot save FASTA using the Remote mode
* [#4286](https://github.com/epam/ketcher/issues/4286) - Editing grid disappears but editing mode is on
* [#4297](https://github.com/epam/ketcher/issues/4297) - When removing nucleotides from the canvas, the preview of the nucleotide does not disappear, if you leave the cursor over it
* [#4192](https://github.com/epam/ketcher/issues/4192) - Export to SVG/PNG ignores "Show hydrogen labels" option
* [#3775](https://github.com/epam/ketcher/issues/3775) - Phenylalanine mustard is displayed incorrectly in the Structure library
* [#4296](https://github.com/epam/ketcher/issues/4296) - When pressing the Enter or the Spacebar, the “Edit mode” drop-down opens and closes randomly in the Text-editing mode
* [#4028](https://github.com/epam/ketcher/issues/4028) - When monomers are selected Del and Backspace hotkey delete selected monomers and switches to Erase tool
* [#4356](https://github.com/epam/ketcher/issues/4356) - Clear canvas button doesn't work in Sequence mode
* [#4369](https://github.com/epam/ketcher/issues/4369) - Del button works as Backspace button that is wrong
* [#4329](https://github.com/epam/ketcher/issues/4329) - Cyclic chains disappear from canvas when switching to sequence mode
* [#4252](https://github.com/epam/ketcher/issues/4252) - Migrate to Indigo v1.19.0 in-browser module
