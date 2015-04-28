User Manual: SQL Server
=======================

Basics
------

Data representation
~~~~~~~~~~~~~~~~~~~

Bingo supports Daylight SMILES with some ChemAxon extensions and MDL
(Symyx) Molfile/Rxnfile formats both in the text and binary
representation. All methods like ``Mass``, ``Gross``, ``Molfile``,
``SMILES`` and etc. have same functions for binary data with ``B``
suffix: ``MassB``, ``GrossB`` and etc. Please look at the corresponding
section of `Bingo User Manual for
Oracle <user-manual-oracle.html#data-representation>`__ for details.

Storage
~~~~~~~

Suppose you have a table with a ``nvarchar``, ``varchar`` or 'varbinary'
column containing a Molfiles/Rxnfiles or SMILES with molecules or
reactions. In order to make Bingo work with your table, you would need a
column in your table containing a unique integer number for each
molecule or reaction. Normally, although not necessary, this is a
primary key. If you have a ``[n]varchar`` field as the primary key, you
still have to add a unique integer field.

Once you have prepared your table, you can execute
``CheckMoleculeTable`` or ``CheckReactionTable`` to ensure that all the
records are valid. These functions return table with invalid records and
corresponding error message. All molecules or reactions that are in this
table will be excluded from the chemical index. You can update these
molecules later after indexing.

After you have prepared and checked your table, you can execute
``CreateMoleculeIndex`` or ``CreateReactionIndex`` to make Bingo search
procedures available for you table. The more records the table contains,
the longer it takes to create an index.

Queries
~~~~~~~

You can specify the query molecule as a ``nvarchar`` string containing a
Molfile (including various query features), a SMILES, or a SMARTS
string. For reaction queries, use Rxnfiles, reaction SMILES, or reaction
SMARTS.

**Note:** In order to make substructure search faster, Bingo loads the
indexed molecules into memory. The loading itself takes some time, and
as a result, the first substructure query runs slower than all the
subsequent ones. The loaded molecules are shared across other SQL
sessions, and so other sessions there will not encounter such time lags.
The memory is freed as soon as all the sessions working with this table
are disconnected. You can force Bingo not to unload index cache by
calling ``SetKeepCache`` function.

Molecules
---------

Creating an Index
~~~~~~~~~~~~~~~~~

The same syntax is for command to creates the index:

::

    exec bingo.CreateMoleculeIndex '$table', '$id', '$molecule';

``$table`` is the name of the table containing molecule data in column
``$molecule`` and the unique integer identifier in column ``$id``.

Updating and Dropping Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add, remove, or edit records in the table after the index is
created. Adding records does not slow down the queries, i.e. the
performance will be the same as if you had indexed the whole table at
once. No re- indexing is required after adding the records.

After you insert, update or delete, you must either:

-  close the SQL session, or
-  execute ``Bingo.FlushOperations()`` procedure.

If the index was modified, any search procedure will be raising an
exception until ``FlushOperations`` is called.

It is much faster to insert, delete or update records in a single SQL
statement rather by doing it one by one. If you have the indexed table,
and you have another portion on molecules that you to add, then you
should do it in a single SQL statement:

::

    insert into <table> (<columns>) select <columns> from <table_with_new_molecules>

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#updating-and-dropping-index>`__ for more
details and recommendations. Please, note that for SQL Server flush
procedure is called ``FlushOperations`` because it must be called after
delete operations too.

Substructure Search
~~~~~~~~~~~~~~~~~~~

The general form of substructure search query is as follows:

::

    select $table.* from $table, bingo.SearchSub('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

``$table`` is the name of the table containing the unique integer
identifier in column ``$id``. ``$query`` is a ``nvarchar`` string
containing the query molfile or SMILES. ``$parameters`` is a
``nvarchar`` string that can be empty or contain some options to pass to
Bingo search engine.

``$n`` is the number defining how many hits you want, at most.

**Note:** It is possible to use the ordinary ``SELECT TOP`` SQL
statement, but using the ``TOP`` parameter in Bingo parameters string
will be better for performance, as in this case the database engine will
not retrieve all the resulting records into memory before returning the
top ``$n`` ones.

You can get all the hits by portions of an arbitrary size. First query
should have ``START`` option:

::

    select $table.* from $table, bingo.SearchSub('$table', $query, '$parameters; TOP $n; START') t
       where $table.$id = t.id;

After that you can get next portion of results by specifying last id,
returned by ``SearchSub`` function:

::

    select $table.* from $table, bingo.SearchSub('$table', $query, '$parameters; TOP $n; NEXT $last_id') t
       where $table.$id = t.id;

**Note:** These ``TOP``, ``START``, and ``NEXT`` options are common for
all Bingo search functions.

In case you need all the hits, you can omit the ``TOP $n`` part of the
parameters string:

::

    select $table.* from $table, bingo.SearchSub('$table', $query, '$parameters') t
       where $table.$id = t.id;

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#substructure-search>`__ to learn the
rules of Bingo substructure matching (including Resonance search,
Conformation search, Affine transformation search), and various query
features available.

Highlighting the resulting molecules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get search results with highlighting by using the
``bingo.SearchSubHi`` function:

::

    select $table.<columns>, t.highlighting from $table, bingo.SearchSubHi('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

``$column`` is the column in your ``$table`` which contain the
molecules.

Or you can use the ``bingo.SubHi`` function on each resulting molecule
to get an Molfile containing the highlighted substructure:

::

    select $table.*, bingo.SubHi($column, $query, '$parameters')
       from $table, bingo.SearchSub('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

SMARTS Search
~~~~~~~~~~~~~

The syntax of SMARTS expression search is similar to the ordinary
substructure search:

::

    select $table.* from $table, bingo.SearchSMARTS('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

The highlighting of SMARTS matches is also done in a similar way to the
ordinary substructure search:

::

    select $table.<columns>, t.highlighting from $table, bingo.SearchSMARTSHi('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

Or

::

    select $table.*, bingo.SMARTSHi($column, $query)
       from $table, bingo.SearchSMARTS('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#smarts-search>`__ to learn the rules of
SMARTS matching in Bingo.

Exact Search
~~~~~~~~~~~~

The general form of exact search query is as follows:

::

    select $table.* from $table, bingo.SearchExact('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

The meaning of ``$table``, ``$id``, ``$query``, ``$parameters``, and
``$n`` is the same as in ``SearchSub`` function.

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
called ``bingo.TAUTOMER_RULES``. By default it contains 3 records with
predefined rules. You can add, remove, or update the defined rules.
Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#tautomer-search>`__ to learn the format
of the tautomer matching rules.

Similarity Search
~~~~~~~~~~~~~~~~~

The general form of similarity search query is as follows:

::

    select $table.* from $table, bingo.SearchSim('$table', $query, '$metric; TOP $n', $bottom, $top) t
       where $table.$id = t.id;

The meaning of ``$table``, ``$id``, ``$query``, and ``$n`` is the same
as in ``SearchSub`` and ``SearchExact`` functions. ``$metric`` is a
``nvarchar`` string defining the metric to use: ``Tanimoto``,
``Tversky``, or ``Euclid-sub``. Please see the corresponding section of
`Bingo User Manual for
Oracle <user-manual-oracle.html#similarity-search>`__ to learn more
about the metrics.

``$bottom`` and ``$top`` are real numbers that specify bottom and top
limits of the required similarity, respectively. By default, the bottom
limit is zero and the top limit is 1, which is the maximum possible
value of similarity. You can specify ``null`` in place of ``$bottom`` or
``$top`` to disable the lower or upper bound. In most cases, you may
want to cancel the upper bound:

::

    select $table.* from $table, bingo.SearchSim('$table', $query, 'Tanimoto; TOP 100', 0.8, null) t
       where $table.$id = t.id;

Gross Formula Search
~~~~~~~~~~~~~~~~~~~~

The general form of gross formula search query is as follows:

::

    select $table.* from $table, bingo.SearchGross('$table', $query, '$TOP $n') t
       where $table.$id = t.id;

The meaning of ``$table``, ``$id``, and ``$n`` is the same as in all
similar functions mentioned above. ``$query`` is a ``nvarchar`` string
which looks like ”>= Cl6”, ”? C4 H4 O”, or ”= C6 H6”. Please see the
corresponding section of the `Bingo User Manual for
Oracle <user-manual-oracle.html#gross-formula-search>`__ to see some
examples.

Molecular Weight Search
~~~~~~~~~~~~~~~~~~~~~~~

The general form of molecular weight search query is as follows:

::

    select $table.* from $table, bingo.SearchMolecularWeight('$table', $bottom, $top, 'TOP $n') t
       where $table.$id = t.id;

``$table``, ``$id``, and ``$n`` have the usual meaning. ``$bottom`` and
``$top`` are numbers that specify the range to which the molecular
weight of the resulting molecules must belong. You can cancel the lower
or upper limit by specifying ``null`` in place of ``$bottom`` or
``$top``.

Format Conversion
~~~~~~~~~~~~~~~~~

You can convert a molecule to SMILES string with ``bingo.SMILES``
function:

::

    select bingo.SMILES(molfile) from mytable;

    select t.id, bingo.SMILES(molfile)
       from mytable, bingo.SearchSub(mytable, 'NNC1C=CC=CC=1', '') t
       where mytable.id = t.id;

You can get a SMILES string of a highlighted molfiles:

::

    select t.id, bingo.SMILES(bingo.SubHi(molfile, 'NNC1C=CC=CC=1', ''))
       from mytable, bingo.SearchSub(mytable, 'NNC1C=CC=CC=1', 'TOP 100') t
       where mytable.id = t.id;

You can convert a molecule to Molfile using the ``bingo.Molfile``
function:

::

    select bingo.Molfile('C1=CC2=C(C=C1)C=CC=C2');

The automatic layout procedure is performed to calculate the 2D
coordinates of the resulting molecule.

You can convert a molecule to CML format using the ``bingo.CML``
function:

::

    select bingo.CML('C1=CC2=C(C=C1)C=CC=C2');

Canonical SMILES computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the ``bingo.CanSMILES()`` function to generate canonical
SMILES strings for molecules represented as Molfiles or SMILES strings.
Please see the corresponding section of `Bingo User Manual for
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

The following command creates the index:

::

    exec bingo.CreateReactionIndex '$table', '$id', '$reaction';

``$table`` is the name of the table containing chemical reaction data in
column ``$reaction`` and the unique integer identifier in column
``$id``.

Reaction Substructure Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The general form of reaction substructure search query is as follows:

::

    select $table.* from $table, bingo.SearchRSub('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

``$table`` is the name of the table containing the unique integer
identifier in column ``$id``. ``$query`` is a ``nvarchar`` string
containing the query Rxnfile or reaction SMILES.

``$n`` is the number defining how many hits you want, at most.

**Note:** It is possible to use the ordinary ``SELECT TOP`` SQL
statement, but using the ``TOP`` parameter in Bingo parameters string
will be better for performance, as in this case the database engine will
not retrieve all the resulting records into memory before returning the
top ``$n`` ones.

You can get all the hits by portions of an arbitrary size. First query
should have ``START`` option:

::

    select $table.* from $table, bingo.SearchRSub('$table', $query, '$parameters; TOP $n; START') t
       where $table.$id = t.id;

After that you can get next portion of results by specifying last id,
returned by ``SearchSub`` function:

::

    select $table.* from $table, bingo.SearchRSub('$table', $query, '$parameters; TOP $n; NEXT $last_id') t
       where $table.$id = t.id;

**Note:** These ``TOP``, ``START``, and ``NEXT`` options are common for
all Bingo search functions.

In case you need all the hits, you can omit the ``TOP $n``, leaving the
empty string:

::

    select $table.* from $table, bingo.SearchRSub('$table', $query, '') t
       where $table.$id = t.id;

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#substructure-search-1>`__ to learn the
rules of Bingo reaction substructure matching and various query features
available.

SMARTS Search
~~~~~~~~~~~~~

The syntax of SMARTS expression search is similar to the ordinary
substructure search:

::

    select $table.* from $table, bingo.SearchRSMARTS('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

The highlighting of SMARTS matches is also done in a similar way to the
ordinary reaction substructure search:

::

    select $table.<columns>, t.highlighting from $table, bingo.SearchRSMARTSHi('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

Or

::

    select $table.*, bingo.RSMARTSHi($column, $query)
       from $table, bingo.SearchSMARTS('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#smarts-search-1>`__ to learn the rules
of SMARTS matching in Bingo.

Exact Search
~~~~~~~~~~~~

The general form of exact search query is as follows:

::

    select $table.* from $table, bingo.SearchRExact('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

The meaning of ``$table``, ``$id``, ``$query``, ``$parameters``, and
``$n`` is the same as in ``SearchSub`` function.

Please see the corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#exact-search-1>`__ to learn the rules of
Bingo exact matching and various flags available for ``$parameters``
string.

Highlighting the resulting reactions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get the highlighted results by using ``BingoSearchRSub``
function:

::

    select $table.<columns>, t.highlighting from $table, bingo.SearchRSubHi('$table', $query, '$parameters; TOP $n') t
       where $table.$id = t.id;

Or you can use the ``bingo.RSubHi`` function on each resulting reaction
to get an Rxnfile containing the highlighted substructure:

::

    select $table.*, bingo.RSubHi($column, $query)
       from $table, bingo.SearchRSub('$table', $query, 'TOP $n') t
       where $table.$id = t.id;

``$column`` is the column in your ``$table`` which contain the
reactions.

Automatic Atom-to-Atom mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can compute reaction AAM by calling ``bingo.AAM`` function:

::

    select bingo.AAM($reaction, $strategy);

As ``$reaction`` you can specify a ``nvarchar`` string containing
reaction SMILES or Rxnfile. The return value is an Rxnfile. In case the
given reaction is represented as a reaction SMILES, the automatic
reaction layout is performed.

The corresponding section of `Bingo User Manual for
Oracle <user-manual-oracle.html#automatic-atom-to-atom-mapping>`__
describes the allowable values of the ``$strategy`` parameter and shows
some examples.

Format Conversion
~~~~~~~~~~~~~~~~~

You can convert a reaction to reaction SMILES string with
``bingo.RSMILES`` function:

::

    select bingo.RSMILES(rxnfile) from mytable;

    select t.id, bingo.RSMILES(rxnfile)
       from mytable, bingo.SearchRSub(mytable, '>>NNC1C=CC=CC=1', '') t
       where mytable.id = t.id;

You can get a SMILES string of a highlighted molfiles:

::

    select t.id, bingo.RSMILES(bingo.RSubHi(molfile, '>>NNC1C=CC=CC=1'))
       from mytable, bingo.SearchRSub(mytable, '>>NNC1C=CC=CC=1', 'TOP 100') t
       where mytable.id = t.id;

You can convert a reaction SMILES string to Rxnfile using the
``bingo.Rxnfile`` function:

::

    select bingo.Rxnfile('COC(=O)CC1=CC(=C)NC2=C1C(=O)CCC2>>ONC(=O)CC1=CC(=O)NC2=C1C(CCC2)=NO');

The automatic layout procedure is performed to calculate the 2D
coordinates of the resulting reaction.

You can convert a reaction to a reaction CML using the ``bingo.RCML``
function:

::

    select bingo.RCML('COC(=O)CC1=CC(=C)NC2=C1C(=O)CCC2>>ONC(=O)CC1=CC(=O)NC2=C1C(CCC2)=NO');

Reaction Fingerprints
~~~~~~~~~~~~~~~~~~~~~

You can generate a reaction fingerprint via ``bingo.RFingeprint``
function. The syntax is the same as for Bingo for Oracle, and it is
described `in this
section <user-manual-oracle.html#reaction-fingerprints>`__.

Importing and Exporting Data
----------------------------

Importing SDFiles, RDFiles, and SMILES files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can import a molecule or reaction table from an SDF file. You can
also import SDF fields corresponding to each record in the SDF file.
Prior to importing, you have to create the table manually:

::

    create table $table ($id int, $column nvarchar(max), ...);
    exec bingo.ImportSDF '$table', '$column', '$filename.sdf[.gz]', '$sdf_id $id[, $other_columns]';

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

    create table nci (nsc int, molfile nvarchar(max));
    exec bingo.ImportSDF 'nci', 'molfile', 'C:\Users\Administrator\july2008_2d.sdf', 'nsc nsc';

GZip-compressed data is detected automatically in ImportSDF, and so you
can call it the same way:

::

    exec bingo.ImportSDF 'nci', 'molfile', 'C:\Users\Administrator\july2008_2d.sdf.gz', 'nsc nsc';

Importing RDF files is done with ``ImportRDF()`` function the same way
as SDF files:

::

    create table $table ($id int, $column nvarchar(max), ...);
    exec bingo.ImportRDF '$table', '$column', '$filename.rdf[.gz]', '$sdf_id $id[, $other_columns]';

Importing multi-line molecule or reaction SMILES file is done the
similar way with the ``ImportSMILES()`` function:

::

    create table $table ($id int, $column nvarchar(max), ...);
    exec bingo.ImportSMILES '$table', '$column', '$filename.sdf[.gz]', '$id';

The identifier within SMILES string, which goes for the ``$id`` column,
is anything that goes after the molecule or reaction, separated by
space.

**Note:** When you import the file contents to a table, the old table
contents are not removed. Thus, you can import multiple files into the
same table.

Exporting SDFiles
~~~~~~~~~~~~~~~~~

Exporting SDF files is conducted in a similar way to importing. You can
export the molecule or reaction table to an SDF file.

::

    EXEC Bingo.ExportSDF '$table', '$column', '$filename', '$other_columns'

Example of exporting the PubChem database to the ``/tmp/pubchem.sdf``
file:

::

    EXEC Bingo.ExportSDF 'PUBCHEM.COMPOUNDS', 'structure', 'c:/tmp/pubchem.sdf', 'cid, name, mw'

Utility functions
-----------------

Extracting the Names of Molecules and Reactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``bingo.Name`` function extracts the molecule or reaction name from
Molfile, Rxnfile, or SMILES string.

::

    SELECT bingo.Name(molfile) from mytable;

    SELECT bingo.Name('c1ccc2ccccc2c1 Naphthalene');

Calculating Molecule Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``bingo.Mass`` function returns the molecular weight of the given
molecule, represented as a Molfile or SMILES string. It has an
additional parameter which defines the 'kind' of the resulting molecular
mass value.

-  ``Bingo.Mass($molecule, '`` is a short for
   ``Bingo.Mass($molecule, 'molecular-weight')``.
-  ``Bingo.Mass($molecule, 'molecular-weight')`` returns the molecular
   weight.
-  ``Bingo.Mass($molecule, 'most-abundant-mass')`` returns the `most
   abundant
   mass <http://en.wikipedia.org/wiki/Mass%20%28mass%20spectrometry%29#Most%20abundant%20mass#Most%20abundant%20mass>`__,
   which is calculated using most likely isotopic composition for a
   single random molecule.
-  ``Bingo.Mass($molecule, 'monoisotopic-mass')`` returns the
   `monoisotopic
   mass <http://en.wikipedia.org/wiki/Monoisotopic_mass>`__, which is
   calculated using the most abundant isotope of each element.

Here are some examples of using the ``Bingo.Mass()`` operator:

::

    select bingo.Mass('C1C=CC=CC=1', '');

    select bingo.MolecularWeight(molfile, 'most-abundant-mass') from mytable;

Similarly, ``bingo.Gross()`` function returns the gross formula of the
given molecule

::

    select bingo.Gross('C1C=CC=CC=1');

    select bingo.Gross(molfile) from mytable;

Checking Molecules and Reactions for Correctness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the ``bingo.CheckMolecule()`` function to check that
molecules are presented in acceptable form. If the molecule has some
problems (unsupported format, exceeded valence, incorrect
stereochemistry), the functions returns a string with the description of
the problem. Is the molecule is represented with a correct Molfile or
SMILES string, the function returns ``null``.

::

    SELECT bingo.CheckMolecule($molecule);

    SELECT $table.*, bingo.CheckMolecule($column) from $table where bingo.CheckMolecule($column) is not null;

Similarly, you can check reactions for correctness with the
``bingo.CheckReaction()`` function:

::

    SELECT bingo.CheckReaction($reaction);

    SELECT $table.*, bingo.CheckReaction($column) from $table where bingo.CheckReaction($column) is not null;

To check the whole table you can use ``CheckMoleculeTable`` and
``CheckReactionTable`` functions. It is much faster to check the whole
table then to check each molecule one by one.

The following command checks the table for invalid molecules/reactions:

::

    select * from bingo.CheckMoleculeTable('$table', '$id', '$molecule')
    select * from bingo.CheckReactionTable('$table', '$id', '$reaction_column')

``$table`` is the name of the table containing molecule/reaction data in
column ``$molecule``/``$reaction`` and the unique integer identifier in
column ``$id``.

These functions returns a table with molecule/reactions that have
mistakes. Such records will not be added to them chemical index. Before
indexing new table we recommend you to call this method and correct
mistakes. If molecule is correct by Bingo gives a error message on it
then we can fix it if you provide us the molecule with mistakes. The
easiest way to do this is to collect problematic molecules into one
table and then call ExportSDF on this table. For example:

::

    select t.id, t.data, err.msg into molecules_with_mistakes from <table> t, bingo.CheckMoleculeTable('<table>', 'id', 'data') err where t.id=err.id
    exec bingo.ExportSDF 'molecules_with_mistakes', 'data', 'c:/molecules_with_mistakes.sdf', 'id, msg'

Permissions management
----------------------

The following users and user roles are created during installation of
Bingo :

-  User **bingo**. All procedures and functions are signed by a
   certificate that is mapped to this user. **bingo** has permissions to
   create tables in the database. Every procedure and every function of
   Bingo has has both current user permissions and **bingo** user
   permissions during execution.
-  **bingo\_reader** user role. This user role has permissions to
   execute Bingo functions because functions don't have side effects.
-  **bingo\_operator** user role. This user role has permissions to
   execute public Bingo procedures and functions. **bingo\_operator**
   also inherits **bingo\_reader** permissions.

So for precise permissions management you need:

-  For Bingo index creation your need to grant user bingo **alter**
   permissions on the such table, because index creation attaches
   triggers to the specified table for inserting, updating and deleting
   records.
-  Add operator user to the **bingo\_operator** user role. Such users
   will have permissions to create/drop molecule and reaction index.
-  Add ordinary user to the **bingo\_reader** user role. Such users will
   have permissions to perform molecule and reaction search queries.

Maintenance
-----------

Obtaining Bingo Version Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    select bingo.GetVersion();

Viewing the Log File
~~~~~~~~~~~~~~~~~~~~

The log file is called ``bingo_sql_server.log`` and located in the
system temporary directory on the server file system. Usually it is:
``C:\Windows\Temp\bingo_sql_server.log`` or
``C:\Windows\ServiceProfiles\NetworkService\AppData\bingo_sql_server.log``.
To find out the log file location you can call:

::

    exec bingo._WriteLog 'Some text'

This procedure adds specified text to the log file and prints to the
output path to the log file.

All operation of Bingo is logged. All error and warning messages (not
necessarily visible in SQL session) are logged. Some performance
measures of the SQL queries are written to the log as well.
