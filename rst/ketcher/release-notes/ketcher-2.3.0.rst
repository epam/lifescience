Ketcher 2.3.0
#############

*22 July 2021*

*******
Summary
*******

We are glad to announce that a new stable version of Ketcher `2.3.0 <https://github.com/epam/ketcher/releases/tag/v2.3.0>`__ is released. 
The main features implemented in scope of this release are support of enhanced stereochemistry, ability to save structure as an image file, text tool, and support of multiple reaction arrows.


**New features and improvements** 

* Stereo Flags shouldn't appear for structures without correct stereocenters `#418 <https://github.com/epam/ketcher/issues/418>`__ 

* It's impossible to open Ketcher with already entered molecule `#601 <https://github.com/epam/ketcher/issues/601>`__

* Add a warning when saving a reaction equilibrium arrow in a format that does not support it `#543 <https://github.com/epam/ketcher/issues/543>`__

* Add possibility to replace api path while App is building by passing additional argument `#507 <https://github.com/epam/ketcher/issues/507>`__

* Add multiple arrow support for the same canvas `#145 <https://github.com/epam/ketcher/issues/145>`__

* SETTINGS for the STEREO FLAGS and STEREO MARKS `#60 <https://github.com/epam/ketcher/issues/60>`__

* SAVE and OPEN STRUCTURE with STEREO MARKS `#64 <https://github.com/epam/ketcher/issues/64>`__

* Set PUBLIC_URL as './' by default `#508 <https://github.com/epam/ketcher/issues/508>`__

* Add possibility to add plain text on canvas `#144 <https://github.com/epam/ketcher/issues/144>`__

* Colors for the STEREO FLAGS and STEREO MARKS `#62 <https://github.com/epam/ketcher/issues/62>`__

* Implement "Create Stereo Marks" window `#417 <https://github.com/epam/ketcher/issues/417>`__

* Add support for hydrogen bonds `#72 <https://github.com/epam/ketcher/issues/72>`__

* Representation of Stereo Flags `#57 <https://github.com/epam/ketcher/issues/57>`__

* Stereocenter should disappear after replacing the stereobond with the dative bond or the double cis/trans bond `#554 <https://github.com/epam/ketcher/issues/554>`__

* Implement "Enhanced Stereochemistry" window `#527 <https://github.com/epam/ketcher/issues/527>`__

* Chiral flag should be removed when all Up/Down stereobonds are removed `#61 <https://github.com/epam/ketcher/issues/61>`__

* User can change the text of the four Stereo flags `#518 <https://github.com/epam/ketcher/issues/518>`__

* Rename the "Do not show the Stereo flags" setting and change the default value `#556 <https://github.com/epam/ketcher/issues/556>`__

* Rendering only feature `#107 <https://github.com/epam/ketcher/issues/107>`__

* Add possibility to save structure as image `#437 <https://github.com/epam/ketcher/issues/437>`__

* Unclear/inconsistent handling of absolute/relative stereochemistry `#290 <https://github.com/epam/ketcher/issues/290>`__

* Label Display At Stereogenic Centers for the STEREO FLAGS and STEREO MARKS `#63 <https://github.com/epam/ketcher/issues/63>`__

* Extend Text tool by bold, italic, subscript and superscript support `#339 <https://github.com/epam/ketcher/issues/339>`__

* Move dative/hydrogen bond tools to a separate block in the 'Bond' tool menu `#538 <https://github.com/epam/ketcher/issues/538>`__

* Add the ability to save information about the coordinates of the Stereo flags in * .ket `#559 <https://github.com/epam/ketcher/issues/559>`__

* Update position of stereo flag while structure is moved `#167 <https://github.com/epam/ketcher/issues/167>`__


**Bugfixes**

* Adding a stereo flag when opening the structure `#632 <https://github.com/epam/ketcher/issues/632>`__

* Incorrect template addition `#676 <https://github.com/epam/ketcher/issues/676>`__

* The descriptor overlaps the structure after Layout `#219 <https://github.com/epam/ketcher/issues/219>`__

* Layout action does not work on the distorted S-group members `#671 <https://github.com/epam/ketcher/issues/671>`__

* No alert error message when trying to open incorrect InChi string `#657 <https://github.com/epam/ketcher/issues/657>`__

* "Undo" after template merging does not work correctly `#670 <https://github.com/epam/ketcher/issues/670>`__

* Stereo-label doesn't update after stereoBond flipping `#661 <https://github.com/epam/ketcher/issues/661>`__

* Left toolbar is not visible in Firefox `#612 <https://github.com/epam/ketcher/issues/612>`__

* Redo does not work for simple object "Shape line" after moving its dots `#635 <https://github.com/epam/ketcher/issues/635>`__

* IE: Save as *.svg file does not work `#627 <https://github.com/epam/ketcher/issues/627>`__

* Atom is not underlined in red after adding to the template `#636 <https://github.com/epam/ketcher/issues/636>`__

* Application crashes after saving a template `#652 <https://github.com/epam/ketcher/issues/652>`__

* The incorrect structure when marks "Load as fragment" `#633 <https://github.com/epam/ketcher/issues/633>`__

* IE: The structure does not open `#624 <https://github.com/epam/ketcher/issues/624>`__

* The application doesn't work after "Undo" `#615 <https://github.com/epam/ketcher/issues/615>`__

* When marks "Load as fragment and copy to the Clipboard" structure don't save to clipboard `#634 <https://github.com/epam/ketcher/issues/634>`__

* Modal windows don't close when pressing the esc button `#626 <https://github.com/epam/ketcher/issues/626>`__

* The structure with R-Group is not visible `#621 <https://github.com/epam/ketcher/issues/621>`__

* Multiple arrows are saved as a reaction in Daylight Smiles format `#590 <https://github.com/epam/ketcher/issues/590>`__

* Ketcher build does not work on Linux `#505 <https://github.com/epam/ketcher/issues/505>`__

* Rotation angle doesn't display after I change its value `#380 <https://github.com/epam/ketcher/issues/380>`__

* 'Calculated values' - The data in 'Elemental analysis' field is displayed incorrectly `#445 <https://github.com/epam/ketcher/issues/445>`__

* Calculated values: old values blink before displaying new once `#389 <https://github.com/epam/ketcher/issues/389>`__

* 'Add text' - The initially created text object remains selected after adding the second one `#464 <https://github.com/epam/ketcher/issues/464>`__

* 'Add text' - It's not obvious how to reduce the "Text editor" window when a scroll is present in it `#473 <https://github.com/epam/ketcher/issues/473>`__

* 'Add text'- Impossible to edit a single letter text object `#470 <https://github.com/epam/ketcher/issues/470>`__

* 'Add text' - Double scroll appears when a long text is entered into the "Text editor" window `#467 <https://github.com/epam/ketcher/issues/467>`__

* 'Save Structure' and 'Structure Check' windows are enlarged when trying to save/check a big molecule `#454 <https://github.com/epam/ketcher/issues/454>`__

* It is possible to save a structure in incorrect format when network connection is slow `#456 <https://github.com/epam/ketcher/issues/456>`__

* The error occurs when trying to undo the delete action for a structure with stereo bonds `#485 <https://github.com/epam/ketcher/issues/485>`__

* Blank page appears after trying to save a reaction with an R-Group member `#488 <https://github.com/epam/ketcher/issues/488>`__

* A part of S-group brackets is enlarged after Cut - Undo actions `#448 <https://github.com/epam/ketcher/issues/448>`__

* 'Add text'- 'Cut'/'Copy' buttons become enabled when a text object is added to the canvas `#472 <https://github.com/epam/ketcher/issues/472>`__

* Incorrect rendering of Stereo Flags in reactions `#58 <https://github.com/epam/ketcher/issues/58>`__

* Console error after delete - undo/redo actions with a structure with stereobonds `#573 <https://github.com/epam/ketcher/issues/573>`__

* "Help" module doesn't display correctly in IE11 `#572 <https://github.com/epam/ketcher/issues/572>`__

* Incorrect stereo flag calculation `#579 <https://github.com/epam/ketcher/issues/579>`__

* Browser crash when copy and paste a sgroup structure `#592 <https://github.com/epam/ketcher/issues/592>`__

* Stereo labels after pasting display incorrectly `#194 <https://github.com/epam/ketcher/issues/194>`__

* The Stereo labels and Attached Data keep their positions after the Flip action `#201 <https://github.com/epam/ketcher/issues/201>`__

* Stereo Flag is not highlighted `#604 <https://github.com/epam/ketcher/issues/604>`__

* Vertical/Horizontal flip hot keys don't work correctly `#524 <https://github.com/epam/ketcher/issues/524>`__

* Error message when copying structure `#606 <https://github.com/epam/ketcher/issues/606>`__

* Blank page and a console error appear while saving `#514 <https://github.com/epam/ketcher/issues/514>`__

* Simple objects - An error in console after the 'Undo' action `#511 <https://github.com/epam/ketcher/issues/511>`__

* 'Add text'- 'Cut'/'Copy' buttons are disabled when a text object is added to the canvas `#522 <https://github.com/epam/ketcher/issues/522>`__

* Error message when trying to open *.ket files with stereochemistry features `#532 <https://github.com/epam/ketcher/issues/532>`__

* 3D Viewer - The light mode doesn't work `#531 <https://github.com/epam/ketcher/issues/531>`__

* Stereo flags are confused with stereo marks in *.ket files `#544 <https://github.com/epam/ketcher/issues/544>`__

* Unable to paste the text objects after cut/copy `#551 <https://github.com/epam/ketcher/issues/551>`__

* The periodic table opens when a text object is selected with the Lasso/Rectangle/Fragment selection tools `#549 <https://github.com/epam/ketcher/issues/549>`__

* Stereo label (E) saves in .smi file `#208 <https://github.com/epam/ketcher/issues/208>`__

* Wrong modal window, a blank page and an error in console after trying to add the Attachment points/R-sites to a structure `#499 <https://github.com/epam/ketcher/issues/499>`__
