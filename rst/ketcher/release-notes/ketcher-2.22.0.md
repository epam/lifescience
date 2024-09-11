
# Ketcher 2.22.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#3934](https://github.com/epam/ketcher/issues/3934) – Support selection entity selection flag in KET format
* [#4307](https://github.com/epam/ketcher/issues/4307) – Migrate Monomer library from MOL V2K to KET format
* [#4388](https://github.com/epam/ketcher/issues/4388) – Allow Nucleoside of sequence edit in RNA builder
* [#4427](https://github.com/epam/ketcher/issues/4427) – Store custom presets in browser local cache by
* [#4495](https://github.com/epam/ketcher/issues/4495) – UI support for IDT import/export
* [#4530](https://github.com/epam/ketcher/issues/4530) – Convert Rx connection points created in molecules mode into chem attachment points in macromolecules mode
* [#4531](https://github.com/epam/ketcher/issues/4531) – Allow moving and connecting "small" structures in macro mode
* [#4539](https://github.com/epam/ketcher/issues/4539) – Export macromolecules canvas as svg image
* [#4692](https://github.com/epam/ketcher/issues/4692) – Cursors should be copied from small mode
* [#4697](https://github.com/epam/ketcher/issues/4697) – Highlight connection point (change mouse cursor) on mouse hover
* [#4311](https://github.com/epam/ketcher/issues/4311) – Send monomer library from Ketcher to Indigo upon monomers import/export
* [#4530](https://github.com/epam/ketcher/issues/4530) – Add ability to define attachment points for molecules
* [#4380](https://github.com/epam/ketcher/issues/4380) – Display IDT aliases in monomer library
* [#4701](https://github.com/epam/ketcher/issues/4701) – Unify toolbars with small molecules mode
* [#4530](https://github.com/epam/ketcher/issues/4530) – Add ability to define attachment points for molecules fixes
* [#5391](https://github.com/epam/ketcher/issues/5391) – Migrate to Indigo 1.21.0 in-browser module

### Bugfixes and improvements
* [#3943](https://github.com/epam/ketcher/issues/3943) – System allow to create atoms with Charge value out or range
* [#3501](https://github.com/epam/ketcher/issues/3501) – 3d mol files appear as 2D in Miew
* [#4349](https://github.com/epam/ketcher/issues/4349) – Selection does not work in sequence editing with Shift+Up/Down arrow combination
* [#4508](https://github.com/epam/ketcher/issues/4508) – In the Text-editing mode, when selecting nucleotides linked through phosphates R2-R2, an error appears in the Console
* [#4340](https://github.com/epam/ketcher/issues/4340) – When adding new nucleotides to the beginning of a row, the order of the chains changes in the Sequence mode
* [#4470](https://github.com/epam/ketcher/issues/4470) – Any click on toolbar buttons should cause cancel of "Modify in RNA builder" process
* [#4479](https://github.com/epam/ketcher/issues/4479) – Quick double paste operation from clipboard leads to invalid entities on canvas
* [#4488](https://github.com/epam/ketcher/issues/4488) – System doesn't allow duplicate same preset twice
* [#4501](https://github.com/epam/ketcher/issues/4501) – The system allows you to paste on canvas while modifying nucleotides in the RNA builder
* [#4640](https://github.com/epam/ketcher/issues/4640) – Presets saved to local storage appear on canvas after switching Macro/Micro modes
* [#4615](https://github.com/epam/ketcher/issues/4615) – Implement sorting for RNA builder components
* [#4543](https://github.com/epam/ketcher/issues/4543) – The cleared object is not returned by the Undo button in the Macromolecules mode.
* [#4590](https://github.com/epam/ketcher/issues/4590) – RNA Structure is broken while we Copy from Macro and Paste to Micro canvas.
* [#4509](https://github.com/epam/ketcher/issues/4509) – In the Text-editing mode, when inserting a fragment after pressing Ctrl+V twice, the cursor is moved to another row
* [#3816](https://github.com/epam/ketcher/issues/3816) – Added validations and monomer Item disablement
* [#4575](https://github.com/epam/ketcher/issues/4575) – New Sequences are created while we add cyclic to middle of sequence.
* [#4693](https://github.com/epam/ketcher/issues/4693) – Incorrect bond alignment to tBu S-group
* [#4730](https://github.com/epam/ketcher/issues/4730) – System doubles number of pasted monomers after switching from flex to sequence
* [#4734](https://github.com/epam/ketcher/issues/4734) – Monomers from macro mode are not erased by Erase tool in micro mode
* [#4690](https://github.com/epam/ketcher/issues/4690) – Undo problem while layout is changed on the Snack of Flex modes and switch through modes
* [#4744](https://github.com/epam/ketcher/issues/4744) – When changing zoom level in macro mode, there is no percentage indication
* [#4739](https://github.com/epam/ketcher/issues/4739) – Pasting IDT structures via clipboard does not work
* [#4740](https://github.com/epam/ketcher/issues/4740) – Delete of cycled sequence from the canvas causes delete of another cycled sequence bond that makes it non-cycled
* [#4764](https://github.com/epam/ketcher/issues/4764) – IDT label is not shown or shown but layout is broken after load sequence from ket
* [#4726](https://github.com/epam/ketcher/issues/4726) – Delete of nucleoside symbol turns another nucleoside to nucleotide
* [#4777](https://github.com/epam/ketcher/issues/4777) – Incorrect valence for carbon atom in ring with attachment point after saving and reopening file
* [#4801](https://github.com/epam/ketcher/issues/4801) – Cut operation for attachment points makes canvas inaccessible/in-operational and delete entire molecule
* [#4708](https://github.com/epam/ketcher/issues/4708) – Forbid merging cyclic sequences on delete in Sequence mode
* [#4823](https://github.com/epam/ketcher/issues/4823) – In sequence mode, each press adds two characters and when deleted, also removes two
* [#4824](https://github.com/epam/ketcher/issues/4824) – Cycled chain breaks sequence canvas and entire app
* [#4839](https://github.com/epam/ketcher/issues/4839) – System loses connections to molecule R2 if there is no R1 attachment point
* [#4836](https://github.com/epam/ketcher/issues/4836) – Molecule changes position after saving and opening from file
* [#4840](https://github.com/epam/ketcher/issues/4840) – Paste from clipboard does not work for molecules in macro mode
* [#4879](https://github.com/epam/ketcher/issues/4879) – Save to mol for micro and macro structures connected through attachment points works wrong
* [#4973](https://github.com/epam/ketcher/issues/4973) – Connection between molecule and monomer lost after opening and saving to ket
