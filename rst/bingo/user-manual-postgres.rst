User Manual: PostgreSQL
=======================

Basics
------

Data representation
~~~~~~~~~~~~~~~~~~~

Bingo supports Daylight SMILES with some ChemAxon extensions and MDL
(Symyx) Molfile/Rxnfile formats both in the text and binary
representation. Please look at the corresponding section of `Bingo User
Manual for Oracle <user-manual-oracle.html#data-representation>`__ for
details.

Storage
~~~~~~~

Suppose you have a table with a ``text``, ``varchar`` or ``bytea``
column containing a Molfiles/Rxnfiles or SMILES with molecules or
reactions.

Once you have prepared your table, you can execute ``CheckMolecule`` or
``CheckReaction`` to ensure that all the records are valid. These
functions return not null string with invalid records corresponding
error messages. All molecules or reactions that are in this table will
be excluded from the chemical index. You can update these molecules
later after indexing.

After you have prepared and checked your table, you can execute
``Create Index`` to make Bingo search procedures available for you
table. The more records the table contains, the longer it takes to
create an index.

Queries
~~~~~~~

You can specify the query molecule as a ``varchar`` string containing a
Molfile (including various query features), a SMILES, or a SMARTS
string. For reaction queries, use Rxnfiles, reaction SMILES, or reaction
SMARTS.

Molecules
---------

Creating an Index
~~~~~~~~~~~~~~~~~

The following command creates the index for text column:

::

    create index $index on $table using bingo_idx ($column bingo.molecule)

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$index`` is the name of the new index.

The following command creates the index for bytea (binary) column:

::

    create index $index on $table using bingo_idx ($bcolumn bingo.bmolecule)

-  ``$table`` is the name of the table containing molecules in the
   binary column ``$bcolumn``.
-  ``$index`` is the name of the new index.

Updating and Dropping Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add, remove, or edit records in the table after the index is
created. Adding records does not slow down the queries, i.e. the
performance will be the same as if you had indexed the whole table at
once. No re- indexing is required after adding the records.

After you delete, you must call ``autovacuum`` utility functions to
clean up the index.

Substructure Search
~~~~~~~~~~~~~~~~~~~

The general form of substructure search query is as follows:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.sub

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$query`` is a ``text`` string containing the query molfile or
   SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#substructure-search>`__ to learn the
rules of Bingo substructure matching (including Resonance search,
Conformation search, Affine transformation search), and various query
features available.

SMARTS Search
~~~~~~~~~~~~~

The syntax of SMARTS expression search is similar to the ordinary
substructure search:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.smarts

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$query`` is a ``text`` string containing the query molfile or
   SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#smarts-search>`__ to learn the rules of
SMARTS matching in Bingo.

Exact Search
~~~~~~~~~~~~

The general form of exact search query is as follows:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.exact

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$query`` is a ``text`` string containing the query molfile or
   SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#exact-search>`__ to learn the rules of
Bingo exact matching and various flags available for ``$parameters``
string.

Tautomer Search
~~~~~~~~~~~~~~~

Tautomer search is implemented within Substructure and Exact search
functions, and requires ``TAU`` flag to be specified in ``$parameters``
string. Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#tautomer-search>`__ to learn the rules
of Bingo exact and substructure tautomer matching.

Customizing the Rules
^^^^^^^^^^^^^^^^^^^^^

Your database (to which you have installed Bingo) contains a table
called ``bingo.bingo_tau_config``. By default it contains 3 records with
predefined rules. You can add, remove, or update the defined rules.
Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#tautomer-search>`__ to learn the format
of the tautomer matching rules.

Similarity Search
~~~~~~~~~~~~~~~~~

The general form of similarity search query is as follows:

::

    select * from $table where $column @ ($bottom, $top, '$query', '$metric')::bingo.sim

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$query`` is a ``text`` string containing the query molfile or
   SMILES.
-  ``$metric`` is a ``varchar`` string defining the metric to use:
   ``Tanimoto``, ``Tversky``, or ``Euclid-sub``.
-  ``$bottom`` and ``$top`` are real numbers that specify bottom and top
   limits of the required similarity, respectively.

By default, the bottom limit is zero and the top limit is 1, which is
the maximum possible value of similarity. You can specify ``null`` in
place of ``$bottom`` or ``$top`` to disable the lower or upper bound. In
most cases, you may want to cancel the upper bound:

::

    select * from $table where $column @ (0.8, null, '$query', 'Tanimoto')::bingo.sim

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#similarity-search>`__ to learn more
about the metrics.

Gross Formula Search
~~~~~~~~~~~~~~~~~~~~

The general form of gross formula search query is as follows:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.gross

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$query`` is a ``text`` string which looks like ”>= Cl6”, ”? C4 H4
   O”, or ”= C6 H6”.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of the `Bingo User Manual for
Oracle <user-manual-oracle.html#gross-formula-search>`__ to see some
examples.

Molecular Weight Search
~~~~~~~~~~~~~~~~~~~~~~~

The general form of molecular weight query is as follows:

::

    select bingo.getWeight('$molecule', '$mass_type')

To use the bingo index the search query is:

::

    select * from $table where $column > '$bottom'::bingo.mass AND $column < '$top'::bingo.mass

-  ``$table`` is the name of the table containing molecules in the
   column ``$column``.
-  ``$bottom`` and ``$top`` are numbers that specify the range to which
   the molecular weight of the resulting molecules must belong.

Format Conversion
~~~~~~~~~~~~~~~~~

You can convert a molecule to SMILES string using the function:

::

    select bingo.SMILES('$molecule');

You can convert a molecule to Molfile using the function:

::

    select bingo.Molfile('$molecule');

The automatic layout procedure is performed to calculate the 2D
coordinates of the resulting molecule.

You can convert a molecule to CML format using the function:

::

    select bingo.CML('$molecule');

-  $molecule is a ``text`` string or ``bytea`` containing the query
   molfile or SMILES.

Conversion to Binary Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``bingo.CompactMolecule()`` operator can be used for converting
Molfiles and SMILES to the internal binary format. The operator works
equally well with ``text`` and ``bytea`` operands. The operator always
returns the ``bytea`` result.

::

    select bingo.CompactMolecule($molfile, $xyz);

    select bingo.CompactMolecule($smiles, $xyz);

    select bingo.CompactMolecule($column, $xyz) FROM $table;

The ``$xyz`` parameter must be 0 or 1. If it is 1, the positions of
atoms are saved to the binary format. If it is zero, the positions are
skipped.

Canonical SMILES computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the function:

::

    select bingo.CanSMILES('$molecule')

to generate canonical SMILES strings for molecules represented as
Molfiles or SMILES strings. Please see the corresponding section of
`Bingo User Manual for
Oracle <user-manual-oracle.html#canonical-smiles>`__ to learn the
benefits of Bingo canonical SMILES format.

Molecule Fingerprints
~~~~~~~~~~~~~~~~~~~~~

You can generate a molecule fingerprint via ``bingo.Fingerprint``
function. The syntax is the same as for Bingo for Oracle, and it is
described `in this
section <user-manual-oracle.html#molecule-fingerprints>`__.

InChI and InChIKey
~~~~~~~~~~~~~~~~~~

You can use ``bingo.InChI`` and ``bingo.InChIKey`` function to get InChI
and InChIKey strings. The syntax is the same as for Bingo for Oracle,
and it is described `in this
section <user-manual-oracle.html#inchi-and-inchikey>`__.

Reactions
---------

Creating an Index
~~~~~~~~~~~~~~~~~

The following command creates the index for text columns:

::

    create index $index on $table using bingo_idx ($column bingo.reaction)

-  ``$table`` is the name of the table containing chemical reaction data
   in the column ``$column``.
-  ``$index`` is the name of the new index.

The following command creates the index for bytea (binary) columns:

::

    create index $index on $table using bingo_idx ($bcolumn bingo.breaction)

-  ``$table`` is the name of the table containing chemical reaction data
   in the binary column ``$bcolumn``.
-  ``$index`` is the name of the new index.

Reaction Substructure Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The general form of reaction substructure search query is as follows:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.rsub

-  ``$table`` is the name of the table containing chemical reaction data
   in the column ``$column``.
-  ``$query`` is a ``text`` string containing the query Rxnfile or
   reaction SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#substructure-search-1>`__ to learn the
rules of Bingo reaction substructure matching and various query features
available.

Reaction SMARTS Search
~~~~~~~~~~~~~~~~~~~~~~

The syntax of SMARTS expression search is similar to the ordinary
substructure search:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.rsmarts

-  ``$table`` is the name of the table containing chemical reaction data
   in the column ``$column``.
-  ``$query`` is a ``text`` string containing the query Rxnfile or
   reaction SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#smarts-search-1>`__ to learn the rules
of SMARTS matching in Bingo.

Reaction Exact Search
~~~~~~~~~~~~~~~~~~~~~

The general form of exact search query is as follows:

::

    select * from $table where $column @ ('$query', '$parameters')::bingo.rexact

-  ``$table`` is the name of the table containing chemical reaction data
   in the column ``$column``.
-  ``$query`` is a ``text`` string containing the query Rxnfile or
   reaction SMILES.
-  ``$parameters`` is a ``varchar`` string that can be empty or contain
   some options to pass to Bingo search engine.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#exact-search-1>`__ to learn the rules of
Bingo exact matching and various flags available for ``$parameters``
string.

Automatic Atom-to-Atom mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can compute reaction AAM by calling the function:

::

    select bingo.AAM('$reaction', '$strategy');

-  ``$reaction`` is a ``text`` string containing reaction SMILES or
   Rxnfile.
-  ``$strategy`` is a ``varchar`` string defining the strategy to use:
   ``CLEAR``, ``DISCARD``, ``ALTER`` or ``KEEP``.
-  The return value is an Rxnfile. In case the given reaction is
   represented as a reaction SMILES, the automatic reaction layout is
   performed.

The corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#automatic-atom-to-atom-mapping>`__
describes the allowable values of the ``$strategy`` parameter and shows
some examples.

Format Conversion
~~~~~~~~~~~~~~~~~

You can convert a reaction to reaction SMILES string using the function:

::

    select bingo.RSMILES('$reaction')

You can convert a reaction SMILES string to Rxnfile using the function:

::

    select bingo.Rxnfile('$reaction');

The automatic layout procedure is performed to calculate the 2D
coordinates of the resulting reaction.

You can convert a reaction to a reaction CML using the function:

::

    select bingo.RCML('$reaction');

-  ``$reaction`` is a ``text`` string containing reaction SMILES or
   Rxnfile.

Conversion to binary format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Bingo.CompactReaction()`` operator can be used for converting
Rxnfiles and reaction SMILES to internal binary format. The operator
works equally well with ``text`` and ``bytea`` operands. The operator
always returns the ``bytea`` result.

::

    SELECT Bingo.CompactReaction($rxnfile, $xyz) ;

    SELECT Bingo.CompactReaction($rsmiles, $xyz)L;

    SELECT Bingo.CompactReaction($column, $xyz) FROM $table;

The ``$xyz`` parameter must be 0 or 1. If it is 1, the positions of
atoms are saved to the binary format. If it is zero, the positions are
skipped.

Reaction Fingerprints
~~~~~~~~~~~~~~~~~~~~~

You can generate a reaction fingerprint via ``bingo.RFingeprint``
function. The syntax is the same as for Bingo for Oracle, and it is
described `in this
section <user-manual-oracle.html#reaction-fingerprints>`__.

Importing and Exporting Data
----------------------------

Importing SDFiles, RDFiles and SMILES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can import a molecule or reaction table from an SDF file. You can
also import SDF fields corresponding to each record in the SDF file.
Prior to importing, you have to create the table manually:

::

    create table $table ($id int, $column text, ...);
    select bingo.ImportSDF ('$table', '$column', '$sdf_id $id[, $other_columns]', '$filename.sdf[.gz]');

-  ``$table`` is the name of the table containing molfiles in
   ``$column``
-  ``$id`` is another column of the table, containing unique integer
   identifiers, which are read from ``$sdf_id`` field of the SDF file.
-  ``$other_columns`` is the comma-separated list of space-separated
   'property-column' pairs that are to be imported. Each given SDF
   property is mapped to the given table column. You can specify an
   empty string if there are no properties to import.
-  $filename is the location of the resulting file on the *server
   filesystem*.

A simple example of importing the
`NCI <http://dtp.nci.nih.gov/docs/3d_database/Structural_information/structural_data.html>`__
2D compound database would be the following:

::

    create table nci (nsc int, molfile text);
    select bingo.ImportSDF('nci', 'molfile', 'nsc nsc', 'C:/Users/Administrator/july2008_2d.sdf');

Importing RDF files is done with ``ImportRDF()`` function the same way
as SDF files:

::

    create table $table ($id int, $column text, ...);
    select bingo.ImportRDF ('$table', '$column', '$rdf_id $id[, $other_columns]', '$filename.rdf[.gz]');

Importing multi-line molecule or reaction SMILES file is done the
similar way with the ``ImportSMILES()`` function:

::

    select bingo.ImportSMILES('$table', '$column', '$id', '$filename');

-  ``$table``, ``$column``, and ``$filename`` have the usual meaning
-  ``$id`` is the column where molecule and reaction identifiers go. The
   identifier within SMILES string is anything that goes after the
   molecule or reaction, separated by space. It is allowed to pass an
   empty string or NULL as the ``$id`` parameter, if there are no
   identifiers in the SMILES file subject to import.

**Note:** When you import the file contents to a table, the old table
contents are not removed. Thus, you can import multiple files into the
same table.

Exporting SDFiles and RDFiles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can export a molecule table to a SDF file. You can also export table
fields corresponding to each record in the SDF file:

::

    create table $table ($id int, $column text, ...);
    ...
    select bingo.ExportSDF ('$table', '$column', '$id[, $other_columns]', '$filename.sdf');

-  ``$table`` is the name of the table containing molfiles in
   ``$column``
-  ``$id`` is another column of the table, containing unique integer
   identifiers, which are written to ``$id`` field of the SDF file.
-  ``$other_columns`` is the comma-separated list of space-separated
   'property-column' pairs that are to be imported. Each given SDF
   property is mapped to the given table column. You can specify an
   empty string if there are no properties to export.
-  $filename is the location of the resulting file on the *server
   filesystem*.

A simple example of exporting the
`NCI <http://dtp.nci.nih.gov/docs/3d_database/Structural_information/structural_data.html>`__
2D compound database would be the following:

::

    create table nci (nsc int, molfile text);
    ...
    select bingo.ExportSDF('nci', 'molfile', 'nsc', 'C:/Users/Administrator/july2008_2d.sdf');

Exporting RDF files is done with ``ExportRDF()`` function the same way
as SDF files:

::

    create table $table ($id int, $column text, ...);
    ...
    select bingo.ExportRDF ('$table', '$column', '$id[, $other_columns]', '$filename.rdf');

Utility functions
-----------------

Extracting Names
~~~~~~~~~~~~~~~~

``bingo.getName`` function extracts the molecule or reaction name from
Molfile, Rxnfile, or SMILES string.

::

    select bingo.getName(molfile) from mytable;

    select bingo.getName('c1ccc2ccccc2c1 Naphthalene');

Calculating Molecule Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``bingo.getMass`` function returns the molecular weight of the given
molecule, represented as a Molfile or SMILES string. It has an
additional parameter which defines the 'kind' of the resulting molecular
mass value.

-  ``Bingo.getMass($molecule, '`` is a short for
   ``Bingo.getWeight($molecule, 'molecular-weight')``.
-  ``Bingo.getWeight($molecule, 'molecular-weight')`` returns the
   molecular weight.
-  ``Bingo.getWeight($molecule, 'most-abundant-mass')`` returns the
   `most abundant
   mass <http://en.wikipedia.org/wiki/Mass%20%28mass%20spectrometry%29#Most%20abundant%20mass#Most%20abundant%20mass>`__,
   which is calculated using most likely isotopic composition for a
   single random molecule.
-  ``Bingo.getWeight($molecule, 'monoisotopic-mass')`` returns the
   `monoisotopic
   mass <http://en.wikipedia.org/wiki/Monoisotopic_mass>`__, which is
   calculated using the most abundant isotope of each element.

Here are some examples of using the ``Bingo.getMass()`` operator:

::

    select bingo.getMass('C1C=CC=CC=1', '');

    select bingo.getWeight(molfile, 'most-abundant-mass') from mytable;

Similarly, ``bingo.Gross()`` function returns the gross formula of the
given molecule

::

    select bingo.Gross('C1C=CC=CC=1');

    select bingo.Gross(molfile) from mytable;

Checking for Correctness
~~~~~~~~~~~~~~~~~~~~~~~~

You can use the ``bingo.CheckMolecule()`` function to check that
molecules are presented in acceptable form. If the molecule has some
problems (unsupported format, exceeded valence, incorrect
stereochemistry), the functions returns a string with the description of
the problem. Is the molecule is represented with a correct Molfile or
SMILES string, the function returns ``null``.

::

    select bingo.CheckMolecule($molecule);

    select $table.*, bingo.CheckMolecule($column) from $table where bingo.CheckMolecule($column) is not null;

Similarly, you can check reactions for correctness with the
``bingo.CheckReaction()`` function:

::

    select bingo.CheckReaction($reaction);

    select $table.*, bingo.CheckReaction($column) from $table where bingo.CheckReaction($column) is not null;

Reading Files on Server
~~~~~~~~~~~~~~~~~~~~~~~

The ``Bingo.FileToText()`` function accepts a text file path and loads a
file from the server file system to PostgreSQL text.

::

    select bingo.FileToText($path);

Usually you may want to load the query molecule in the following way:

::

    select * form $table where $column @ (bingo.FileToText($path), '')::bingo.sub;

The ``Bingo.FileToBlob()`` function accepts a text file path and loads a
file from the server file system to PostgreSQL bytea.

::

    select bingo.FileToBlob($path);

Permissions management
----------------------

Let the schema name **bingo** was specified during installation of the
Bingo cartridge. Let the user **test\_user** is going to create the
bingo index on a table. There are two objects user will work with to
create the bingo index.

-  Schema **bingo**. All procedures and functions are signed by a
   certificate that is mapped to this schema.
-  Two configuration tables **bingo.bingo\_config** and
   **bingo.bingo\_tau\_config** with all the index parameters

So for precise permissions management you need:

-  For Bingo index creation your need to grant user **test\_user** usage
   permissions on the schema **bingo**
-  Add permission to read table **bingo.bingo\_config** and
   **bingo.bingo\_tau\_config**

Set permissions for building the index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    grant usage on schema bingo to test_user;
    grant select on table bingo.bingo_config to test_user;
    grant select on table bingo.bingo_tau_config to test_user;

Maintenance
-----------

Obtaining Bingo Version Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    select bingo.GetVersion();

Viewing the Log File
~~~~~~~~~~~~~~~~~~~~

All operation of Bingo is logged into the PostgreSQL native LOG. All
error and warning messages (not necessarily visible in SQL session) are
logged. Some performance measures of the SQL queries are written to the
log as well.
