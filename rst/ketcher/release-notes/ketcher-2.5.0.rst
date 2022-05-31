Ketcher 2.5.0
#############

*30 May 2022*

*******
Summary
*******

We are happy to announce that new version `2.5.0 <https://github.com/epam/ketcher/releases/tag/v2.5.0>`__ of Ketcher has been released. 

Ketcher 2.5 release was focused on improving the user experience and design of the application along with delivery of other functions.
It has fresh and updated icons combined with renewed color scheme and new canvas zoom approach. Fullscreen ability can provide great sketcher experience even if Ketcher is embedded in the small frame. File operations flows and other functions have received an improved flows and renewed dialog windows. Access to the Extended table became much more easy and Template library will now combine ready-for-use templates along with set of predefined functional groups.

Please be aware Ketcher 2.5 has been tested with Indigo version 1.7.1 (`standalone <https://www.npmjs.com/package/indigo-ketcher/v/1.7.1>`__ and `remote <https://hub.docker.com/layers/indigo-service/epmlsop/indigo-service/1.7.1/images/sha256-007b5c395f6cbc6d2ec81c93a46ff343fb268096e9e747b52ede0516fd043792?context=explore>`__).

The whole list of changes can be found below.


**New features and improvements** 

* Ketcher redesign (see `related issues <https://github.com/epam/ketcher/issues?q=is%3Aissue+is%3Aclosed+milestone%3A%22Release+2.5.0%22+label%3A%22epic%3A+new+ux%2Fui%22>`__ for details)
* Full-screen mode support for Ketcher `#1273 <https://github.com/epam/ketcher/issues/1273>`__
* use iframe embed standalone version ketcher init error `#1235 <https://github.com/epam/ketcher/issues/1235>`__
* Implement miew viewer with miew-react `#1188 <https://github.com/epam/ketcher/issues/1188>`__
* Extend ketcher API: Add possibility to run server functions `#1172 <https://github.com/epam/ketcher/issues/1172>`__
* Arrow Tool: Elliptical Arrows `#1045 <https://github.com/epam/ketcher/issues/1045>`__
* Text Tool: Add special symbols `#1044 <https://github.com/epam/ketcher/issues/1044>`__
* Option to save as InChIKey `#1334 <https://github.com/epam/ketcher/issues/1334>`__
* Enabling wildcard atom button in top-level UI `#1409 <https://github.com/epam/ketcher/issues/1409>`__
* Support of custom headers `#1628 <https://github.com/epam/ketcher/issues/1628>`__


**Bugfixes**

* Cannot deserialize input JSON if using Clean Up functionality on structure containing R-Groups `#1391 <https://github.com/epam/ketcher/issues/1391>`__
* Via ketcher The size of mol displayed in the editor is inconsistent between calling ketcher.setMolecule(）and direct copy and paste `#1322 <https://github.com/epam/ketcher/issues/1322>`__
* An error message is displayed when server functions are applied to an R-group member with invalid stereocenters. `#1452 <https://github.com/epam/ketcher/issues/1452>`__
* Functional Group abbreviation context menu can't be opened without selecting FG `#1386 <https://github.com/epam/ketcher/issues/1386>`__
* Invisible enhanced flag interferes with user selection `#1332 <https://github.com/epam/ketcher/issues/1332>`__
* Strict mode warnings in console `#1290 <https://github.com/epam/ketcher/issues/1290>`__
* Button group is not be presented if ketcher is in a drawer `#1325 <https://github.com/epam/ketcher/issues/1325>`__
* Focus lost on second symbol while trying to enter atom label `#1294 <https://github.com/epam/ketcher/issues/1294>`__
* Incorrect vertical scrollbar when saving in Daylight SMILES format `#1307 <https://github.com/epam/ketcher/issues/1307>`__
* Sending structure to renderer in molfile format instead of ketcher format `#1300 <https://github.com/epam/ketcher/issues/1300>`__
* Structure check modal window causes error when closed right after update `#1291 <https://github.com/epam/ketcher/issues/1291>`__
* Incorrect horizontal scrollbars in Save Structure modal window `#1292 <https://github.com/epam/ketcher/issues/1292>`__
* Templates with simple objects are incorrect after refreshing the page `#1276 <https://github.com/epam/ketcher/issues/1276>`__
* Shift between pointer and atom `#1272 <https://github.com/epam/ketcher/issues/1272>`__
* ketcher-react not working out of the box with create-react-app `#1241 <https://github.com/epam/ketcher/issues/1241>`__
* Error on opening .txt file `#1149 <https://github.com/epam/ketcher/issues/1149>`__
* Settings - Preview images of structures (Templates Library, FG Library) do not respect global display settings `#900 <https://github.com/epam/ketcher/issues/900>`__
* Clear Canvas hotkey not working on MacOS `#397 <https://github.com/epam/ketcher/issues/397>`__
* can not setMolecule in onInit `#1174 <https://github.com/epam/ketcher/issues/1174>`__
* Stereomarks and stereoflag are not displayed for templates with stereocenters `#1258 <https://github.com/epam/ketcher/issues/1258>`__
* Atom IDs are not shown when settings specify to display them `#1231 <https://github.com/epam/ketcher/issues/1231>`__
* Extra scrollbar in Data S-Groups modal when Field name contains long string `#1312 <https://github.com/epam/ketcher/issues/1312>`__
* Tool refers to unmounted canvas instance when new file is opened `#1057 <https://github.com/epam/ketcher/issues/1057>`__
* Open, Save and Reset buttons in Settings window looks unclickable (grey) `#1350 <https://github.com/epam/ketcher/issues/1350>`__
* Incorrect double click behavior in Custom Templates window `#1364 <https://github.com/epam/ketcher/issues/1364>`__
* No waiting for server to respond between Structure Check checkboxes turning on/off `#1367 <https://github.com/epam/ketcher/issues/1367>`__
* The floating windows don't close after clicking on the ESC button `#1504 <https://github.com/epam/ketcher/issues/1504>`__
* Different merging of templates from template list and from template library `#1587 <https://github.com/epam/ketcher/issues/1587>`__
* It's not possible to select parts of different structures using the 'Shift' key. `#1552 <https://github.com/epam/ketcher/issues/1552>`__
* It's possible to create a custom template with a duplicate name `#1553 <https://github.com/epam/ketcher/issues/1553>`__
* Incorrect rendering of Data S-Group when it is applied to part of the cyclic structure `#1575 <https://github.com/epam/ketcher/issues/1575>`__
* List/Not List atoms are converted to 'L#' symbols after the replacement of atoms by the R-group label is undone `#1530 <https://github.com/epam/ketcher/issues/1530>`__
* Cannot deserialize input JSON if using server functionalities on a structure containing Not List atoms `#1603 <https://github.com/epam/ketcher/issues/1603>`__
* Wrong sign for specific types while ket-generation `#1600 <https://github.com/epam/ketcher/issues/1600>`__
* Unable to save a reaction in server formats if text is present on the canvas `#1444 <https://github.com/epam/ketcher/issues/1444>`__
* Elements should be hidden when the attribute hiddenControls is used `#1601 <https://github.com/epam/ketcher/issues/1601>`__
* The valence of monovalent atoms is displayed incorrectly in the structure after the Copy/Paste actions `#1531 <https://github.com/epam/ketcher/issues/1531>`__
* The structure with reaction is displayed incorrectly after applying the Layout `#1617 <https://github.com/epam/ketcher/issues/1617>`__
* R-Group definition changes when server functions are applied `#1487 <https://github.com/epam/ketcher/issues/1487>`__