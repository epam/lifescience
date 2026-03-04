
# Ketcher 3.10.0

## What's Changed

### New features
- [#7500](https://github.com/epam/ketcher/issues/7500) – Update the monomer preview
- [#7633](https://github.com/epam/ketcher/issues/7633) – Allow for setting of modification type in the monomer creation wizard
- [#7932](https://github.com/epam/ketcher/issues/7932) – Add warning messages to the monomer creation wizard in case of unusual leaving group atoms
- [#7928](https://github.com/epam/ketcher/issues/7928) – Allow for setting of HELM alias in the monomer creation wizard
- [#8200](https://github.com/epam/ketcher/issues/8200) – Add parameter to Editor to disable saving new monomers to local storage
- [#8281](https://github.com/epam/ketcher/issues/8281) – Adjust subscription to library update event of Ketcher API
- [#7905](https://github.com/epam/ketcher/issues/7905) – Selection logic change and toolbar icons enabling for the monomer creation wizard
- [#7970](https://github.com/epam/ketcher/issues/7970) – Include 'Create cyclic structure' option in the context menu for Flex mode

### Bugfixes and improvements
- [#8602](https://github.com/epam/ketcher/issues/8602) – Migrate to Indigo v1.38.0 in-browser module
- [#7971](https://github.com/epam/ketcher/issues/7971) – Update the help document (3.9.)
- [#7887](https://github.com/epam/ketcher/issues/7887) – Molecule rotation causes error in console: Uncaught TypeError: Cannot read properties of undefined (reading 'pp')
- [#4467](https://github.com/epam/ketcher/issues/4467) – Ket label should be renamed to Ket Format
- [#7746](https://github.com/epam/ketcher/issues/7746) – System replace few spaces in monomer name to one space on monomer preview
- [#7421](https://github.com/epam/ketcher/issues/7421) – "Ghost image" of CHEM is white (different from "ghost image" of other monomer types)
- [#7740](https://github.com/epam/ketcher/issues/7740) – System should not allow to fill Symbol and Name fields if Type is not selected on Monomer creation wizard
- [#3742](https://github.com/epam/ketcher/issues/3742) – Wrong tooltip for "minimize window" button (shows "expand window")
- [#7373](https://github.com/epam/ketcher/issues/7373) – "Grabbing hand" mouse cursor is absent on grabbing monomers from the library
- [#5570](https://github.com/epam/ketcher/issues/5570) – PNG and SVG exported images should be identical to how the canvas looks like in case of Chiral label
- [#8294](https://github.com/epam/ketcher/issues/8294) – Do allow to collapse s-groups (superatom type) without name
- [#7936](https://github.com/epam/ketcher/issues/7936) – Add tooltips to some attachment points in the monomer creation wizard
- [#7997](https://github.com/epam/ketcher/issues/7997) – For non-potential-AAs the related context menu option (Mark as connection point,) should be disabled
- [#8328](https://github.com/epam/ketcher/issues/8328) – Modification drop-down list is not ordered as required (Natural Amino Acid first, others alphabetically)
- [#8377](https://github.com/epam/ketcher/issues/8377) – Add data-topology and data-reacting-center attributes for bonds
- [#7553](https://github.com/epam/ketcher/issues/7553) – Dropdown for switching between Macro and Micro modes does not appear in fullscreen mode
- [#5520](https://github.com/epam/ketcher/issues/5520) – Percentages for mixed bases ain't sorted from biggest to smallest in tooltip
- [#8414](https://github.com/epam/ketcher/issues/8414) – System should throw The following string cannot be interpreted as an AxoLabs string. error if symbols without brackets cannot be interpreted
- [#8039](https://github.com/epam/ketcher/issues/8039) – Ketcher doesn't send input_format parameter to Indigo in case of AxoLab load request
- [#8418](https://github.com/epam/ketcher/issues/8418) – All monomers from SDF loaded via updateMonomersLibrary appear in Base group instead of their correct classes
- [#8404](https://github.com/epam/ketcher/issues/8404) – No documentation for libraryUpdate event subscription
- [#8463](https://github.com/epam/ketcher/issues/8463) – Batch monomer import aborts on a single invalid entry and does not indicate which record failed Standalone mode
- [#8599](https://github.com/epam/ketcher/issues/8599) – Correct the stereo-bonds of sugars

---

### Additional notes:
- Ketcher 3.10.0 has been built and tested with Indigo version 1.38 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.38.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.38.0/images/sha256-40d4d9d732606381a5a3bc9ae5e5ed94a0a948c6e6460e33278285d3d2e71d4a)).
