#####################
Stereocenters options
#####################


.. indigo_option::
    :name: ignore-stereochemistry-errors
    :type: boolean
    :default: false
    :short: When reading a Molfile/Rxnfile with incorrectly marked stereobonds, ignore them rather than raise an error.

    Sometimes molecules contain stereobond marks that do not define stereocenters properly. It can be either mistake made by a user, or stereoconfiguration notation is not known to Indigo. Let's condside the following molecule:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: data/stereoerrors.mol
        :nocode:

        indigo.setOption("ignore-stereochemistry-errors", True)
        m = indigo.loadMoleculeFromFile('data/stereoerrors.mol')
        indigoRenderer.renderToFile(m, 'result.png')

    Stereobond near Oxygen atom is probably set in a wrong direction bny mistake, and when loaded with Indigo one gets an exception about invalid stereobonds configuration:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: data/stereoerrors.mol
        :noimage:

        # Load structure and get exception about stereocenters
        try:
            m = indigo.loadMoleculeFromFile('data/stereoerrors.mol')
        except IndigoException, ex:
            print("Exception: " + str(ex))

    To load this structure we can ignore such errors:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :codename: opt-ignore-stereo-load
        :noimage:

        indigo.setOption("ignore-stereochemistry-errors", True)
        m = indigo.loadMoleculeFromFile('data/stereoerrors.mol')

    All other valid stereocenters are loaded. All stereobond marks are also loaded even if they correspond to an invalid stereocenter. In the example below we see that ``layout`` methods marked only valid stereocenter.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: opt-ignore-stereo-load

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


.. indigo_option::
    :name: stereochemistry-bidirectional-mode
    :type: boolean
    :default: false
    :short: Treat stereobond direction bond not only for a pointed stereocenter, but for the neighbour as well.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: data/bidirect.mol

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


