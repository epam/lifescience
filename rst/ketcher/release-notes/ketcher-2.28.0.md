
# Ketcher 2.28.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
- [#5678](https://github.com/epam/ketcher/issues/5678) - Introduce creating antisense chains
- [#5925](https://github.com/epam/ketcher/issues/5925) - Layout for antisense chains in sequence mode
- [#5712](https://github.com/epam/ketcher/issues/5712) - Update snake layout logic taking into account hydrogen bonds
- [#5990](https://github.com/epam/ketcher/issues/5990) - Extend Ketcher API to allow updating monomers library
- [#5630](https://github.com/epam/ketcher/issues/5630) - Mark all modified monomers on canvas (flex and snake modes)
- [#5629](https://github.com/epam/ketcher/issues/5629) - Mark modified amino acids on canvas in sequence mode
- [#5854](https://github.com/epam/ketcher/issues/5854) - Add "Copy to Clipboard" to the export window
- [#5618](https://github.com/epam/ketcher/issues/5618) - Ketcher doesn't trigger change event in macromolecule mode
- [#5515](https://github.com/epam/ketcher/discussions/5515) - Add ketcher calculate values API
- [#6008](https://github.com/epam/ketcher/issues/6008) - Update indigo to 1.27.0 in browser module


### Bugfixes and improvements
- [#5873](https://github.com/epam/ketcher/issues/5873) - Export to ket (and getKET function) change incrementally internal IDs every call
- [#5270](https://github.com/epam/ketcher/issues/5270) - Warning should not displayed for importing CDXML, base64 CDX
- [#5351](https://github.com/epam/ketcher/issues/5351) - Inform User to Apply Layout after Settings Adjustment
- [#5931](https://github.com/epam/ketcher/issues/5931) - Copy/Cut-Paste functionality not working for microstructures in Macro mode
- [#5982](https://github.com/epam/ketcher/issues/5982) - Label shift problem for ambiguous monomers
- [#5954](https://github.com/epam/ketcher/issues/5954) - The reaction with catalysts is displayed incorrect with ACS style setting and after layout
- [#4352](https://github.com/epam/ketcher/issues/4352) - Gap between button and drop-down list of Macro modes
- [#5855](https://github.com/epam/ketcher/issues/5855) - System reset micromolecule canvas settings to default if switched to Macro mode and back
- [#5974](https://github.com/epam/ketcher/issues/5974) - Paste to canvas recogniton logic should be changed
- [#3813](https://github.com/epam/ketcher/issues/3813) - Page auto jump to top when ketcher editor inited
- [#5988](https://github.com/epam/ketcher/issues/5988) - Exception when modifying a functional group after adding a Ketcher editor subscription
- [#6068](https://github.com/epam/ketcher/issues/6068) - Same chain configuration imported by different HELM layouted differently (anyway - both are wrong)
- [#6089](https://github.com/epam/ketcher/issues/6089) - Antisense creation doesn't work for the chain if not eligable base present in other chain presented in selection
- [#6061](https://github.com/epam/ketcher/issues/6061) - RNA chain remain flipped after hydrogen bond removal
- [#6067](https://github.com/epam/ketcher/issues/6067) - Two chains connected by H-bond arranged wrong if third bond present on the canvas
- [#6070](https://github.com/epam/ketcher/issues/6070) - System doesn't flip chain if connected to monomer but not to base
- [#6074](https://github.com/epam/ketcher/issues/6074) - System doesn't flip chain if connected to monomer but not to base (2)
- [#6080](https://github.com/epam/ketcher/issues/6080) - System doesn't flip chain if connected to monomer but not to base (3)
- [#6075](https://github.com/epam/ketcher/issues/6075) - In case of multipal H-bonds system should arrange antisence chain to first base of bottom chain
- [#6076](https://github.com/epam/ketcher/issues/6076) - Two-to-one base H-bond connection layouted wrong
- [#6077](https://github.com/epam/ketcher/issues/6077) - H-bond is not alligned to Snake mode view in some cases
- [#6081](https://github.com/epam/ketcher/issues/6081) - Smaller chain should be at the bottom
- [#6087](https://github.com/epam/ketcher/issues/6087) - Antisense layout is wrong for any ambiguouse base from the library
- [#6097](https://github.com/epam/ketcher/issues/6097) - System creates antisense chain only for top chain if many of chains selected
- [#6102](https://github.com/epam/ketcher/issues/6102) - System keeps antisense base layout and enumeration even after chain stops being antisense (and vice versa)
- [#6105](https://github.com/epam/ketcher/issues/6105) - Layout works wrong if bases of the same chain connected by H-bonds
- [#6086](https://github.com/epam/ketcher/issues/6086) - Unable to create antisense chains for ambiguous monomers from the library
- [#6107](https://github.com/epam/ketcher/issues/6107) - Create Antisense Strand doesn't work in some cases
- [#6096](https://github.com/epam/ketcher/issues/6096) - Antisense creation works wrong in case of partial selection
- [#6109](https://github.com/epam/ketcher/issues/6109) - Antisense of layout doesn't work on flex mode after load
- [#6083](https://github.com/epam/ketcher/issues/6083) - Creation of antisense chain causes monomer re-arrangement on the flex canvas
- [#6115](https://github.com/epam/ketcher/issues/6115) - Lets get back to U (instead of T) for the complementary base of A
- [#6129](https://github.com/epam/ketcher/issues/6129) - Undo operation creates unremovable bonds on the canvas (clear canvas doesn't help)
- [#6161](https://github.com/epam/ketcher/issues/6161) - Stereo flags are displayed despite enabling 'Ignore chiral flag' in MOL V2000 files
- [#6185](https://github.com/epam/ketcher/issues/6185) – Make SGroups expandable while placed within a chain