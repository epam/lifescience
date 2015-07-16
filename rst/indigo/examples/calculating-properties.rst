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
    iter = indigo.tautomerEnumerate(molecule, 'INCHI')
    lst = list()
    for mol in iter:
        lst.append(mol.clone().canonicalSmiles())

    lst.sort()
    print "\n".join(map(lambda x, y: str(x) + ") " + y, range(1, len(lst) + 1), lst))


If the molecule is aromatized before enumeration, the list of tautomers will be aromatized (if possible):

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    molecule = indigo.loadMolecule('OC1C2C=NNC=2N=CN=1')
    molecule.aromatize()

    #print the list of tautomers for the molecule
    iter = indigo.tautomerEnumerate(molecule, 'INCHI')
    lst = list()
    for mol in iter:
        lst.append(mol.clone().canonicalSmiles())

    lst.sort()
    print "\n".join(map(lambda x, y: str(x) + ") " + y, range(1, len(lst) + 1), lst))

Please notice that the number of tautomers could be different in aromatized and dearomatized forms.
This happens because some aromatized forms could have different dearomatized representations.
