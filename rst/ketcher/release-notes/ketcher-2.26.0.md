
# Ketcher 2.26.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#5400](https://github.com/epam/ketcher/issues/5400) – Expand macromolecules in micro mode
* [#5359](https://github.com/epam/ketcher/issues/5359) – Display molecules in macro mode: basic structures with atoms and bonds
* [#5325](https://github.com/epam/ketcher/issues/5325) – Change natural analogue of monomers
* [#5324](https://github.com/epam/ketcher/issues/5324) – Change symbols of monomers
* [#5323](https://github.com/epam/ketcher/issues/5323) – Change names of monomers
* [#5195](https://github.com/epam/ketcher/issues/5195) – Some content problems in monomer library
* [#5111](https://github.com/epam/ketcher/issues/5111) – Change structure of monomers
* [#4984](https://github.com/epam/ketcher/issues/4984) – Highlight atoms and bonds
* [#4965](https://github.com/epam/ketcher/issues/4965) – View only mode
* [#4986](https://github.com/epam/ketcher/issues/4986) – Ctrl+move copy
* [#1838](https://github.com/epam/ketcher/issues/1838) – Create custom top toolbar buttons
* [#5156](https://github.com/epam/ketcher/issues/5156) – Add new option in settings acs style
* [#5154](https://github.com/epam/ketcher/issues/5154) – Change "Double bond width" setting
* [#5175](https://github.com/epam/ketcher/issues/5175) – Allow entering values in settings with the precision of one decimal place
* [#4982](https://github.com/epam/ketcher/issues/4982) – Choose both directions of wedged/hashed bonds from right-clicking the bond
* [#5435](https://github.com/epam/ketcher/issues/5435) – Change bond length for ACS styles settings
* [#5351](https://github.com/epam/ketcher/issues/5351) – Change the default size of a plus and the arrows
* [#5945](https://github.com/epam/ketcher/issues/5945) – Update indigo to 1.25.0 in browser module

### Bugfixes and improvements
* [#5430](https://github.com/epam/ketcher/issues/5430) – Fix ESLint error in selectClearCanvasTool function
* [#4983](https://github.com/epam/ketcher/issues/4983) – Settings for the "attachment point tool" don't update with changed pixel settings
* [#4757](https://github.com/epam/ketcher/issues/4757) – Incorrect stereo-label placement for (E) and (Z)
* [#5536](https://github.com/epam/ketcher/issues/5536) – White screen is displayed after change direction of wedge bond
* [#5296](https://github.com/epam/ketcher/issues/5296) – Save Support for RDF Format
* [#5615](https://github.com/epam/ketcher/issues/5615) – Overlapping UI elements in Query Properties right-click menu
* [#4394](https://github.com/epam/ketcher/issues/4394) – In the Sequence mode, the tooltip “Start new sequence” is shown outside of the canvas
* [#5651](https://github.com/epam/ketcher/issues/5651) – The reaction can't save to MDL RXN V3000 (returns RXN V2000 instead)
* [#5597](https://github.com/epam/ketcher/issues/5597) – New rendering for highlight
* [#5561](https://github.com/epam/ketcher/issues/5561) – Set a new name for the button acs style
* [#5672](https://github.com/epam/ketcher/issues/5672) – Multiple duplicate items
* [#5205](https://github.com/epam/ketcher/issues/5205) – Edit Connection points dialog can cause invalid connection between monomers
* [#5709](https://github.com/epam/ketcher/issues/5709) – Unable to load variant sugar from HELM - system throws an error: Convert error! {}
* [#5710](https://github.com/epam/ketcher/issues/5710) – Unable to load variant phosphate from HELM - system throws an error: Convert error! {}
* [#5711](https://github.com/epam/ketcher/issues/5711) – Unable to load variant CHEM from HELM - system throws an error: Convert error! {}
* [#5621](https://github.com/epam/ketcher/issues/5621) – O and U sumbols are not supported in sequence mode
* [#5612](https://github.com/epam/ketcher/issues/5612) – The file size is the same when saved to png
* [#5634](https://github.com/epam/ketcher/issues/5634) – ketcher.getMolfile() stopped working for macro canvas with peptides
* [#5649](https://github.com/epam/ketcher/issues/5649) – Default values for bond settings (at least for bond) got corrupted and become wrong after ver 2.26 version installed
* [#4316](https://github.com/epam/ketcher/issues/4316) – In the Sequence and Flex mode the nucleotide preview is closely adjacent to the left edge of the screen
* [#5557](https://github.com/epam/ketcher/issues/5557) – Bond/monomer tooltip preview placed wrong in on edge cases
* [#5097](https://github.com/epam/ketcher/issues/5097) – Selection frame is displayed improperly for overlapped images
* [#5148](https://github.com/epam/ketcher/issues/5148) – Image changes the layer to top after scaling actions
* [#5581](https://github.com/epam/ketcher/issues/5581) – If switch to View Only Mode with Fragment Selection you cannot change or select another selection mode
* [#5657](https://github.com/epam/ketcher/issues/5657) – Clear canvas doesn't work for micro structures on macro mode
* [#5679](https://github.com/epam/ketcher/issues/5679) – Unable to establish connection between micro structure and macro ones
* [#5401](https://github.com/epam/ketcher/issues/5401) – Side-chain connections are not displayed in Snake mode
* [#5662](https://github.com/epam/ketcher/issues/5662) – Fix inability to select Erase tool after monomer expansion
* [#5612](https://github.com/epam/ketcher/issues/5612) – The file size is the same when saved to png
* [#5686](https://github.com/epam/ketcher/issues/5686) – Bonds between micro and macro structures couldn't be selected and deleted
* [#5659](https://github.com/epam/ketcher/issues/5659) – Moving of selected microstructures on macro canvas works wrong
* [#5665](https://github.com/epam/ketcher/issues/5665) – Show remove abbreviation dialog when trying to erase expanded monomer
* [#5725](https://github.com/epam/ketcher/issues/5725) – Cursor position is incorrect when editing sequence in Macro mode
* [#5800](https://github.com/epam/ketcher/issues/5800) – Application crashes with white screen in Macro mode when loading local storage data from a previous version
* [#5758](https://github.com/epam/ketcher/issues/5758) – Highlight only bonds when selected bonds + atoms
* [#5703](https://github.com/epam/ketcher/issues/5703) – Added tooltip for image resolution option
* [#5673](https://github.com/epam/ketcher/issues/5673) – Micro structures connected to polymer chains are not shown on Sequence mode canvas
* [#5650](https://github.com/epam/ketcher/issues/5650) – The reaction with catalysts is displayed incorrect with ACS style setting and after layout
* [#5761](https://github.com/epam/ketcher/issues/5761) – Fix minimal distances for mult-tail validation in KET format
* [#5413](https://github.com/epam/ketcher/issues/5413) – Can't add specific SVG image to Canvas in Mozilla Firefox
* [#5434](https://github.com/epam/ketcher/issues/5434) – Document creation and behaviour of custom buttons
* [#5776](https://github.com/epam/ketcher/issues/5776) – Add API Method getRdf for retrieving RDF representation of structures
* [#5786](https://github.com/epam/ketcher/issues/5786) – Uncaught TypeError is in console when trying to move tail of Multi-Tailed Arrow added from KET with small size between tails
* [#5753](https://github.com/epam/ketcher/issues/5753) – Issue with moving of tail of Multi-Tailed arrow with several tails when user needs to move the tail close to another one
* [#5679](https://github.com/epam/ketcher/issues/5679) – Unable to establish connection between micro structure and macro ones
* [#5848](https://github.com/epam/ketcher/issues/5848) – Unable to establish connection between micro structure and sugar or phosphate (and partially - unresolved monomer)
* [#5703](https://github.com/epam/ketcher/issues/5703) – The picture is incorrect when image resolution high and bond thickness changing
* [#5685](https://github.com/epam/ketcher/issues/5685) – The diagonal bond in the molecule is displayed incorrect with ACS style
* [#5674](https://github.com/epam/ketcher/issues/5674) – Inconsistent behavior of copy-paste and cut-paste operations with macromolecule abbreviations
* [#5658](https://github.com/epam/ketcher/issues/5658) – Incorrect selection behavior when using Selection tool on Macromolecule abbreviations
* [#5699](https://github.com/epam/ketcher/issues/5699) – After bulk deletion of monomer abbreviations, Undo returns expanded monomers
* [#5836](https://github.com/epam/ketcher/issues/5836) – R-Group fragment labels font size doesn't defined by Sub Font size property at Settings
* [#5834](https://github.com/epam/ketcher/issues/5834) – S-Group (Data type) Field value label font size uses Settings - Font size property value instead of Sub font size one
* [#5833](https://github.com/epam/ketcher/issues/5833) – Importing functional groups (e.g. Boc, Bn, CF3) ignores drawing settings (e.g. ACS style)
* [#5809](https://github.com/epam/ketcher/issues/5809) – System opens wrong context menu for monomers on micro canvas if clicked on atom or bond
* [#5887](https://github.com/epam/ketcher/issues/5887) – After save and load a MOL V3000 file in macro and micro mode, bond connections are changed, and the microstructures are shifted
* [#5814](https://github.com/epam/ketcher/issues/5814) – On Remote environment, the reaction/molecule can't be saved to V3000 formats (returns V2000 instead): MOL, RXN, SDF, RDF
* [#5886](https://github.com/epam/ketcher/issues/5886) – Loading a KET file in macro mode, bond connections are preserved but microstructures are shifted
