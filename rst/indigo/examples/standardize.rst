.. _indigo-example-standardize:

===========
Standardize
===========

These examples show how to use different standardize option.

------
Stereo
------

.. code-block:: python

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

.. image:: ../../assets/indigo/render/indigorenderer_527964ef842912c52f81607c9069f8eb49b9ea7f.svg
    :scale: 100


-------
Charges
-------

.. code-block:: python

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

.. image:: ../../assets/indigo/render/indigorenderer_96eefc74e6e2e78efad408324ecb19bfc51d5383.svg
    :scale: 100

--------
Geometry
--------

.. code-block:: python

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

.. image:: ../../assets/indigo/render/indigorenderer_90c91c6042de1bbac803e34b369f29aa357f89c6.svg
    :scale: 100

-----
Query
-----

.. code-block:: python

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

.. image:: ../../assets/indigo/render/indigorenderer_1f817ae3dd242c35c4553f7682bb37f59933f9c7.svg
    :scale: 100

----
Misc
----

.. code-block:: python

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

.. image:: ../../assets/indigo/render/indigorenderer_a30f078489b272882883e0cf984328fb49110083.svg
    :scale: 100
