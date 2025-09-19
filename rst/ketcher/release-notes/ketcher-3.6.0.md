
# Ketcher 3.6.0

## What's Changed

### New features
- [#6404](https://github.com/epam/ketcher/issues/6404) – Drag and drop for the library elements in macromolecules mode
- [#7164](https://github.com/epam/ketcher/issues/7164) – Introduce marking of nucleotide components
- [#7125](https://github.com/epam/ketcher/issues/7125) – Support for reaction arrows and reaction pluses in macromolecules mode
- [#7132](https://github.com/epam/ketcher/issues/7132) – Update and add icons to right-click drop-down menus in all modes
- [#7347](https://github.com/epam/ketcher/issues/7347) – Migrate to Indigo v1.34.0 in-browser module

### Bugfixes and improvements
- [#7231](https://github.com/epam/ketcher/issues/7231) – Update the help document (3.5)
- [#7073](https://github.com/epam/ketcher/issues/7073) – Unable to create hydrogen bond: Uncaught RangeError: Maximum call stack size exceeded
- [#7178](https://github.com/epam/ketcher/issues/7178) – The tooltip appears behind the context menu options
- [#7187](https://github.com/epam/ketcher/issues/7187) – IDT code shown wrong for SS3 chem
- [#6410](https://github.com/epam/ketcher/issues/6410) – Incorrect bond attachment to micro molecules in Macro Mode
- [#7277](https://github.com/epam/ketcher/issues/7277) – Cannot open multiple instance of Ketcher in one window
- [#6986](https://github.com/epam/ketcher/issues/6986) – Context menu appears on both canvas in molecules mode for several Ketcher instances on same page
- [#7207](https://github.com/epam/ketcher/issues/7207) – Rectangular input field should be wide enough to fit any (at least 4) digit number
- [#7117](https://github.com/epam/ketcher/issues/7117) – Chemical elements disappear when attempting to Expand the Structure in Micro mode after selecting one in Macro mode
- [#7170](https://github.com/epam/ketcher/issues/7170) – Monomer tooltip appears and remain in place even if mouse cursor moved away
- [#7209](https://github.com/epam/ketcher/issues/7209) – The ruler is limited to 190 divisions
- [#7365](https://github.com/epam/ketcher/issues/7365) – Console errors appear when using actions on structures with nucleotide component marking
- [#7386](https://github.com/epam/ketcher/issues/7386) – Delete operation causes exception: Uncaught (in promise) Error: Minified Redux error
- [#7432](https://github.com/epam/ketcher/issues/7432) – Security: form-data uses unsafe random function in form-data for choosing boundary
- [#7371](https://github.com/epam/ketcher/issues/7371) – Mouse cursor doesn't positioned at the top left corner of preset

---

### Additional notes:
- Ketcher 3.6.0 has been built and tested with Indigo version 1.34 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.34.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.34.0-rc.1/images/sha256-74b6c7d6d5ce454bdf0bbebd5e032e991155434ba6d2ddbf7b589b5d777291a1)).
