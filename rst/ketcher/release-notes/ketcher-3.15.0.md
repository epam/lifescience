
# Ketcher 3.15.0

## What's Changed

### New features
- [#9118](https://github.com/epam/ketcher/issues/9118) – Update KET and SDF format to include information about preset phosphate position
- [#9129](https://github.com/epam/ketcher/issues/9129) – Allow 5' position of the phosphate in the monomer creation wizard
- [#9310](https://github.com/epam/ketcher/issues/9310) – Expand RNA Builder presets to support 5' phosphates using preset connections

### Bugfixes and improvements
- [#9358](https://github.com/epam/ketcher/issues/9358) – Rotation tool: A dashed bounding box disappears when the focus is moved outside of the browser window
- [#9368](https://github.com/epam/ketcher/issues/9368) – Rotation tool: Rotation handle does not change its view (color and icon) when rotation mode is activated
- [#5568](https://github.com/epam/ketcher/issues/5568) – The "magnet angle" is too large; drawing arrows ±15° of n·90° is impossible; to forbid one third of possible angles is too much.
- [#9377](https://github.com/epam/ketcher/issues/9377) – Right-click on monomer should not only open context menu but select monomer if it was right-clicked
- [#9374](https://github.com/epam/ketcher/issues/9374) – Rotation tool: Current rotation angle is not displayed at starting position in Macro mode
- [#9379](https://github.com/epam/ketcher/issues/9379) – `Arrange as a Ring` option in context menu should be visible only on Flex mode (Macromolecules canvas)
- [#9384](https://github.com/epam/ketcher/issues/9384) – The layout mode dropdown is overlapped
- [#9382](https://github.com/epam/ketcher/issues/9382) – Rotation tool: It is possible to move the rotation center when part of structure is selected
- [#9105](https://github.com/epam/ketcher/issues/9105) – The monomer is moved after pressing the "Submit" button for any type of monomer
- [#7240](https://github.com/epam/ketcher/issues/7240) – ABS label becomes detached from the structure after horizontal or vertical flip
- [#9407](https://github.com/epam/ketcher/issues/9407) – Labels for monomer natural analog category is missing if filter applied in Ketcher popup mode
- [#9060](https://github.com/epam/ketcher/issues/9060) – Search using some AxoLabs aliases fails
- [#9420](https://github.com/epam/ketcher/issues/9420) – System don't show Fullscreen/window mode in correct state if user switches mode being in fullscreen mode
- [#9102](https://github.com/epam/ketcher/issues/9102) – Incorrect selection a part of structure for phosphate when moving mouse from top to bottom
- [#8799](https://github.com/epam/ketcher/issues/8799) – Changing Implicit H count properties thru Atom properties dialog works wrong
- [#9143](https://github.com/epam/ketcher/issues/9143) – System removes bond between monomers if user removes abbreviation from them on molecules canvas
- [#9132](https://github.com/epam/ketcher/issues/9132) – The “Mark as a…” option is displayed after switching to another type in the Attributes panel
- [#8937](https://github.com/epam/ketcher/issues/8937) – Disable molecules/macromolecules switcher and settings when the monomer creation wizard is active
- [#9474](https://github.com/epam/ketcher/issues/9474) – AxoLabs alias is missing from library preset card preview tooltip and symbol preview tooltip on sequence canvas
- [#9141](https://github.com/epam/ketcher/issues/9141) – System removes atoms that holds unoccopied leaving groups if user removes abbreviation from monomer on molecules canvas
- [#9130](https://github.com/epam/ketcher/issues/9130) – It is not possible to save only the sugar and phosphate in the Nucleotide (preset) type
- [#6772](https://github.com/epam/ketcher/issues/6772) – SYNC mode button is absent if sense/antisense chain pasted from clipboard
- [#7021](https://github.com/epam/ketcher/issues/7021) – Monomer layout inside r-group box become corrupted if user grabs and moves bond between monomers
- [#6476](https://github.com/epam/ketcher/issues/6476) – Unable to paste using Ctrl+V chain from clipboard after clear canvas action
- [#9140](https://github.com/epam/ketcher/issues/9140) – The Structure selection after moving the entire Structure is incorrect.
- [#9460](https://github.com/epam/ketcher/issues/9460) – Implicit H count value doesn't change number of attached hydrogens if applied to canbon (C)
- [#9198](https://github.com/epam/ketcher/issues/9198) – Expand monomer on molecules canvas works wrong if monomer consists of one atom and one leaving group - shows empty structure
- [#9542](https://github.com/epam/ketcher/issues/9542) – Update the hint for preset components defining in the monomer creation wizard
- [#8960](https://github.com/epam/ketcher/issues/8960) – Number associated with symbol is visible
- [#8402](https://github.com/epam/ketcher/issues/8402) – Scrollbar appears unnecessarily in “Create Monomer” attributes panel after selecting Type, and disappears when expanding Aliases
- [#4248](https://github.com/epam/ketcher/issues/4248) – The “File format” drop-down does not open in the “Save Structure” window in the full-screen mode
- [#9590](https://github.com/epam/ketcher/issues/9590) – Fix vite server config error and remove warnings
- [#8394](https://github.com/epam/ketcher/issues/8394) – HELM (and IDT) alias collision should log error in console
- [#6616](https://github.com/epam/ketcher/issues/6616) – Hydrogen bond layouted in flex style on snake mode
- [#4675](https://github.com/epam/ketcher/issues/4675) – It is impossible to cut a structure from a canvas using Ctrl+X
- [#9455](https://github.com/epam/ketcher/issues/9455) – Nucleotide presets: Unable to create preset after adding and removing simple extensions – console error
- [#9123](https://github.com/epam/ketcher/issues/9123) – Monomers disappearing when expanding/collapsing in Molecules Mode after moving in Macromolecules Mode
- [#5198](https://github.com/epam/ketcher/issues/5198) – Added a darker hover state for selected sequence items in Sequence Layout Mode.
- [#6239](https://github.com/epam/ketcher/issues/6239) – Aromatic bond is mirrored if used as inside one on Macro canvas
- [#8818](https://github.com/epam/ketcher/issues/8818) – Add/Remove explicit hydrogens operation inside create monomer wizard causes exception: process is not defined
- [#7141](https://github.com/epam/ketcher/issues/7141) – System shows molecular mass and molecular formula even if few chains on the canvas
- [#4694](https://github.com/epam/ketcher/issues/4694) – Add Hotkeys in Macro Mode Similar to Micro Mode
- [#8142](https://github.com/epam/ketcher/issues/8142) – System allow to load monomers with invalid HELM aliases
- [#6851](https://github.com/epam/ketcher/issues/6851) – Bond to C10H20 superatom rendered wrong if loaded from CDXML
- [#9617](https://github.com/epam/ketcher/issues/9617) – Correct the LGA of meK and meE amino-acids
- [#9336](https://github.com/epam/ketcher/issues/9336) – Update the help document (3.14.)
- [#9645](https://github.com/epam/ketcher/issues/9645) – Migrate to Indigo v1.43.0 in-browser module
- [#9774](https://github.com/epam/ketcher/issues/9774) – Change the structure and the name of Gly-ol amino-acid
- [#9828](https://github.com/epam/ketcher/issues/9828) – Copy functionality is broken on Chrome

---

### Additional notes:
- Ketcher 3.15.0 has been built and tested with Indigo version 1.43 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.43.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.43.0/images/sha256-374b57a621eb2a6ddd9332f472d008079ddccfa0a56c8762b6b7080cb965f565)).
