===========
Standardize
===========
    

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-stereo", True);
    indigo.setOption("standardize-charges", True);

    mol1 = indigo.loadMolecule('CCN1C(SC(C)N1)')
    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

