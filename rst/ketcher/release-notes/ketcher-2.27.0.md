
# Ketcher 2.27.0

## What's Changed

Here are the updated release notes with links to the corresponding issues:

### New features
* [#5354](https://github.com/epam/ketcher/issues/5354) – Apply new hash spacing setting to canvas
* [#5579](https://github.com/epam/ketcher/issues/5579) – Introduce Hand tool for macromolecules mode
* [#5590](https://github.com/epam/ketcher/issues/5590) – Zoom in macromolecules mode should be in relation to the top left corner of the structures
* [#5403](https://github.com/epam/ketcher/issues/5403) – Introduce hydrogen bonds in macromolecules mode
* [#5600](https://github.com/epam/ketcher/issues/5600) – Zoom in automatically upon import of small sequences
* [#5637](https://github.com/epam/ketcher/issues/5637) – Display hydrogen in atom label for molecules in macromolecules mode
* [#5556](https://github.com/epam/ketcher/issues/5556) – Allow import and export of sequences with three letter amino acid codes
* [#5640](https://github.com/epam/ketcher/issues/5640) – Multiple monomers expansion in micro molecules mode
* [#5187](https://github.com/epam/ketcher/issues/5187) – Introduce new amino-acid colors
* [#6174](https://github.com/epam/ketcher/issues/6174) – Update indigo to 1.26.0 in browser module

### Bugfixes and improvements
* [#5370](https://github.com/epam/ketcher/issues/5370) – System should remember the canvas mode on Molecules/Macromolecules mode switch (do not switch to Sequernce by default)
* [#5372](https://github.com/epam/ketcher/issues/5372) – Toggling between Flex and Sequence modes causes loosing layout info
* [#5564](https://github.com/epam/ketcher/issues/5564) – Search of ambiguous monomers doesn't work
* [#4475](https://github.com/epam/ketcher/issues/4475) – Numbers on top of letters are not centered
* [#4936](https://github.com/epam/ketcher/issues/4936) – Applying Enhanced Stereochemistry to monomers causes its disappear from the canvas (and exception in console)
* [#4941](https://github.com/epam/ketcher/issues/4941) – System shows Edit S-Group option for every bond of molecule if it has attachment point
* [#5181](https://github.com/epam/ketcher/issues/5181) – getKet duplicates items when macro molecules are use
* [#5398](https://github.com/epam/ketcher/issues/5398) – Elliptic arrow icons order is wrong at arrow toolbar
* [#5935](https://github.com/epam/ketcher/issues/5935) – Unable to establish hydrogen bond connection if monomer has no free attachment points
* [#5941](https://github.com/epam/ketcher/issues/5941) – Hydrogen bonds remain in place on monomer delete
* [#5940](https://github.com/epam/ketcher/issues/5940) – Copy/paste operation works wrong (copy only two hydrogen bonds and drops others)
* [#5933](https://github.com/epam/ketcher/issues/5933) – Error message is wrong if user tries to establish hydrogen bond if it is already exist
* [#5967](https://github.com/epam/ketcher/issues/5967) – System should not change monomer position after switching from Molecules to Macromolecules - Sequence
* [#5972](https://github.com/epam/ketcher/issues/5972) – Export to three letter amino acid codes cause convert error
* [#5969](https://github.com/epam/ketcher/issues/5969) – Load from file having only micro structures on macro canvas causes unnecessary zoom up to 200% and shift molecule to top left angle
* [#5970](https://github.com/epam/ketcher/issues/5970) – Unable to connect monomer to molecule in snake mode
* [#5949](https://github.com/epam/ketcher/issues/5949) – Delete of micro molecules bonds works wrong (or doesn't work)
* [#5910](https://github.com/epam/ketcher/issues/5910) – Fix closest sgroup detection to allow focusing on entities within expanded monomer's bounding box
