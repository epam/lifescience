
# Ketcher 3.18.0

## What's Changed

### New features
- [#10173](https://github.com/epam/ketcher/issues/10173) – Support HELM aliases for CHEMs
- [#10166](https://github.com/epam/ketcher/issues/10166) – Edit all instances of monomers from molecules mode
- [#10174](https://github.com/epam/ketcher/issues/10174) – Align the Ketcher library with the new HELM library
- [#6918](https://github.com/epam/ketcher/issues/6918) – Support for stereo-flags in macromolecules mode
- [#10167](https://github.com/epam/ketcher/issues/10167) – Support S-groups in macromolecules mode
- [#10837](https://github.com/epam/ketcher/issues/10837) – Migrate to Indigo v1.46.0-rc.2 in-browser module

### Bugfixes and improvements
- [#5576](https://github.com/epam/ketcher/issues/5576) – System mix up sequences from two files loaded one after another
- [#9671](https://github.com/epam/ketcher/issues/9671) – Context menu works wrong for embedded Ketcher
- [#10172](https://github.com/epam/ketcher/issues/10172) – Update some preset-specific error messages
- [#10039](https://github.com/epam/ketcher/issues/10039) – Nucleotide preset: External AP of a phosphate is not always displayed in the preset tab
- [#9750](https://github.com/epam/ketcher/issues/9750) – RNA Builder: Phosphate position picker is not visible when modifying preset in Sequence mode
- [#9780](https://github.com/epam/ketcher/issues/9780) – Save the polymer type switcher (RNA/DNA/PEP) to browser cache
- [#5760](https://github.com/epam/ketcher/issues/5760) – The type file of module 'ketcher-standalone' cannot be resolved.
- [#6013](https://github.com/epam/ketcher/issues/6013) – System reposition monomers on the canvas if ACS setting were applied
- [#8188](https://github.com/epam/ketcher/issues/8188) – No error if data structure doesn't comply with data structure of sdf and CTFile formats specification
- [#399](https://github.com/epam/ketcher/issues/399) – Security: shell-quote quote() does not escape newlines in object .op values
- [#9715](https://github.com/epam/ketcher/issues/9715) – No gray arrows appear when hovering on the bond in the direction leading to an already marked component in Monomer Creation Wizard
- [#10034](https://github.com/epam/ketcher/issues/10034) – System doesn't assing added bonds to defined Preset component
- [#3882](https://github.com/epam/ketcher/issues/3882) – Changing at least one atom position causes entire molecule repositioning after Aromatize/Dearomatize
- [#8133](https://github.com/epam/ketcher/issues/8133) – Impossible to restrict adding invalid monomer types (e.g. Unknown base, Micromolecule) through API
- [#3963](https://github.com/epam/ketcher/issues/3963) – After removing a monomer from Favorites tab, its tooltip does not disappear and interferes interaction with other monomers
- [#10021](https://github.com/epam/ketcher/issues/10021) – Hover structure using Structure selection tool shows outline for each atom/bond separately
- [#6177](https://github.com/epam/ketcher/issues/6177) – System losts hydrogen bond connections between monomers
- [#3437](https://github.com/epam/ketcher/issues/3437) – Preview and displaying of Cycloheptane on the canvas doesn't match
- [#10095](https://github.com/epam/ketcher/issues/10095) – Indicator number on an antisense chain
- [#7980](https://github.com/epam/ketcher/issues/7980) – Undo in Sequence mode restores bond detached from monomer abbreviation
- [#7822](https://github.com/epam/ketcher/issues/7822) – Already taken connection points are not marked
- [#10238](https://github.com/epam/ketcher/issues/10238) – Search by IDT alias with position indicator
- [#4452](https://github.com/epam/ketcher/issues/4452) – System doesn't allow to unselect already selected nucleotides
- [#10040](https://github.com/epam/ketcher/issues/10040) – Provide a support for one or several different BIOVIA Specifications
- [#7536](https://github.com/epam/ketcher/issues/7536) – Incorrect preview position when adding monomer via arrow button after Undo operation
- [#2198](https://github.com/epam/ketcher/issues/2198) – Save button enabled when Molecule name contains only spaces
- [#9121](https://github.com/epam/ketcher/issues/9121) – The Attributes panel should be disabled for a non-continuous selection of the Nucleotide (preset) type
- [#9555](https://github.com/epam/ketcher/issues/9555) – Multiple side chain connection linkers
- [#6162](https://github.com/epam/ketcher/issues/6162) – RemoteStructServiceProvider Custom Header does not sent to backend
- [#8249](https://github.com/epam/ketcher/issues/8249) – Prevent hanging hydrogen bond when typing after antisense ove
- [#7621](https://github.com/epam/ketcher/issues/7621) – Fix monomer wizard notification scrolling and stale error state
- [#4716](https://github.com/epam/ketcher/issues/4716) – Individual sequences are merged by replacing the middle sequence in Sequence mode
- [#5661](https://github.com/epam/ketcher/issues/5661) – Carbon label doesn't apper in case of 180 degree angle on macro mode
- [#6004](https://github.com/epam/ketcher/issues/6004) – Stereo flag (ABS) position ignoring text and shapes
- [#10196](https://github.com/epam/ketcher/issues/10196) – Disable the "Open..." and "Save as..." icons in the Creation Wizard mode
- [#4663](https://github.com/epam/ketcher/issues/4663) – Wrong Preset name with technical information while copy/paste Preset name
- [#10269](https://github.com/epam/ketcher/issues/10269) – Incorrect monomer name is loaded into the wizard when using "Edit Instance" option
- [#6767](https://github.com/epam/ketcher/issues/6767) – Dashes (lines) are missing in sense chains
- [#8608](https://github.com/epam/ketcher/issues/8608) – System should not allow to create monomer for molecule that has explicitly defined R-Group connected to non-complient bond
- [#10280](https://github.com/epam/ketcher/issues/10280) – Rotation tool: Rotation center color remains unchanged on hover when whole structure is selected
- [#10351](https://github.com/epam/ketcher/issues/10351) – Replace Chlorophyll A_dative molecule in the library from v3000 format to v2000 one
- [#10283](https://github.com/epam/ketcher/issues/10283) – Rotation tool: Current rotation angle values remain positive beyond 180 degrees instead of switching to negative
- [#10322](https://github.com/epam/ketcher/issues/10322) – Undo operation doesn't work in some cases
- [#6826](https://github.com/epam/ketcher/issues/6826) – Undo/Redo after deleting a sequence via right-click places it incorrectly in the sequence list
- [#5442](https://github.com/epam/ketcher/issues/5442) – Bond preview tooltip layout is wrong for unknown monomers
- [#10346](https://github.com/epam/ketcher/issues/10346) – Update the help document (3.17.)
- [#11335](https://github.com/epam/ketcher/issues/11335) – Errors in console when Reaction Plus tool is active

---

### Additional notes:
- Ketcher 3.18.0 has been built and tested with Indigo version 1.46 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.46.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.46.0/images)).
