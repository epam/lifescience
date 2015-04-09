.. _indigo-example-standardize:

===========
Standardize
===========

These examples show how to use different standardize option.

------
Stereo
------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-stereo", True);

    mol1 = indigo.loadMolecule('CCN1C(SC(C)N1)')
    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')



-------
Charges
-------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-charges", True);

    mol1 = indigo.loadMolecule("CN(=O)=O")

    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

--------
Geometry
--------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-keep-largest", "true")
    mol1 = indigo.loadMolecule("NN.C.CC.CCC")

    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

-----
Query
-----

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-charges", "false");
    indigo.setOption("standardize-make-non-h-to-c-atoms", "true")
    mol1 = indigo.loadQueryMolecule("CN1C=NC(=C1)C(=O)O")

    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

----
Misc
----

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-charges", "false");
    indigo.setOption("standardize-make-non-h-to-c-atoms", "false")

    indigo.setOption("standardize-neutralize-zwitterions", "true")
    mol1 = indigo.loadMolecule("[CH++][CH--]")

    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')
