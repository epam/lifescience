Options
=======

Input/Output
------------

+--------------------+--------------------+--------------------+--------------------+
| Option             | Type               | Description        | Default            |
+====================+====================+====================+====================+
| ``ignore-stereoche | boolean            | When reading a     | false              |
| mistry-errors``    |                    | Molfile/Rxnfile    |                    |
|                    |                    | with incorrectly   |                    |
|                    |                    | marked             |                    |
|                    |                    | stereobonds,       |                    |
|                    |                    | ignore them rather |                    |
|                    |                    | than raise an      |                    |
|                    |                    | error.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``ignore-noncritic | boolean            | When true, the     | false              |
| al-query-features` |                    | "bond topology",   |                    |
| `                  |                    | "stereo care",     |                    |
|                    |                    | "ring bond count", |                    |
|                    |                    | and "unsaturation" |                    |
|                    |                    | specifications are |                    |
|                    |                    | ignored when a     |                    |
|                    |                    | non-query molecule |                    |
|                    |                    | is being loaded.   |                    |
|                    |                    | Otherwise, an      |                    |
|                    |                    | error is raised.   |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``treat-x-as-pseud | boolean            | Treat 'X' atoms in | false              |
| oatom``            |                    | Molfiles/Rxnfiles  |                    |
|                    |                    | as pseudoatoms,    |                    |
|                    |                    | rather than "any   |                    |
|                    |                    | halogen" query     |                    |
|                    |                    | atoms.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``skip-3d-chiralit | boolean            | Do not calculate   | false              |
| y``                |                    | chirality of 3D    |                    |
|                    |                    | input structures.  |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``molfile-saving-m | string             | -  ``2000``: force | ``auto``           |
| ode``              |                    |    saving Molfiles |                    |
|                    |                    |    and Rxnfiles to |                    |
|                    |                    |    v2000 format,   |                    |
|                    |                    |    not regarding   |                    |
|                    |                    |    if there are    |                    |
|                    |                    |    features that   |                    |
|                    |                    |    can not be      |                    |
|                    |                    |    represented in  |                    |
|                    |                    |    v2000.          |                    |
|                    |                    | -  ``3000``: force |                    |
|                    |                    |    saving Molfiles |                    |
|                    |                    |    and Rxnfiles to |                    |
|                    |                    |    v3000 format,   |                    |
|                    |                    |    not regarding   |                    |
|                    |                    |    if there are    |                    |
|                    |                    |    features that   |                    |
|                    |                    |    can not be      |                    |
|                    |                    |    represented in  |                    |
|                    |                    |    v2000.          |                    |
|                    |                    | -  ``auto``:       |                    |
|                    |                    |    detect if       |                    |
|                    |                    |    saving to v3000 |                    |
|                    |                    |    is really       |                    |
|                    |                    |    needed, and     |                    |
|                    |                    |    then save to    |                    |
|                    |                    |    v3000.          |                    |
|                    |                    |    Otherwise, save |                    |
|                    |                    |    to v2000.       |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``molfile-saving-n | boolean            | Do no write the    | false              |
| o-chiral``         |                    | "Chiral" flag when |                    |
|                    |                    | saving Molfiles    |                    |
|                    |                    | and Rxnfiles       |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``molfile-saving-s | boolean            | Do no write the    | false              |
| kip-date``         |                    | current date into  |                    |
|                    |                    | Molfiles, Rxnfiles |                    |
|                    |                    | and RDFiles        |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``smiles-saving-wr | boolean            | Write names when   | false              |
| ite-name``         |                    | saving via generic |                    |
|                    |                    | saver interface in |                    |
|                    |                    | SMILES mode        |                    |
+--------------------+--------------------+--------------------+--------------------+

Rendering
---------

+--------------------+--------------------+--------------------+--------------------+
| Option             | Type               | Description        | Default            |
+====================+====================+====================+====================+
| ``render-output-fo | string             | Obligatory.        | -                  |
| rmat``             |                    | ``png``, ``svg``,  |                    |
|                    |                    | ``pdf`` are        |                    |
|                    |                    | allowed. On        |                    |
|                    |                    | Windows, ``emf``   |                    |
|                    |                    | is also allowed.   |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-bond-leng | integer            | Desired average    | 100                |
| th``               |                    | bond length in     |                    |
|                    |                    | pixels. The actual |                    |
|                    |                    | average bond       |                    |
|                    |                    | length may be less |                    |
|                    |                    | if the             |                    |
|                    |                    | ``render-image-siz |                    |
|                    |                    | e``                |                    |
|                    |                    | option is set. To  |                    |
|                    |                    | reset this         |                    |
|                    |                    | setting, you can   |                    |
|                    |                    | set its value to   |                    |
|                    |                    | -1.                |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-image-siz | size               | Width and height   | -                  |
| e``                |                    | of target image.   |                    |
|                    |                    | If not set, is     |                    |
|                    |                    | calculated         |                    |
|                    |                    | automatically      |                    |
|                    |                    | according to       |                    |
|                    |                    | ``render-bond-leng |                    |
|                    |                    | th``.              |                    |
|                    |                    | To reset this      |                    |
|                    |                    | setting, you can   |                    |
|                    |                    | set the values of  |                    |
|                    |                    | width and height   |                    |
|                    |                    | to -1.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-margins`` | size               | Horizontal and     | 0x0                |
|                    |                    | vertical margins   |                    |
|                    |                    | around the image,  |                    |
|                    |                    | in pixels.         |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-base-colo | color              | The default color  | black              |
| r``                |                    | for atoms and      |                    |
|                    |                    | bonds.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-backgroun | color              | Background color.  | transparent        |
| d-color``          |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-label-mod | string             | -  ``all``: show   | ``terminal-hetero` |
| e``                |                    |    all atoms       | `                  |
|                    |                    | -  ``terminal-hete |                    |
|                    |                    | ro``:              |                    |
|                    |                    |    show            |                    |
|                    |                    |    heteroatoms,    |                    |
|                    |                    |    terminal atoms, |                    |
|                    |                    |    atoms with      |                    |
|                    |                    |    radical,        |                    |
|                    |                    |    charge,         |                    |
|                    |                    |    isotope,        |                    |
|                    |                    |    explicit        |                    |
|                    |                    |    valence, and    |                    |
|                    |                    |    atoms having    |                    |
|                    |                    |    two adjacent    |                    |
|                    |                    |    bonds in a line |                    |
|                    |                    | -  ``hetero``: the |                    |
|                    |                    |    same as         |                    |
|                    |                    |    ``terminal-hete |                    |
|                    |                    | ro``,              |                    |
|                    |                    |    but without     |                    |
|                    |                    |    terminal atoms  |                    |
|                    |                    | -  ``none``: hide  |                    |
|                    |                    |    all labels,     |                    |
|                    |                    |    show only bonds |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-highlight | boolean            | Always show labels | false              |
| ed-atoms-visible`` |                    | of highlighted     |                    |
|                    |                    | atoms.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-implicit- | boolean            | Show implicit      | true               |
| hydrogens-visible` |                    | hydrogens on       |                    |
| `                  |                    | visible atoms.     |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-superatom | string             | -  ``expand``:     | ``expand``         |
| -mode``            |                    |    render expanded |                    |
|                    |                    |    superatoms      |                    |
|                    |                    | -  ``collapse``:   |                    |
|                    |                    |    render just the |                    |
|                    |                    |    superatoms'     |                    |
|                    |                    |    names           |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-coloring` | boolean            | Turn on atom       | false              |
| `                  |                    | coloring, e.g.     |                    |
|                    |                    | nitrogen is blue,  |                    |
|                    |                    | oxygen is red,     |                    |
|                    |                    | etc.               |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-highlight | boolean            | Enable             | false              |
| -thickness-enabled |                    | highlighting with  |                    |
| ``                 |                    | thick bonds and    |                    |
|                    |                    | bold atom labels.  |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-highlight | boolean            | Enable             | true               |
| -color-enabled``   |                    | highlighting with  |                    |
|                    |                    | color.             |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-highlight | color              | The color to be    | red                |
| -color``           |                    | used for           |                    |
|                    |                    | highlighting.      |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-data-sgro | color              | Color of data      | black              |
| up-color``         |                    | SGroup labels.     |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-aam-color | color              | Atom-by-atom       | black              |
| ``                 |                    | mapping indices    |                    |
|                    |                    | color in           |                    |
|                    |                    | reactions.         |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-stereo-st | string             | -  ``old``: Only   | ``old``            |
| yle``              |                    |    display the     |                    |
|                    |                    |    "Chiral" sign   |                    |
|                    |                    |    when            |                    |
|                    |                    |    appropriate.    |                    |
|                    |                    | -  ``ext``:        |                    |
|                    |                    |    Display "abs",  |                    |
|                    |                    |    "and", "or"     |                    |
|                    |                    |    labels near     |                    |
|                    |                    |    each            |                    |
|                    |                    |    stereocenter.   |                    |
|                    |                    | -  ``none``: Hide  |                    |
|                    |                    |    all the         |                    |
|                    |                    |    information     |                    |
|                    |                    |    about the       |                    |
|                    |                    |    stereogroups.   |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-relative- | float              | Set the thickness  | 1.0                |
| thickness``        |                    | of a bond to X/30  |                    |
|                    |                    | of the average     |                    |
|                    |                    | bond length.       |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-catalysts | string             | -  ``above``:      | ``above-and-below` |
| -placement``       |                    |    place reaction  | `                  |
|                    |                    |    catalysts above |                    |
|                    |                    |    the reaction    |                    |
|                    |                    |    arrow           |                    |
|                    |                    | -  ``above-and-bel |                    |
|                    |                    | ow``:              |                    |
|                    |                    |    place reaction  |                    |
|                    |                    |    calalysts above |                    |
|                    |                    |    and below the   |                    |
|                    |                    |    reaction arrow  |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment`` | string             | Put a single-line  | -                  |
|                    |                    | comment at the top |                    |
|                    |                    | or bottom of the   |                    |
|                    |                    | image. If the      |                    |
|                    |                    | image size is set  |                    |
|                    |                    | explicitly, it     |                    |
|                    |                    | must not be        |                    |
|                    |                    | smaller than the   |                    |
|                    |                    | size of the        |                    |
|                    |                    | comment bounding   |                    |
|                    |                    | box.               |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment-p | string             | ``top`` or         | ``bottom``         |
| osition``          |                    | ``bottom``.        |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment-o | integer            | Vertical space (in | 0                  |
| ffset``            |                    | pixels) between    |                    |
|                    |                    | the comment and    |                    |
|                    |                    | the rendered       |                    |
|                    |                    | structure or       |                    |
|                    |                    | reaction.          |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment-a | float              | 0 is for alignment | 0.5                |
| lignment``         |                    | to the left, 1 is  |                    |
|                    |                    | for the alignment  |                    |
|                    |                    | to the right, 0.5  |                    |
|                    |                    | is for centering   |                    |
|                    |                    | the comment. Note  |                    |
|                    |                    | that this setting  |                    |
|                    |                    | has no effect if   |                    |
|                    |                    | comment is larger  |                    |
|                    |                    | than the           |                    |
|                    |                    | molecule/reaction  |                    |
|                    |                    | rendered.          |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment-f | integer            | Font size for the  | 20                 |
| ont-size``         |                    | comment in         |                    |
|                    |                    | absolute units,    |                    |
|                    |                    | roughly equal to   |                    |
|                    |                    | the height in      |                    |
|                    |                    | pixels.            |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-comment-c | color              | Color to use for   | black              |
| olor``             |                    | the comment.       |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-atom-ids- | boolean            | Show atom numbers  | false              |
| visible``          |                    | (for debugging     |                    |
|                    |                    | purposes only).    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-bond-ids- | boolean            | Show bond numbers  | false              |
| visible``          |                    | (for debugging     |                    |
|                    |                    | purposes only).    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``render-atom-bond | boolean            | Show atom and bond | false              |
| -ids-from-one``    |                    | numbers starting   |                    |
|                    |                    | from one, not from |                    |
|                    |                    | zero.              |                    |
+--------------------+--------------------+--------------------+--------------------+

Rendering in Grid
-----------------

+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Option                            | Type      | Description                                                                                                                                                                                                 | Default   |
+===================================+===========+=============================================================================================================================================================================================================+===========+
| ``render-grid-margins``           | size      | Horizontal and vertical margins around the grid cell, in pixels.                                                                                                                                            | 0, 0      |
+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| ``render-grid-title-property``    | string    | The name of the molecule's property that defines the title that is put under each molecule. If not defined, no titles are shown. The special value "^NAME" means to use the molecule's name as its title.   | -         |
+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| ``render-grid-title-alignment``   | float     | 0 is for alignment to the left, 1 is for the alignment to the right, 0.5 is for centering the title. Note that this setting has no effect if the title is larger than the molecule rendered.                | 0.5       |
+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| ``render-grid-title-font-size``   | integer   | Font size for the title in absolute units, roughly equal to the height in pixels.                                                                                                                           | 20        |
+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| ``render-grid-title-offset``      | integer   | Vertical space (in pixels) between the title and the rendered structure.                                                                                                                                    | 0         |
+-----------------------------------+-----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Fingerprinting
--------------

+----------------------+-----------+------------------------------------------------------------------------+-----------+
| Option               | Type      | Description                                                            | Default   |
+======================+===========+========================================================================+===========+
| ``fp-ord-qwords``    | int       | Size of "ordinary" part of a fingerprint, in 8-byte blocks.            | 25        |
+----------------------+-----------+------------------------------------------------------------------------+-----------+
| ``fp-sim-qwords``    | int       | Size of "similarity" part of a fingerprint, in 8-byte blocks.          | 8         |
+----------------------+-----------+------------------------------------------------------------------------+-----------+
| ``fp-any-qwords``    | int       | Size of "any" part of a fingerprint, in 8-byte blocks.                 | 15        |
+----------------------+-----------+------------------------------------------------------------------------+-----------+
| ``fp-tau-qwords``    | int       | Size of "tautomer" part of a fingerprint, in 8-byte blocks.            | 10        |
+----------------------+-----------+------------------------------------------------------------------------+-----------+
| ``fp-ext-enabled``   | boolean   | Sets whether to include or not 3-byte "EXT" part of the fingerprint.   | true      |
+----------------------+-----------+------------------------------------------------------------------------+-----------+

Layout
------

+-----------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Option                      | Type   | Description                                                                                                                                                                                            | Default   |
+=============================+========+========================================================================================================================================================================================================+===========+
| ``layout-max-iterations``   | int    | The maximum number of iterations allowed for the layout procedure to run (the number is internally multiplied by 10000). If the limit is reached, an exception is thrown. Zero value means no limit.   | 0         |
+-----------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Substructure Matching
---------------------

+--------------------+--------------------+--------------------+--------------------+
| Option             | Type               | Description        | Default            |
+====================+====================+====================+====================+
| ``embedding-unique | string             | Defines how the    | ``atoms``          |
| ness``             |                    | uniqueness of a    |                    |
|                    |                    | substructure match |                    |
|                    |                    | is determined when |                    |
|                    |                    | counting or        |                    |
|                    |                    | iterating unique   |                    |
|                    |                    | matches.           |                    |
|                    |                    |                    |                    |
|                    |                    | -  ``atoms``: by   |                    |
|                    |                    |    atoms; "CCC"    |                    |
|                    |                    |    matches "C1CC1" |                    |
|                    |                    |    once            |                    |
|                    |                    | -  ``bonds``: by   |                    |
|                    |                    |    bonds, "CCC"    |                    |
|                    |                    |    matches "C1CC1" |                    |
|                    |                    |    three times     |                    |
|                    |                    | -  ``none``: no    |                    |
|                    |                    |    test for        |                    |
|                    |                    |    uniqueness;     |                    |
|                    |                    |    "CCC" matches   |                    |
|                    |                    |    "C1CC1" six     |                    |
|                    |                    |    times           |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``max-embeddings`` | int                | The maximum number | 10000              |
|                    |                    | of embeddings      |                    |
|                    |                    | allowed to         |                    |
|                    |                    | enumerate when     |                    |
|                    |                    | counting all       |                    |
|                    |                    | embeddings. If the |                    |
|                    |                    | limit is reached,  |                    |
|                    |                    | an exception is    |                    |
|                    |                    | thrown. Zero value |                    |
|                    |                    | means no limit.    |                    |
+--------------------+--------------------+--------------------+--------------------+

R-Group Deconvolution
---------------------

+-----------------------------------+-----------+------------------------------+-----------+
| Option                            | Type      | Description                  | Default   |
+===================================+===========+==============================+===========+
| ``deconvolution-aromatization``   | boolean   | Aromatize input molecules.   | true      |
+-----------------------------------+-----------+------------------------------+-----------+

Reaction Products Enumeration
-----------------------------

+--------------------+--------------------+--------------------+--------------------+
| Option             | Type               | Description        | Default            |
+====================+====================+====================+====================+
| ``rpe-multistep-re | boolean            | Enable multistep   | false              |
| actions``          |                    | reactions.         |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``rpe-mode``       | string             | -  ``grid``:       | grid               |
|                    |                    |    different sets  |                    |
|                    |                    |    of monomers     |                    |
|                    |                    |    react in        |                    |
|                    |                    |    different tubes |                    |
|                    |                    | -  ``one-tube``:   |                    |
|                    |                    |    reactions take  |                    |
|                    |                    |    place in one    |                    |
|                    |                    |    tube            |                    |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``rpe-self-reactio | boolean            | Enable             | false              |
| n``                |                    | intramolecular     |                    |
|                    |                    | reactions, where   |                    |
|                    |                    | one molecule of    |                    |
|                    |                    | monomers can play  |                    |
|                    |                    | role of two (or    |                    |
|                    |                    | more) reactants.   |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``rpe-max-depth``  | integer            | Maximum level of   | 2                  |
|                    |                    | representing       |                    |
|                    |                    | product like a     |                    |
|                    |                    | monomer (works     |                    |
|                    |                    | only with          |                    |
|                    |                    | ``rpe-multistep-re |                    |
|                    |                    | actions``          |                    |
|                    |                    | enabled).          |                    |
+--------------------+--------------------+--------------------+--------------------+
| ``rpe-max-products | integer            | Maximum amount of  | 1000               |
| -count``           |                    | generated          |                    |
|                    |                    | products.          |                    |
+--------------------+--------------------+--------------------+--------------------+

InChI
-----

+---------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| Option              | Type     | Description                                                                                                                                                        | Default   |
+=====================+==========+====================================================================================================================================================================+===========+
| ``inchi-options``   | string   | Options supported by the official InChI plugin: /NEWPSOFF /DoNotAddH /SNon /SRel /SRac /SUCF /ChiralFlagON /ChiralFlagOFF /SUU /SLUUD /FixedH /RecMet /KET /15T.   | -         |
+---------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
