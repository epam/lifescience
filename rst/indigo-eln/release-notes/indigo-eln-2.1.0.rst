Ketcher 2.0.0beta
#################

*29 December 2017*

*******
Summary
*******

We are glad to announce that a new Ketcher version **2.0.0 beta** is released. 

`Source code <https://github.com/epam/ketcher/releases/tag/2.0.0-beta.1>`__

Please also use the latest `indigo service <../../download/service.html>`__ version.

Our team sends best wishes for the Holiday Season!


**New features and improvements**: 

* Add the possibility to Save structure as Extended SMILE

* Incorrect rendering (in Marvin) Ketcher SMILES for AND Enantiomer 

* Create saveSmiles() for Ketcher 

* Change the Bond type for several bonds at the same time 

* Structure can be fused bond to bond 

* Moving the structure with attached data 

* The 'cyclic' Rgroup definition should be forbidden 

* Problem with rendering a few condensed benzene rings 

* Add the possibility to save structure with necessary filename and add "Filename" field in the "Save Structure" window. 

* Include AuxInfo in InChI String 

* Templates for reaction



**Bugfixes**:

* Reaction Mapping Tool doesn't work after auto-mapping tool. 

* "Erase" doesn't delete selected structures when user crosses the scrollbars. 

* Incorrect order of "OK" and "Cancel" buttons in the "Settings" window. 

* The hyphen in the SMILES string for the aromatic structures 

* The application buttons are rendered incorrectly 

* [Edge40]: Double "Cancel" appears in "Label Edit" menu after adding template from Template Library. 

* The 'Label Edit' window opens during the moving of the scroll box 

* Structure with Sgroup cannot be saved as template 

* Message doesn't appears when user tries to dearomatize the structure with query-bonds. 

* Some templates have incorrect attachment atom 

* [Edge40]: Ketcher reboots after adding R-Group to the structure with template from Template Library 

* Fragment/Rectangle Selection tool's focus disappeared after changing the screen size 

* Selection Tool: Lasso Selection tool becomes active on the Toolbar after copy/cut/paste with other Selection tool 

* Fragment Selection Tool: selection disappeared when user click the canvas keep pressing Shift key 

* [Cosmetic only] Misprint in the error message using paste tool 

* Fragment Selection Tool: uncomfortable selection 

* Multiple warning for the Selection Tools in the Dev Console 

* [Edit Templates]: incorrect rendering of the descriptors, reaction arrow and plus signs 

* Calculate CIP tool returns incorrect position type for s-group data 

* The joint bond of the fused fragment should be the same as the bond of the moved structure 

* Custom Templates:One atoms of the structure is not displayed in the "Label edit" window 

* Tool palette doesn't close 

* Valence error after the Aromatize action 

* Template structures appear on canvas without Chiral flag 

* Problems with Undo after some actions with structures with Sgroups 

* The Double bonds in the first fused benzene are changed with the Single one 

* The structure is moved without stereo labels and attached data 

* Chiral flag persists on the canvas after delete or cut structure 

* Unpredictable behavior of the Undo action for the pasted/inserted reaction 

* [All browsers] Incorrect Undo/Redo behavior 

* About window: text about Indigo version overlaps the 'Indigo Toolkit' text 

* The Stereo labels and Attached Data keep their positions after the Flip action 

* Templates appear without saved attached data 

* Structure doesn't save to template when user chooses any format except MDL Molfile 

* Ketcher hangs after user adds empty template to the canvas 

* Two structures with the same R-fragment Tool appeared as two separate structures inside different square brackets 

* Incorrect error message appears when "Filename" field in "Save Structure" window is empty. 

* The structures of the reaction are relocated relative to each other after save or cut/paste. 

* Selection tool's focus disappeared after copy/paste of reaction arrow. 

* Reaction is relocated on the canvas after saving in rxn-format. 

* Incorrect bond rendering after refactoring 

* Buttons "Open From File", "Cancel", "Save To File" and "Save To Templates" have different styles. 

* The button "Open From File" doesn't work when user clicks at this button before, below or after the text "Open From File". 

* R-Group window appears when user clicks the scroll bar or scroll box 

* The Rotation angle value should appear 

* Checker: warning about Chirality 


