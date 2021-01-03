#################
Rendering options
#################

General
=======

.. code::
    :name: render-with-different-options
    :hidden:

    def renderWithOptions (mol, name, optvalues, draw_default=False, separator='='):
        if draw_default:
            indigo.setOption("render-comment", "default")
            indigoRenderer.renderToFile(mol, 'result.png')

        for idx, value in enumerate(optvalues):
            indigo.setOption("render-comment", "%s%s%s" % (name, separator, value))
            indigo.setOption(name, value)
            indigoRenderer.renderToFile(mol, 'result_%d.png' % (idx))

    def renderMolfileWithOptions (molfile, name, optvalues, draw_default=False, separator='='):
        mol = indigo.loadMoleculeFromFile(molfile)
        renderWithOptions(mol, name, optvalues, draw_default=draw_default, separator=separator)

    def renderRxnfileWithOptions (rxnfile, name, optvalues):
        rxn = indigo.loadReactionFromFile(rxnfile)
        renderWithOptions(rxn, name, optvalues)

.. indigo_option::
    :name: render-output-format
    :type: string
    :default: automatic
    :short:
        Image file format.

    If this option is not set, then Indigo deduces image format from the file extension.
    Supported formats:
    
    * png
    * pdf
    * svg
    * emf (windows)
    * cdxml (not all options are supported)

.. indigo_option::
    :name: render-image-size
    :type: size
    :default: auto
    :short:
        Width and height of target image.

        If not set, is calculated automatically according to ``render-bond-length``. To reset this setting, you can set the values of width and height to -1. This options defines both width and height that can be set independently via ``render-image-width`` and ``render-image-height`` options.

    .. image:: ../../assets/indigo/render/indigorenderer_3c11ad279c390a28ce067ee73041a6b87ade9e3f0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_3c11ad279c390a28ce067ee73041a6b87ade9e3f1.svg
        :scale: 50

.. indigo_option::
    :name: render-bond-length
    :type: integer
    :default: 100
    :short:
        Desired average bond length in pixels

        The actual average bond length may be less if the ``render-image-size`` option is set. To reset this setting, you can set its value to -1. This option scales label size as well.

    .. image:: ../../assets/indigo/render/indigorenderer_f7be387e6db7f616aa9ba3ab3958a118e3313dea0.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_f7be387e6db7f616aa9ba3ab3958a118e3313dea1.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_f7be387e6db7f616aa9ba3ab3958a118e3313dea2.svg
        :scale: 33

.. indigo_option::
    :name: render-relative-thickness
    :type: float
    :default: 1.0
    :short:
        Set the thickness of bonds and atom labels to X/30 of the average bond length.

    .. image:: ../../assets/indigo/render/indigorenderer_a07a656adc406186148b2958a3995aaeef6abc570.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_a07a656adc406186148b2958a3995aaeef6abc571.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_a07a656adc406186148b2958a3995aaeef6abc572.svg
        :scale: 33


.. indigo_option::
    :name: render-image-width
    :type: int
    :default: auto
    :short: Image width

.. indigo_option::
    :name: render-image-height
    :type: int
    :default: auto
    :short: Image height

.. indigo_option::
    :name: render-image-max-width
    :type: int
    :default: auto
    :short: Maximum image width

.. indigo_option::
    :name: render-image-max-height
    :type: int
    :default: auto
    :short: Maximum image height

.. indigo_option::
    :name: render-margins
    :type: size
    :default: auto
    :short:
        Horizontal and vertical margins around the image, in pixels.

.. indigo_option::
    :name: render-coloring
    :type: boolean
    :default: false
    :short:
        Turn on atom coloring, e.g. nitrogen is blue, oxygen is red, etc.

    .. image:: ../../assets/indigo/render/indigorenderer_4c2f2f8b5b88aaa0cde640208fc5f2006c87a4c80.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_4c2f2f8b5b88aaa0cde640208fc5f2006c87a4c81.svg
        :scale: 50

.. indigo_option::
    :name: render-base-color
    :type: coloring
    :default: black (0, 0, 0)
    :short:
        The default color for atoms and bonds.

    .. image:: ../../assets/indigo/render/indigorenderer_217893bd7c00aa95187cef8027eebbc6d77030ce0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_217893bd7c00aa95187cef8027eebbc6d77030ce1.svg
        :scale: 50

.. indigo_option::
    :name: render-background-color
    :type: color
    :default: transparent
    :short:
        Background color.

    .. image:: ../../assets/indigo/render/indigorenderer_dfbba4ab12e62b149d2d445a353832a6d4bd28d60.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_dfbba4ab12e62b149d2d445a353832a6d4bd28d61.svg
        :scale: 50

    Combination of both ``render-background-color`` and ``render-base-color`` can be used to get negative:

    .. code-block:: python

        m = indigo.loadMoleculeFromFile('data/render_example1.mol')

        indigo.setOption("render-background-color", "0, 0, 0")
        indigo.setOption("render-base-color", "1, 1, 1")

        indigoRenderer.renderToFile(m, "result.png")

    .. image:: ../../assets/indigo/render/indigorenderer_5afc363772e39448d1cd4d5adbf562adbc786795.svg
        :scale: 100

.. indigo_option::
    :name: render-label-mode
    :type: enum
    :default: terminal-hetero
    :short:
        Atom label rendering mode

    **all**
        show all atoms

    **terminal-hetero**
        show heteroatoms, terminal atoms, atoms with radical, charge, isotope, explicit valence, and atoms having two adjacent bonds in a line

    **hetero**
        the same as terminal-hetero, but without terminal atoms

    **none**
        hide all labels, show only bonds

    .. image:: ../../assets/indigo/render/indigorenderer_56e221e816798873127eae5ff474f83b47516fb30.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_56e221e816798873127eae5ff474f83b47516fb31.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_56e221e816798873127eae5ff474f83b47516fb32.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_56e221e816798873127eae5ff474f83b47516fb33.svg
        :scale: 25

.. indigo_option::
    :name: render-hdc-offset
    :type: offset
    :default: 0, 0
    :short: Offset for the rendering area

    .. image:: ../../assets/indigo/render/indigorenderer_5f464c2e2487526b06b2a1470d133836ea5045a80.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_5f464c2e2487526b06b2a1470d133836ea5045a81.svg
        :scale: 50

Comments
========

.. indigo_option::
    :name: render-comment
    :type: string
    :default: 
    :short:
        Put a comment at the top or bottom of the image

     If the image size is set explicitly, it must not be smaller than the size of the comment bounding box.

     All the examples on this page contain comment with option value.

     Comment can have multiple line:

    .. image:: ../../assets/indigo/render/indigorenderer_bd0d6512e3230e62589572a289adf0ba004904ac0.svg
        :scale: 100

.. indigo_option::
    :name: render-comment-font-size
    :type: integer
    :default: 20
    :short:
        Font size for the comment in absolute units, roughly equal to the height in pixels.

    .. image:: ../../assets/indigo/render/indigorenderer_466f5b8ed55a03de5496ec9ad39de337c9b72cbd0.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_466f5b8ed55a03de5496ec9ad39de337c9b72cbd1.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_466f5b8ed55a03de5496ec9ad39de337c9b72cbd2.svg
        :scale: 33

.. indigo_option::
    :name: render-comment-alignment
    :type: enum
    :default: center
    :short: Comment alignment

    Supported values: left, right, center, center-left

    .. image:: ../../assets/indigo/render/indigorenderer_d85affdde4f867d5960bde527951095797c1d58d0.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_d85affdde4f867d5960bde527951095797c1d58d1.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_d85affdde4f867d5960bde527951095797c1d58d2.svg
        :scale: 25

    .. image:: ../../assets/indigo/render/indigorenderer_d85affdde4f867d5960bde527951095797c1d58d3.svg
        :scale: 25


.. indigo_option::
    :name: render-comment-color
    :type: color
    :default: black
    :short:
        Color to use for the comment.

    .. image:: ../../assets/indigo/render/indigorenderer_fb119fbd66421752aca14a7c74518a6781b6133b0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_fb119fbd66421752aca14a7c74518a6781b6133b1.svg
        :scale: 50

.. indigo_option::
    :name: render-bond-line-width
    :type: float
    :default: 1.0
    :short:
        Relative bond line width

    .. image:: ../../assets/indigo/render/indigorenderer_76584355aaca4915a4e67d873c0b81ab9ce6b5f00.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_76584355aaca4915a4e67d873c0b81ab9ce6b5f01.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_76584355aaca4915a4e67d873c0b81ab9ce6b5f02.svg
        :scale: 33

.. indigo_option::
    :name: render-comment-position
    :type: enum
    :default: bottom
    :short:
        top or bottom.

    .. image:: ../../assets/indigo/render/indigorenderer_720c541ef1469ab19d2838f359b7d5e75f9ef98e0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_720c541ef1469ab19d2838f359b7d5e75f9ef98e1.svg
        :scale: 50

.. indigo_option::
    :name: render-comment-offset
    :type: integer
    :default: 0
    :short:
        Vertical space (in pixels) between the comment and the rendered structure or reaction.

    .. image:: ../../assets/indigo/render/indigorenderer_a29812dee01a7255f847acd27a8db84445731a580.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_a29812dee01a7255f847acd27a8db84445731a581.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_a29812dee01a7255f847acd27a8db84445731a582.svg
        :scale: 33

Chemistry
=========

.. indigo_option::
    :name: render-implicit-hydrogens-visible
    :type: boolean
    :default: True
    :short:
        Show implicit hydrogens on visible atoms.

    .. image:: ../../assets/indigo/render/indigorenderer_bb170c86f5ee1dc585166e5390269a0d475c29bf0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_bb170c86f5ee1dc585166e5390269a0d475c29bf1.svg
        :scale: 50


.. indigo_option::
    :name: render-atom-ids-visible
    :type: boolean
    :default: False
    :short:
        Show atom numbers (for debugging purposes only).

    .. image:: ../../assets/indigo/render/indigorenderer_6f053b6acb6a81d303b625911c85a649227eac310.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_6f053b6acb6a81d303b625911c85a649227eac311.svg
        :scale: 50

.. indigo_option::
    :name: render-bond-ids-visible
    :type: boolean
    :default: False
    :short:
        Show bond numbers (for debugging purposes only).

    .. image:: ../../assets/indigo/render/indigorenderer_a7b5ecc20c2aab239e409dc68c7c3ec162cd0b2e0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_a7b5ecc20c2aab239e409dc68c7c3ec162cd0b2e1.svg
        :scale: 50

.. indigo_option::
    :name: render-atom-bond-ids-from-one
    :type: boolean
    :default: False
    :short:
        Show atom and bond numbers starting from one, not from zero.


.. indigo_option::
    :name: render-aam-color
    :type: color
    :default: black
    :short: Atom-by-atom mapping indices color in reactions.

    .. image:: ../../assets/indigo/render/indigorenderer_2d4b51b4095d744294e0a4b18dd40230c8e664f30.svg
        :scale: 100

.. indigo_option::
    :name: render-atom-color-property
    :type: string
    :default: none
    :short: S-group name for atom colors

    Indigo can use a specified color for each atom and interpolate these colors for bond rendering.

    .. code-block:: python

        # Load structure
        m = indigo.loadMolecule('CC(=C)C1=C(C)C(C)=CC(O)=C1NCCCCC=O')
        
        # Add data sgroups with 'color' description
        m.addDataSGroup([0, 1, 2, 3], [], "color", "0.155, 0.55, 0.955")
        m.addDataSGroup([4, 5, 6, 16, 17, 18], [], "color", "0.955, 0.155, 0.155")
        
        indigo.setOption("render-atom-color-property", "color")
        indigo.setOption('render-coloring', False)
        indigoRenderer.renderToFile(m, 'result.png')

    .. image:: ../../assets/indigo/render/indigorenderer_bfb81f9acd9910b65776d216ac99637f46e02283.svg
        :scale: 100

    See :ref:`indigo-example-atom-coloring` for a larger example.

.. indigo_option::
    :name: render-bold-bond-detection
    :type: boolean
    :default: true
    :short: Detect and draw bold bond for Haworth projection

    Input: :download:`data/bold-bond.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_1bc28b16c239ff2c4e4bd87858d8743f2b4a13cd0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_1bc28b16c239ff2c4e4bd87858d8743f2b4a13cd1.svg
        :scale: 50

.. indigo_option::
    :name: render-catalysts-placement
    :type: enum
    :default: above-and-below
    :short: Reaction catalysts place relative to the reaction arrow

    Input: :download:`data/catalysts3000.rxn`

    .. image:: ../../assets/indigo/render/indigorenderer_b6c60f30bd0cc1572a0865431b90994855115fa80.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_b6c60f30bd0cc1572a0865431b90994855115fa81.svg
        :scale: 50


.. indigo_option::
    :name: render-center-double-bond-when-stereo-adjacent
    :type: boolean
    :default: false
    :short: Center double done if there is an attached stereobond

    .. image:: ../../assets/indigo/render/indigorenderer_e40818900fba8c7e8b4bf18e05a6552c536ce6a10.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_e40818900fba8c7e8b4bf18e05a6552c536ce6a11.svg
        :scale: 50

.. indigo_option::
    :name: render-data-sgroup-color
    :type: color
    :default: black
    :short: Color for data-sgroups

    Input: :download:`data/render_example-sgroup.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_e18eb2e98d5eea2b76442abaa014b5f81ef12eb80.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_e18eb2e98d5eea2b76442abaa014b5f81ef12eb81.svg
        :scale: 50



.. indigo_option::
    :name: render-stereo-style
    :type: enum (old, ext, none)
    :default: old
    :short: Stereocenters rendering mode

    **old**:
        Only display the "Chiral" sign when appropriate.
    **ext**:
        Display "abs", "and", "or" labels near each stereocenter.
    **none**:
        Hide all the information about the stereogroups.

    Input: :download:`data/stereo-chiral.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_45bbf8dc3fd3f1a657d113e5f8290004b699a5fe0.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_45bbf8dc3fd3f1a657d113e5f8290004b699a5fe1.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_45bbf8dc3fd3f1a657d113e5f8290004b699a5fe2.svg
        :scale: 33

    `Old` style of rendering is used only with ordinary stereocenters, and enhanced stereocenters with `and` and `or` groups are rendered the same in the `old` and `ext` mode:

    Input: :download:`data/stereo-chiral2.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_2ffd17f6774edd33a8e5c7622aa0a8180955981a0.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_2ffd17f6774edd33a8e5c7622aa0a8180955981a1.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_2ffd17f6774edd33a8e5c7622aa0a8180955981a2.svg
        :scale: 33


.. indigo_option::
    :name: render-superatom-mode
    :type: enum (expand, collapse)
    :default: expand
    :short: Superatoms rendering mode

    Input: :download:`data/abbr.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_47ecde5d4f564604570713bf01f4aa9513aee8a80.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_47ecde5d4f564604570713bf01f4aa9513aee8a81.svg
        :scale: 50

.. indigo_option::
    :name: render-valences-visible
    :type: boolean
    :default: true
    :short: Render explicit valences

    .. image:: ../../assets/indigo/render/indigorenderer_0353c45c93208719837a25cd05e68583a4e2a73f0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_0353c45c93208719837a25cd05e68583a4e2a73f1.svg
        :scale: 50

Highlighting
============

.. indigo_option::
    :name: render-highlight-color
    :type: color
    :default: red
    :short: The color to be used for highlighting.

    Input: :download:`data/highlighting.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_e905816881c8d623ce00c9e36c772bfd193700890.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_e905816881c8d623ce00c9e36c772bfd193700891.svg
        :scale: 50

.. indigo_option::
    :name: render-highlight-color-enabled
    :type: boolean
    :default: true
    :short: Enable highlighting with color.

    Input: :download:`data/highlighting.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_3d437ca521688ef7272f242d9f7139493fec3f110.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_3d437ca521688ef7272f242d9f7139493fec3f111.svg
        :scale: 50

.. indigo_option::
    :name: render-highlight-thickness-enabled
    :type: boolean
    :default: false
    :short: Enable highlighting with thick bonds and bold atom labels.

    Input: :download:`data/highlighting.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_c31cb16e30c5cc90f32e10593163cb2a0448691d0.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_c31cb16e30c5cc90f32e10593163cb2a0448691d1.svg
        :scale: 50

.. indigo_option::
    :name: render-highlighted-labels-visible
    :type: boolean
    :default: False
    :short:
        Always show labels of highlighted atoms.

    Input: :download:`data/highlighting.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_684946bb4d432e3399d9428862c423b9e7e9e1580.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_684946bb4d432e3399d9428862c423b9e7e9e1581.svg
        :scale: 50
