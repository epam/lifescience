#######
Options
#######

Indigo instance represents an environment for IndigoObjects. Many methods in Indigo has additional options that can be set via Indigo.setOption method:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("render-comment", "text comment")
    indigo.setOption("render-comment-color", "0, 0.4, 0.5")
    indigo.setOption("ignore-stereochemistry-errors", True)

.. rubric::
    Contents

.. toctree::
    :maxdepth: 1


    input-output-options.rst
    layout-options.rst
    rendering-options.rst
    grid-rendering-options.rst
    substructure-matching-options.rst
    stereocenters-options
    fingerprints.rst
    deconvolution.rst
    aromaticity.rst
    timeout.rst
    reaction-product-enumeration.rst
    inchi.rst
    standardize

Options Table
-------------

.. indigo_options_table::


