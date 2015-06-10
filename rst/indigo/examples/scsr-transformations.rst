.. _indigo-example-scsr-transformations:

====================
SCSR Transformations
====================

--------------------------------------------
Transform SCSR into full CTAB representation
--------------------------------------------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/scsr-example1.mol
    
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


------------------------
Transform CTAB into SCSR
------------------------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/scsr-example2.mol,data/scsr-templates.mol
    
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
