.. _indigo-example-calculating-properties:

======================
Calculating Properties
======================

This examples shows how to calculate different molecule and reaction properties

.. _indigo-example-canonical-smiles:

----------------
Canonical Smiles
----------------

The following code prints canonical smiles string for a given structure

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    
    # Load structure
    mol = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')

    #print canonical smiles for a molecule
    print(mol.canonicalSmiles())

|
The example below prints canonical smiles string for a given reaction

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    rxn = indigo.loadReaction('[CH2:1]=[CH:2][CH:3]=[CH:4][CH2:5][H:6]>>[H:6][CH2:1][CH:2]=[CH:3][CH:4]=[CH2:5]')

    #print canonical smiles for a reaction
    print(rxn.canonicalSmiles())

