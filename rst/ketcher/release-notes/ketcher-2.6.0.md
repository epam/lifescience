# Ketcher 2.6.0

**Summary**

We are happy to announce that new version 2.6.0 of Ketcher has been released.

Ketcher 2.6.0 release was focused on adding support agents in reactions and updating of Ketcher API along with the delivery of other functions.

Please be aware Ketcher 2.6.0 has been tested with Indigo version 1.8.0 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.8.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.8.0/images/sha256-31b184c42594228230b063cfe4dd35fd163d7add5c682689e96c5e23e3d72290?context=explore)).

The whole list of changes can be found below.

**New features and improvements**

* [#1717](https://github.com/epam/ketcher/issues/1717): ketcher/example doc (or code) is broken. Updated docs 
* [#1722](https://github.com/epam/ketcher/issues/1722): Implement addFragment method
* [#1723](https://github.com/epam/ketcher/issues/1723): convert Daylight SMILES using indigo API
* [#1734](https://github.com/epam/ketcher/issues/1734): Support CDXML in Ketcher
* [#1753](https://github.com/epam/ketcher/issues/1753): Add dearomatize on load to settings
* [#1754](https://github.com/epam/ketcher/issues/1754): Add method set/get setting to the Ketcher API 
* [#1755](https://github.com/epam/ketcher/issues/1755): Block UI when setMolecule is called
* [#1757](https://github.com/epam/ketcher/issues/1757): Reduce unnecessary info call
* Fix [#typo](https://github.com/epam/ketcher/pull/1742)

**Bugfixes**
* [#1404](https://github.com/epam/ketcher/issues/1404): Text cannot be exported to pictures 
* [#1616](https://github.com/epam/ketcher/issues/1616): The added Reaction Plus to the structure is lost after applying the Layout 
* [#1700](https://github.com/epam/ketcher/issues/1700): PNG file is not shown in Remote
* [#1701](https://github.com/epam/ketcher/issues/1701): SVG file is not shown in Remote
* [#1709](https://github.com/epam/ketcher/issues/1709): Text nodes lose after save to SVG
* [#1717](https://github.com/epam/ketcher/issues/1717): ketcher/example doc (or code) is broken
* [#1733](https://github.com/epam/ketcher/issues/1733): Ketcher creates invalid molfiles with "NaN" 
* [#1735](https://github.com/epam/ketcher/issues/1735): Update Ketcher format for text node
* [#1736](https://github.com/epam/ketcher/issues/1736): Can't save as an rxn file if reaction consists of two or more reaction arrows
* [#1741](https://github.com/epam/ketcher/issues/1741): Cannot read properties of undefined (reading 'aid')
* [#1762](https://github.com/epam/ketcher/issues/1762): File with text saved in .ket format won't open 
* [#1792](https://github.com/epam/ketcher/issues/1792): Pasting Ket files with Unicode is failed 
