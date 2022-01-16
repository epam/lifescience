Ketcher 2.4.0
#############

*30 December 2021*

*******
Summary
*******

We are happy to announce that new version `2.4.0 <https://github.com/epam/ketcher/releases/tag/v2.4.0>`__ of Ketcher has been released. 


**New features and improvements** 

* Add an error handler to inform a user about the server problems `#555 <https://github.com/epam/ketcher/issues/555>`__
* Implement support of Functional Groups `#692 <https://github.com/epam/ketcher/issues/692>`__
* Use Internal format to communicate with Indigo side `#571 <https://github.com/epam/ketcher/issues/571>`__
* Getting static files from ketcher-react package itself `#857 <https://github.com/epam/ketcher/issues/857>`__
* It should be impossible to add attachment point(s) to an atom with R-Group Label and vice versa `#513 <https://github.com/epam/ketcher/issues/513>`__
* 'Save As' Window - Rename 'Graph Format' to 'Ket Format' `#837 <https://github.com/epam/ketcher/issues/837>`__
* Redesign Error window `#898 <https://github.com/epam/ketcher/issues/898>`__
* Add warning message when saving structure with QUERY in Smiles format `#712 <https://github.com/epam/ketcher/issues/712>`__
* New design of modal windows `#894 <https://github.com/epam/ketcher/issues/894>`__
* 'Custom Templates' button isn't highlighted in black color when the user chouse Template to add on canvas `#880 <https://github.com/epam/ketcher/issues/880>`__
* Scrolling the left toolbar programmatically `#779 <https://github.com/epam/ketcher/issues/779>`__
* Update Ketcher API to allow to download structure in any formats `#737 <https://github.com/epam/ketcher/issues/737>`__
* Hiding buttons on the left menu `#713 <https://github.com/epam/ketcher/issues/713>`__
* Add global error handling `#726 <https://github.com/epam/ketcher/issues/726>`__
* Transform dialogs global css styles into css modules `#277 <https://github.com/epam/ketcher/issues/277>`__
* Styles are not component based `#699 <https://github.com/epam/ketcher/issues/699>`__
* Add the ability to turn off the auto fade of AND/OR stereo labels `#689 <https://github.com/epam/ketcher/issues/689>`__
* Make decomposition of arrow tool `#696 <https://github.com/epam/ketcher/issues/696>`__
* Add additional arrow types `#697 <https://github.com/epam/ketcher/issues/697>`__
* Implement resizing of arrows `#698 <https://github.com/epam/ketcher/issues/698>`__
* Decomposition of Copy button `#707 <https://github.com/epam/ketcher/issues/707>`__
* Copy drawing to the clipboard as an image `#691 <https://github.com/epam/ketcher/issues/691>`__
* Text Tool: Add Font Size `#703 <https://github.com/epam/ketcher/issues/703>`__
* When a user creates two connected double/triple bonds they should appear at a 180 degree angle `#526 <https://github.com/epam/ketcher/issues/526>`__
* Atom/Bond property should be applied for all selected objects `#156 <https://github.com/epam/ketcher/issues/156>`__
* onChange property on the ketcher-react `#645 <https://github.com/epam/ketcher/issues/645>`__


**Bugfixes**

* Error message Convert error! IndigoException: inchi-wrapper: Indigo-InChI: InChI generation failed: Empty structure Code: 2. InChi for empty canvas `#1058 <https://github.com/epam/ketcher/issues/1058>`__
* IndigoException: element: can not calculate valence on C, charge 0, connectivity 6 `#995 <https://github.com/epam/ketcher/issues/995>`__
* Reaction arrow and plus are removed after Clean Up action `#1131 <https://github.com/epam/ketcher/issues/1131>`__
* Generate structure from InChI String - Incorrect structure rendering in Remote mode `#824 <https://github.com/epam/ketcher/issues/824>`__
* Calculated Values tool: When calculating reaction, there is different behavior in different modes `#650 <https://github.com/epam/ketcher/issues/650>`__
* When saving file in InChi format atom's alias is taken as query `#656 <https://github.com/epam/ketcher/issues/656>`__
* Server functions do not work with structures with dative/hydrogen bonds `#668 <https://github.com/epam/ketcher/issues/668>`__
* Atom is not changed if change in Label Edit window `#1102 <https://github.com/epam/ketcher/issues/1102>`__
* 'generateImageAsync' method does not work in Remote mode `#371 <https://github.com/epam/ketcher/issues/371>`__
* Stereocenter labels color gradient does not work in Firefox `#1163 <https://github.com/epam/ketcher/issues/1163>`__
* (E) and (Z) stereo labels appear so far from stereobonds after calculate cip action `#1158 <https://github.com/epam/ketcher/issues/1158>`__
* It is impossible to change arrow when the arrow selected by selection tool `#1151 <https://github.com/epam/ketcher/issues/1151>`__
* Benzene ring loses circle when exporting `#838 <https://github.com/epam/ketcher/issues/838>`__
* ket file with no nodes cannot be deserialized `#1137 <https://github.com/epam/ketcher/issues/1137>`__
* Convert error! Cannot read properties of undefined (reading 'slice') on opening file in Extended Smiles format and Daylight Smiles format `#1143 <https://github.com/epam/ketcher/issues/1143>`__
* S-Group: incorrect rendering when using structures from Template pallete and different options from S-Group Properties window `#797 <https://github.com/epam/ketcher/issues/797>`__
* 'Calculated Values' works incorrect for selected structure `#1112 <https://github.com/epam/ketcher/issues/1112>`__
* Cannot read properties of undefined (reading 'struct') error if connect two (or more) Cyclopentadiene(T) and click Aromatize `#984 <https://github.com/epam/ketcher/issues/984>`__
* Aromatic structure changes to not aromatic if try to connect with other structure `#1093 <https://github.com/epam/ketcher/issues/1093>`__
* It is not possible to rotate R-group member if it was opened from file `#1074 <https://github.com/epam/ketcher/issues/1074>`__
* Convert error if Load file as fragment and Ctrl+V `#1052 <https://github.com/epam/ketcher/issues/1052>`__
* Redo action does not work for R-Group members if Cut->Paste->Undo->Redo `#1054 <https://github.com/epam/ketcher/issues/1054>`__
* Structure shouldn't flipped when a part structure is selected `#1029 <https://github.com/epam/ketcher/issues/1029>`__
* Error when apply 3D to empty canvas `#1003 <https://github.com/epam/ketcher/issues/1003>`__
* Incorrect bond rendering on Benzene ring after dearomatize `#1005 <https://github.com/epam/ketcher/issues/1005>`__
* Copy/Cut and Paste don't work with Plus `#1036 <https://github.com/epam/ketcher/issues/1036>`__
* Error message when trying to calculate values of the structures with the hydrogen and dative bonds `#540 <https://github.com/epam/ketcher/issues/540>`__
* Copy/Past actions dont work for simple objects `#1030 <https://github.com/epam/ketcher/issues/1030>`__
* Copy/Cut/Paste for any Arrow. If copy any arrow and past- Arrow Open Angle always pasted `#1038 <https://github.com/epam/ketcher/issues/1038>`__
* Bond Tool - Double/ Triple bonds: When a user changing chain structure Double/ Triple bound should appear at a 180-degree angle `#834 <https://github.com/epam/ketcher/issues/834>`__
* Atom Generics (except A) and Special nodes are replaced with R# after saving in Daylight Smile format. `#39 <https://github.com/epam/ketcher/issues/39>`__
* Disable "Copy" button if nothing selected on the canvas `#990 <https://github.com/epam/ketcher/issues/990>`__
* Incorrect double bonds building `#986 <https://github.com/epam/ketcher/issues/986>`__
* Error message when try to open file with extension other than Custom files `#962 <https://github.com/epam/ketcher/issues/962>`__
* Not possible to expand Shape figure if it is selected `#947 <https://github.com/epam/ketcher/issues/947>`__
* Dependency installation failure `#926 <https://github.com/epam/ketcher/issues/926>`__
* Custom Templates - Templates duplicated when user saving templates with the same name `#889 <https://github.com/epam/ketcher/issues/889>`__
* Add possibility to hide elements by passing query parameter `#862 <https://github.com/epam/ketcher/issues/862>`__
* 'S-Group Properties' window - 'Absolute' radio button checked in all case `#866 <https://github.com/epam/ketcher/issues/866>`__
* S-Group tool - 'S-Group Properties' symbols are not clickable `#850 <https://github.com/epam/ketcher/issues/850>`__
* Hotkeys aren't working without previously clicking on canvas or any buttons `#813 <https://github.com/epam/ketcher/issues/813>`__
* Simple Objects - Shape Line: Wrong 'Shape Line' color when clicking on icon `#786 <https://github.com/epam/ketcher/issues/786>`__
* Simple Objects - Shape Rectangle: The error appears when drawing a rectangle of small height `#787 <https://github.com/epam/ketcher/issues/787>`__
* If User create simple molecule on canvas when it is minimum zoom value - molecule have increased distance between atoms. `#180 <https://github.com/epam/ketcher/issues/180>`__
* Stereo flag is overlapped with a structure `#602 <https://github.com/epam/ketcher/issues/602>`__
* Open from file window - File formats are duplicated `#839 <https://github.com/epam/ketcher/issues/839>`__
* Recognize molecule - Ketcher is broken when clicking the 'Recognize molecule' button `#820 <https://github.com/epam/ketcher/issues/820>`__
* If a structure with double bond(s) is the first structure created on the canvas the double bond is rendered incorrectly `#517 <https://github.com/epam/ketcher/issues/517>`__
* Save to Templates - Errors are appear when trying to save to templates structure with reaction arrow `#821 <https://github.com/epam/ketcher/issues/821>`__
* Save to Templates - The structure isn't displayed correctly in the 'Template edit' window when saving structure with Simple Objects `#822 <https://github.com/epam/ketcher/issues/822>`__
* Can not open InChi AuxInfo file in Standalone mode `#667 <https://github.com/epam/ketcher/issues/667>`__
* 'Template Edit' window: There is no 'Atom Id: xx, Bond Id: yy' text under the template image after changing Atom/Bond ID `#807 <https://github.com/epam/ketcher/issues/807>`__
* Template Library: there is no limit for input symbols when editing structure name or add new template in library `#799 <https://github.com/epam/ketcher/issues/799>`__
* Structure with NOT[] atom does not open `#641 <https://github.com/epam/ketcher/issues/641>`__
* Not all atom properties are shown if an Alias was set `#674 <https://github.com/epam/ketcher/issues/674>`__
* Stereo doesn't update after two bonds merge `#684 <https://github.com/epam/ketcher/issues/684>`__
* The gradient stays for mixed (&) stereomarks when 'Bonds Only' is selected in 'Color stereogenic centers' `#677 <https://github.com/epam/ketcher/issues/677>`__
* When selecting several structures with Segment Selection Tool they are not moving together `#628 <https://github.com/epam/ketcher/issues/628>`__
* Copy image fails in remote mode `#1007 <https://github.com/epam/ketcher/issues/1007>`__
* Standalone mode. Error on saving chain structure with connected Double Cis/Trans Bond `#1010 <https://github.com/epam/ketcher/issues/1010>`__
* Layout action do not work with structures with dative/hydrogen bonds `#669 <https://github.com/epam/ketcher/issues/669>`__