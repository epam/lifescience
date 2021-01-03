#####################
Stereocenters options
#####################


.. indigo_option::
    :name: ignore-stereochemistry-errors
    :type: boolean
    :default: false
    :short: When reading a Molfile/Rxnfile with incorrectly marked stereobonds, ignore them rather than raise an error.

    Sometimes molecules contain stereobond marks that do not define stereocenters properly. It can be either mistake made by a user, or stereoconfiguration notation is not known to Indigo. Let's condside the following molecule:

    Input: :download:`data/stereoerrors.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_c233d91eab44d2961f49a49b722bbb4fd7f19beb.svg
        :scale: 100

    Stereobond near Oxygen atom is probably set in a wrong direction bny mistake, and when loaded with Indigo one gets an exception about invalid stereobonds configuration:

    .. code-block:: python

        # Load structure and get exception about stereocenters
        try:
            m = indigo.loadMoleculeFromFile('data/stereoerrors.mol')
        except IndigoException, ex:
            print("Exception: " + str(ex))

    Input: :download:`data/stereoerrors.mol`

    Output:

    .. code-block:: text

        Exception: molfile loader: direction of bond #1 makes no sense

    To load this structure we can ignore such errors:

    .. code-block:: python

        indigo.setOption("ignore-stereochemistry-errors", True)
        m = indigo.loadMoleculeFromFile('data/stereoerrors.mol')

    All other valid stereocenters are loaded. All stereobond marks are also loaded even if they correspond to an invalid stereocenter. In the example below we see that ``layout`` methods marked only valid stereocenter.

    .. code-block:: python

        print("Smiles:\n" + m.smiles())

        indigo.setOption("render-comment", "Original")
        indigoRenderer.renderToFile(m, 'result_1.png')

        indigo.setOption("render-comment", "With bond indices")
        indigo.setOption("render-bond-ids-visible", True)
        indigoRenderer.renderToFile(m, 'result_2.png')
        indigo.setOption("render-bond-ids-visible", False)

        m.layout()
        indigo.setOption("render-comment", "After cleanup")
        indigoRenderer.renderToFile(m, 'result_3.png')

    .. image:: ../../assets/indigo/render/indigorenderer_ccdb476c0abec6500124086d93594adf7b28c9701.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_ccdb476c0abec6500124086d93594adf7b28c9702.svg
        :scale: 33

    .. image:: ../../assets/indigo/render/indigorenderer_ccdb476c0abec6500124086d93594adf7b28c9703.svg
        :scale: 33

    Output:

    .. code-block:: text

        Smiles:
        O(C(C(N)=O)C)C([C@H](C)O)=O |&1:7,r|

.. indigo_option::
    :name: stereochemistry-bidirectional-mode
    :type: boolean
    :default: false
    :short: Treat stereobond direction bond not only for a pointed stereocenter, but for the neighbour as well.

    .. code-block:: python

        print("stereochemistry-bidirectional-mode")
        # Load structure 
        m = indigo.loadMoleculeFromFile('data/bidirect.mol')
        print("False: " + m.smiles())
        indigo.setOption("render-comment", "False")
        indigoRenderer.renderToFile(m, 'result_1.png')
        
        #Set option
        indigo.setOption("stereochemistry-bidirectional-mode", True)
        m2 = indigo.loadMoleculeFromFile('data/bidirect.mol')
        print("True: " + m2.smiles())

        indigo.setOption("render-comment", "True")
        indigoRenderer.renderToFile(m2, 'result_2.png')

    Input: :download:`data/bidirect.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_ebec709332c1a380896746827e2e84b7104290b11.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_ebec709332c1a380896746827e2e84b7104290b12.svg
        :scale: 50

    Output:

    .. code-block:: text

        stereochemistry-bidirectional-mode
        False: OCC(C)[C@@H](C)C[C@@H](C)C(C)CN |w:2,9,&1:4,7,r|
        True: OCC(C)C(C)CC(C)C(C)CN |w:2,4,7,9,r|


.. indigo_option::
   :name: stereochemistry-detect-haworth-projection
   :type: boolean
   :default: false
   :short: Detect Haworth projection

    .. code-block:: python

        # Load structure
        q = indigo.loadQueryMoleculeFromFile('data/projection_ordinary.mol')
        t = indigo.loadMoleculeFromFile('data/projection_haworth.mol')
        
        # Render structures
        indigo.setOption("render-comment", "projection_ordinary")
        indigoRenderer.renderToFile(q, 'result_1.png')
        indigo.setOption("render-comment", "projection_haworth")
        indigoRenderer.renderToFile(t, 'result_2.png')
        
        # Match with haworth-projection option disabled
        matcher = indigo.substructureMatcher(t)
        print("match with haworth-projection turned OFF: " + str(matcher.match(q) != None))

        # Load and match with haworth-projection option enabled
        indigo.setOption("stereochemistry-detect-haworth-projection", "True")
        t2 = indigo.loadMoleculeFromFile('data/projection_haworth.mol')
        matcher = indigo.substructureMatcher(t2)
        print("match with haworth-projection turned ON: " + str(matcher.match(q) != None))

    Input: :download:`data/projection_ordinary.mol`, :download:`data/projection_haworth.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_714a92369463ccdd051549b975978e6d927d14c91.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_714a92369463ccdd051549b975978e6d927d14c92.svg
        :scale: 50

    Output:

    .. code-block:: text

        match with haworth-projection turned OFF: False
        match with haworth-projection turned ON: True
