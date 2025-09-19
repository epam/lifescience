
# Ketcher 3.7.0

## What's Changed

### New features
- [#6552](https://github.com/epam/ketcher/issues/6552) – Create a monomer from a selected part of the structure
- [#6785](https://github.com/epam/ketcher/issues/6785) – Support aliases from HELM
- [#3253](https://github.com/epam/ketcher/issues/3253) – Introduce the arrow button on library cards for easy monomer/preset addition to canvas
- [#7430](https://github.com/epam/ketcher/issues/7430) – Adjust sgroup hover rendering to remove overlapping parts
- [#6150](https://github.com/epam/ketcher/issues/6150) – Add the star atom to the special nodes section of the extended table
- [#7535](https://github.com/epam/ketcher/issues/7535) – Add api for switching between macromolecules and molecules modes
- [#7660](https://github.com/epam/ketcher/issues/7660) – Migrate to Indigo v1.35.0 in-browser module

### Bugfixes and improvements
- [#7377](https://github.com/epam/ketcher/issues/7377) – Update the help document (3.6.)
- [#7351](https://github.com/epam/ketcher/issues/7351) – Profiling and optimization for many monomers on molecules canvas
- [#6270](https://github.com/epam/ketcher/issues/6270) – Add "About" (i) and "Help" (?) buttons to the main toolbar in macromolecules mode
- [#7222](https://github.com/epam/ketcher/issues/7222) – Incorrect leaving group atoms for expanded monomers
- [#7168](https://github.com/epam/ketcher/issues/7168) – Opening the 3D Templates section in Structure Library causes multiple errors in the DevTools console
- [#7252](https://github.com/epam/ketcher/issues/7252) – Integrate with SonarQube
- [#7273](https://github.com/epam/ketcher/issues/7273) – System loads micro-macro connected structure on snake canvas and created understandable bond
- [#7283](https://github.com/epam/ketcher/issues/7283) – Context menu is wrong if clicked on top of sequence
- [#7205](https://github.com/epam/ketcher/issues/7205) – Layout shift when changing mode from sequence to flex and back upon first macromolecules mode initialization
- [#7245](https://github.com/epam/ketcher/issues/7245) – Missing tooltip for standalone input field in ruler control
- [#7440](https://github.com/epam/ketcher/issues/7440) – Area selection doesn't work till bond/atom reposition
- [#7381](https://github.com/epam/ketcher/issues/7381) – Create documentation for 'change' event subscription
- [#7152](https://github.com/epam/ketcher/issues/7152) – Copy keyboard shortcut works wrong for text content
- [#7423](https://github.com/epam/ketcher/issues/7423) – It is possible to drag monomer from library and drop it to sequence canvas
- [#7512](https://github.com/epam/ketcher/issues/7512) – Library doesn't fit view port in Sequence mode in Popup mode
- [#7513](https://github.com/epam/ketcher/issues/7513) – "Ghost image" doesn't positioned below mouse cursor if dragged from Library to canvas in popup mode
- [#7531](https://github.com/epam/ketcher/issues/7531) – Arrow icon appears in Sequence mode, violating requirement for Snake and Flex modes only
- [#7538](https://github.com/epam/ketcher/issues/7538) – Unable to add ambiguous monomers via arrow button - no preview and errors in console
- [#7539](https://github.com/epam/ketcher/issues/7539) – No tooltip shown and invalid attachment allowed when adding a monomer without R1 to selected monomer with free R2
- [#7548](https://github.com/epam/ketcher/issues/7548) – Tooltip not shown and addition allowed when multiple monomers with free R2 are selected
- [#7551](https://github.com/epam/ketcher/issues/7551) – Monomer drag-n-drop from Library to the canvas doesn't work for peptides it they were clicked on Sequence canvas
- [#7562](https://github.com/epam/ketcher/issues/7562) – Tooltip overlaps monomers when hovering over arrow button on monomer card
- [#7575](https://github.com/epam/ketcher/issues/7575) – Monomer creation wizard opens despite selection being connected via non simple bond
- [#7576](https://github.com/epam/ketcher/issues/7576) – Create monomer wizard is available for structures containing S-groups, R-groups, or extended table atoms
- [#7577](https://github.com/epam/ketcher/issues/7577) – "Create a monomer" button becomes active for disconnected structures
- [#7563](https://github.com/epam/ketcher/issues/7563) – Selection after chain/monomer addition (autochain improvement)
- [#7580](https://github.com/epam/ketcher/issues/7580) – Zoom actions in Monomer Wizard throw errors in the console
- [#7601](https://github.com/epam/ketcher/issues/7601) – Wizard allows editing atoms and bonds via right-click menu without showing an error
- [#7604](https://github.com/epam/ketcher/issues/7604) – Name, Symbol, Natural analogue input fields are not highlighted when left empty and Submit is clicked in Monomer Wizard
- [#7606](https://github.com/epam/ketcher/issues/7606) – Pasting text into Symbol or Name fields in Monomer Wizard triggers unrelated "Convert error"
- [#7607](https://github.com/epam/ketcher/issues/7607) – Missing S-group name in KET after saving a monomer via the wizard
- [#7609](https://github.com/epam/ketcher/issues/7609) – Symbol uniqueness validation is missing in Monomer Wizard (no error, no highlight)
- [#7612](https://github.com/epam/ketcher/issues/7612) – Natural analogue is not cleared when monomer type changes
- [#7614](https://github.com/epam/ketcher/issues/7614) – After creating a monomer via wizard, switching to macro mode shows two separate entities instead of one
- [#7615](https://github.com/epam/ketcher/issues/7615) – Phantom structure remains on canvas after closing wizard and is visible in exported files
- [#7620](https://github.com/epam/ketcher/issues/7620) – Creating a monomer from a partial benzene selection causes console errors and no hover highlight on created region
- [#7624](https://github.com/epam/ketcher/issues/7624) – Created Sugars and Phosphates via wizard are not added to Macro library
- [#7625](https://github.com/epam/ketcher/issues/7625) – No validation against existing monomers - newly created monomer with duplicate name overwrites the existing one in the library
- [#7627](https://github.com/epam/ketcher/issues/7627) – Selection tools stop working after creating first monomer via wizard when many structures are on canvas
- [#7629](https://github.com/epam/ketcher/issues/7629) – API does not implement library change subscription
- [#7684](https://github.com/epam/ketcher/issues/7684) – Only selected atoms connected with bonds should be taken into account on monomer creation
- [#7714](https://github.com/epam/ketcher/issues/7714) – System shouldn't allow to create monomer for selected structure that have any non-simple single bonds to non-selected parts of the structure
- [#7692](https://github.com/epam/ketcher/issues/7692) – System shouldn't allow to create monomer for molecules with R-Groups attachment points
- [#7691](https://github.com/epam/ketcher/issues/7691) – System shouldn't allow to create monomer for molecules with R-Groups
- [#7725](https://github.com/epam/ketcher/issues/7725) – Hand tool and Area Selection Tool buttons close Monomer creation wizard if pressed
- [#7722](https://github.com/epam/ketcher/issues/7722) – Connection preview does not follow cursor and AP to AP connection is not possible
- [#6581](https://github.com/epam/ketcher/issues/6581) – Monomer placement offset from cursor when Ketcher runs in a popup with increased browser zoom

---

### Additional notes:
- Ketcher 3.7.0 has been built and tested with Indigo version 1.35 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.35.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.35.0/images/sha256-4c6730c0c6cce76af968317ceecb8b2501a1fefc81211e0ddf881fb58250d9a0)).
