
# Ketcher 3.19.0

## What's Changed

### New features
- [#7926](https://github.com/epam/ketcher/issues/7926) – Expanding Drag-and-Drop functionality to support bond establishment
- [#10311](https://github.com/epam/ketcher/issues/10311) – Add Isotopes option to Check Structure
- [#10344](https://github.com/epam/ketcher/issues/10344) – Support for atom lists in macromolecules mode
- [#7864](https://github.com/epam/ketcher/issues/7864) – New options in the context menu - Editing monomers from molecules mode in the monomer creation wizard
- [#10345](https://github.com/epam/ketcher/issues/10345) – Support for extended table atoms in macromolecules mode
- [#9549](https://github.com/epam/ketcher/issues/9549) – Color Picker UI

### Bugfixes and improvements
- [#2701](https://github.com/epam/ketcher/issues/2701) – 'List' and 'Not List' atoms are not fully highlighted
- [#5045](https://github.com/epam/ketcher/issues/5045) – ketcher.setMolecule doesn't work for IDT files
- [#5169](https://github.com/epam/ketcher/issues/5169) – Simple Objects are duplicated after saving in Macro mode
- [#7935](https://github.com/epam/ketcher/issues/7935) – Export to SVG works different (and not well) in popup mode
- [#5502](https://github.com/epam/ketcher/issues/5502) – Structures shift to center of canvas when enabling viewOnlyMode through the API
- [#3885](https://github.com/epam/ketcher/issues/3885) – System shows "Any atom" atom with custom query incorrectly
- [#6719](https://github.com/epam/ketcher/issues/6719) – Line (dash) is missing between nucleotide and nucleoside if no connection in antisense for second chain pair
- [#5857](https://github.com/epam/ketcher/issues/5857), [#5676](https://github.com/epam/ketcher/issues/5676) – Fix coordinates calculation for v2000 format
- [#3774](https://github.com/epam/ketcher/issues/3774) – Enhanced Stereochemistry label is immediately placed on canvas when selecting templates from the library
- [#6736](https://github.com/epam/ketcher/issues/6736) – System doesn't establish H-bonds with any type of @ symbol on Establish Hydrogen Bond option
- [#10381](https://github.com/epam/ketcher/issues/10381) – Replacing a Whole Sequence Breaks Two-Stranded Chain Structure
- [#7392](https://github.com/epam/ketcher/issues/7392) – Paste option enabled even if clipboard is empty or contains not applicable content
- [#10453](https://github.com/epam/ketcher/issues/10453) – Keyboard shortcuts tooltip text should be shown correct on Mac
- [#10420](https://github.com/epam/ketcher/issues/10420) – AND/OR center labels overlap atom labels in Macromolecules Flex mode
- [#6868](https://github.com/epam/ketcher/issues/6868) – Sugars and phosphates does not reset monomer counting if put into backbone chain
- [#10375](https://github.com/epam/ketcher/issues/10375) – Application crashes when user tries to edit generic S-Group
- [#6799](https://github.com/epam/ketcher/issues/6799) – Adding dash to the gap from the left doesn't work
- [#8182](https://github.com/epam/ketcher/issues/8182) – Forbidden to define preset (group) name with wrong symbols
- [#1449](https://github.com/epam/ketcher/issues/1449) – The Template Library sections are opening slowly
- [#10247](https://github.com/epam/ketcher/issues/10247) – Nucleotide preset: Incorrect highlighting of tabs in case of missing components
- [#3269](https://github.com/epam/ketcher/issues/3269) – When click on the dividing lines, the context menu disappears
- [#8969](https://github.com/epam/ketcher/issues/8969) – Ketcher crashes in dev mode
- [#6234](https://github.com/epam/ketcher/issues/6234) – Thick foreground bond looks wrong on Macro canvas
- [#9441](https://github.com/epam/ketcher/issues/9441) – Nucleotide presets: Incorrect highlighting of the component when active tab is not component's tab
- [#10382](https://github.com/epam/ketcher/issues/10382) – Fix undo-ing changes work wrong
- [#7939](https://github.com/epam/ketcher/issues/7939) – Unable to export monomer to SDF V2000 - system always returns SDF V3000 content
- [#10398](https://github.com/epam/ketcher/issues/10398) – Fix keyboard events (Ghost molecule appears after typing on inactive ketcher canvas)
- [#2818](https://github.com/epam/ketcher/issues/2818) – Periodic Table: P, F, Cs atoms weight is out of the box
- [#7128](https://github.com/epam/ketcher/issues/7128) – Molecular formula letters not same level in Macromolecule Properties
- [#6056](https://github.com/epam/ketcher/issues/6056) – Ambiguous monomers (not from our library) are not marked as modified
- [#1804](https://github.com/epam/ketcher/issues/1804) – Opening Ket file with 4 S-groups, last one getting lost
- [#2174](https://github.com/epam/ketcher/issues/2174) – Undo not working in atom mapping, unable to remove mapping
- [#5388](https://github.com/epam/ketcher/issues/5388) – Preserve static objects and reaction molecules when applying 3D mode
- [#10470](https://github.com/epam/ketcher/issues/10470) – Enable Copolymer as an independent S-group type
- [#10515](https://github.com/epam/ketcher/issues/10515) – Change the pI tooltip
- [#5149](https://github.com/epam/ketcher/issues/5149) – Only elements are moving with the cursor while adding User Template to the Canvas
- [#5116](https://github.com/epam/ketcher/issues/5116) – System shows side bond connection for CHEM symbol to itself in sequence mode
- [#3425](https://github.com/epam/ketcher/issues/3425) – When selecting one atom in each of two different structures, the S-group button does not work
- [#2388](https://github.com/epam/ketcher/issues/2388) – Stereochemistry button isn't disabled when user selects structure without stereocenters
- [#3508](https://github.com/epam/ketcher/issues/3508) – Bond is shifted when list of atoms (at least 3) or few general atom's properties are specified at label near to the next atom
- [#6461](https://github.com/epam/ketcher/issues/6461) – Adding monomers from the library is impossible for sense/antisense chains in edit mode
- [#6761](https://github.com/epam/ketcher/issues/6761) – Removing last monomer after nucleotide leaves it as nucleotide instead of nucleoside in sense chain
- [#10477](https://github.com/epam/ketcher/issues/10477) – RNA Builder should load first preset from the library if Cancel pressed
- [#8174](https://github.com/epam/ketcher/issues/8174) – An IDT alias for one of the positions (5', internal, 3') must be unique in the whole library
- [#10221](https://github.com/epam/ketcher/issues/10221) – Support library searching using three letter amino-acid codes
- [#3483](https://github.com/epam/ketcher/issues/3483) – False selection of several atoms at the same time in the Extended Table
- [#7406](https://github.com/epam/ketcher/issues/7406) – Rotation angle for monomer is not preserved correctly in KET
- [#7211](https://github.com/epam/ketcher/issues/7211) – Keep the ruler input visible after reload
- [#5331](https://github.com/epam/ketcher/issues/5331) – Attempt to replace monomer on improper one from the library to the sequence causes wrong error message
- [#7547](https://github.com/epam/ketcher/issues/7547) – Attachment points for star atoms got missed if loaded from KET as New project and have R-Group Fragment molecule near
- [#3705](https://github.com/epam/ketcher/issues/3705) – Change bond type using keyboard shortcuts while hovering on bond
- [#7140](https://github.com/epam/ketcher/issues/7140) – Update the layout for CHEM-containing sequences
- [#2950](https://github.com/epam/ketcher/issues/2950) – No warning message after entering 0 in some numeric fields in Settings
- [#7020](https://github.com/epam/ketcher/issues/7020) – Non-interactive resize element in “Calculate Properties” window
- [#7316](https://github.com/epam/ketcher/issues/7316) – Fix slow melting temperature update when changing measurement units in Calculate Properties
- [#6770](https://github.com/epam/ketcher/issues/6770) – Adding monomers to antisense chain doesn't work in some cases
- [#7043](https://github.com/epam/ketcher/issues/7043) – Fix multi-line textbox vertical position when taller than viewport
- [#6735](https://github.com/epam/ketcher/issues/6735) – Include unsplit nucleotides in the creation of antisense chains
- [#10735](https://github.com/epam/ketcher/issues/10735) – Ambiguous bases (not from our library) have to be enumerated as regular bases if they are part of preset
- [#3529](https://github.com/epam/ketcher/issues/3529) – Value '0' for Ring membership, Ring size, Connectivity not displayed on structure and the values for Implicit H count are not displayed at all
- [#4451](https://github.com/epam/ketcher/issues/4451) – Unable to move sequence (on Flex mode)
- [#10758](https://github.com/epam/ketcher/issues/10758) – Expression injection and self-hosted runner fork PR protection
- [#10737](https://github.com/epam/ketcher/issues/10737) – Preset with ambiguous bases (not from our library) should be covered
- [#4976](https://github.com/epam/ketcher/issues/4976) – Side-chain connections remain transparent, after deleting at least one side-chain connection on the canvas
- [#8176](https://github.com/epam/ketcher/issues/8176) – An IDT alias for one of the positions (5', internal, 3') must be unique in the whole library (another case)
- [#7126](https://github.com/epam/ketcher/issues/7126) – Merging all chains on the canvas to one doesn't trigger recalculation in Calculate Properties window
- [#5329](https://github.com/epam/ketcher/issues/5329) – Prevent Structure Library crash for R-Group templates
- [#10753](https://github.com/epam/ketcher/issues/10753) – Update the help document (3.18)
- [#10814](https://github.com/epam/ketcher/issues/10814) – Migrate to Indigo v1.47.0-rc.1 in-browser module
- [#11945](https://github.com/epam/ketcher/issues/11945) – Macromolecules API stops working if ketcher instance destroyed and created again
- [#11947](https://github.com/epam/ketcher/issues/11947) – Errors in console when typing in sequence mode (RNA/DNA) symbols that don't exist in library
- [#11981](https://github.com/epam/ketcher/issues/11981) – Copy/paste doesn't work in Firefox 155

---

### Additional notes:
- Ketcher 3.19.0 has been built and tested with Indigo version 1.47 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.47.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.47.0/images/sha256-ce2b7056a50f35359469bb94e96134f0692cb6dd6b2156b774d2c16ef1c569e9)).
