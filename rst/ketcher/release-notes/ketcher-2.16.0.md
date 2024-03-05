
# Ketcher 2.16.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

* [#2370](https://github.com/epam/ketcher/issues/2370) - erase tool for macromolecules editor
* [#2367](https://github.com/epam/ketcher/issues/2367) - Ability to move items on the canvas
* [#2994](https://github.com/epam/ketcher/issues/2994) - Attachment points should be within S-Group brackets
* [#3229](https://github.com/epam/ketcher/issues/3229) - Run macromolecules e2e tests on ci
* [#3276](https://github.com/epam/ketcher/issues/3276) - Remove 'Edit attachment point...' from right-click context menu
* [#3230](https://github.com/epam/ketcher/issues/3230) - Support parsing KET file for macromolecules on ketcher side
* [#3221](https://github.com/epam/ketcher/issues/3221) - add shortcut shift+tab for switching selection mode
* [#3323](https://github.com/epam/ketcher/issues/3323) - Update schema.json for atom query specific properties
* [#3298](https://github.com/epam/ketcher/issues/3298) - Add simple atom query primitives to the query specific properties
* [#3326](https://github.com/epam/ketcher/issues/3326) - Add text field for query SMARTS advanced features
* [#3347](https://github.com/epam/ketcher/issues/3347) – Horizontal scroll appears after opening certain structures
* [#2518](https://github.com/epam/ketcher/issues/2518) - Update project npm dependencies to remove vulnerabilities
* [#3328](https://github.com/epam/ketcher/issues/3328) - Add bond custom query field
* [#2909](https://github.com/epam/ketcher/issues/2909) - movement of structure ceases when it reaches the boundaries of canvas requiring the consistent movement of mouse to continue its motion
* [#3129](https://github.com/epam/ketcher/issues/3129) - Full template preview following mouse cursor
* [#3338](https://github.com/epam/ketcher/issues/3338) - New S-Group type Query component level grouping
* [#3372](https://github.com/epam/ketcher/issues/3372) - Update customQuery for bonds using topology
* [#3040](https://github.com/epam/ketcher/issues/3040) - Provide additional logging
* [#3371](https://github.com/epam/ketcher/issues/3371) - Merge ring bond count, degree and atomic mass atom properties
* [#3340](https://github.com/epam/ketcher/issues/3340) - Make any atom and atom list part of the Atom properties
* [#3004](https://github.com/epam/ketcher/issues/3004) - Allow to select items from the Favorites tab
* [#3088](https://github.com/epam/ketcher/issues/3088) - Rotate monomer attachment point to bond direction
* [#3174](https://github.com/epam/ketcher/issues/3174) - RNA Bases are filtered wrong
* [#3339](https://github.com/epam/ketcher/issues/3339) - Add empty options for atom charges and isotops
* [#3387](https://github.com/epam/ketcher/issues/3387) - Save atom properties for atom list in ket format
* [#3398](https://github.com/epam/ketcher/issues/3398) - When you save atom in ket format with substitutionCount greater then 6 , it is impossible to open it
* [#3293](https://github.com/epam/ketcher/issues/3293) - Reduce the amount of flaky and failed tests
* [#3408](https://github.com/epam/ketcher/issues/3408) - When insert a smarts with two query groups after inserting smarts with one query group error appear
* [#3445](https://github.com/epam/ketcher/issues/3445) - Atom properties "Substitution count" and "Ring bond count" convert incorrectly to custom query
* [#3431](https://github.com/epam/ketcher/issues/3431) – warnings appear while saving any structure as daylight smarts
* [#3250](https://github.com/epam/ketcher/issues/3250) - Rna monomer accordion library should open from top to bottom
* [#3459](https://github.com/epam/ketcher/issues/3459) - All atom attributes should be displayed as SMARTS if at least one purely SMARTS attribute exists
* [#3393](https://github.com/epam/ketcher/issues/3393) - Add new keyboard shortcut "ctrl+alt+V" for pasting as SMARTS
* [#3502](https://github.com/epam/ketcher/issues/3502) - Custom query is not correctly represented on canvas - only atom number is displayed
* Macro: [#3250](https://github.com/epam/ketcher/issues/3250) - Rna monomer accordion library should open from top to bottom
* Macro: [#3280](https://github.com/epam/ketcher/issues/3280) - Displaying a long peptide chain on a canvas. Snake-like layout
* Macro: [#3373](https://github.com/epam/ketcher/issues/3373) - Rotate Attachment Point Unused
* Macro: [#3041](https://github.com/epam/ketcher/issues/3041) – RNA Builder. Delete presets
* Macro: [#3385](https://github.com/epam/ketcher/issues/3385) - Overlapping of bonds between 2 monomers
* Macro: [#3251](https://github.com/epam/ketcher/issues/3251) - Rna preset name should be autofilled when user selects rna parts
* Macro: [#3420](https://github.com/epam/ketcher/issues/3420) - Monomer does not move on first click and drug
* Autotests: [#3436](https://github.com/epam/ketcher/issues/3436) - Autotests: query attributes for SMARTS
* Autotests: [#3581](https://github.com/epam/ketcher/issues/3581) - add tests for missed test cases based on done tickets for smarts
* Autotests: [#3170](https://github.com/epam/ketcher/issues/3170) - reduce the number of tests with fixme
* Autotests: [#3169](https://github.com/epam/ketcher/issues/3169) - Open and Save files (InChi)
* Autotests: [#3204](https://github.com/epam/ketcher/issues/3204) - Charge Tool
* Autotests: [#3189](https://github.com/epam/ketcher/issues/3189) - Templates - Salts and Solvents
* Autotests: [#3100](https://github.com/epam/ketcher/issues/3100) - Selection Tool->Bond Properties and Select All
* Autotests: [#3089](https://github.com/epam/ketcher/issues/3089) - autotests functional groups lookup abbreviations
* Autotests: [#3271](https://github.com/epam/ketcher/issues/3271) - Save files
* Autotests: [#3168](https://github.com/epam/ketcher/issues/3168) - Open and Save files (Mol-files)
* Autotests: [#3319](https://github.com/epam/ketcher/issues/3319) - Actions with structures
* Autotests: [#3303](https://github.com/epam/ketcher/issues/3303) - Open and Save files (CDX)
* Autotests: [#3054](https://github.com/epam/ketcher/issues/3054) - create autotests for default settings verification
* Autotests: [#3108](https://github.com/epam/ketcher/issues/3108) - Clean Tools and Layout
* Autotests: [#2884](https://github.com/epam/ketcher/issues/2884) - create autotests for mapping/unmapping and reaction tools
* Autotests: [#3359](https://github.com/epam/ketcher/issues/3359) - File management - open and save files
* Autotests: [#3016](https://github.com/epam/ketcher/issues/3016) - create autotests for easy to implement TCses
* Autotests: [#3289](https://github.com/epam/ketcher/issues/3289) - Clear Canvas
* Autotests: [#3411](https://github.com/epam/ketcher/issues/3411) - Create autotests for chain tool
* Autotests: [#3416](https://github.com/epam/ketcher/issues/3416) - editing tools and zoom
* Autotests: [#2885](https://github.com/epam/ketcher/issues/2885) - Create autotests for atom tools
* Autotests: [#3053](https://github.com/epam/ketcher/issues/3053) - Autotests limited automation cases for atom tool
* Autotests: [#3429](https://github.com/epam/ketcher/issues/3429) - Multiple Group
* Autotests: [#3052](https://github.com/epam/ketcher/issues/3052) - editing tools zoom test cases
* Autotests: [#3386](https://github.com/epam/ketcher/issues/3386) - Functional Groups
* Autotests: [#3377](https://github.com/epam/ketcher/issues/3377) - Reagents - CML file format
* Autotests: [#2924](https://github.com/epam/ketcher/issues/2924) - test cases for functional groups and toolbar
* Autotests: [#3400](https://github.com/epam/ketcher/issues/3400) - Toolbar
* Autotests: [#3181](https://github.com/epam/ketcher/issues/3181) - Open and Save files (RXN)
* Autotests: [#3318](https://github.com/epam/ketcher/issues/3318) - Create autotests for attachment point tool
* Autotests: [#3186](https://github.com/epam/ketcher/issues/3186) – rectangle selection tool
* Autotests: [#3185](https://github.com/epam/ketcher/issues/3185) - Lasso Selection Toolbar – Layout should not be called if there are coordinates in extended smiles