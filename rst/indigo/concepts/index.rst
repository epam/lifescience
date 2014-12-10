Concepts
========

.. toctree::
    :hidden:

    deco
    combichem
    transformation

File Formats
------------

Indigo supports the following molecule and reaction formats:

-  Daylight SMILES with ChemAxon extensions
-  Daylight SMARTS (including reactions)
-  CML (including reactions)
-  MDL (Symyx) Molfile and Rxnfile, both v2000 and v3000
-  MDL (Symyx) SDFile and RDFile
-  All the above in GZip-compressed form

Daylight Formats with ChemAxon and CurlySMILES Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Almost all features of the original Daylight
`SMILES <http://www.daylight.com/dayhtml/doc/theory/theory.smiles.html>`__
format are supported, including:

-  Aromatic rings
-  Hydrogen counters
-  Tetrahedral and allene-like stereocenters
-  Cis-trans double bonds
-  Disconnected structures
-  Reaction atom-to-atom mapping (AAM)

The only features that are not supported are:

-  "Up or unspecified", "down or unspecified" notation ("/?", "\\?")
-  Square-planar, trigonal-bipyramidal, and octahedral stereo
   configurations.

Almost all features of the original Daylight
`SMARTS <http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html>`__
format are supported, including:

-  Aromatic and aliphatic atoms
-  SSSR (smallest set of smallest rings) calculation
-  Logical operators
-  Atom environments (nested SMARTS)
-  Component-level grouping

The only features that are not supported are:

-  Constraint "h" (implicit hydrogen count). Hydrogens can be stored
   implicitly or explicitly in the database, and this difference should
   not affect the search results. "H" (total hydrogen count) may be used
   instead
-  All features of SMILES format that are not supported

The following ChemAxon SMILES
`extensions <http://www.chemaxon.com/marvin/help/formats/cxsmiles-doc.html>`__
are supported:

-  Radical numbers: monovalent, divalent singlet, and divalent triplet
-  `Stereogroups <http://www.chemaxon.com/jchem/doc/user/query_stereochemistry.html>`__
-  Pseudo-atoms (atom aliases)
-  Fragment level grouping in reactions

The following extensions from the
`CurlySMILES <http://www.jcheminf.com/content/3/1/1>`__ format are
supported:

-  Simple polymers: {-}...{+n}
-  Multiple groups: {-}...{+nn=5}

MDL Formats
~~~~~~~~~~~

MDL (Symyx) Molfiles and Rxnfiles are supported by Indigo. Both format
versions (2000 and 3000) are supported. Almost all format features are
supported, including:

-  Pseudo-atoms (atom aliases)
-  Stereogroups
-  R-Groups (Markush queries)
-  Query atoms and query bonds
-  Various query flags on atoms and bonds
-  Atom positions
-  3D constraints in v2000 Molfiles
-  Reaction atom-to-atom mapping (AAM)
-  Reacting centers and stereo inv/ret flags
-  Data SGroups, polymers, superatoms (abbreviations)

The only features that are not supported are:

-  3D constraints in v3000 Molfiles

Molecules and Query Molecules
-----------------------------

Indigo treats "real" molecules different from query molecules in certain
ways.

-  Only a query molecule can contain query features like "any" atoms,
   atom lists, etc.
-  Only a query molecule can contain R-Groups (although R-Sites can be
   present in "real" molecule too)
-  Only a query molecule can be matched as a substructure
-  Only a "real" molecule can be matched against by the substructure
   matcher.
-  Only "real" molecules can be subject to MCS/common scaffold
   computation.
-  Canonical SMILES can be calculated only on "real" molecules.

Similar rules apply to "real" reactions and query reactions:

-  Only a query reaction can be matched as a substructure in the
   reaction substructure matcher.
-  Only a "real" reaction can be matched against by the reaction
   substructure matcher.

There is never an ambiguity whether a particular object is a
molecule/reaction or query molecule/reaction. While most input formats
(Molfile/Rxnfile, SMILES) can store both types, different calls are
provided for loading them as "real" or query objects. SMARTS strings
always are loaded as query molecules, for obvious reasons.

Substructure and SMARTS Matching
--------------------------------

Indigo provides full capabilities for substructure matching of query
molecules, including ones loaded from SMARTS expressions. In the `Bingo
User
Manual <../../bingo/user-manual-oracle.html#substructure-search>`__, you
can find examples of substructure matches.

Differences between SMARTS and query SMILES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While a lot of SMARTS notation is allowed when loading SMILES as a
query, there are differences between SMARTS and query SMILES:

-  SMARTS fragments $(...) are not allowed in query SMILES.

-  Empty bond designator (like 'CC' or 'cc') denotes 'single or
   aromatic' bond in SMARTS. In query SMILES, it denotes aromatic bond,
   if it belongs to a ring and has both end atoms aromatic (lowercase);
   otherwise, it denotes a single bond.

-  'C' within SMARTS means aliphatic carbon, while 'C' within query
   SMILES means any carbon. The same applies to 'B', 'N', 'O', 'S', 'P'.
   'C1~C~C~C~C~C~1' won't match 'c1ccccc1' as SMARTS, but it will do so
   as query SMILES.

-  SMARTS queries are not fed to aromaticity matcher. 'c1-c=c-c=c-c=1'
   won't match 'c1ccccc1' as SMARTS, but it will do so as query SMILES.

Exact Matching
--------------

Indigo can perform exact matching of pairs of molecules, or pairs of
reactions.

Molecule Similarity
-------------------

Indigo provides various molecule similarity measures, all based on
originally developed fingerprints. In the `Bingo User
Manual <../../bingo/user-manual-oracle.html#similarity-search>`__, you
can find detailed description and examples.

Canonical SMILES
----------------

Canonical SMILES generated by Indigo are, according to Daylight and
ChemAxon terminology, unique SMILES with isomeric information, or
*absolute* SMILES. All significant molecular features, such as isotopes,
charges, radicals, stereocenters, stereogroups, cis-trans bonds, and
aromaticity, are encoded into SMILES in a canonical form. A canonical
SMILES string defines the molecule independently of any particular
representation (atom renumbering, stereogroup renumbering,
explicit/implicit hydrogens). So, the equality of the canonical SMILES
of two molecules guarantees that these molecules are the same, and vice
versa.

'Useless' stereocenters
~~~~~~~~~~~~~~~~~~~~~~~

Stereocenter is not considered useful when it does not provide any
information for distinguishing stereoisomers. Such useless stereocenters
are ignored in canonical SMILES generated by Indigo.

From the pictures below, you can see that all the three molecules
specify the same mixture. This is represented in the fact that Indigo
gives identical canonical SMILES for them.

+------------+-------------------------------------------------+
| |image3|   | **Canonical SMILES:**                           |
|            |  C[C@@H]1CC(C(=O)N1)1N2CC(C)3CN1CC(C)(C2)C3=O   |
+------------+-------------------------------------------------+
| |image4|   | **Canonical SMILES:**                           |
|            |  C[C@@H]1CC(C(=O)N1)1N2CC(C)3CN1CC(C)(C2)C3=O   |
+------------+-------------------------------------------------+
| |image5|   | **Canonical SMILES:**                           |
|            |  C[C@@H]1CC(C(=O)N1)1N2CC(C)3CN1CC(C)(C2)C3=O   |
+------------+-------------------------------------------------+

**Note:** Query features are not supported for canonicalization.

Scaffold Detection
------------------

Indigo incorporates two algorithms (exact and approximate) of maximum
common substructure (MCS) computation. Each of the algorithms can
operate on an arbitrary amount of input structures. Thus, it is possible
to pass the found scaffold to the `R-Group
decovolution <#r-group-deconvolution>`__ procedure.

Moreover, if the scaffold detection procedure has found more than one
MCS, it is possible to obtain all of them.

R-Group Deconvolution
---------------------

With a collection of structures and a scaffold that is common for these
structures, it is possible to perform the R-Group deconvolution (R-Group
decomposition). The result of this procedure will be a scaffold with
marked R-sites (R1, R2, ...), and the actual substituents for these
R-sites for each of the input structures.

Examples are available on a `separate page <deco.html>`__.

Layout
------

Indigo is capable of performing layout (cleanup) of molecules and
reactions. After the layout procedure, the average length of the bonds
in a molecule will always be around 1.0. The procedure is not sensitive
to the present molecular coordinates.

Rendering
---------

Indigo provides high-quality 2D rendering capabilities for molecule and
reactions. All the chemical features (including query features) are
rendered properly following the IUPAC recommendations
(`1 <http://www.iupac.org/publications/pac/78/10/1897/>`__,
`2 <http://www.iupac.org/publications/pac/80/2/0277/>`__) for graphical
representation. The features that are not covered by IUPAC (mostly,
query features) are drawn in such a way that they do not overlay the
primary structure.

With Indigo, it is possible to display highlighted bonds and atoms with
specified color and/or with thick lines and bold characters.

The full list of options is available on the
`options <../api/options.html#rendering>`__ page.

The following output formats are supported for rendering:

-  Adobe PDF
-  Portable Network Graphics (PNG)
-  Scalable Vector Graphics (SVG)

On Windows platforms, Indigo is also able to:

-  Render directly to a given device context (HDC)
-  Produce .NET Bitmap objects
-  Produce Enhanced Metafile Format (EMF) files and .NET Metafile
   objects

Produced PNGs and Bitmaps are transparent unless the background is set
explicitly. Produced SVGs, PDFs, and Metafiles contain no raster
fragments.

In the `Bingo User Manual <../../bingo/user-manual-oracle.html>`__, you
can find examples of rendered molecules and reactions. All the pictures
in this manual were rendered to SVG by Indigo.

Combinatorial Chemistry
-----------------------

Indigo provides a reaction products enumerator, which has the following
features:

-  Query features (any bonds, any atoms)
-  Accurate tetrahedral and cis-trans stereochemistry transformation
   based on atom-to-atom mapping
-  Intramolecular reactions
-  Exhaustive product enumeration from available monomers (products are
   used as monomers)
-  Two generation modes: grid (monomers are assigned to wells and to
   reactants) and “one tube” (all monomers are mixed together)
-  Support of functional groups with two attachment points
-  Results are generated without duplicates even if source monomers are
   symmetrical

The full list of options is available on the
`options <../api/options.html#reaction-products-enumeration>`__ page.

The examples are available on a `separate page <combichem.html>`__.

.. |image0| image:: ../../assets/indigo/concepts/cano_mol1.svg
.. |image1| image:: ../../assets/indigo/concepts/cano_mol2.svg
.. |image2| image:: ../../assets/indigo/concepts/cano_mol3.svg
.. |image3| image:: ../../assets/indigo/concepts/cano_mol1.svg
.. |image4| image:: ../../assets/indigo/concepts/cano_mol2.svg
.. |image5| image:: ../../assets/indigo/concepts/cano_mol3.svg
