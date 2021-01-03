.. _indigo-example-scsr-transformations:

====================
SCSR Transformations
====================

--------------------------------------------
Transform SCSR into full CTAB representation
--------------------------------------------

.. code-block:: python
    
    # Load structure
    file = "data/scsr-example1.mol"
    mol1 = indigo.loadMoleculeFromFile(file)
    mol2 = mol1.clone();

    mol2.transformSCSRtoCTAB()
    mol2.layout()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

Input: :download:`data/scsr-example1.mol`

.. image:: ../../assets/indigo/render/indigorenderer_c0ccb92117fa480d9a8dfdf0fe374a201c5f039e.svg
    :scale: 100


------------------------
Transform CTAB into SCSR
------------------------

.. code-block:: python
    
    # Load structure
    file1 = "data/scsr-example2.mol"
    mol1 = indigo.loadMoleculeFromFile(file1)
    mol2 = mol1.clone();

    file2 = "data/scsr-templates.mol"
    templates = indigo.loadMoleculeFromFile(file2)
    mol2.transformCTABtoSCSR(templates)
    mol2.layout()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

Input: :download:`data/scsr-example2.mol`, :download:`data/scsr-templates.mol`

.. image:: ../../assets/indigo/render/indigorenderer_ac7056efbe09096e375b51339911ffff8bb43a85.svg
    :scale: 100
