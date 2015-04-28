***************
Generic options
***************



.. indigo_option::
    :name: ignore-noncritical-query-features
    :type: boolean
    :default: false
    :short: 
        When true, the "bond topology", "stereo care", "ring bond count", and "unsaturation" specifications are
        ignored when a non-query molecule is being loaded.

    Indigo has two kind of molecule object: molecule and query molecule. Query molecules represent patterns for ordinary molecules and they are used in substructure search. Many properties are not defined for query molecules, for example, implicit hydrogens count, because query molecule is a pattern. 

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: data/noncritial_query.mol

        # Load structure and get exception about stereocenters
        query = indigo.loadQueryMoleculeFromFile('data/noncritial_query.mol')
        indigoRenderer.renderToFile(query, 'result.png')

    When such query molecule is loaded as ordinary molecule Indigo throws an exception about query features:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        # Load structure and get exception about query features
        try:
            m = indigo.loadMoleculeFromFile('data/noncritial_query.mol')
        except IndigoException, ex:
            print("Exception: " + str(ex))

    To load such structure we have to set ``ignore-noncritical-query-features`` option.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        indigo.setOption("ignore-noncritical-query-features", True)
        m = indigo.loadMoleculeFromFile('data/noncritial_query.mol')
        indigoRenderer.renderToFile(m, 'result.png')

.. indigo_option::
    :name: treat-x-as-pseudoatom
    :type: boolean
    :default: false
    :short: 
        Treat 'X' atoms in Molfiles/Rxnfiles as pseudoatoms, rather than "any halogen" query atoms.

.. indigo_option::
    :name: skip-3d-chirality
    :type: boolean
    :default: false
    :short: 
        Do not calculate chirality of 3D input structures.

    Indigo automatically reconstructs stereocenters when loading structures from chemical files with 3D coordinates. 

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: data/3d-chiral.mol

        m = indigo.loadMoleculeFromFile('data/3d-chiral.mol')
        indigo.setOption("render-comment", "3D coordinates")
        indigoRenderer.renderToFile(m, 'result_1.png')

        m.layout()
        indigo.setOption("render-comment", "2D coordinates")
        indigoRenderer.renderToFile(m, 'result_2.png')

.. indigo_option::
    :name: molfile-saving-mode
    :type: enum (auto, 2000, 3000)
    :default: auto
    :short: 
        Molfile saving mode

    **2000:**
        force saving Molfiles and Rxnfiles to v2000 format, not regarding if there are features that can not be represented in v2000.
    **3000:**
        force saving Molfiles and Rxnfiles to v3000 format, not regarding if there are features that can not be represented in v2000.
    **auto:**
        detect if saving to v3000 is really needed, and then save to v3000. Otherwise, save to v2000.


.. indigo_option::
    :name: molfile-saving-no-chiral
    :type: boolean
    :default: false
    :short: 
        Do no write the "Chiral" flag when saving Molfiles and Rxnfiles


.. indigo_option::
    :name: molfile-saving-skip-date
    :type: boolean
    :default: false
    :short: 
        Do no write the current date into Molfiles, Rxnfiles and RDFiles

.. indigo_option::
    :name: smiles-saving-write-name
    :type: boolean
    :default: false
    :short: 
        Write names when saving via generic saver interface in SMILES mode
        
    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        # Create molecules and set their names
        m1 = indigo.loadMolecule('[H][C@](C)(N)O')
        m1.setName("Molecule 1")
        m2 = indigo.loadMolecule('C1=CC=CC=C1')
        m2.setName("Molecule 2")

        indigo.setOption("smiles-saving-write-name", True)

        # Create string stream and save molecules in SMILES format into it
        buffer = indigo.writeBuffer()
        saver = indigo.createSaver(buffer, "smi")
        saver.append(m1)
        saver.append(m2)

        print(buffer.toString())

.. indigo_option::
    :name: filename-encoding
    :type: enum (ascii, utf-8)
    :default: ascii
    :short: 
        File names encoding
        

.. indigo_option::
    :name: serialize-preserve-ordering
    :type: boolean
    :default: false
    :short: 
        Preserve atom and bond ordering in the serialization procedure
        

