################
Indigo 1.2.2beta
################

*12 November 2015*

*******
Summary
*******


**New features and improvements**:

* New layout algorithm. ``SMART`` layout mode was added.( :ref:`details <indigo-1.2.2b-layout>`)

* SGroup rich support was implemented.( Please see :ref:`details <indigo-1.2.2b-sgroups>`)

* SCSR Transformations ( :ref:`details <indigo-1.2.2b-scsr>`)

* Tautomer enumeration was implemented ( :ref:`details <indigo-1.2.2b-tautomer>`)

* Ionize and pKa calculation methods (:ref:`details <indigo-1.2.2b-pka>`)

* CIP descriptors simplest implementation (:ref:`details <indigo-1.2.2b-cip>`)

* New Maven repository deployment (:ref:`details <indigo-1.2.2b-maven>`)

**Bugfixes**:

* SGroups related bugs were fixed

* Layout bugfixes

* `Bug <https://github.com/epam/Indigo/issues/22>`__ with dearomatization was fixed 

* `Bug <https://github.com/epam/Indigo/issues/21>`__ with CDX empty objects

* SDF ordering issue was fixed

* Other small bugfixes




*******
Details
*******

.. _indigo-1.2.2b-layout:

======
HEADER
======

Text

.. _indigo-1.2.2b-sgroups:

======
HEADER
======

Text


.. _indigo-1.2.2b-scsr:

======
HEADER
======

Text


.. _indigo-1.2.2b-tautomer:

======
HEADER
======

Text


.. _indigo-1.2.2b-pka:

======
HEADER
======

Text


.. _indigo-1.2.2b-cip:

======
HEADER
======

Text


.. _indigo-1.2.2b-maven:


======
HEADER
======

Text


.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("standardize-stereo", True);

    mol1 = indigo.loadMolecule('CCN1C(SC(C)N1)')
    mol2 = mol1.clone()

    mol2.standardize()

    array = indigo.createArray()

    mol1.setProperty("grid-comment", "before")
    mol2.setProperty("grid-comment", "after")
    
    array.arrayAdd(mol1)
    array.arrayAdd(mol2)

    indigo.setOption("render-grid-title-property", "grid-comment")
    indigo.setOption("render-grid-margins", "20, 10")
    indigo.setOption("render-grid-title-offset", "10")

    indigoRenderer.renderGridToFile(array, None, 2, 'result.png')



