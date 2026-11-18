
# Ketcher 3.21.0

## What's Changed

### New features
- [#3709](https://github.com/epam/ketcher/issues/3709) – Displaying Warning message in case of files with no atoms
- [#10458](https://github.com/epam/ketcher/issues/10458) – Set n as the default polymer label for SRU Polymer
- [#7182](https://github.com/epam/ketcher/issues/7182) – Update the appearance of fields in the "Calculate Properties" window when there is no data for a property
- [#10489](https://github.com/epam/ketcher/issues/10489) – Add an explanation about atom/bond IDs to the "Check structure" window
- [#9457](https://github.com/epam/ketcher/issues/9457) – Settings Improvements in Molecules Tab: Typos, Tool Tips, and Dropdown Rename Requirements
- [#11899](https://github.com/epam/ketcher/issues/11899) – Retain history between macro and micro molecule modes
- [#4384](https://github.com/epam/ketcher/issues/4384) – Chinese interface localization
- [#10825](https://github.com/epam/ketcher/issues/10825) – Update the help document (3.20.)
- [#9370](https://github.com/epam/ketcher/issues/9370) – Editing monomers from macromolecules molecules mode in the monomer creation wizard
- [#6595](https://github.com/epam/ketcher/issues/6595) – Modification of one side of the AS duplex should influence the other

### Bugfixes and improvements
- [#7780](https://github.com/epam/ketcher/issues/7780) – Selected selection tool in Macro mode is not saved to Local storage and resets to Rectangle tool after reload
- [#6125](https://github.com/epam/ketcher/issues/6125) – R2 should be NH2 for Phosphorodiamidate
- [#5429](https://github.com/epam/ketcher/issues/5429) – Selection of PNG/SVG images can't be saved to KET
- [#8357](https://github.com/epam/ketcher/issues/8357) – System should not load monomer to the library if modificationTypes value contain improper symbols
- [#6458](https://github.com/epam/ketcher/issues/6458) – Long bond incorrectly turns into a direct bond when moving the second monomer
- [#2524](https://github.com/epam/ketcher/issues/2524) – After appearance of EDIT ABBREVIATION modal, hotkey switching does not work until you click on the canvas
- [#9690](https://github.com/epam/ketcher/issues/9690) – RNA Builder: Monomers remain grayed out after canceling preset creation
- [#9693](https://github.com/epam/ketcher/issues/9693) – RNA Builder: Default preset name changes unexpectedly after switching phosphate picker from 3' to 5'
- [#4320](https://github.com/epam/ketcher/issues/4320) – 'general.dearomatize-on-load' setting does not work for MOL V2000 structures inserted via API
- [#9104](https://github.com/epam/ketcher/issues/9104) – The Nucleotide Phosphate becomes broken or separates if the Sugar part is moved slightly beforehand
- [#4150](https://github.com/epam/ketcher/issues/4150) – Unable to remove last selected atom selection if bond already selected
- [#11521](https://github.com/epam/ketcher/issues/11521) – Contract abbreviation option is missing for Nucleotide s-group type
- [#6941](https://github.com/epam/ketcher/issues/6941) – Snake mode auto-layout doesn't work if user come to Snake mode from Micromolecules one
- [#4896](https://github.com/epam/ketcher/issues/4896) – Preset with sugar without R3 AP can be created, when choosing base directly from the "Bases" section
- [#10248](https://github.com/epam/ketcher/issues/10248) – Nucleotide preset: Atom not highlighted red if corresponding component tab is active
- [#9333](https://github.com/epam/ketcher/issues/9333) – Some AxoLabs format codes are not supported
- [#4528](https://github.com/epam/ketcher/issues/4528) – In the Sequence mode pressing Enter toggles the Fullscreen mode on and off, and changes the “Fullscreen mode” button
- [#3268](https://github.com/epam/ketcher/issues/3268) – Incorrect display of Attachment points along with Atom Properties
- [#4445](https://github.com/epam/ketcher/issues/4445) – Macro: Context menu opened outside selection have to remove selection in the same manner as it works in Micro mode
- [#10405](https://github.com/epam/ketcher/issues/10405) – Hovering over a data S-group should give the tooltip preview of FiledName=FiledValue with the atom/bond/structure
- [#5177](https://github.com/epam/ketcher/issues/5177) – The search in the Library uses different algorithms when searching for hyphen and underscore
- [#11078](https://github.com/epam/ketcher/issues/11078) – Paste option is enabled in Macromolecules mode when the clipboard is empty or contains not applicable content
- [#7503](https://github.com/epam/ketcher/issues/7503) – Bond/monomer tooltip preview placed wrong in on edge cases
- [#11915](https://github.com/epam/ketcher/issues/11915) – Cells with no data should be greyed out (disabled) on Calculate properties panel
- [#7681](https://github.com/epam/ketcher/issues/7681) – monomer creation works wrong
- [#11984](https://github.com/epam/ketcher/issues/11984) – Unable to load structure from mol v3000
- [#5938](https://github.com/epam/ketcher/issues/5938) – System allow to edit (and change) hydrogen bond type to another
- [#5275](https://github.com/epam/ketcher/issues/5275) – Size of elements is reduced after Save to KET format if the element is corrupted
- [#6173](https://github.com/epam/ketcher/issues/6173) – Antisense creation is not possible if non eligible for antisense creation chain present in the selection
- [#6800](https://github.com/epam/ketcher/issues/6800) – Adding Enter doesn't break sequence on two chains (in SYNC ON mode) if we cut between letter symbol and dash
- [#7775](https://github.com/epam/ketcher/issues/7775) – Inconsistent selection highlight colors between Rectangle and Lasso tools compared to Micro mode
- [#7199](https://github.com/epam/ketcher/issues/7199) – Ruler slider becomes locked when dragged beyond canvas edge
- [#7800](https://github.com/epam/ketcher/issues/7800) – Edit attachment point dialog overlaps the atom being edited and doesn't move upon scrolling canvas
- [#5583](https://github.com/epam/ketcher/issues/5583) – Incorrect selection display when using ketcher.editor.options API
- [#6943](https://github.com/epam/ketcher/issues/6943) – System does retain snake mode layout once passing from Flex mode to Micro mode thru Snake mode
- [#5448](https://github.com/epam/ketcher/issues/5448) – Existing elements on Canvas are moved after adding elements to Canvas from file
- [#12015](https://github.com/epam/ketcher/issues/12015) – Monomer atomic structures should not be affected by rotation/flipping if collapsed
- [#12467](https://github.com/epam/ketcher/issues/12467) – Added configuration for Ketcher to disable some parts of functionality
- [#5575](https://github.com/epam/ketcher/issues/5575) – After user selects add text/picture/arrows/plus/static objects it should default switch to select tool
- [#12731](https://github.com/epam/ketcher/issues/12731) – Jest crashes with SyntaxError in consumer apps due to intl-messageformat ESM import



---

### Additional notes:
- Ketcher 3.21.0 has been built and tested with Indigo version 1.49 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.49.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.49.0/images)).
