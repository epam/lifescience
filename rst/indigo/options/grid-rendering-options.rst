######################
Grid rendering options
######################

.. indigo_option::
    :name: render-grid-margins
    :type: size
    :default: 0, 0
    :short: Horizontal and vertical margins around the grid cell, in pixels.

.. indigo_option::
    :name: render-grid-title-property
    :type: string
    :default: none
    :short: The name of the molecule's property that defines the title that is put under each molecule.

    If not defined, no titles are shown. The special value "^NAME" means to use the molecule's name as its title.

    .. code-block:: python

        array = indigo.createArray()
        for m in indigo.iterateSDFile('data/pubchem-subset.sdf'):
            array.arrayAdd(m)

        indigo.setOption("render-grid-margins", "10, 10")
        indigo.setOption("render-grid-title-offset", "10")
        indigo.setOption("render-comment-position", "top")
        indigo.setOption("render-grid-title-font-size", "15")

        indigo.setOption("render-grid-title-property", "PUBCHEM_MOLECULAR_WEIGHT")
        indigo.setOption("render-comment", "PUBCHEM_MOLECULAR_WEIGHT")
        indigoRenderer.renderGridToFile(array, None, 2, "result_2.png")

        indigo.setOption("render-grid-title-property", "PUBCHEM_COORDINATE_TYPE")
        indigo.setOption("render-comment", "PUBCHEM_COORDINATE_TYPE")
        indigoRenderer.renderGridToFile(array, None, 2, "result_1.png")

    Input: :download:`data/pubchem-subset.sdf`

    .. image:: ../../assets/indigo/render/indigorenderer_f2c0953e4d94d496be0b86e91d17c3081f9a4ced2.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_f2c0953e4d94d496be0b86e91d17c3081f9a4ced1.svg
        :scale: 50


.. indigo_option::
    :name: render-grid-title-alignment
    :type: enum
    :default: center
    :short: Cell title alignment

    Supported values: left, right, center, center-left

    .. code-block:: python

        array = indigo.createArray()
        for m in indigo.iterateSDFile('data/pubchem-subset.sdf'):
            array.arrayAdd(m)

        indigo.setOption("render-grid-margins", "10, 10")
        indigo.setOption("render-grid-title-offset", "10")
        indigo.setOption("render-comment-position", "top")
        indigo.setOption("render-grid-title-font-size", "15")
        indigo.setOption("render-grid-title-alignment", "center-left")

        indigo.setOption("render-grid-title-property", "PUBCHEM_COORDINATE_TYPE")
        indigo.setOption("render-comment", "render-grid-title-alignment=center-left")
        indigoRenderer.renderGridToFile(array, None, 2, "result_1.png")
    
    Input: :download:`data/pubchem-subset.sdf`

    .. image:: ../../assets/indigo/render/indigorenderer_1f76fdbc2b15e2ce3e18489cad7cfb7e9ed273b61.svg
        :scale: 100

.. indigo_option::
    :name: render-grid-title-font-size
    :type: int
    :default: 20
    :short: Font size for the title in absolute units, roughly equal to the height in pixels.

.. indigo_option::
    :name: render-grid-title-offset
    :type: int
    :default: 0
    :short: Vertical space (in pixels) between the title and the rendered structure.
