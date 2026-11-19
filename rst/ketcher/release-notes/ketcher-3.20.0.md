
# Ketcher 3.20.0

## What's Changed

### New features
- [#10816](https://github.com/epam/ketcher/issues/10816) – Add error handling and user feedback for "Save to SDF" in Templates dialog
- [#7455](https://github.com/epam/ketcher/issues/7455) – Support monomer replacement with drag-and-drop from library
- [#11093](https://github.com/epam/ketcher/issues/11093) – Flip the positions of unoccupied R3 and R4 attachment points
- [#8921](https://github.com/epam/ketcher/issues/8921) – "Edit monomer" window: Editing monomers from molecules mode in the monomer creation wizard
- [#8924](https://github.com/epam/ketcher/issues/8924) – Deleting/modifying of an AP that participates in bonds on canvas - Editing monomers from molecules mode in the monomer creation wizard

### Bugfixes and improvements
- [#6707](https://github.com/epam/ketcher/issues/6707) – Enter key in single-strand edit mode incorrectly breaks both chains instead of only one
- [#6142](https://github.com/epam/ketcher/issues/6142) – An error occurred while saving nucleotides with different connections
- [#10273](https://github.com/epam/ketcher/issues/10273) – RNA Builder: Inappropriate sugars are not disabled when the phosphate position is specified before any components are added
- [#7076](https://github.com/epam/ketcher/issues/7076) – The chemical elements are arranged in reverse order
- [#7232](https://github.com/epam/ketcher/issues/7232) – getSmiles() promise never resolves in standalone mode
- [#10228](https://github.com/epam/ketcher/issues/10228) – Modification type value missing after BILN/HELM export and import
- [#10323](https://github.com/epam/ketcher/issues/10323) – Hydrogen bonds disappears after user expands monomer on Molecules canvas
- [#7701](https://github.com/epam/ketcher/issues/7701) – Sync mode button does not appear just after antisense creation
- [#10856](https://github.com/epam/ketcher/issues/10856) – Fix unable to connect two or more monomers to atom in a row
- [#5669](https://github.com/epam/ketcher/issues/5669) – render labels for expanded monomers
- [#3152](https://github.com/epam/ketcher/issues/3152) – The Abbreviation lookup appears when pressing the shortcut "0" several times
- [#2429](https://github.com/epam/ketcher/issues/2429) – Triple Bond is drawn at the various angles when click on Template and Chain atoms
- [#11335](https://github.com/epam/ketcher/issues/11335) – Errors in console when Reaction Plus tool is active
- [#10829](https://github.com/epam/ketcher/issues/10829) – No blank option in Subtype dropdown after selecting a subtype on S-Group Properties dialog
- [#4525](https://github.com/epam/ketcher/issues/4525) – After inserting the “black” error messages somewhere, the message text is displayed in the wrong format
- [#3842](https://github.com/epam/ketcher/issues/3842) – Micro: No max length limit for atom custom query feature cause exception if content size too big
- [#7367](https://github.com/epam/ketcher/issues/7367) – Only bonds remain on canvas after applying 3D Viewer to structures marked as nucleotide components
- [#7129](https://github.com/epam/ketcher/issues/7129) – Calculate Properties window clears on mouse release when macromolecules are connected via a microstructure without attachment points
- [#10681](https://github.com/epam/ketcher/issues/10681) – Ambiguous monomers (not from our library) should have white labels for more contrast over grey belt
- [#3946](https://github.com/epam/ketcher/issues/3946) – Selection for molecules with Inversions and hydrogens works wrong
- [#6170](https://github.com/epam/ketcher/issues/6170) – TypeError: Cannot read properties of undefined (reading pp)
- [#3884](https://github.com/epam/ketcher/issues/3884) – System can't load molecule from clipboard if it ends with few carriage returns
- [#5462](https://github.com/epam/ketcher/issues/5462) – Using the RemoteStructServiceProvider will result in an error message
- [#10734](https://github.com/epam/ketcher/issues/10734) – Base number in the chain should disappear once it stops being a part of preset
- [#5474](https://github.com/epam/ketcher/issues/5474) – Ambiguous monomer are not scaled in expanded Select Connection Points dialog
- [#11419](https://github.com/epam/ketcher/issues/11419) – Ambiguous monomers (not from our library) should have grey belts in preview tooltip and Edit/Select Attachment Points dialog
- [#4087](https://github.com/epam/ketcher/issues/4087) – System should correctly report that it can't open target pptx because it protected by password
- [#4858](https://github.com/epam/ketcher/issues/4858) – Non-user friendly way of exiting RNA builder
- [#10846](https://github.com/epam/ketcher/issues/10846) – RNA/DNA/PEP switcher on Macromolecules mode on Mac has Windows hotkey tooltips
- [#11083](https://github.com/epam/ketcher/issues/11083) – In the Monomer Edit modal window, the Response option appears as OK instead of Yes
- [#3515](https://github.com/epam/ketcher/issues/3515) – Uncaught TypeError: Cannot read properties of undefined (reading eventBus) in react
- [#346](https://github.com/epam/ketcher/issues/346) – Promise failing during benzene rings render
- [#2350](https://github.com/epam/ketcher/issues/2350) – Access Ketcher iframe via JavaScript, .ketcher undefined
- [#4218](https://github.com/epam/ketcher/issues/4218) – Cannot read properties of null
- [#2637](https://github.com/epam/ketcher/issues/2637) – Import error
- [#5206](https://github.com/epam/ketcher/issues/5206) – Start new sequence between two side chains works wrong
- [#6501](https://github.com/epam/ketcher/issues/6501) – Microstructure saved as MOL V2000 instead of MOL V3000 in Macro Mode
- [#3797](https://github.com/epam/ketcher/issues/3797) – working ketcher component in React
- [#5023](https://github.com/epam/ketcher/issues/5023) – Splitting molecule on pieces with attachment points of each cause crash when switching to Macro mode
- [#5237](https://github.com/epam/ketcher/issues/5237) – Preset replacement in view mode works wrong
- [#10419](https://github.com/epam/ketcher/issues/10419) – Stereo flag is not displayed when copy-pasting a structure containing a stereo flag in Macro mode
- [#6430](https://github.com/epam/ketcher/issues/6430) – Direction symbol is wrong for antisense chain in edit mode (pointed to the right)
- [#4444](https://github.com/epam/ketcher/issues/4444) – Macro: It is possible to remove selection while in Modify in RNA Builder mode
- [#12018](https://github.com/epam/ketcher/issues/12018) – ketcher-standalone binaryWasm builds ship an unresolved web-worker import and no Indigo worker
- [#12125](https://github.com/epam/ketcher/issues/12125) – Preview tooltip glitch problem
- [#11889](https://github.com/epam/ketcher/issues/11889) – Bonds in atomic structures behave as targets for a new connection in macromolecules mode

---
### Additional notes:
- Ketcher 3.20.0 has been built and tested with Indigo version 1.48 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.48.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.48.0/images/sha256-85b89d427c2a9e2f9e513e2ae9e3190477fdd9ed517bcf8bd8a27eb5229036c4)).
