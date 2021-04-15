Ketcher 2.2.0
#############

*15 April 2021*

*******
Summary
*******

We are glad to announce that a new stable version of Ketcher `2.2.0 <https://github.com/epam/ketcher/releases/tag/v2.2.0>`__ is released. 
The main goal of current release was adding support of standalone mode. 
The list of changes related to this functionality can be found `here <https://github.com/epam/ketcher/milestone/3>`__. 


**New features and improvements** 

* Get Molfile in v3000 format `#21 <https://github.com/epam/ketcher/issues/21>`__ 

* Track if origin file was changed `#246 <https://github.com/epam/ketcher/issues/246>`__

* Add save to MDL molfile v3000 support `#190 <https://github.com/epam/ketcher/issues/190>`__

* Transform global css selectors into css classes `#278 <https://github.com/epam/ketcher/issues/278>`__

* Split Ketcher into Core and Presentations modules `#196 <https://github.com/epam/ketcher/issues/196>`__

* Extend editor API to generate png files based on structure `#240 <https://github.com/epam/ketcher/issues/240>`__

* Fire custom event on structure change `#54 <https://github.com/epam/ketcher/issues/54>`__

* Add delete button for user templates `#160 <https://github.com/epam/ketcher/issues/160>`__

* Add ketcherWindow.ketcher.getSmilesExt() method `#266 <https://github.com/epam/ketcher/issues/266>`__

* Add possibility to hide buttons on control panel `#244 <https://github.com/epam/ketcher/issues/244>`__

* Add bonds information for ket format in DAT s-groups `#280 <https://github.com/epam/ketcher/issues/280>`__

* Add indicator to inform users about execution of 'heavy' operations `#255 <https://github.com/epam/ketcher/issues/255>`__

* Ketcher API: Add possibility to save RXN files `#296 <https://github.com/epam/ketcher/issues/296>`__

* Add ellipse simple object `#85 <https://github.com/epam/ketcher/issues/85>`__

* 'Font' field should be disabled untill list will be loaded `#321 <https://github.com/epam/ketcher/issues/321>`__

* Modal window displaying in Ketcher instance format `#325 <https://github.com/epam/ketcher/issues/325>`__

* Simple Objects selection and resizing mechanism `#315 <https://github.com/epam/ketcher/issues/315>`__

* Add ability to download image in several formats `#373 <https://github.com/epam/ketcher/issues/373>`__

* Allow select simple object by several points in selection area `#367 <https://github.com/epam/ketcher/issues/367>`__


**Bugfixes**

* If structure contains SRU-Group User can't click 'Calculated Values' button - nothing happens after clicking. `#215 <https://github.com/epam/ketcher/issues/215>`__

* Stereo labels appears on not stereo structure after 'Aromatize' action. `#206 <https://github.com/epam/ketcher/issues/206>`__

* User can create incorrect Multiple S-Group but can't save and warning message doesn't appears. `#175 <https://github.com/epam/ketcher/issues/175>`__

* Calculated Values displays some values from last calculation `#279 <https://github.com/epam/ketcher/issues/279>`__

* Remove process.env.PUBLIC_URL from ketcher-react `#282 <https://github.com/epam/ketcher/issues/282>`__

* Fonts drop-down list can't be opened when User opens settings for the second time `#320 <https://github.com/epam/ketcher/issues/320>`__

* User can't copy/cut and paste part of structure or structure with SRU-polymer S-Group. `#177 <https://github.com/epam/ketcher/issues/177>`__

* When User draw circle without height - Ketcher becomes disabled. `#317 <https://github.com/epam/ketcher/issues/317>`__

* Error after Undo/Redo actions when User has edited S-Group `#311 <https://github.com/epam/ketcher/issues/311>`__

* Unable to calculate values for selected structure `#361 <https://github.com/epam/ketcher/issues/361>`__

* S-Group brackets place in incorrect place on structure with double bonds and sprouted single bonds `#269 <https://github.com/epam/ketcher/issues/269>`__

* Calculated values for reaction: missing last bracket for chemical formula `#364 <https://github.com/epam/ketcher/issues/364>`__

* The structures with atoms with valences rendering incorrectly after saving `#46 <https://github.com/epam/ketcher/issues/46>`__

* Different structure between ketcher.setMolecule() and ketcher.ui.load() `#386 <https://github.com/epam/ketcher/issues/386>`__

* Templates in template library are shifted down when Ketcher have less than 855px width `#338 <https://github.com/epam/ketcher/issues/338>`__

* Display Settings: 'Show hydrogen labels' triggers error `#391 <https://github.com/epam/ketcher/issues/391>`__

* 'Calculated values' fields are editable `#388 <https://github.com/epam/ketcher/issues/388>`__

* Incorrect behavior of Ketcher after deleting of a part of R-Group member `#419 <https://github.com/epam/ketcher/issues/419>`__

* In Template Library scroll bar jumps up and down when it is centered `#184 <https://github.com/epam/ketcher/issues/184>`__

* Incorrect behavior of Ketcher after deleting of a part of S-Group member `#433 <https://github.com/epam/ketcher/issues/433>`__

* 'Any Atom' tool incorrect behavior when selected with hotkey or typed in from keyboard `#368 <https://github.com/epam/ketcher/issues/368>`__

* 'Custom Templates' - User templates are shown without the images in the right pane of the 'Template library' `#431 <https://github.com/epam/ketcher/issues/431>`__
