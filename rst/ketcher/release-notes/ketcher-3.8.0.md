
# Ketcher 3.8.0

## What's Changed

### New features
- [#6287](https://github.com/epam/ketcher/issues/6287) – Expanding the snap functionality to monomer groups inside of a structure
- [#7441](https://github.com/epam/ketcher/issues/7441) – Allow for modification of the attachment points in the monomer creation wizard
- [#6657](https://github.com/epam/ketcher/issues/6657) – Bump react to ^19.0.0 in ketcher-react package
- [#6358](https://github.com/epam/ketcher/issues/6358) – Add lasso selection/fragment selection tool in macromolecules mode
- [#7554](https://github.com/epam/ketcher/issues/7554) – Correct existing and add new structures to the library with appropriate IDT codes
- [#7221](https://github.com/epam/ketcher/issues/7221) – Change the colour of nucleobases
- [#7384](https://github.com/epam/ketcher/issues/7384) – Create documentation for hiding toolbar buttons
- [#7505](https://github.com/epam/ketcher/issues/7505) – Update the help document (3.7.)
- [#7760](https://github.com/epam/ketcher/issues/7760) – Migrate to Indigo v1.36.0 in-browser module

### Bugfixes and improvements
- [#7222](https://github.com/epam/ketcher/issues/7222) – Incorrect leaving group atoms for expanded monomers
- [#6993](https://github.com/epam/ketcher/issues/6993) – Atoms and "monomer to atom bonds" are not removed when all other bonds are removed from atom
- [#7619](https://github.com/epam/ketcher/issues/7619) – Pressing ? key at Text Editor form while creation text label opens Macromolecules help link
- [#7525](https://github.com/epam/ketcher/issues/7525) – Specify a target origin for this message. vulnerability
- [#6747](https://github.com/epam/ketcher/issues/6747) – Unnecessary leaving groups (R-groups) appear upon "Removing Abbreviation" of expanded monomer when an attachment point is occupied
- [#7571](https://github.com/epam/ketcher/issues/7571) – Ctrl+M does not open monomer creation wizard when selection meets conditions
- [#7683](https://github.com/epam/ketcher/issues/7683) – Remove Add attachment point functionality
- [#7578](https://github.com/epam/ketcher/issues/7578) – Undo/Redo restores partial selection after cancelling monomer creation
- [#7509](https://github.com/epam/ketcher/issues/7509) – Export to SVG doesn't work in Ketcher mode
- [#7788](https://github.com/epam/ketcher/issues/7788) – Tooltip and restriction not triggered when selecting monomer without R2 in Macro mode
- [#7794](https://github.com/epam/ketcher/issues/7794) – Selection remains on original structure after creating Antisense RNA/DNA and cannot be cleared by canvas click
- [#7782](https://github.com/epam/ketcher/issues/7782) – In Macro mode selection tool resets to Rectangle when switching between Flex, Snake, and Sequence modes
- [#7791](https://github.com/epam/ketcher/issues/7791) – Highlight is not secured for clicked r label in monomer creation wizard
- [#7152](https://github.com/epam/ketcher/issues/7152) – Copy keyboard shortcut works wrong for text content
- [#7837](https://github.com/epam/ketcher/issues/7837) – Unable to create monomer if molecule loaded from KET
- [#7846](https://github.com/epam/ketcher/issues/7846) – Connection between created monomer and the rest of molecule got lost after monomer creation
- [#7814](https://github.com/epam/ketcher/issues/7814) – Connection point enumeration is wrong if they are already enumerated form range [3-8]
- [#7688](https://github.com/epam/ketcher/issues/7688) – Attached groups are lost when saving and reopening monomer created via Monomer Wizard in KET format
- [#7828](https://github.com/epam/ketcher/issues/7828) – Unable to assign atom as a leaving group event if it is eligable
- [#7806](https://github.com/epam/ketcher/issues/7806) – Problematic points are not highlighted in red when validation is failed
- [#7877](https://github.com/epam/ketcher/issues/7877) – Ketcher losts attachment point name on loading s-group from mol v3000
- [#7786](https://github.com/epam/ketcher/issues/7786) – In Snake mode after Undo bonds remain on canvas and cause console errors
- [#7777](https://github.com/epam/ketcher/issues/7777) – Incorrect shortcut displayed for selection tools in Macro mode
- [#7854](https://github.com/epam/ketcher/issues/7854) – Ketcher api doesn't work in proper order
- [#7785](https://github.com/epam/ketcher/issues/7785) – Clicking toolbar buttons resets selection tool from Lasso/Fragment to Rectangle
- [#7784](https://github.com/epam/ketcher/issues/7784) – In Sequence mode selection tool resets to Rectangle when entering or exiting sequence edit mode
- [#7850](https://github.com/epam/ketcher/issues/7850) – System doesn't add the leaving group atom (a hydrogen) by default at the end of the bond connecting the attachment atom and the non-selected part of the structure
- [#7807](https://github.com/epam/ketcher/issues/7807) – Selection of cyclic molecule causes application crash: Uncaught ReferenceError: process is not defined
- [#7817](https://github.com/epam/ketcher/issues/7817) – Connection point enumeration is wrong R-groups outside [1-8] range
- [#7838](https://github.com/epam/ketcher/issues/7838) – The leaving group atom (a hydrogen) is not added by default at the end of the bond
- [#7821](https://github.com/epam/ketcher/issues/7821) – Connection point enumeration is wrong R-groups outside [3-8] range
- [#7813](https://github.com/epam/ketcher/issues/7813) – System should not allow to create monomer if atom with many R-groups in the selection
- [#7815](https://github.com/epam/ketcher/issues/7815) – System changes right connection point (R2) to left one (R1) if no R1 group defined
- [#7816](https://github.com/epam/ketcher/issues/7816) – System swaps left connection point (R2) and right connection point (R1) if R2 group was created early that R1
- [#7606](https://github.com/epam/ketcher/issues/7606) – Pasting text into Symbol or Name fields in Monomer Wizard triggers unrelated "Convert error"
- [#7801](https://github.com/epam/ketcher/issues/7801) – Incorrect edit dialog behaviour when right-clicking on attachment atom
- [#7798](https://github.com/epam/ketcher/issues/7798) – Atom label is not correct in attributes panel for leaving atoms different from hydrogen
- [#7804](https://github.com/epam/ketcher/issues/7804) – Incorrect atom label upon monomer saving when removing automatically assigned attachment point via R-group

---

### Additional notes:
- Ketcher 3.8.0 has been built and tested with Indigo version 1.36 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.36.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.36.0/images/sha256-a9f6b7cea8e465f097cc36d0dc088a54040439aedbb7ee33da301ae796463344)).
