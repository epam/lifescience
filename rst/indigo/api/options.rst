Options
=======

Input/Output
------------


.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``ignore-stereochemistry-errors``
     - boolean
     - When reading a Molfile/Rxnfile with incorrectly marked stereobonds, ignore them rather than raise an error.
     - false
   * - ``ignore-noncritical-query-features``
     - boolean
     - When true, the "bond topology", "stereo care", "ring bond count", and "unsaturation" specifications are ignored when a non-query molecule is being loaded. Otherwise, an error is raised.
     - false
   * - ``treat-x-as-pseudoatom``
     - boolean
     - Treat 'X' atoms in Molfiles/Rxnfiles as pseudoatoms, rather than "any halogen" query atoms.
     - false
   * - ``skip-3d-chirality``
     - boolean
     - Do not calculate chirality of 3D input structures.
     - false
   * - ``molfile-saving-mode``
     - string
     - * ``2000``: force saving Molfiles and Rxnfiles to v2000 format, not regarding if there are features that can not be represented in v2000.
       * ``3000``: force saving Molfiles and Rxnfiles to v3000 format, not regarding if there are features that can not be represented in v2000.
       * ``auto``: detect if saving to v3000 is really needed, and then save to v3000. Otherwise, save to v2000.
     - ``auto``
   * - ``molfile-saving-no-chiral``
     - boolean
     - Do no write the "Chiral" flag when saving Molfiles and Rxnfiles
     - false
   * - ``molfile-saving-skip-date``
     - boolean
     - Do no write the current date into Molfiles, Rxnfiles and RDFiles
     - false
   * - ``smiles-saving-write-name``
     - boolean
     - Write names when saving via generic saver interface in SMILES mode
     - false
 

Rendering
---------
   
   
.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``render-output-format``
     - string
     - Obligatory. ``png``, ``svg``, ``pdf`` are allowed. On Windows, ``emf`` is also allowed.
     - \-
   * - ``render-bond-length``
     - integer
     - Desired average bond length in pixels. The actual average bond length may be less if the ``render-image-size`` option is set. To reset this setting, you can set its value to -1.
     - 100
   * - ``render-image-size``
     - size
     - Width and height of target image. If not set, is calculated automatically according to ``render-bond-length``. To reset this setting, you can set the values of width and height to -1.
     - \-
   * - ``render-margins``
     - size
     - Horizontal and vertical margins around the image, in pixels.
     - 0x0
   * - ``render-base-color``
     - color
     - The default color for atoms and bonds.
     - black
   * - ``render-background-color``
     - color
     - Background color.
     - transparent
   * - ``render-label-mode``
     - string
     - * ``all``: show all atoms
       * ``terminal-hetero``: show heteroatoms, terminal atoms, atoms with radical, charge, isotope, explicit valence, and atoms having two adjacent bonds in a line
       * ``hetero``: the same as ``terminal-hetero``, but without terminal atoms
       * ``none``: hide all labels, show only bonds
     - ``terminal-hetero``
   * - ``render-highlighted-atoms-visible``
     - boolean
     - Always show labels of highlighted atoms.
     - false
   * - ``render-implicit-hydrogens-visible``
     - boolean
     - Show implicit hydrogens on visible atoms.
     - true
   * - ``render-superatom-mode``
     - string
     - * ``expand``: render expanded superatoms
       * ``collapse``: render just the superatoms' names
     - ``expand``
   * - ``render-coloring``
     - boolean
     - Turn on atom coloring, e.g. nitrogen is blue, oxygen is red, etc.
     - false
   * - ``render-highlight-thickness-enabled``
     - boolean
     - Enable highlighting with thick bonds and bold atom labels.
     - false
   * - ``render-highlight-color-enabled``
     - boolean
     - Enable highlighting with color.
     - true
   * - ``render-highlight-color``
     - color
     - The color to be used for highlighting.
     - red
   * - ``render-data-sgroup-color``
     - color
     - Color of data SGroup labels.
     - black
   * - ``render-aam-color``
     - color
     - Atom-by-atom mapping indices color in reactions.
     - black
   * - ``render-stereo-style``
     - string
     - * ``old``: Only display the "Chiral" sign when appropriate.
       * ``ext``: Display "abs", "and", "or" labels near each stereocenter.
       * ``none``: Hide all the information about the stereogroups.
     - ``old``
   * - ``render-relative-thickness``
     - float
     - Set the thickness of a bond to X/30 of the average bond length.
     - 1.0
   * - ``render-catalysts-placement``
     - string
     - * ``above``: place reaction catalysts above the reaction arrow
       * ``above-and-below``: place reaction calalysts above and below the reaction arrow
     - ``above-and-below``
   * - ``render-comment``
     - string
     - Put a single-line comment at the top or bottom of the image. If the image size is set explicitly, it must not be smaller than the size of the comment bounding box.
     - \-
   * - ``render-comment-position``
     - string
     - ``top`` or ``bottom``.
     - ``bottom``
   * - ``render-comment-offset``
     - integer
     - Vertical space (in pixels) between the comment and the rendered structure or reaction.
     - 0
   * - ``render-comment-alignment``
     - float
     - 0 is for alignment to the left, 1 is for the alignment to the right, 0.5 is for centering the comment. Note that this setting has no effect if comment is larger than the molecule/reaction rendered.
     - 0.5
   * - ``render-comment-font-size``
     - integer
     - Font size for the comment in absolute units, roughly equal to the height in pixels.
     - 20
   * - ``render-comment-color``
     - color
     - Color to use for the comment.
     - black
   * - ``render-atom-ids-visible``
     - boolean
     - Show atom numbers (for debugging purposes only).
     - false
   * - ``render-bond-ids-visible``
     - boolean
     - Show bond numbers (for debugging purposes only).
     - false
   * - ``render-atom-bond-ids-from-one``
     - boolean
     - Show atom and bond numbers starting from one, not from zero.
     - false




Rendering in Grid
-----------------


.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``render-grid-margins``
     - size
     - Horizontal and vertical margins around the grid cell, in pixels.
     - 0, 0
   * - ``render-grid-title-property``
     - string
     - The name of the molecule's property that defines the title that is put under each molecule. If not defined, no titles are shown. The special value "^NAME" means to use the molecule's name as its title.
     - \-
   * - ``render-grid-title-alignment``
     - float
     - 0 is for alignment to the left, 1 is for the alignment to the right, 0.5 is for centering the title. Note that this setting has no effect if the title is larger than the molecule rendered.
     - 0.5
   * - ``render-grid-title-font-size``
     - integer
     - Font size for the title in absolute units, roughly equal to the height in pixels.
     - 20
   * - ``render-grid-title-offset``
     - integer
     - Vertical space (in pixels) between the title and the rendered structure.
     - 0
     
    
Fingerprinting
--------------

.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``fp-ord-qwords``
     - int
     - Size of "ordinary" part of a fingerprint, in 8-byte blocks.
     - 25
   * - ``fp-sim-qwords``
     - int
     - Size of "similarity" part of a fingerprint, in 8-byte blocks.
     - 8
   * - ``fp-any-qwords``
     - int
     - Size of "any" part of a fingerprint, in 8-byte blocks.
     - 15
   * - ``fp-tau-qwords``
     - int
     - Size of "tautomer" part of a fingerprint, in 8-byte blocks.
     - 10
   * - ``fp-ext-enabled``
     - boolean
     - Sets whether to include or not 3-byte "EXT" part of the fingerprint.
     - true

Layout
------

.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``layout-max-iterations``
     - int
     - The maximum number of iterations allowed for the layout procedure to run (the number is internally multiplied by 10000). If the limit is reached, an exception is thrown. Zero value means no limit.
     - 0

     
Substructure Matching
---------------------

.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``embedding-uniqueness``
     - string
     - Defines how the uniqueness of a substructure match is determined when counting or iterating unique matches.
        * ``atoms``: by atoms; "CCC" matches "C1CC1" once
        * ``bonds``: by bonds, "CCC" matches "C1CC1" three times
        * ``none``: no test for uniqueness; "CCC" matches "C1CC1" six times
     - ``atoms``
   * - ``max-embeddings``
     - int
     - The maximum number of embeddings allowed to enumerate when counting all embeddings. If the limit is reached, an exception is thrown. Zero value means no limit.
     - 10000

     
R-Group Deconvolution
---------------------

.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``deconvolution-aromatization``
     - boolean
     - Aromatize input molecules.
     - true

     
Reaction Products Enumeration
-----------------------------



.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``rpe-multistep-reactions``
     - boolean
     - Enable multistep reactions.
     - false
   * - ``rpe-mode``
     - string
     - * ``grid``: different sets of monomers react in different tubes
       * ``one-tube``: reactions take place in one tube
     - grid
   * - ``rpe-self-reaction``
     - boolean
     - Enable intramolecular reactions, where one molecule of monomers can play role of two (or more) reactants.
     - false
   * - ``rpe-max-depth``
     - integer
     - Maximum level of representing product like a monomer (works only with ``rpe-multistep-reactions`` enabled).
     - 2
   * - ``rpe-max-products-count``
     - integer
     - Maximum amount of generated products.
     - 1000

InChI
-----


.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``inchi-options``
     - string
     - Options supported by the official InChI plugin: /NEWPSOFF /DoNotAddH /SNon /SRel /SRac /SUCF /ChiralFlagON /ChiralFlagOFF /SUU /SLUUD /FixedH /RecMet /KET /15T.
     - \-

Standardize
-----------


.. list-table:: 
   :header-rows: 1
   :widths: 40 10 40 10
   
   * - Option
     - Type
     - Description
     - Default
   * - ``standardize-stereo``
     - boolean
     - Sets or repairs the stereo on a molecule.
     - false
   * - ``standardize-charges``
     - boolean
     - Sets the charges on a molecule to a standard form.
     - false
   * - ``standardize-center-molecule``
     - boolean
     - Translates a molecule so its geometric center lies at the origin.
     - false
   * - ``standardize-remove-single-atoms``
     - boolean
     - Removes fragments that consist of only a single heavy atom.
     - false
   * - ``standardize-keep-smallest``
     - boolean
     - Keeps only the smallest fragment in the molecule.
     - false
   * - ``standardize-keep-largest``
     - boolean
     - Keeps only the largest fragment in the molecule.
     - false
   * - ``standardize-remove-largest``
     - boolean
     - Removes the largest fragment in the molecule.
     - false
   * - ``standardize-make-non-h-to-c-atoms``
     - boolean
     - Converts all non-Hydrogen atoms atoms in the molecule to carbon.
     - false
   * - ``standardize-make-non-h-to-a-atoms``
     - boolean
     - Converts all non-Hydrogen atoms in the molecule to the A query atom type.
     - false
   * - ``standardize-make-non-h-c-to-q-atoms``
     - boolean
     - Converts all non-Carbon, non-Hydrogen atoms in the molecule to the Q query atom type.
     - false
   * - ``standardize-make-all-bonds-single``
     - boolean
     - Converts all bonds in the molecule to single bonds.
     - false
   * - ``standardize-clear-coordinates``
     - boolean
     - Sets all x, y, z coordinates to zero.
     - false
   * - ``standardize-straighten-triple-bonds``
     - boolean
     - Finds atoms with triple bonds and non-linear geometry and fixes them so that the bond angles are 180 degrees.
     - false
   * - ``standardize-straighten-allens``
     - boolean
     - Finds atoms with two double-bonds and non-linear geometry and fixes them so that the bond angles are 180 degrees.
     - false
   * - ``standardize-clear-molecule``
     - boolean
     - Deletes all atoms and bonds in the molecule, keeping the molecule object in the data record.
     - false
   * - ``standardize-clear-stereo``
     - boolean
     - Sets all atoms and bonds to NoStereo.
     - false
   * - ``standardize-clear-enhanced-stereo``
     - boolean
     - Removes all relative stereo groupings.
     - false
   * - ``standardize-clear-unknown-stereo``
     - boolean
     - Sets all atoms and bonds marked UnknownStereo to NoStereo.
     - false
   * - ``standardize-clear-unknown-atom-stereo``
     - boolean
     - Sets all atoms marked UnknownStereo to NoStereo.
     - false
   * - ``standardize-clear-unknown-bond-stereo``
     - boolean
     - Sets all bonds marked UnknownStereo to NoStereo.
     - false
   * - ``standardize-clear-cis-trans``
     - boolean
     - Sets all bonds marked CisStereo or TransStereo to UnknownStereo.
     - false
   * - ``standardize-stereo-from-coordinates``
     - boolean
     - Uses 2D coordinates and up/down bond markings (or 3D coordinates) to assign the stereochemistry of the atoms or bonds.
     - false
   * - ``standardize-reposition-stereo-bonds``
     - boolean
     - Repositions the stereo bond markings in an attempt to find the best bond to mark as a wedge bond for each stereo atom.
     - false
   * - ``standardize-reposition-axial-stereo-bonds``
     - boolean
     - Repositions the stereo bond markings for axial stereo centers (allenes and atropisomers) in an attempt to find the best bond to mark as a wedge bond for each center.
     - false
   * - ``standardize-fix-direction-wedge-bonds``
     - boolean
     - Checks the wedge bonds in the molecule to ensure that the wedge is drawn with the stereo atom at the narrow end of the wedge.
     - false
   * - ``standardize-clear-charges``
     - boolean
     - Sets all formal charges to zero.
     - false
   * - ``standardize-highlight-colors``
     - boolean
     - Clears any highlight colors from atoms and bonds.
     - false
   * - ``standardize-neutralize-zwitterions``
     - boolean
     - Converts directly bonded zwitterions (positively charged atom bonded to negatively charged atom, A+B-) to the neutral representation (A=B).
     - false
   * - ``standardize-clear-unusual-valences``
     - boolean
     - Clears any atom valence query features and resets all implicit hydrogen counts to their standard values.
     - false
   * - ``standardize-clear-isotopes``
     - boolean
     - Clears all isotope markings from atoms.
     - false
   * - ``standardize-clear-dative-bonds``
     - boolean
     - Clears all explicit zero-order coordination bonds of dative type (V3000 type-9 bonds).
     - false
   * - ``standardize-clear-hydrogen-bonds``
     - boolean
     - Clears all explicit zero-order hydrogen bonds (V3000 type-10 bonds).
     - false
   * - ``standardize-create-dative-bonds``
     - boolean
     - Create coordination bond (zero-order bond) instead of wrong co-valent bond.
     - false
   * - ``standardize-create-hydrogen-bonds``
     - boolean
     - Create hydrogen bond (zero-order bond) instead of wrong co-valent bond.
     - false
