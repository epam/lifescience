################
Indigo 1.2.2beta
################

*18 November 2015*

*******
Summary
*******


Please note, in this **beta** version Indigo introduces very "new" and "novel" features and algorithms. We look forward to receiving any questions or notes for this version.

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

==================
Layout enhancement
==================

New original algorithm was implemented to improve layout procedure for the difficult cycle structures. New `option <../../examples/layout.html#smart-and-simple-layout>`__ ``SMART`` was added. By using this option, one can compare the layout procedures. 

Please see `examples <../../examples/layout.html>`__ for more details  

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

========================
Enumeration of Tautomers
========================

Indigo provides a method to enumerate tautomers of a selected molecule.
Currently there are two algorithms to enumerate tautomers: based on InChI code and based on a set of reaction SMARTS rules.

The ``iterateTautomers`` method returns an iterator for tautomers. It accepts a molecule and options as parameters.
There are two possible options: ``INCHI`` to use method based on `InChI code <../../../resources.html#inchi-code>`__, and ``RSMARTS`` to use `reaction SMARTS templates <../../../resources.html#rsmarts-rules>`__

Please see the `API description <../../api/index.html#enumeration-of-tautomers>`__ or the :ref:`indigo-example-tautomer-enumeration` for detailed examples.


.. _indigo-1.2.2b-pka:

===========================
Ionize and pKa calculations
===========================

The new ``IndigoObject.ionize`` method can be used for building protonated/deprotonated form
of the molecule in accordance with pH and pH tolerance. pKa model for pKa estimation can be
defined using corresponding `Options <../../options/pka.html>`__ section). 

The ``IndigoObject.getAcidPkaValue`` and ``IndigoObject.getBasicPkaValue`` method can be used for
estimation pKa values for individual atoms in a molecule. pKa model for pKa estimation can be
defined using corresponding `Options <../../options/pka.html>`__ section).

The ``IndigoObject.buildPkaModel`` method is used for building pKa model based on custom structures
set.

See `API methods <../../api/index.html#ionize-of-molecule>`__ for some examples


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

======================
CIP Stereo Descriptors
======================

Indigo provides the CIP stereo descriptors calculations.
These calculations correspond latest chemical nomenclature requirements
(Nomenclature of Organic Chemistry - IUPAC Recommendations and Preferred Names (2013)).
Current implementation includes some simplifications and supports calculations only R/S and E/Z
descriptors. 

Please see the :ref:`indigo-example-cip-descriptors` for detailed examples.

