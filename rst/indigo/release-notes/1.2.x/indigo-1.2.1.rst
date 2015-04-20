############
Indigo 1.2.1
############

*2 April 2013*

*******
Summary
*******


**New features and improvements**:

* Bingo NoSQL new plugin for Indigo was released.( Please see :ref:`details <indigo-1.2.1-bingo-nosql>`)

* ``standardize()`` function was implemented ( :ref:`details <indigo-1.2.1-standardize>`)

* SGroup better support. Loading, saving, searching, editing different types of SGroups  

* ``canonicalSmiles()`` for *Reactions* ( see :ref:`examples <indigo-example-canonical-smiles>`)

* Molfile V3000 type9 and type10 bonds support was implemented

* ChemDraw CDX reader was implemented ( :ref:`details <indigo-1.2.1-cdx>`)

* New option for skipping layout while reaction product enumeration. ( ``TODO``)

* Stereo and cis-trans configuration better support ( :ref:`details <indigo-1.2.1-stereo>`)

* Bidirectional stereocenters mode (used by ChemDraw) support was implemented. :optref:`stereochemistry-bidirectional-mode` option was added.  




**Bugfixes**:

* SGroups releated bugs were fixed

* Indigo now calculates stereocenters for SMARTS like ``[*@H](~*)~*`` ( :ref:`details <indigo-1.2.1-stereo>`)

* Bug with ``countComponents()`` was fixed

* Custom collection names loading in molfile V3000

* Bug with superatoms saving was fixed




*******
Details
*******

.. _indigo-1.2.1-bingo-nosql:

==================
Bingo NoSQL plugin
==================

Bingo NoSQL is a Indigo plugin and non-relational database management system for storing 
chemical information and searching through it. With this plugin you can create databases which will be located on the hard drive of your local machine or some remote server. Bingo NoSQL uses only own and OS functionality for creating and accessing the databases, so there is no need in installing any additional third-party software. For storing chemical structures and other extra information memory-mapped files technology was used. This technology shows better performance than using direct read and write operations, so I/O delays have no significant effect on the Bingo NoSQL speed. See the `Bingo NoSQL <../../../bingo/bingo-nosql.html>`__ page


.. _indigo-1.2.1-standardize:

===========
Standardize 
===========

``standardize`` method can be used to the “standardizing” of the molecule or query (stereo, 
charges, geometry, valences, atoms and bonds properties) in accordance with requirements. The list of applied modifications is defined by options activated in Indigo (full list of available standardize options is described in the corresponding `Options <../../../indigo/options/standardize.html>`__ section). See `examples <../../../indigo/examples/standardize.html>`__ page to find some usage examples.

.. _indigo-1.2.1-cdx:

==========
CDX Format 
==========

Chemdraw CDX format support was implemented. New method ``iterateCDXFile`` was added into Indigo 
API. See :ref:`details <indigo-api-io-reading-files>`

.. _indigo-1.2.1-stereo:

=====================
Stereo better support 
=====================

Improvements and fixes were applied for the stereo algorithm. 
Now Indigo restores stereo configurations according to the given information. Here is an example where stereo configuration is defined *incorrectly*. But for SMARTS pattern it is required to find all molecules with *any* stereo-center, thus no errors should be raised while SMARTS loading.  

.. indigorenderer::
   :indigoobjecttype: code
   :indigoloadertype: code
   :nocode: 
    
   # Load structure
   q = indigo.loadSmarts('[*@H](~*)~*')

   indigo.setOption("render-comment", "SMARTS = [*@H](~*)~*")

   #render query molecule
   indigoRenderer.renderToFile(q, 'result.png')

Release includes also other stereo and cis/trans improvements: loading/serialization, bidirection mode, haworth projection, etc. 
