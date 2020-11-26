Ketcher 2.1.0 beta
##################

*26 November 2020*

*******
Summary
*******

We are glad to announce that a new version of Ketcher **2.1.0 beta** is released. 

`Github <https://github.com/epam/ketcher/releases/tag/v2.1.0-beta>`__

The main features delivered in this release are migration to React, new drawing tool for simple objects (Circle and Rectangle), and ability to download Ketcher as NPM package. 
The whole list of changes can be found below.

**New features and improvements** 

* Introduce Graph format to Ketcher `#53 <https://github.com/epam/ketcher/issues/53>`__

* Migrate Ketcher to React `#70 <https://github.com/epam/ketcher/issues/70>`__

* Need to create the warning message in the case if user tries to save incorrect structure in non-Mol format `#47 <https://github.com/epam/ketcher/issues/47>`__

* Mount on DOM element `#7 <https://github.com/epam/ketcher/issues/7>`__

* Add drawing tool for simple objects `#66 <https://github.com/epam/ketcher/issues/66>`__


**Bugfixes**

* Warning message should appear for S-Groups and Data S-Group while saving in Extended SMILES and Inchi Auxinfo formats `#36 <https://github.com/epam/ketcher/issues/36>`__

* surpressing window.alert popups `#83 <https://github.com/epam/ketcher/issues/83>`__

* Keacher API: add a method to clear ketcher's drawing area `#87 <https://github.com/epam/ketcher/issues/87>`__

* If you fuse a ring to an already drawn one that contains a double bond, the bond is overwritten `#79 <https://github.com/epam/ketcher/issues/79>`__

* Recognize function does not work `#95 <https://github.com/epam/ketcher/issues/95>`__

* Recognize Molecule: pictures in tif-format cannot be loaded `#28 <https://github.com/epam/ketcher/issues/28>`__

