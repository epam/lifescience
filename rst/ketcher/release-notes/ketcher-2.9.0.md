# Ketcher 2.9.0

## What's changed

This release includes several bug fixes, improvements, and new features. Please be aware Ketcher 2.9.0 has been tested with Indigo version 1.10.0 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.10.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.10.0/images/sha256-3f1a4b09488243ff1e64b73b4fa3ef84e8ebbac61cd1a958808376be2afa219f?context=explore)).
Notably, the following changes have been made:

## Features
[#1996](https://github.com/epam/ketcher/issues/1996) – The bond context menu now has the ability to attach or edit s groups. Additionally, when a Data S-Group or S-Group is selected, right-clicking on an atom or bond will open the S-Group Properties window.
[#2192](https://github.com/epam/ketcher/issues/2192) – The canvas will now automatically expand when moving the structure off the page.
[#2329](https://github.com/epam/ketcher/issues/2329) – Unknown super-atoms can now be expanded and collapsed.
[#2005](https://github.com/epam/ketcher/issues/2005) – CDX export has been added to the output formats list.
[#2161](https://github.com/epam/ketcher/issues/2161) – The ignore-chiral-flag parameter has been added to ketcher settings.

## Bug Fixes

[#2135](https://github.com/epam/ketcher/issues/2135) – Functional groups can now be merged into nearby structures.
[#2169](https://github.com/epam/ketcher/issues/2169) – A warning in the console that occurred when the About icon was clicked has been fixed.
[#2033](https://github.com/epam/ketcher/issues/2033) – Atoms now properly protrude beyond the expanded view in Abbreviations.
[#2026](https://github.com/epam/ketcher/issues/2026) – The erase tool's hotkey (Del) can now delete arrows and plus signs.
[#1456](https://github.com/epam/ketcher/issues/1456) – The selected file format in the Save Structure window now matches the mockup.
[#2110](https://github.com/epam/ketcher/issues/2110) – The incorrect merging of functional groups has been fixed.
[#2257](https://github.com/epam/ketcher/issues/2257) – It is now possible to add a bond to a Function Group.
[#2247](https://github.com/epam/ketcher/issues/2247) – Clicking outside of a context menu doesn't apply the currently selected tool.
[#2216](https://github.com/epam/ketcher/issues/2216) – The S-Group pop-up tool tip is no longer positioned so that it overlaps the structure.
[#2123](https://github.com/epam/ketcher/issues/2123) – The hover effect now appears after clicking on bonds or atoms.
[#1954](https://github.com/epam/ketcher/issues/1954) – The selected structure now draws at the mouse cursor after closing the Templates window.
[#2330](https://github.com/epam/ketcher/issues/2330) – Atom editing via the right-click menu is now applied.
[#2316](https://github.com/epam/ketcher/issues/2316) – When hovering over the label R/S, the Indigo system information is not visible.
## Improvements
* [#2093](https://github.com/epam/ketcher/issues/2093) – The s group menus have been combined, and the generic s group has been removed.
* [#1681](https://github.com/epam/ketcher/issues/1681) – React has been upgraded to version 18, and react-contextmenu has been replaced with react-contexify.
* [#1456](https://github.com/epam/ketcher/issues/1456) – The design of the Save Structure Select has been fixed.
* [#2241](https://github.com/epam/ketcher/issues/2241) – The Template window will now open with the previously opened tab.
* [#1990](https://github.com/epam/ketcher/issues/1990) – Functional groups now connect with another functional group on click-and-drag.
* [#2173](https://github.com/epam/ketcher/issues/2173) – The font size drop-down now collapses.
* [#2255](https://github.com/epam/ketcher/issues/2255) – The in-browser module has been migrated to Indigo v1.10.0-rc.4.
* [#1886](https://github.com/epam/ketcher/issues/1886) – The keyboard shortcuts for atoms, bonds, zoom, and functions have been changed.

## Other Changes
Update bug_report.md - add test case field
[#2319](https://github.com/epam/ketcher/issues/2319) – A previous change that caused an inability to add a bond to a Function Group has been reverted.
[#2321](https://github.com/epam/ketcher/issues/2321) – Indigo v1.10.0-rc.4 has been migrated to the in-browser module.
[#2341](https://github.com/epam/ketcher/issues/2341) – The help.md page has been updated to reflect keyboard shortcut changes.

## New Contributors
* @d-mrzv made their first contribution in https://github.com/epam/ketcher/pull/2252

**Full Changelog**: https://github.com/epam/ketcher/compare/v2.8.0...v2.9.0