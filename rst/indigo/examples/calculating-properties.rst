.. _indigo-example-calculating-properties:

======================
Calculating Properties
======================

This examples shows how to calculate different molecule and reaction properties

.. _indigo-example-canonical-smiles:

----------------
Canonical Smiles
----------------

The following code prints canonical smiles string for a given structure:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    
    # Load structure
    mol = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')

    #print canonical smiles for the molecule
    print(mol.canonicalSmiles())


The example below prints canonical smiles string for a given reaction:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    rxn = indigo.loadReaction('[CH2:1]=[CH:2][CH:3]=[CH:4][CH2:5][H:6]>>[H:6][CH2:1][CH:2]=[CH:3][CH:4]=[CH2:5]')

    #print canonical smiles for the reaction
    print(rxn.canonicalSmiles())


.. _indigo-example-tautomer-enumeration:

------------------------
Enumeration of Tautomers
------------------------

The following code prints the list of tautomers for a given molecule:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    molecule = indigo.loadMolecule('OC1C2C=NNC=2N=CN=1')

    #print the list of tautomers for the molecule
    iter = indigo.iterateTautomers(molecule, 'INCHI')
    lst = list()
    array = indigo.createArray()
    index = 1
    for imol in iter:
        mol = imol.clone()
        lst.append(mol.canonicalSmiles())
        mol.setProperty("grid-comment", str(index))
        array.arrayAdd(mol)
        index += 1

    lst.sort()
    print "\n".join(map(lambda x, y: str(x) + ") " + y, range(1, len(lst) + 1), lst))

    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "5")
    indigo.setOption("render-grid-title-property", "grid-comment")
    indigoRenderer.renderGridToFile(array, None, 4, 'result.png')


If the molecule is aromatized before enumeration, the list of tautomers will be aromatized (if possible):

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    molecule = indigo.loadMolecule('OC1C2C=NNC=2N=CN=1')
    molecule.aromatize()

    #print the list of tautomers for the molecule
    iter = indigo.iterateTautomers(molecule, 'INCHI')
    lst = list()
    array = indigo.createArray()
    index = 1
    for imol in iter:
        mol = imol.clone()
        lst.append(mol.canonicalSmiles())
        mol.setProperty("grid-comment", str(index))
        array.arrayAdd(mol)
        index += 1

    lst.sort()
    print "\n".join(map(lambda x, y: str(x) + ") " + y, range(1, len(lst) + 1), lst))

    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "5")
    indigo.setOption("render-grid-title-property", "grid-comment")
    indigoRenderer.renderGridToFile(array, None, 4, 'result.png')

Please notice that the number of tautomers could be different in aromatized and dearomatized forms.
This happens because some aromatized forms could have different dearomatized representations.

The following code uses reaction SMARTS algorithm (may give different set of tautomers):

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    molecule = indigo.loadMolecule('OC1C2C=NNC=2N=CN=1')
    molecule.aromatize()

    #print the list of tautomers for the molecule
    iter = indigo.iterateTautomers(molecule, 'RSMARTS')
    lst = list()
    array = indigo.createArray()
    index = 1
    for imol in iter:
        mol = imol.clone()
        lst.append(mol.canonicalSmiles())
        mol.setProperty("grid-comment", str(index))
        array.arrayAdd(mol)
        index += 1

    lst.sort()
    print "\n".join(map(lambda x, y: str(x) + ") " + y, range(1, len(lst) + 1), lst))

    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "5")
    indigo.setOption("render-grid-title-property", "grid-comment")
    indigoRenderer.renderGridToFile(array, None, 4, 'result.png')

.. _indigo-example-sgroups-search:

--------------
Sgroups search
--------------

The following code prints results of SGroups search requests with different criteria:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/all_features_mol.mol
    
    # Load structure
    indigo.setOption("molfile-saving-mode", "3000")
    file1 = "data/all_features_mol.mol"
    m = indigo.loadMoleculeFromFile(file1)

    sgs = m.findSGroups("SG_TYPE", "SUP")

    for sg in sgs:
       print("Superatom with label %s found" % (m.getSuperatom(sg.getSGroupIndex())).getSGroupName());

    sgs = m.findSGroups("SG_LABEL", "Z")
    print("SGroups with label Z:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_CLASS", "AA")
    print("SGroups with class AA:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_DISPLAY_OPTION", "0")
    print("SGroups expanded:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_BRACKET_STYLE", "0")
    print("SGroups with square brackets:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_DATA", "Selection")
    print("SGroups with data contains Selection:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_DATA_NAME", "comment")
    print("SGroups with data field name comment:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_DATA_DISPLAY", "detached")
    print("SGroups with detached data field:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_DATA_LOCATION", "relative")
    print("SGroups with relative data field:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_ATOMS", "103, 104")
    print("SGroups with atoms 103 and 104:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());

    sgs = m.findSGroups("SG_BONDS", "249, 245")
    print("SGroups with bonds 245 and 249:")
    for sg in sgs:
       print("SGroup Index = %d " % sg.getSGroupIndex() + ", SGroup Type = %s" % sg.getSGroupType());


.. _indigo-example-cip-descriptors:

---------------
CIP Descriptors
---------------

This examples show how to calculate CIP stereo descriptors for different molecules.
Descriptors calculation is activated by corresponding Indigo option ``molfile-saving-add-stereo-desc``
and descriptors are added into generated mol file as data S-groups with special name field
``INDIGO_CIP_DESC``. Setting Indigo option  ``molfile-saving-add-stereo-desc`` to 0 (or false) (the
default value) disables descriptors calculation and removes all such data S-groups during corresponding
mol file generation.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/RS-example.mol
    
    # Load structure
    file = "data/RS-example.mol"
    mol1 = indigo.loadMoleculeFromFile(file)
    mol2 = mol1.clone();

    indigo.setOption("molfile-saving-add-stereo-desc", "1");
    mol2.molfile()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')


.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/ZE-example.mol
    
    # Load structure
    file = "data/ZE-example.mol"
    mol1 = indigo.loadMoleculeFromFile(file)
    mol2 = mol1.clone();

    indigo.setOption("molfile-saving-add-stereo-desc", "1");
    mol2.molfile()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/Z-example.mol
    
    # Load structure
    file = "data/Z-example.mol"
    mol1 = indigo.loadMoleculeFromFile(file)
    mol2 = mol1.clone();

    indigo.setOption("molfile-saving-add-stereo-desc", "1");
    mol2.molfile()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

There are also several examples for complicated structures when different software provides different
CIP stereo descriptors estimations:

The first case is the molecule with isotope inclusion.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/C14_R_iso.mol,data/C14_R_iso_2.mol
    
    # Load structure
    file1 = "data/C14_R_iso.mol"
    file2 = "data/C14_R_iso_2.mol"
    mol1 = indigo.loadMoleculeFromFile(file1)
    mol2 = indigo.loadMoleculeFromFile(file2)

    indigo.setOption("molfile-saving-add-stereo-desc", "1");
    mol1.molfile()
    mol2.molfile()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "first variant")
    mol2.setProperty("grid-comment", "second variant")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

The second case is the molecule with cyclic ligands and heterocycles.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/P-92_2_1_3_ex1.mol,data/P-92_2_1_3_ex2.mol
    
    # Load structure
    file1 = "data/P-92_2_1_3_ex1.mol"
    file2 = "data/P-92_2_1_3_ex2.mol"
    mol1 = indigo.loadMoleculeFromFile(file1)
    mol2 = indigo.loadMoleculeFromFile(file2)

    indigo.setOption("molfile-saving-add-stereo-desc", "1");
    mol1.molfile()
    mol2.molfile()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "first variant")
    mol2.setProperty("grid-comment", "second variant")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')
