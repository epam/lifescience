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

* TGroups and SCSR Transformations ( :ref:`details <indigo-1.2.2b-scsr>`)

* Tautomer enumeration was implemented ( :ref:`details <indigo-1.2.2b-tautomer>`)

* Ionize and pKa calculation methods (:ref:`details <indigo-1.2.2b-pka>`)

* New Maven repository deployment (:ref:`details <indigo-1.2.2b-maven>`)

* CIP descriptors simplest implementation (:ref:`details <indigo-1.2.2b-cip>`)


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

=======
SGroups
=======

There are many kinds of S-groups,
Indigo now supports all described in the format:

-  generic SGroup (GEN)
-  abbreviation (superatom) (SUP)
-  structure repeating unit (SRU)
-  multiple SGroup (MUL)
-  data SGroup (DAT)
-  monomer SGroup (MON)
-  mer SGroup (MER)
-  copolymer SGroup (COP)
-  crosslink SGroup (CRO)
-  modification SGroup (MOD)
-  graft SGroup (GRA)
-  component SGroup (COM)
-  mixture SGroup (MIX)
-  formulation SGroup (FOR)
-  any polymer SGroup (ANY)


Please see new `Indigo API methods <../../api/index.html#sgroups>`__. 


.. _indigo-1.2.2b-scsr:

=======
TGroups
=======

Indigo supports the hybrid representation (SCSR) for a molecule loaded from a V3000 Molfile.
SCSR uses TEMPLATE blocks to represent residues and this representation is widely used for biological sequences.

There are methods for transformation SCSR into full CTAB form and vise versa:

-  ``transformSCSRtoCTAB`` - transforms SCSR into full CTAB representation (templates are transformed into S-groups)
-  ``transformCTABtoSCSR`` - transforms CTAB into SCSR (accepts templates collection and replaces matched fragments by pseudoatoms and corresponding templates)

Examples of usage these methods are in corresponding `Examples <../../examples/scsr-transformations.html>`__ section.



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

.. _indigo-1.2.2b-maven:


========================
Maven Central Repository
========================

All the Indigo Java packages are uploaded to `The Central Repository <http://search.maven.org/#search|ga|1|g%3A%22com.epam.indigo%22>`_.

======================   ===============
GroupId                  ArtifactId
======================   ===============
com.epam.indigo          indigo
com.epam.indigo          indigo-inchi
com.epam.indigo          indigo-renderer
com.epam.indigo          bingo-nosql
======================   ===============

Just add a dependency to your Maven project to download Indigo Java API automatically::

    <dependencies>
        ...
        <dependency>
            <groupId>com.epam.indigo</groupId>
            <artifactId>indigo</artifactId>
            <version>1.2.2beta-r37</version>
        </dependency>
        ...
    </dependencies>


Please note: all Java packages were changed to use ``com.epam`` package

.. _indigo-1.2.2b-cip:

======
HEADER
======

Text

