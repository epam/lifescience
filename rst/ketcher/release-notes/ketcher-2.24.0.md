
# Ketcher 2.24.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#4878](https://github.com/epam/ketcher/issues/4878) – Add/Replace monomer in sequence mode from library
* [#4880](https://github.com/epam/ketcher/issues/4880) – Adjust previews – add APs, show IDT aliases for previews in sequence mode, increase debounce time
* [#4888](https://github.com/epam/ketcher/issues/4888) – Enable editing sequences by click between symbols
* [#4887](https://github.com/epam/ketcher/issues/4887) – Starting new sequences with "Plus" icon on canvas
* [#4780](https://github.com/epam/ketcher/issues/4780) – Remove monomers from the library (Peptides and CHEMs)
* [#5167](https://github.com/epam/ketcher/issues/5176) – Change natural analogue of monomers Peptides and CHEMs)
* [#4787](https://github.com/epam/ketcher/issues/4787) – Change structure of monomers (Peptides and CHEMs)
* [#5166](https://github.com/epam/ketcher/issues/5166) – Change symbols of monomers (Peptides and CHEMs)
* [#4781](https://github.com/epam/ketcher/issues/4781) – Change names of monomers (Peptides and CHEMs)
* [#4905](https://github.com/epam/ketcher/issues/4905) – Open Edit Connection Points dialog via right click on bond
* [#4911](https://github.com/epam/ketcher/issues/4911) – Insert image from ket to canvas
* [#4897](https://github.com/epam/ketcher/issues/4897) – Insert image to canvas via "Add image" tool, Select, Move and Scale the image
* [#4981](https://github.com/epam/ketcher/issues/4981) – Support for SSR
* [#4979](https://github.com/epam/ketcher/issues/4979) – Support for Strict mode
* [#5190](https://github.com/epam/ketcher/issues/5190) – Include Indigo without render module into ketcher-standalone build process
* [#5284](https://github.com/epam/ketcher/issues/5284) – Update Indigo to 1.23.0 in browser module

### Bugfixes and improvements
* [#4763](https://github.com/epam/ketcher/issues/4763) – It is possible to create forbidden RNA preset
* [#4962](https://github.com/epam/ketcher/issues/4962) – Bond tool and Erase tool buttons have to be disabled in Sequence mode (since they are not applicable)
* [#4659](https://github.com/epam/ketcher/issues/4659) – Export result SVG contains some labels that are selectable
* [#4108](https://github.com/epam/ketcher/issues/4108) – There are no tooltips when hovering over each of the sequence modes
* [#4806](https://github.com/epam/ketcher/issues/4806) – It is allowed to change bond type between micro and macro
* [#4936](https://github.com/epam/ketcher/issues/4936) – Applying Enhanced Stereochemistry to monomers causes its disappear from the canvas (and exception in console)
* [#5090](https://github.com/epam/ketcher/issues/5090) – The favorites icon overlaps unsplit nucleotide names in the RNA and favorites tab
* [#4947](https://github.com/epam/ketcher/issues/4947) – Distance between unresolved monomer and preview tooltip is too large and it has no IDT alias
* [#4957](https://github.com/epam/ketcher/issues/4957) – Disabled query features in extended table not disabled in right-click menu
* [#5126](https://github.com/epam/ketcher/issues/5126) – The error appears in the Console, when connecting two unsplit nucleotides in Snake mode
* [#4069](https://github.com/epam/ketcher/issues/4069) – Right-click context menu protrudes beyond edges of the Ketcher workspace
* [#4806](https://github.com/epam/ketcher/issues/4806) – It is allowed to change bond type between micro and macro
* [#5196](https://github.com/epam/ketcher/issues/5196) – An error appears in the Console when opening any section in the RNA tab
* [#5242](https://github.com/epam/ketcher/issues/5242) – Replace phosphate at the end with peptide causes cycled polymer
* [#5184](https://github.com/epam/ketcher/issues/5184) – Fix unresolved monomers bond establishing issue
* [#4935](https://github.com/epam/ketcher/issues/4935) – Enumeration is missing for cycled unsplit nucleotides after load from file (KET/MOL doesn't matter)
* [#5255](https://github.com/epam/ketcher/issues/5255) – Fix adding new monomers to canvas in sequence mode while editing RNA in builder
* [#5245](https://github.com/epam/ketcher/issues/5245) – Replacement of peptide at the end of sequence on preset w/out base works wrong
* [#5228](https://github.com/epam/ketcher/issues/5228) – System insert monomer from the library to the canvas even if it shouldn't (and error message is wrong)
* [#5300](https://github.com/epam/ketcher/issues/5300) – Attempt to insert improper monomer from the library to the sequence causes wrong error
* [#5301](https://github.com/epam/ketcher/issues/5301) – New preset creation process interferes with monomer replacement on the sequence mode
