###################
Aromaticity options
###################

.. indigo_option::
    :name: aromaticity-model
    :type: enum
    :default: basic
    :short: Aromaticity model

    Aromaticity model used in aromatization and dearomatization procedures. Supported values:

    **basic**:
        External double bond for aromatic rings are not allowed

    **generic**
        External double bond are allowed


.. code-block:: python

    m = indigo.loadMolecule('O=c1[nH]c(nc2c1CSCC2)c1ccc(cc1)C(F)(F)F')

    indigo.setOption("render-comment", "Aromatized")
    indigoRenderer.renderToFile(m, "result_1.png")

    indigo.setOption("aromaticity-model", "basic")
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized (basic)")
    indigoRenderer.renderToFile(m, "result_2.png")

    indigo.setOption("aromaticity-model", "generic")
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized (generic)")
    indigoRenderer.renderToFile(m, "result_3.png")

.. image:: ../../assets/indigo/render/indigorenderer_210b033a455bb5265098a7d10aa011a7f7aa8b061.svg
    :scale: 33

.. image:: ../../assets/indigo/render/indigorenderer_210b033a455bb5265098a7d10aa011a7f7aa8b062.svg
    :scale: 33

.. image:: ../../assets/indigo/render/indigorenderer_210b033a455bb5265098a7d10aa011a7f7aa8b063.svg
    :scale: 33

.. indigo_option::
    :name: dearomatize-verification
    :type: boolean
    :default: true
    :short: Verify dearomatization method

    In the dearomatization method Indigo enumerates possible single/double bonds configurations and checks that such configuration is aromatic. If there are no valid dearomatization for a given aromatic system, then Indigo leaves such aromatic system unchanged. With this option disabled Indigo dearomatizes such aromatic system, but without guarantee that this dearomatization is correct. It can be used to convert anti-aromatic rings:

.. code-block:: python

    m = indigo.loadMolecule('c1ccccccc1')

    indigo.setOption("render-comment", "Original\nstructure")
    indigoRenderer.renderToFile(m, "result_1.png")

    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized with\nverification")
    indigoRenderer.renderToFile(m, "result_2.png")

    indigo.setOption("dearomatize-verification", False)
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized without\nverification")
    indigoRenderer.renderToFile(m, "result_3.png")

.. image:: ../../assets/indigo/render/indigorenderer_64a205b625eac91606167f67326e4b4634dd73ca1.svg
    :scale: 33

.. image:: ../../assets/indigo/render/indigorenderer_64a205b625eac91606167f67326e4b4634dd73ca2.svg
    :scale: 33

.. image:: ../../assets/indigo/render/indigorenderer_64a205b625eac91606167f67326e4b4634dd73ca3.svg
    :scale: 33


.. indigo_option::
    :name: unique-dearomatization
    :type: boolean
    :default: false
    :short: Find dearomatization if all possible configurations uniquely define hydrogens.

    Molfile format doesn't store information about hydrogens in aromatic rings and this leads to a situation when two different (tautomers) structure has the same aromatization.

    .. code::
        :hidden:
        :name: code-unique-dearomatization

        m1 = indigo.loadMoleculeFromFile('data/ambiguous_arom1.mol')
        m2 = indigo.loadMoleculeFromFile('data/ambiguous_arom2.mol')

    .. image:: ../../assets/indigo/render/indigorenderer_92997ca46105f8d8f120747a8852eaa2a02fba521.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_92997ca46105f8d8f120747a8852eaa2a02fba522.svg
        :scale: 50

    Molecules (A) and (B) are different, and aromatic forms are the following:

    .. image:: ../../assets/indigo/render/indigorenderer_fd2b85cebb2428032323245bf285c71d33a012761.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_fd2b85cebb2428032323245bf285c71d33a012762.svg
        :scale: 50

    Such aromatic molecules can be dearomatized, all atoms has specific number of implicit hydrogens and we can compute canonical SMILES:

    Output:

    .. code-block:: text

        (A): Nc1[nH]c(O)c[n]1
        (B): Nc1[nH]cc(O)[n]1

    Let's consider that we loaded a molecule (A) or (B) in an aromatic form from molfile. If explicit hydrogens are not saved into molfile then we get the following structure:

    .. image:: ../../assets/indigo/render/indigorenderer_2d8db7fdcd7c9c858037d63ee71e35b7bcaa202a3.svg
        :scale: 100

    Canonical SMILES computation throws an exception on such molecule because we cannot decided if it is (A) or (B).

    Dearomatization method by default doesn't check uniqueness in terms of number of Hydrogens:

    .. code-block:: python

        m3 = indigo.loadMoleculeFromFile('data/ambiguous_arom3.mol')
        m3.dearomatize()

        indigo.setOption("render-comment", "(C)")
        indigoRenderer.renderToFile(m3, "result_3.png")

    .. image:: ../../assets/indigo/render/indigorenderer_13e298caf26dc7b9374b1fbacd3f211a9e8c46d03.svg
        :scale: 100

    But such check it can be set explicitly if needed, and dearomatize method will throw an exception in this case:

    .. code-block:: python

        m3 = indigo.loadMoleculeFromFile('data/ambiguous_arom3.mol')

        indigo.setOption("unique-dearomatization", True)

        try:
            m3.dearomatize()
        except IndigoException, ex:
            print(str(ex))
    
    Output:

    .. code-block:: text

        non-unique dearomatization: Dearomatization is not unique

    But we still can dearomatize structures if number if hydrogens is uniquely defined:

    .. code-block:: python

        m = indigo.loadMoleculeFromFile('data/ambiguous_arom4.mol')
        indigoRenderer.renderToFile(m, "result_1.png")

        indigo.setOption("unique-dearomatization", True)

        m.dearomatize()
        indigoRenderer.renderToFile(m, "result_2.png")

    Input: :download:`data/ambiguous_arom4.mol`

    .. image:: ../../assets/indigo/render/indigorenderer_8162f487b65b5186515d86c663c78d3546a4d5301.svg
        :scale: 50

    .. image:: ../../assets/indigo/render/indigorenderer_8162f487b65b5186515d86c663c78d3546a4d5302.svg
        :scale: 50
