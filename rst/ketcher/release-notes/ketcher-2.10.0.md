
# Ketcher 2.10.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

* [#2273](https://github.com/epam/ketcher/issues/2273) - When the user selects and moves an atom on a Functional Group or Salt, it doesn't replace the atom in the structure.
* [#2113](https://github.com/epam/ketcher/issues/2113) - The hovered structure now gets saved in the molecule.
* [#2062](https://github.com/epam/ketcher/issues/2062) - RXN v2000: Detection of molecule above/below arrow as reagent doesn't work.
* [#2362](https://github.com/epam/ketcher/issues/2362) - Removed the appearance of a tooltip under the mouse cursor for Functional Groups/Salts and Solvents abbreviations.
* [#2403](https://github.com/epam/ketcher/issues/2403) - Fixed wrong tooltip and label in 'Extended Table'.
* [#2421](https://github.com/epam/ketcher/issues/2421) - Added locators and/or functions for tools sub-menus.
* [#2029](https://github.com/epam/ketcher/issues/2029) - Completely replaced yarn with npm commands throughout the project.
* [#2355](https://github.com/epam/ketcher/issues/2355) - Added DisableQueryElements parameter to disable query elements from the extended table.
* [#2246](https://github.com/epam/ketcher/issues/2246) - Multiple bond editing now correctly changes bond types for all selected bonds.
* [#2425](https://github.com/epam/ketcher/issues/2425) - The cancel button now correctly reverses adding a template to expanded and contracted functional group main.
* [#2446](https://github.com/epam/ketcher/issues/2446) - Structures are no longer drawn outside the viewbox when changing rendering options.
* [#2427](https://github.com/epam/ketcher/issues/2427) - When moving a structure outside of the canvas, the structure now moves smoothly.
* [#2353](https://github.com/epam/ketcher/issues/2353) - The CTRL+SHIFT+0 hotkey now works for 'Zoom 100%'.
* [#2402](https://github.com/epam/ketcher/issues/2402) - The atom under the mouse cursor no longer freezes on the canvas if you move the cursor away from the dragged atom.
* [#1855](https://github.com/epam/ketcher/issues/1855) - Benzene rings are now fused rings connection without valence errors.
* [#2456](https://github.com/epam/ketcher/issues/2456) - Updated KET json schema to support explicit implicit hydrogens.
* [#2441](https://github.com/epam/ketcher/issues/2441) - Added a warning message about localStorage to the templates window.
* [#2052](https://github.com/epam/ketcher/issues/2052) - Expanded and collapsed unknown super atoms properly.
* [#2482](https://github.com/epam/ketcher/issues/2482) - Ketcher with iFrame now loads without scrollbars activated.
* [#2442](https://github.com/epam/ketcher/issues/2442) - When hovering over an atom or bond, the hotkey CTRL+Z (Undo) now works.
* [#2420](https://github.com/epam/ketcher/issues/2420) - The hotkey (Del) can now delete Functional Groups and Salts abbreviations.
* [#2454](https://github.com/epam/ketcher/issues/2454) - After clicking the undo button, the edit abbreviation popup now appears.
* [#2245](https://github.com/epam/ketcher/issues/2245) - Settings: 'Terminal and Hetero' is now selected as default, and the 'on' option is now working.
* [#225](https://github.com/epam/ketcher/issues/225) - Added support for stereo cip values in ket format.
* [#2458](https://github.com/epam/ketcher/issues/2458) - Migrated to Indigo v1.11.0-rc.1 in-browser module.
* [#2257](https://github.com/epam/ketcher/issues/2257) - Users can now add a bond to a functional group using the bond tool.
* [#1865](https://github.com/epam/ketcher/issues/1865) - Extended SMILES saved from Ketcher might be invalid for RDKit.
* [#2516](https://github.com/epam/ketcher/issues/2516) - When creating a Superatom, part of the structure no longer disappears.
* [#2528](https://github.com/epam/ketcher/issues/2528) - The erase tool now completely removes the Functional Groups if selected via the hotkey CTRL + A.
* [#2530](https://github.com/epam/ketcher/issues/2530) - Tooltip for created Data S-Group now appears after hover on it.
* [#2113](https://github.com/epam/ketcher/issues/2113) - The hovered structure no longer gets into the saved molecule.
* [#2420](https://github.com/epam/ketcher/issues/2420) - The hotkey (Del) can now delete Functional Groups and Salts abbreviations.
* [#2548](https://github.com/epam/ketcher/issues/2548) - If the name of a Superatom matches an abbreviation in Custom Templates, then a tooltip is shown on hover.
* [#2517](https://github.com/epam/ketcher/issues/2517) - A file with Superatom now opens without missing part of the structure.
* [#2273](https://github.com/epam/ketcher/issues/2273) - When the user selects and moves an atom on a Functional Group or Salt, it now replaces the atom in the structure.
* [#2585](https://github.com/epam/ketcher/issues/2585) - Changed the behavior of "Show hydrogen labels" setting so that the "on" value works the same way as "terminal and hetero".
* [#2614](https://github.com/epam/ketcher/issues/2614) - Contracted unknown superatom is now parsed as expanded, and brackets with name are no longer lost.
* [#2636](https://github.com/epam/ketcher/issues/2636) - Users can now contract or expand Unknown Superatoms that are parsed via API in MolV3000, KET, CDX, CDXML, CML, Base64CDX formats.
* [#2656](https://github.com/epam/ketcher/issues/2656) - After opening or pasting an unknown superatom onto the canvas, it is now interactive.