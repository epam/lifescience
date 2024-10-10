
# Ketcher 2.25.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#4884](https://github.com/epam/ketcher/issues/4884) – Implement basic preview display for monomer bonds
* [#4554](https://github.com/epam/ketcher/issues/4554) – Support ambiguous monomers in Ketcher (flex mode)
* [#5186](https://github.com/epam/ketcher/issues/5186) – Add ambiguous monomers to the library and allow their addition to the canvas
* [#4556](https://github.com/epam/ketcher/issues/4556) – Support of ambiguous monomers in sequence view
* [#4557](https://github.com/epam/ketcher/issues/4557) – Support of ambiguous monomers in small molecules mode
* [#4872](https://github.com/epam/ketcher/issues/4872) – New approach and UI for switching between types in sequence mode
* [#4555](https://github.com/epam/ketcher/issues/4555) – Preview for ambiguous monomers
* [#5224](https://github.com/epam/ketcher/issues/5224) – Implement basic preview in connection modal for ambiguous monomer
* [#4861](https://github.com/epam/ketcher/issues/4861) – Introducing multi-tail arrows
* [#4985](https://github.com/epam/ketcher/issues/4985) – Support retrosynthetic arrows
* [#4853](https://github.com/epam/ketcher/issues/4853) – Search monomer in library by IDT
* [#4926](https://github.com/epam/ketcher/issues/4926) – Add IDT alias to chem monomer
* [#5244](https://github.com/epam/ketcher/issues/5244) – Add CHEMs to the library
* [#5264](https://github.com/epam/ketcher/issues/5264) – Add amino acids to the library
* [#5152](https://github.com/epam/ketcher/issues/5152) – Add new settings for ACS style
* [#5560](https://github.com/epam/ketcher/issues/5560) – Update Indigo to 1.24.0 in browser module

### Bugfixes and improvements
* [#5200](https://github.com/epam/ketcher/issues/5200) – The users choice is not saved in the settings but is recalculated in px
* [#4658](https://github.com/epam/ketcher/issues/4658) – Some bonds remain selected on export to SVG in Snake mode
* [#5201](https://github.com/epam/ketcher/issues/5201) – it is not possible to enter a value when selecting cm inch pt manually in the settings
* [#5454](https://github.com/epam/ketcher/issues/5454) – Export of variant monomers to Sequence/FASTA doesn't work for presets
* [#5425](https://github.com/epam/ketcher/issues/5425) – Undo-Redo operations over ambiguous monomer causes broken canvas
* [#5464](https://github.com/epam/ketcher/issues/5464) – Undo operation removes ambiguous monomer from the canvas but keep in the KET file export
* [#5209](https://github.com/epam/ketcher/issues/5209) – Cancel of Edit Connection points dialog cause existed connection points eliminated
* [#5453](https://github.com/epam/ketcher/issues/5453) – Circle with monomer number should be few pixels down
* [#5427](https://github.com/epam/ketcher/issues/5427) – Preview tooltip for mixture ambiguous monomer shows wrong percentages
* [#5466](https://github.com/epam/ketcher/issues/5466) – HELM inline SMILES monomer canvas color is wrong
* [#5470](https://github.com/epam/ketcher/issues/5470) – Export of different mixed and alternatives peptides (with different proportions and percents) works wrong
* [#5313](https://github.com/epam/ketcher/issues/5313) – Creation preset without phosphate causes R3-less sugars disabled in the library
* [#5447](https://github.com/epam/ketcher/issues/5447) – Added fixed precision class, updated multi-tail calculations with fixed precision usage
* [#5368](https://github.com/epam/ketcher/issues/5368) – An error appears in the Console, when dragging a bond between any monomers
* [#4212](https://github.com/epam/ketcher/issues/4212) – Limit size of structures in preview
* [#5473](https://github.com/epam/ketcher/issues/5473) – Export of different mixed and alternatives RNAs (with different proportions and percents) works wrong
* [#5465](https://github.com/epam/ketcher/issues/5465) – Export of different mixed monomers (with different ratios) works wrong
* [#5512](https://github.com/epam/ketcher/issues/5512) – System saves mixture ambiguous monomers as alternatives ambiguous monomers
* [#5519](https://github.com/epam/ketcher/issues/5519) – Alias labels for mixed bases loaded from IDT are wrong
* [#5521](https://github.com/epam/ketcher/issues/5521) – Sugar color is wrong if loaded from HELM with inline SMILES
* [#5545](https://github.com/epam/ketcher/issues/5545) – After uploading a multi-character monomer in HELM format, abbreviations in sequence mode are cluttered together
