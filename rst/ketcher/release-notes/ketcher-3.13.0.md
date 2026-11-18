
# Ketcher 3.13.0

## What's Changed

### New features
- [#8948](https://github.com/epam/ketcher/issues/8948) – Add fragment selection tool and rename structure selection tooltip

### Bugfixes and improvements
- [#8245](https://github.com/epam/ketcher/issues/8245) – Small molecules positioning rule is not respected when connected to multiple monomers in different chains
- [#7927](https://github.com/epam/ketcher/issues/7927) – Monomer area selection works wrong if user uses mouse wheel to scroll down
- [#7729](https://github.com/epam/ketcher/issues/7729) – “Field value” textbox is active in “S-Group Properties” modal when “Context” field is empty
- [#7899](https://github.com/epam/ketcher/issues/7899) – CIP labels got rendered under the bond after atom selection and move
- [#8981](https://github.com/epam/ketcher/issues/8981) – Stereo bonds between monomers become single bonds if monomer collapsed
- [#8986](https://github.com/epam/ketcher/issues/8986) – ketcher-standalone memory leak
- [#8980](https://github.com/epam/ketcher/issues/8980) – System shows bad valence for atoms that attached to bonds that connects monomers
- [#8987](https://github.com/epam/ketcher/issues/8987) – Labels for monomer natural analog category is missing if filter applied
- [#7153](https://github.com/epam/ketcher/issues/7153) – Molecule from expanded monomer disappears on switching to Macromolecules mode
- [#9065](https://github.com/epam/ketcher/issues/9065) – System shows natural analog category for phosphates
- [#9078](https://github.com/epam/ketcher/issues/9078) – Update the help document (3.12.)
- [#9084](https://github.com/epam/ketcher/issues/9084) – Ketcher saves incorrect attachment points configuration for new nucleotides

---

### Additional notes:
- Ketcher 3.13.0 has been built and tested with Indigo version 1.41 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.41.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.41.0/images/sha256-3a49239844d663ff211b3b231066b7e78f99008c73236d7b772c2af368cbe268)).
