# Ketcher 2.7.0
## What's Changed

Release 2.7.0 is now available.
Please be aware Ketcher 2.7.0 has been tested with Indigo version 1.8.3 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.9.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.9.0/images/sha256-c558047f1b359678e204fd9d32951d8c87b45e49c508b4b434a35ddb88c8e8d9?context=explore)).

**New features and bug fixes**

* [#2028](https://github.com/epam/ketcher/issues/2028) Hotkey: Atom symbols are not displayed under mouse cursor while mouse hovers over the canvas
* [#2081](https://github.com/epam/ketcher/issues/2081) – migrate to indigo v1.9.0-rc.3 in browser module
* [#2096](https://github.com/epam/ketcher/issues/2096) – updated indigo version to 1.9.0-rc.4
* [#1998](https://github.com/epam/ketcher/issues/1998): Functional Groups: The abbreviation and hovering preview 'Boc' is displayed as 'Bn'
* [#2015](https://github.com/epam/ketcher/issues/2015): Migrate to Indigo v1.9.0-rc.2 in-browser module
* [#1984](https://github.com/epam/ketcher/issues/1984): Hot key: If a 'Hand tool' is selected, then when you press any hot key (e.g. 'C','S','O','N') Ketcher crashes
* [#1934](https://github.com/epam/ketcher/issues/1934): Hot key 1 turns sulfur into carbon when cursor over the atom
* [#2020](https://github.com/epam/ketcher/issues/2020): When hovering over a functional group for the first time a lot of errors are generated in console
* [#1955](https://github.com/epam/ketcher/issues/1955): Selection tool: The highlight of structure, abbreviation is not reset when clicking on the canvas
* [#1986](https://github.com/epam/ketcher/issues/1986) SMILES: Pasting structure with small letters throw an error
* [#1973](https://github.com/epam/ketcher/issues/1973): App crashes when template dialog is closed and reopened and there is text in the search filter
* [#1959](https://github.com/epam/ketcher/issues/1959): SDF files are not available as part of npm ketcher-react package
* [#1957](https://github.com/epam/ketcher/issues/1957): Migrate to Indigo v1.9.0-rc.1 in-browser module
* [#1958](https://github.com/epam/ketcher/issues/1958): Improve performance, when opening Salts and Solvents tab
* [#1967](https://github.com/epam/ketcher/issues/1967): base64 file parsing causes an error
* [#1915](https://github.com/epam/ketcher/issues/1915) – improved search performance in template dialog
* [#1864](https://github.com/epam/ketcher/issues/1864) If the coordinates have a centroid that is far from zero, the molecule placed far offscreen
* [#1920](https://github.com/epam/ketcher/issues/1920) Salts and Solvents tab: Abbreviation is expanded after adding to the canvas
* [#1921](https://github.com/epam/ketcher/issues/1921): Salts and Solvents tab: When you place abbreviations on the canvas and hover the mouse it's draw the structure by clipping it
* [#1911](https://github.com/epam/ketcher/issues/1911) Hovering over some functional groups crops the expanded view of it (refactoring previous implementation)
* [#1888](https://github.com/epam/ketcher/issues/1888) Ability to add custom name and values for data sgroup
* [#1912](https://github.com/epam/ketcher/issues/1912): update help.md with updated list of keyboard shortcuts
* [#1922](https://github.com/epam/ketcher/issues/1922) Salts and Solvents tab: Structure appears for a second in the upper left corner after removing abbreviation
* [#1939](https://github.com/epam/ketcher/issues/1939) The hover panel is displayed incorrectly
* [#1936](https://github.com/epam/ketcher/issues/1936) Adding functional group to atom generate a JavaScript console error
* [#1929](https://github.com/epam/ketcher/issues/1929) CDX detected as MOL
* [#1914](https://github.com/epam/ketcher/issues/1914) Data S-Group: In the window 'S-Group Properties' the names of the radio buttons are displayed without separation
* [#1640](https://github.com/epam/ketcher/issues/1640) add cdx support
* [#1824](https://github.com/epam/ketcher/issues/1824) Show underlying structure on mouse hover for functional groups and salts&solvents
* [#1894](https://github.com/epam/ketcher/issues/1894) Add support for extra spaces and quotes in alias for mol v2000 files
* [#1827](https://github.com/epam/ketcher/issues/1827) Highlight currently selected tool with mouse cursor and toolbox icons
* [#1820](https://github.com/epam/ketcher/issues/1820) Create Salts and Solvents tab and include basic structures
* [#1823](https://github.com/epam/ketcher/issues/1823) When select a structure from template window it automatically starts to be added to canvas
* [#1826](https://github.com/epam/ketcher/issues/1826) Keyboard shortcut should not change current tool if cursor is over an atom
* [#1878](https://github.com/epam/ketcher/issues/1878) Fix husky and add prettier-write task to pre-commit hook
* [#1852](https://github.com/epam/ketcher/issues/1852) Automatic selection of mol v2000 or mol v3000 encoding
* [#1811](https://github.com/epam/ketcher/issues/1811) Update existing functional groups by missing common groups
* [#1825](https://github.com/epam/ketcher/issues/1825) Introduce keyboard shortcuts for atoms not shown on the right panel
* [#1801](https://github.com/epam/ketcher/issues/1801) Refactor standalone struct service. Get rid of unnecessary Indigo-worker creation
* [#1694](https://github.com/epam/ketcher/issues/1694) Elements styles are overwriting other styles
* [#1863](https://github.com/epam/ketcher/issues/1863) Remote version has less save options than the standalone version
* [#1810](https://github.com/epam/ketcher/issues/1810) – Make functional group name layout close to attachment point
* [#1845](https://github.com/epam/ketcher/issues/1845) [Rotate Tool] Button actions are mixed up: Horizontal Flip button makes Vertical Flip and Vertical Flip button makes Horizontal Flip
* [#1822](https://github.com/epam/ketcher/issues/1822) When open template window search text should be selected as default
* [#1802](https://github.com/epam/ketcher/issues/1802) Refresh the interface when the scroll axis appears again, it will automatically scroll to the bottom
* [#1782](https://github.com/epam/ketcher/issues/1782) add layout method to ketcher api
* [#1788](https://github.com/epam/ketcher/issues/1788) Update format when saving template library to sdf
