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
    m = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')

    #print canonical smiles
    print(m.canonicalSmiles())

