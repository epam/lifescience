
# Ketcher 3.9.0

## What's Changed

### New features
- [#7690](https://github.com/epam/ketcher/issues/7690) – Allow for modification of the structure in the monomer creation wizard
- [#7730](https://github.com/epam/ketcher/issues/7730) – Continuation of attachment points editing in the monomer creation wizard
- [#7748](https://github.com/epam/ketcher/issues/7748) – AxoLabs format support
- [#7674](https://github.com/epam/ketcher/issues/7674) – Add ability to update monomers library API in SDF format
- [#7560](https://github.com/epam/ketcher/issues/7560) – Improving snake layout logic to include small molecules
- [#7709](https://github.com/epam/ketcher/issues/7709) – Update the help document (3.8.)
- [#8270](https://github.com/epam/ketcher/issues/8270) – Migrate to Indigo v1.37.0 in-browser module

### Bugfixes and improvements
- [#7572](https://github.com/epam/ketcher/issues/7572) – "Create a monomer" option is missing in right-click menu when selection meets conditions
- [#7443](https://github.com/epam/ketcher/issues/7443) – Save to SDF button is missed on Salts and Solvents tab in Structure Library dialog
- [#7359](https://github.com/epam/ketcher/issues/7359) – Stereochemistry dialog crashes Ketcher if only one stereo bond on the canvas
- [#7697](https://github.com/epam/ketcher/issues/7697) – IDT alias of CHEM 5TAMRA is displayed wrong
- [#7919](https://github.com/epam/ketcher/issues/7919) – Change the symbol of CHEM Cy5.5 dye
- [#5417](https://github.com/epam/ketcher/issues/5417) – IDT aliases not shown at preview tooltip at Monomer Library
- [#5202](https://github.com/epam/ketcher/issues/5202) – Update visuals in Right-click context menu
- [#7395](https://github.com/epam/ketcher/issues/7395) – Line between Paste option and Create RNA antisense strand option is missing in the context menu
- [#7364](https://github.com/epam/ketcher/issues/7364) – Gap between icon and Delete label is twice bigger than it should be in Molecules mode
- [#7327](https://github.com/epam/ketcher/issues/7327) – Missing separator line above "Delete" in context menu
- [#7256](https://github.com/epam/ketcher/issues/7256) – Ketcher losts aliasHELM property for unknown monomers that makes export to HELM incorrect
- [#7912](https://github.com/epam/ketcher/issues/7912) – Errors in console in dev mode "Cannot update a component"
- [#7770](https://github.com/epam/ketcher/issues/7770) – Pressing Right Scroll Arrow button of top menu cause exception to console
- [#7700](https://github.com/epam/ketcher/issues/7700) – System allow to delete monomers leaving connected bonds on the canvas
- [#7934](https://github.com/epam/ketcher/issues/7934) – Export to SVG Documets works wrong for unsplite nucleotides with dash symbole (-) in alias
- [#7649](https://github.com/epam/ketcher/issues/7649) – Undo/redo works wrong for monomer reposition corrected by snapping
- [#7783](https://github.com/epam/ketcher/issues/7783) – Microstructure disappears from canvas in Sequence mode when adding new sequence row
- [#7918](https://github.com/epam/ketcher/issues/7918) – Change the IDT alias format in the library file and adjust the logic for IDT aliases on preview
- [#7581](https://github.com/epam/ketcher/issues/7581) – Undo/Redo buttons become inactive and canvas Up, Bottom, Left and Right toolbars remain active inside Monomer Wizard
- [#7893](https://github.com/epam/ketcher/issues/7893) – System shouldn't allow to create monomers for selection with aromatic bonds to non-selected part
- [#7923](https://github.com/epam/ketcher/issues/7923) – Undo after deleting RNA preset connected to benzene ring leaves undeletable artifacts in Flex, Snake, and Sequence modes
- [#7914](https://github.com/epam/ketcher/issues/7914) – Microstructure not removed properly with Redo, duplicates on repeated Undo/Redo in Sequence mode
- [#7978](https://github.com/epam/ketcher/issues/7978) – Create monomer process changes atom of not related part of the molecule
- [#7979](https://github.com/epam/ketcher/issues/7979) – Pressing right Command key on Mac causes errors in DevTool Console (left Command works fine)
- [#8000](https://github.com/epam/ketcher/issues/8000) – Monomer Wizard allows creation of monomer with Functional Group
- [#8002](https://github.com/epam/ketcher/issues/8002) – No validation message shown for minimal monomer structure in Monomer Wizard
- [#8005](https://github.com/epam/ketcher/issues/8005) – Changing name for attachment points works wrong
- [#8040](https://github.com/epam/ketcher/issues/8040) – R2 attachment point is missing for vinU monomer
- [#8041](https://github.com/epam/ketcher/issues/8041) – System loads invdC monomer as unresolved monomer from AxoLabs
- [#8067](https://github.com/epam/ketcher/issues/8067) – Do not save added or updated monomer in local storage
- [#8068](https://github.com/epam/ketcher/issues/8068) – Unable to update monomer library via API on Remote Ketcher – input format error
- [#8070](https://github.com/epam/ketcher/issues/8070) – Existing Presets in the library disappear after adding new preset via API
- [#8123](https://github.com/epam/ketcher/issues/8123) – HELM (and IDT) alias collision is possible after library update
- [#8296](https://github.com/epam/ketcher/issues/8296) – Create Monomer tool can not be hidden by toolbar buttons config

---

### Additional notes:
- Ketcher 3.9.0 has been built and tested with Indigo version 1.37 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.37.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.37.0/images/sha256-51e95fc6d5f2efafc921c5804ff54bbb846c2b4a4739e9419e4a2ef7471d01ef)).
