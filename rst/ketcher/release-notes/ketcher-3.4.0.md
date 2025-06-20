
# Ketcher 3.4.0

## What's Changed

### New features
- [#6832](https://github.com/epam/ketcher/issues/6832) – Update the help document 3.3
- [#6625](https://github.com/epam/ketcher/issues/6625) – Support of expanded monomer option
- [#6271](https://github.com/epam/ketcher/issues/6271) – Support for CIP stereo labels in macromolecules mode
- [#5727](https://github.com/epam/ketcher/issues/5727) – Add "Calculate Properties" for macromolecules
- [#5797](https://github.com/epam/ketcher/issues/5797) – Highlighting attachment point of expanded monomers on hover in micromolecules mode
- [#7237](https://github.com/epam/ketcher/issues/7237) – Migrate to Indigo v1.32.0 in-browser module

### Bugfixes and improvements
- [#4838](https://github.com/epam/ketcher/issues/4838) – Incorrect structure for Phe-L-Phenylalanine in template library
- [#5497](https://github.com/epam/ketcher/issues/5497) – Refactor (SnakeModePolymerBondRenderer): Create and use `SVGPathDAttributeUtil`
- [#6288](https://github.com/epam/ketcher/issues/6288) – Incorrect numbering in sequence
- [#6871](https://github.com/epam/ketcher/issues/6871) – Connection points become visible and broken if user switch window focus from one app to another and back
- [#6870](https://github.com/epam/ketcher/issues/6870) – Enter key adds undeletable preset to preset section
- [#4476](https://github.com/epam/ketcher/issues/4476) – Tooltips in sequence mode not disappear after right-click on letters
- [#6762](https://github.com/epam/ketcher/issues/6762) – System shows natural analog monomer as modified if source mol file contains only 3-letters natural analog name
- [#6791](https://github.com/epam/ketcher/issues/6791) – Change activation area of the New sequence button
- [#6788](https://github.com/epam/ketcher/issues/6788) – Reduce "Add new sequence" control width
- [#7008](https://github.com/epam/ketcher/issues/7008) – Support of expanded monomer options doesn't work if monomer loaded from file/clipboard
- [#7007](https://github.com/epam/ketcher/issues/7007) – Rotation doesn't work for expanded monomers on Molecules mode
- [#5791](https://github.com/epam/ketcher/issues/5791) – It is possible to expand unknown nucleotide on micromolecules canvas
- [#5789](https://github.com/epam/ketcher/issues/5789) – It is possible to expand ambiguous monomers on micromolecules canvas
- [#7014](https://github.com/epam/ketcher/issues/7014) – No tooltip displayed for the “Calculate Properties” button in main toolbar
- [#7019](https://github.com/epam/ketcher/issues/7019) – Data in “Calculate Properties” window disappears after switching browser tabs, selection remains
- [#7030](https://github.com/epam/ketcher/issues/7030) – Missing Celsius symbol (°C) in “Melting temperature” label
- [#7039](https://github.com/epam/ketcher/issues/7039) – App crashes when adding Ambiguous Amino Acids to peptide sequence with open Calculate Properties window
- [#7015](https://github.com/epam/ketcher/issues/7015) – Alt+C / Option+C hotkey does not open the “Calculate Properties” window
- [#7033](https://github.com/epam/ketcher/issues/7033) – calculateMacroProperties API is called immediately on sequence selection, even when Calculate Properties window is closed
- [#7018](https://github.com/epam/ketcher/issues/7018) – Unable to clear monomer selection after switching browser tabs
- [#7026](https://github.com/epam/ketcher/issues/7026) – Calculate properties for peptides are missing in case of mixed peptide and RNA/DNA chain
- [#7017](https://github.com/epam/ketcher/issues/7017) – “Calculate Properties” shows wrong behavior when sequence is connected to microstructure
- [#7062](https://github.com/epam/ketcher/issues/7062) – Rotation is incorrect upon exporting transformed monomer to SVG or PNG
- [#7074](https://github.com/epam/ketcher/issues/7074) – Formula in "Calculate Properties" window is not updated when selecting monomers with connected microstructure
- [#7034](https://github.com/epam/ketcher/issues/7034) – Unipositive ions default value is shown in nM instead of mM for double-stranded sequence selection
- [#7085](https://github.com/epam/ketcher/issues/7085) – Ketcher does not send bond type to Indigo if connection is different from R2–R1, causing missing data in "Calculate Properties"
- [#7027](https://github.com/epam/ketcher/issues/7027) – Incorrect highlight (missing fill) for leaving-group atoms
- [#7028](https://github.com/epam/ketcher/issues/7028) – Turquoise monomer outline has incorrect gap for attachment points and blue outline too thin
- [#7096](https://github.com/epam/ketcher/issues/7096) – Clearing canvas while "Calculate Properties" window is open causes console errors
- [#6974](https://github.com/epam/ketcher/issues/6974) – System removes monomers from Molecules mode canvas is switched from Macro mode (bonds remain!) if ketcher in embedded mode (custom style iframe)
- [#7118](https://github.com/epam/ketcher/issues/7118) – Cannot edit concentration values of unipositive ions and oligonucleotides in Calculate Properties
- [#7249](https://github.com/epam/ketcher/issues/7249) – Input fields for ion concentration and oligonucleotides become inactive after clearing or entering zero
- [#7266](https://github.com/epam/ketcher/issues/7266) – Oligonucleotides input field becomes unresponsive after entering zero

---

### Additional notes:
- Ketcher 3.4.0 has been built and tested with Indigo version 1.32 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.32.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.32.0/images/sha256-d739c8474cea3051354e306320235037a55ab91b207e07eef45f8187b9eceecb)).
