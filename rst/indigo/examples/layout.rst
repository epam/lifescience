.. _indigo-example-layout:

=======================
Layout (2D coordinates)
=======================

This example shows work of automatic layout

-----------------------
Smart and simple layout
-----------------------

This examples shows difference beetwen "smart" and "simple" layout:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/smart-simple-compare.smi
    
    # Load structure
    file = "data/smart-simple-compare.smi"
    array = indigo.createArray()
    for mol1 in indigo.iterateSmilesFile(file):
        mol2 = mol1.clone()
        indigo.setOption("smart-layout", "false")
        mol1.layout()
        mol1.setProperty("grid-comment", "simple")
        array.arrayAdd(mol1)
        indigo.setOption("smart-layout", "true")
        mol2.layout()
        mol2.setProperty("grid-comment", "smart")
        array.arrayAdd(mol2)
    
    indigo.setOption("render-bond-length", "14")
    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "5")
    
    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')

Content of the file :download:`data/smart-simple-compare.smi` with 6 molecules that is used in the example above:
    
.. literalinclude:: data/smart-simple-compare.smi
