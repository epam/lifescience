#############
InChI options
#############

.. indigo_option::
    :name: inchi-options
    :type: string
    :default: none
    :short: Options supported by the official InChI plugin.

    The following options are supported by the official InChI plugin:

    * /NEWPSOFF
    * /DoNotAddH
    * /SNon
    * /SRel
    * /SRac
    * /SUCF
    * /ChiralFlagON
    * /ChiralFlagOFF
    * /SUU
    * /SLUUD
    * /FixedH
    * /RecMet
    * /KET
    * /15T


.. code-block:: python

    m = indigo.loadMolecule("CC1CC(C)OC(C)N1")
    print(indigoInchi.getInchi(m))

    indigo.setOption("inchi-options", "/SUU")
    print(indigoInchi.getInchi(m))

    indigo.setOption("inchi-options", "/DoNotAddH /SUU")
    print(indigoInchi.getInchi(m))

Output:

.. code-block:: text

    InChI=1S/C7H15NO/c1-5-4-6(2)9-7(3)8-5/h5-8H,4H2,1-3H3
    InChI=1/C7H15NO/c1-5-4-6(2)9-7(3)8-5/h5-8H,4H2,1-3H3/t5?,6?,7?
    InChI=1/C7NO/c1-5-4-6(2)9-7(3)8-5
