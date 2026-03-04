
# Ketcher 3.11.0

## What's Changed

### New features
- [#8248](https://github.com/epam/ketcher/issues/8248) – Define nucleotide presets using the monomer creation wizard (POC)
- [#8254](https://github.com/epam/ketcher/issues/8254) – Allow for stereo bonds up and down to be a bond between AA and LGA
- [#8383](https://github.com/epam/ketcher/issues/8383) – Introduce library searching using HELM aliases, AxoLabs aliases, and modification types
- [#7915](https://github.com/epam/ketcher/issues/7915) – Enable flipping of all expanded monomers in a structure
- [#8363](https://github.com/epam/ketcher/issues/8363) – Include 'Arrange as a Ring' button for Flex mode

### Bugfixes and improvements
- [#8386](https://github.com/epam/ketcher/issues/8386) – Update the help document (3.10.)
- [#8739](https://github.com/epam/ketcher/issues/8739) – Migrate to Indigo v1.39.0-rc.1 in-browser module
- [#4188](https://github.com/epam/ketcher/issues/4188) – Choosing wedged/hashed bond direction doesn't work from right-clicking context menu
- [#7148](https://github.com/epam/ketcher/issues/7148) – Number of selected elements in context menu is wrong for sense/antisense chain
- [#7735](https://github.com/epam/ketcher/issues/7735) – System shows inner circles of aromatized benzene rings from collapsed monomers on Molecules canvas
- [#6855](https://github.com/epam/ketcher/issues/6855) – Labels for empty ambiguous monomer categories are present in the library
- [#7244](https://github.com/epam/ketcher/issues/7244) – File format name for Sequence is cut off in Save Structure modal dropdown
- [#5578](https://github.com/epam/ketcher/issues/5578) – Peptide section for ambiguous monomers should have "Ambiguous Amino Acids" name
- [#5580](https://github.com/epam/ketcher/issues/5580) – Order of sections for ambiguous bases is wrong - Ambiguous Bases should come first
- [#5927](https://github.com/epam/ketcher/issues/5927) – Font size and label position should be corrected at "Open structure" dialog
- [#7995](https://github.com/epam/ketcher/issues/7995) – Unable to create more than one attachment point per atom
- [#8395](https://github.com/epam/ketcher/issues/8395) – "Attachment points are set
- [#5481](https://github.com/epam/ketcher/issues/5481) – Ambiguous CHEM shown wrong at Sequence mode
- [#5799](https://github.com/epam/ketcher/issues/5799) – S-Group properties window should be disabled for monomers
- [#7385](https://github.com/epam/ketcher/issues/7385) – Cannot delete and copy microstructures via right-click context menu in macromolecule canvas
- [#4772](https://github.com/epam/ketcher/issues/4772) – Fix Platinum valence
- [#8403](https://github.com/epam/ketcher/issues/8403) – There is no way to remove HELM alias
- [#7506](https://github.com/epam/ketcher/issues/7506) – Tooltip is shown in wrong place for ambigous monomers in popup mode
- [#8461](https://github.com/epam/ketcher/issues/8461) – Function calls should not pass extra arguments
- [#6737](https://github.com/epam/ketcher/issues/6737) – `5NitInd` unsplit nucleotide should be shown as X symbol instead of @ one
- [#8459](https://github.com/epam/ketcher/issues/8459) – Getters and setters should access the expected fields
- [#5361](https://github.com/epam/ketcher/issues/5361) – getInChIKey returns just the InChI string as JSON
- [#5751](https://github.com/epam/ketcher/issues/5751) – Establishing connection between ambiguous CHEMs works wrong
- [#5214](https://github.com/epam/ketcher/issues/5214) – The tooltip does not appear below the cursor when hovering over the "plus" button and stripe
- [#6725](https://github.com/epam/ketcher/issues/6725) – Ambiguous sugars (alternatives and mixed) in sequence shown as % symbol instead of @ symbol
- [#4891](https://github.com/epam/ketcher/issues/4891) – When using the "ketcher.setMode(mode)" method, the icon of the "Type mode" drop-down does not change
- [#8554](https://github.com/epam/ketcher/issues/8554) – System losts AxoLabs alias while save it KET
- [#8556](https://github.com/epam/ketcher/issues/8556) – System losts Modification types values while save it KET
- [#7372](https://github.com/epam/ketcher/issues/7372) – "Ghost image" doesn't satisfy the UX design
- [#6731](https://github.com/epam/ketcher/issues/6731) – Ambiguous phosphates (alternatives and mixed) in sequence shown as % symbol instead of @ symbol
- [#8584](https://github.com/epam/ketcher/issues/8584) – Tooltip for attachment points appears too far from attachment point
- [#8397](https://github.com/epam/ketcher/issues/8397) – Context menu remains visible after creating cyclic structure via right-click menu
- [#7776](https://github.com/epam/ketcher/issues/7776) – In Macro mode clicking on Selection tool icon does not open dropdown menu as in Micro mode
- [#4645](https://github.com/epam/ketcher/issues/4645) – In the "Modify RNA Builder" mode, when hovering over the buttons "Yes" and "Cancel" in the "Update Sequence" window, tooltips are displayed
- [#7610](https://github.com/epam/ketcher/issues/7610) – R-groups are not shown if to Open from file as New project
- [#7559](https://github.com/epam/ketcher/issues/7559) – Charge tools doesn't work for "star" atoms
- [#7022](https://github.com/epam/ketcher/issues/7022) – Dropdown for units (Da/kDa/MDa) is not aligned in width with the selector button
- [#5677](https://github.com/epam/ketcher/issues/5677) – Preview for chain of CHEMs works wrong in sequence mode
- [#5664](https://github.com/epam/ketcher/issues/5664) – Selection circle is different on micro and macro mode
- [#5469](https://github.com/epam/ketcher/issues/5469) – Preview tooltips for monomers loaded from HELM with inline smiles are wrong
- [#7956](https://github.com/epam/ketcher/issues/7956) – Presence of R32 group in molecule makes impossible to create monomer from it
- [#5534](https://github.com/epam/ketcher/issues/5534) – Ambiguous monomer tooltip content doesn't sorted properly in case of equal quantities
- [#5382](https://github.com/epam/ketcher/issues/5382) – System shouln't allow user to load empty mol file - Add to Canvas should be disabled
- [#7689](https://github.com/epam/ketcher/issues/7689) – No tooltip shown and invalid attachments allowed when adding monomers consecutively without moving mouse from arrow button
- [#5567](https://github.com/epam/ketcher/issues/5567) – System losts height data during copy/paste operation
- [#7191](https://github.com/epam/ketcher/issues/7191) – Change 3SS6 monomer type to Phosphate
- [#8726](https://github.com/epam/ketcher/issues/8726) – Name should not be mandatory any more, Symbol value should be used instead if user left it empty
- [#8723](https://github.com/epam/ketcher/issues/8723) – User should be able to type ambiguous monomers symbols in edit sequence mode (current sequence type should be taken in to account)
- [#6730](https://github.com/epam/ketcher/issues/6730) – System doesn't unite ambiguous bases (alternatives and mixed) into one @ symbol
- [#8721](https://github.com/epam/ketcher/issues/8721) – Create a monomer button remain selected (colored) after user done with monomer creation (creation wizard got closed)
- [#8720](https://github.com/epam/ketcher/issues/8720) – Library update event is triggered after API usage
- [#7578](https://github.com/epam/ketcher/issues/7578) – Undo/Redo restores partial selection after cancelling monomer creation
- [#8752](https://github.com/epam/ketcher/issues/8752) – All types of ambiguous monomers alone represented on sequence canvas as @ symbol should be represented
- [#7519](https://github.com/epam/ketcher/issues/7519) – In case of multiple R1 or R2 groups second R1/R2 groups should be assigned to the smallest available Rn (n>2) if available
- [#5922](https://github.com/epam/ketcher/issues/5922) – Non-polar amino acid (with W as natural analog) should have shade of green but currently it is violet
- [#5445](https://github.com/epam/ketcher/issues/5445) – Labels for ambiguous monomers at Bond Preview tooltip are wrong
- [#7189](https://github.com/epam/ketcher/issues/7189) – Unknown unsplit nucleotide looks like chem
- [#8846](https://github.com/epam/ketcher/issues/8846) – Unable to create more than one nucleotide monomer - system throws exception
- [#8845](https://github.com/epam/ketcher/issues/8845) – Creation nucleortide preset causes som bonds to disappear
- [#8847](https://github.com/epam/ketcher/issues/8847) – Former molecule selection causes invalid attachment point creation in Monomer creation wizard

---

### Additional notes:
- Ketcher 3.11.0 has been built and tested with Indigo version 1.39 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.39.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.39.0/images/sha256-f123ddf09033a88978f0a81f4e3e9bb617fa7034a9c57bea76fae876321ed8fc)).
