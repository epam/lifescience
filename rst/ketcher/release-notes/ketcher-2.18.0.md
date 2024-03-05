
# Ketcher 2.18.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

* [#3582](https://github.com/epam/ketcher/issues/3582) - AP are shown after closing modal
* [#3585](https://github.com/epam/ketcher/issues/3585) - APs are redrawn incorrectly after opening the modal window
* [#3583](https://github.com/epam/ketcher/issues/3583) - selected AP is duplicated while drawing the bond
* [#3551](https://github.com/epam/ketcher/issues/3551) - macro oxygen cannot be a leaving group in a chemical reaction
* [#3553](https://github.com/epam/ketcher/issues/3553) - macro while pulling bond onto monomer a preview is shown when hover monomer
* [#3610](https://github.com/epam/ketcher/issues/3610) - performance issues after selecting and moving large amount of monomers
* [#2414](https://github.com/epam/ketcher/issues/2414) - fix for bonds creation broken after merge of undo/redo task.
* [#3604](https://github.com/epam/ketcher/issues/3604) - macro preview window of micro structure shows pieces of macro structures
* [#3563](https://github.com/epam/ketcher/issues/3563) - Modal window for connecting attachment points does not match the design
* [#3614](https://github.com/epam/ketcher/issues/3614) – Add API method to check, whether a query structure is selected
* [#3651](https://github.com/epam/ketcher/issues/3651) - different coordinate systems are used in micro and macro mode
* [#3640](https://github.com/epam/ketcher/issues/3640) - macro after reloading the page monomers added to the favorites section disappear
* [#3830](https://github.com/epam/ketcher/issues/3830) – Aromatizing/Dearomatizing changes molecula position
* [#3833](https://github.com/epam/ketcher/issues/3833) - Chirality query property is missing from context menu
* [#3872](https://github.com/epam/ketcher/issues/3872) - Add support for all query properties in Mol V2000
* [#3685](https://github.com/epam/ketcher/issues/3685) – Implement add/remove explicit hydrogens
* [#3846](https://github.com/epam/ketcher/issues/3846) - macro class field is absent after serialisation to ket
* [#3915](https://github.com/epam/ketcher/issues/3915) - Pasting does not work in Firefox browser at all
* [#3914](https://github.com/epam/ketcher/issues/3914) – Add support for opening structures in CDX format embedded into MS PowerPoint
* [#3914](https://github.com/epam/ketcher/issues/3914) - Add support for opening structures in CDX format embedded into MS PowerPoint
* [#3949](https://github.com/epam/ketcher/issues/3949) - Parameter "sgroups" does not appear in .ket file if a S-Group is applied to structure along with molecule
* [#2177](https://github.com/epam/ketcher/issues/2177) - library.svg removal
* [#3967](https://github.com/epam/ketcher/issues/3967) - Exception if you paste from clipboard using Ctrl+Alt+V (Smile insert)
* [#3961](https://github.com/epam/ketcher/issues/3961) - system disorganize molecules and labels during loading from pptx file (base64 cdx format)
* [#3934](https://github.com/epam/ketcher/issues/3934) - Support selection entity selection flag in KET format
* [#3970](https://github.com/epam/ketcher/issues/3970) - Brackets are displayed incorrectly when a S-Group is added to an atom or an expanded Functional Group or Salt is added to an atom of a structure
* [#4045](https://github.com/epam/ketcher/issues/4045) - System doesn't save selection state for custom query bonds
* [#4048](https://github.com/epam/ketcher/issues/4048) - Right-click menu appears away from structure or is not visible at all on canvas
* [#4008](https://github.com/epam/ketcher/issues/4008) - design implementation is different from the reference design
* [#4091](https://github.com/epam/ketcher/issues/4091) - Zoom menu does not appear if ketcher injected in popup
* [#4097](https://github.com/epam/ketcher/issues/4097) - Cursor position misalignment after switching in fullscreen after changing ketcher settings
* [#4082](https://github.com/epam/ketcher/issues/4082) - Canvas preview render work at 14 times faster in Firefox than in Chrome
* [#4128](https://github.com/epam/ketcher/issues/4128) - Adding hydrogens moves molecules to the center of the screen
* Macro: [#3559](https://github.com/epam/ketcher/issues/3559) - The full screen button is in a place that doesn't match the design
* Macro: [#2414](https://github.com/epam/ketcher/issues/2414) - macro undo and redo tool
* Macro: [#3598](https://github.com/epam/ketcher/issues/3598) - Fix CI test command and unit tests
* Macro: [#2414](https://github.com/epam/ketcher/issues/2414) - "Undo and Redo" tool
* Macro: [#3530](https://github.com/epam/ketcher/issues/3530) - Labels in attachment points selection popup are small for large molecules
* Macro: [#3580](https://github.com/epam/ketcher/issues/3580) - Add possibility to expand "Select Attachment Points" Modal
* Macro: [#3495](https://github.com/epam/ketcher/issues/3495) - Is not possible to add RNA presets into the Favourite library
* Macro: [#3222](https://github.com/epam/ketcher/issues/3222) - Enumeration of linear and branch chains
* Macro: [#3630](https://github.com/epam/ketcher/issues/3630) - restrict micro and macro structures merging
* Macro: [#3531](https://github.com/epam/ketcher/issues/3531) – provide save/open ket and molv3000 ketcher api for macromolecules
* Macro: [#3601](https://github.com/epam/ketcher/issues/3601) - attachment points aren't disappearing in snake viewed chain of peptides when hovering them multiple times
* Macro: [#3469](https://github.com/epam/ketcher/issues/3469) - add snake bond algorithm .md
* Macro: [#3633](https://github.com/epam/ketcher/issues/3633) – undo/redo does not toggle snake mode
* Macro: [#3635](https://github.com/epam/ketcher/issues/3635) - Misalignment of monomers when imposing on top of each other
* Macro: [#3601](https://github.com/epam/ketcher/issues/3601) – attachment points aren't disappearing in snake viewed chain of peptides when hovering them multiple times
* Macro: [#3691](https://github.com/epam/ketcher/issues/3691) - Ket file does not include atom numbers associated with the leaving groups after saving
* Macro: [#3718](https://github.com/epam/ketcher/issues/3718) - Pressing Snake mode button causes exception
* Macro: [#3719](https://github.com/epam/ketcher/issues/3719) - Unable to load from file: System throws Convert Error! error message
* Macro: [#3660](https://github.com/epam/ketcher/issues/3660) - After removing the abbreviation in micro mode and switching to macro mode, the monomer disappears
* Macro: [#3702](https://github.com/epam/ketcher/issues/3702) - 'Uncaught DOMException' error in DevTool console after switch from Macro to Micro mode
* Macro: [#3651](https://github.com/epam/ketcher/issues/3651) - different coordinate systems are used in micro and macro mode
* Macro: [#3766](https://github.com/epam/ketcher/issues/3766) - Incorrect attachment point labels parsing from ket
* Macro: [#3719](https://github.com/epam/ketcher/issues/3719) - Unable to load from file: System throws Convert Error! error message
* Macro: [#3787](https://github.com/epam/ketcher/issues/3787) - System allow to connect block to already occupied connection (that cases invalide saved files)
* Macro: [#3666](https://github.com/epam/ketcher/issues/3666) - After opening a file in macro mode, structure is not in center of the screen and need scroll to find it
* Macro/Micro: [#3738](https://github.com/epam/ketcher/issues/3738) - Switching from Macromolecules view to Molecules view causes crash if custom aromatic hydrocarbon was connected with monomer
* Macro: [#3900](https://github.com/epam/ketcher/issues/3900) - The last letter in RNA Builder name field cannot be deleted
* Macro: [#3899](https://github.com/epam/ketcher/issues/3899) - Attachment points do not disappear when hover is removed from some monomers.
* Macro: [#3545](https://github.com/epam/ketcher/issues/3545) - N- C-ends /5' - 3' - ends display in peptide /RNA chains
* Macro: [#3874](https://github.com/epam/ketcher/issues/3874) - R2 label is displayed on attachment atom instead of leaving group in monomer preview
* Macro: [#3756](https://github.com/epam/ketcher/issues/3756) - Loading from file and than - Undo changes causes exceptions and breakes selection/moving fuctionality
* Macro: [#3712](https://github.com/epam/ketcher/issues/3712) - Pressing Layout/Clean Up button cleanup all macromoleculas from canvas
* Macro: [#3667](https://github.com/epam/ketcher/issues/3667) – Monomers are stacked and difficult to read after importing a file
* Macro: [#3692](https://github.com/epam/ketcher/issues/3692) - Leaving groups are not displayed correctly in preview when switching to Micro mode
* Macro: [#3820](https://github.com/epam/ketcher/issues/3820) - System doesn't close Save dialog after Save button pressed
* Macro: [#3703](https://github.com/epam/ketcher/issues/3703) – Selected monomer does not appear above the others
* Macro: [#3786](https://github.com/epam/ketcher/issues/3786) - Connection works wrong
* Macro: [#3757](https://github.com/epam/ketcher/issues/3757) - Save to file and than Load it back eliminate monomer names from preview tooltip
* Macro: [#3713](https://github.com/epam/ketcher/issues/3713) - Hot keys for toolbar buttons are not implemented in Macromoleculas view
* Macro: [#3815](https://github.com/epam/ketcher/issues/3815) - Change the color of the occupied attachment points from orange to dark green
* Macro: [#3853](https://github.com/epam/ketcher/issues/3853) – cannot erase entered text in the search box in monomer library
* Macro: [#3981](https://github.com/epam/ketcher/issues/3981) - Monomers are positioned below bonds that connect them
* Macro: [#4014](https://github.com/epam/ketcher/issues/4014) - Monomers (attachment points) cannot be connected by a bond in Firefox browser
* Macro: [#3917](https://github.com/epam/ketcher/issues/3917) - Lack of consistency in hotkeys between micro and macro mods and absence of tooltips with information about hotkeys
* Autotests: [#3454](https://github.com/epam/ketcher/issues/3454) - peptide monomer library
* Autotests: [#3579](https://github.com/epam/ketcher/issues/3579) - refactor - removing unnecessary folder
* Autotests: [#3451](https://github.com/epam/ketcher/issues/3451) - rna monomer library and rna builder
* Autotests: [#3632](https://github.com/epam/ketcher/issues/3632) - autotests macromicro switcher
* Autotests: [#3436](https://github.com/epam/ketcher/issues/3436) - autotests query attributes for smarts
* Autotests: [#3565](https://github.com/epam/ketcher/issues/3565) - Selection Tool 
