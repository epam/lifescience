**Summary**

We are happy to announce that new version 2.6.0 of Ketcher has been released.

Ketcher 2.6.0 release was focused on adding support agents in reactions and updating of Ketcher API along with the delivery of other functions.

Please be aware Ketcher 2.6.0 has been tested with Indigo version 1.8.0 ([standalone](https://www.npmjs.com/package/indigo-ketcher/v/1.8.0) and [remote](https://hub.docker.com/layers/epmlsop/indigo-service/1.8.0/images/sha256-31b184c42594228230b063cfe4dd35fd163d7add5c682689e96c5e23e3d72290?context=explore)).

The whole list of changes can be found below.

## What's Changed

**New features and improvements**

* #1717: ketcher/example doc (or code) is broken. Updated docs https://github.com/epam/ketcher/pull/1721
* #1722: Implement addFragment method https://github.com/epam/ketcher/pull/1759
* #1723: convert Daylight SMILES using indigo API https://github.com/epam/ketcher/pull/1726
* #1734: Support CDXML in Ketcher https://github.com/epam/ketcher/pull/1766
* #1753: Add dearomatize on load to settings https://github.com/epam/ketcher/pull/1769
* #1754: Add method set/get setting to the Ketcher API https://github.com/epam/ketcher/pull/1769
* #1755: Block UI when setMolecule is called https://github.com/epam/ketcher/pull/1765
* #1757: Reduce unnecessary info call https://github.com/epam/ketcher/pull/1761
* Fix typo https://github.com/epam/ketcher/pull/1742

**Bugfixes**
* #1404: Text cannot be exported to pictures 
* #1616: The added Reaction Plus to the structure is lost after applying the Layout 
* #1700: PNG file is not shown in Remote
* #1701: SVG file is not shown in Remote
* #1709: Text nodes lose after save to SVG
* #1717: ketcher/example doc (or code) is broken https://github.com/epam/ketcher/pull/1721
* #1733: Ketcher creates invalid molfiles with "NaN" https://github.com/epam/ketcher/pull/1779
* #1735: Update Ketcher format for text node https://github.com/epam/ketcher/pull/1737
* #1736: Can't save as an rxn file if reaction consists of two or more reaction arrows https://github.com/epam/ketcher/pull/1749
* #1741: Cannot read properties of undefined (reading 'aid') https://github.com/epam/ketcher/pull/1748
* #1762: File with text saved in .ket format won't open https://github.com/epam/ketcher/pull/1763
* #1792: Pasting Ket files with Unicode is failed https://github.com/epam/ketcher/pull/1793
