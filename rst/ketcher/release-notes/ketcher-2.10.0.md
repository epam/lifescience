This release includes several bug fixes, improvements, and new features. Please be aware Ketcher 2.10.0 has been tested with Indigo version 1.11.0 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.11.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.11.0/images/sha256-eca445777e7b87b3e37b81b46b51a4e77bd5c1f15c25bc3d9cd7a7ffabc8d3ff?context=explore)).

## What's Changed

* #2273 When user selects and moves atom on Functional Group or Salt it doesn't replaces atom in the structure
* #2113 Hovered structure gets into the saved molecule
* #2062 RXN v2000: Detection molecule above/below arrow as reagent doesn't work
* #2362 Remove appearance of a tooltip under mouse cursor for Functional Groups/Salts and Solvents abbreviations
* #2403 Wrong tooltip and label in 'Extended Table'
* #2421 Add locators and/or functions for tools sub-menus
* #2029 Completely replace yarn with npm commands throughout the project
* #2355 Add DisableQueryElements parameter to disable query elements from extended table
* #2246 Multiple bond editing changes bond types to all selected bonds
* #2425 The cancel button does not reverse adding template to expanded and contracted functional group main
* #2446 Structures are drawn outside the viewbox, when changing rendering options
* #2427 When moving a structure outside of the canvas, structure does not move smoothly
* #2353 CTRL+SHIFT+0 hotkey not working for 'Zoom 100%'
* #2402 Atom under mouse cursor on click and drag freezes on canvas if you move cursor away from dragged atom
* #1855 Make benzene rings fused rings connection without valence errors
* #2456 Update KET json schema to support explicit implicit hydrogens
* #2441 Add a warning message about localStorage to templates window
* #2052 Expand collapse unknown super atom
* #2482 Ketcher with iFrame loads with scrollbars activated
* #2442 When mouse hovering on atom or bond hotkey CTRL+Z (Undo) is not working
* #2420 Hotkey (Del) can't delete Functional Groups and Salts abbreviation
* #2454 After clicking undo button edit abbreviation popup do not appear
* #2245 Settings: `Terminal and Hetero` is not selected as default and `on` option is not working
* #225 Add support for stereo cip values in ket format
* #2458 Migrate to Indigo v1.11.0-rc.1 in-browser module
* #2257 Unable to add a bond to a functional group by bond tool
* #1865 Extended SMILES saved from Ketcher might be invalid for RDKit
* #2516 When create Superatom part of the structure disappears
* #2528 Erase tool does not completely remove the Functional Groups if it selecting via the hot key CTRL + A
* #2530 Tooltip for created Data S-Group not appears after hover on it
* #2113 Hovered structure gets into the saved molecule
* #2420 Hotkey (Del) can't delete Functional Groups and Salts abbreviation
* #2548 If name of Superatom matches abbreviation in Custom Templates, then tooltip is shown on hover
* #2517 File with Superatom opens without part of structure
* #2273 When user selects and moves atom on Functional Group or Salt it doesn't replaces atom in the structure
* #2585 Change behaviour of "Show hydrogen labels" setting so the "on" value works the same way as "terminal and hetero"
* #2614 Contracted unknown superatom is parsed as expanded, and brackets with name are lost
* #2636 Unable to contract or expand Unknown Superatoms that are parsed via API in MolV3000, KET, CDX, CDXML, CML, Base64CDX formats
* #2656 After opening or pasting an unknown superatom onto canvas, it becomes non-interactive