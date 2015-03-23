User Manual: NoSQL
==================

Basics
------

Data representation
~~~~~~~~~~~~~~~~~~~

Bingo NoSQL supports all formats which is supported by Indigo.

Storage
~~~~~~~

All databases data like chemical structures in binary format, fingerprints, hashes and other is stored in memory mapped files in folder that is defined by user at ``createDatabaseFile`` method parameter.


Queries
~~~~~~~

You can specify the query molecule as a string containing a Molfile (including various query features), a SMILES, or a SMARTS string.  For reaction queries use Rxnfiles, reaction SMILES, or reaction SMARTS.

Molecules
---------

Creating an Index
~~~~~~~~~~~~~~~~~

The following function creates the database for molecules:

::

    bingo_db = Bingo.createDatabaseFile(indigo, 'db_dir', 'molecule', '')

-  ``bingo_db`` is the created database object
-  ``indigo`` is the indigo instance
-  ``'db_dir'`` is the path to the new database directory
-  ``'molecule'`` is the option which defines that database will contain molecules
-  ``''`` is the string that can contain additional options

   +  ``min_mmf_size`` - first mmf file size in megabytes (not less than 32mb). Example: ``min_mmf_size:64``
   +  ``min_mmf_size`` - largest mmf file size in megabytes. Example: ``max_mmf_size:1024``
   +  ``read_only`` - if ``true`` no changes in database are accepted, only one thread can open database with ``read_only:false`` option. Example: ``read_only:true``
   +  ``id_key`` - name of the records property that contain id. If that option is defined, then ``insert`` method will try to find records property with such name and set it as records id in database.``id_key:mol_id``

Updating and Closing Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add or remove records in the database after it was created. No re-indexing is required after adding the records.
To load and insert molecules to database you can do:

::

    mol1 = indigo.loadMolecule('C1CCCCC1')
    id1 = bingo_db.insert(mol1)
    mol2 = indigo.loadMolecule('C1CCNCC1')
    id2 = bingo_db.insert(mol2)
    
-  ``indigo`` is the indigo instance
-  ``bingo_db`` is the current database object
-  ``id1`` and ``id2`` are the indices of the added records. By these indices you can then access database records

Or you can insert record to database with your id:
::

   bingo_db.insert(mol1, 100)

Exception will be thrown if id '100' is already has been used.

The following function will remove record from database:

::

    bingo_db.delete(id1) 

To close database when you've done working with it call next function:

::

    bingo_db.close()
    
    
Loading Index
~~~~~~~~~~~~~

The following function opens the database:

::

    bingo_db = Bingo.loadDatabaseFile(indigo, 'db_dir', '')

-  ``bingo_db`` is the loaded database object
-  ``indigo`` is the indigo instance
-  ``'db_dir'`` is the path to the database directory
-  ``''`` is the string that can contain additional options



Substructure Search
~~~~~~~~~~~~~~~~~~~

To run substructure search through your database you can do next couble of steps.

Load your query molecule:
::

    query = indigo.loadQueryMolecule('CC')

Next function will create bingos substracture matcher object:
::

    sub_matcher = bingo_db.searchSub(query, '')

-  ``''`` is the matcher options

   +  ``part:<id of the part>/<number of parts>`` is the option for partial search. Example: ``part:1/5``

And then iterate results with matchers ``next()`` method:
::

    while sub_matcher.next():
        print(sub_matcher.getCurrentId())
    exact_matcher.close()

-  ``getCurrentId()`` will return id of the matched record

Exact Search
~~~~~~~~~~~~

Exact search can be done similarly as substructure search:

::

    exact_matcher = bingo_db.searchExact(query, '')
    while exact_matcher.next():
        print(exact_matcher.getCurrentId())
    exact_matcher.close()

Similarity Search
~~~~~~~~~~~~~~~~~

The general form of similarity search query is as follows:

::

    sim_matcher = bingo_db.searchSim(query, minSim, maxSim, sim_type)

Here is:

-  ``minSim`` and ``minSim`` are the real numbers, min and max bound of possible similarity value
-  ``bingo_db`` is the current database object
-  ``query`` is the query molecule
-  ``sim_type`` is the string that defines similarity measure type:

   +  ``'tanimoto'`` - Tanimotos measure
   +  ``'tversky'`` - Tverskys measure
   +  ``'euclid'`` - Euclids measure


The following loop will print all results of similarity matching:
::

    cur_mol = sim_matcher.getIndigoObject()
    while sim_matcher.next():
        print(sim_matcher.getCurrentId())
        print(sim_matcher.getCurrentSimilarityValue())
        print(cur_mol.smiles())
    sim_matcher.close()

-  ``sim_matcher.getIndigoObject()`` will return object that will contain result target molecule at each iteration
-  ``sim_matcher.getCurrentId()`` will return current result record id
-  ``sim_matcher.getCurrentSimilarityValue()`` will return similarity value of current result and query
-  ``cur_mol.smiles()`` is the Indigos function that return smiles string for an object

Gross Formula Search
~~~~~~~~~~~~~~~~~~~~

Gross formula search can be done as described below:

::

    formula_matcher = bingo_db.searchMolFormula('C1CCNCC1', '')
    while formula_matcher.next():
        print(formula_matcher.getCurrentId())
    formula_matcher.close()
    
Where:

-  ``'C1CCNCC1'`` is the query formula

Reactions
---------

Creating an Index
~~~~~~~~~~~~~~~~~

The following function creates the database for reactions:

::

    bingo_db = Bingo.createDatabaseFile(indigo, 'db_dir', 'reaction', '')

-  ``bingo_db`` is the created database object
-  ``indigo`` is the indigo instance
-  ``'db_dir'`` is the path to the new database directory
-  ``'reaction'`` is the option which defines that database will contain reactions.
-  ``''`` is the string that can contain additional options


Updating and Closing Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add or remove records in the database after it was created. No re-indexing is required after adding the records.
To load and insert reactions to database you can do:

::

    rxn1 = indigo.loadReaction('C1CCCCC1>>CCC')
    id1 = bingo_db.insert(rxn1)
    rxn2 = indigo.loadReaction('C1CCNCC1>>CCN')
    id2 = bingo_db.insert(rxn2)
    
-  ``indigo`` is the indigo instance.
-  ``bingo_db`` is the current database object
-  ``id1`` and ``id2`` are the indices of the added records. By these indices you can then access to database records.

Or you can insert record to database with your id:
::

   bingo_db.insert(rxn1, 100)

Exception will be thrown if id '100' is already has been used.

The following function will remove record from database:

::

    bingo_db.delete(id1) 

To close database when you've done working with it call next function:

::

    bingo_db.close()

Loading Index
~~~~~~~~~~~~~

Follow the steps described in 'Molecules' section `Loading Index <user-manual-nosql.html#loading-index>`__

Reaction Substructure Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run substructure search through your database you can do next couble of steps.

Load your query reaction:
::

    query = indigo.loadQueryMolecule('CC>>CN')

And then follow the steps described in 'Molecules' section `Substructure Search <user-manual-nosql.html#substructure-search>`__

Reaction Exact Search
~~~~~~~~~~~~~~~~~~~~~

Follow the steps described in 'Molecules' section `Exact Search <user-manual-nosql.html#exact-search>`__

Reaction Similarity Search
~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps described in 'Molecules' section `Similarity Search <user-manual-nosql.html#similarity-search>`__

Reaction Gross Formula Search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow the steps described in 'Molecules' section `Gross Formula Search <user-manual-nosql.html#gross-formula-search>`__


Remaining results estimation
----------------------------

Next functions will return remaining time and results count estimations:
::

    sim_matcher.estimateRemainingResultsCount()
    sim_matcher.estimateRemainingResultsCountError()
    sim_matcher.estimateRemainingTime()))

Python example:
---------------

.. code-block:: python

    #Bingo database creating
    bingo = Bingo.createDatabaseFile(indigo, 'db_dir', 'molecule', '')
     
    # Molecules loading and inserting them to database
    m = indigo.loadMolecule('C1CCCCC1')
    bingo.insert(m)
    m = indigo.loadMolecule('C1CCNCC1')  
    bingo.insert(m)
     
    # Query molecule loading
    qm = indigo.loadQueryMolecule('C')
     
    # Bingo substructure matcher creation
    matcher = bingo.searchSub(qm, '')
     
    # Results iterating (robj will contain result target molecule on each iteration)
    robj = matcher.getIndigoObject()
    while matcher.next():  
        print(matcher.getCurrentId())
        print(robj.smiles())
     
    # Substructure matcher closing
    matcher.close()
     
    # Bingo database closing
    bingo.close()

C Interface
-----------

1) Creation/loading/closing database.

.. code-block:: cpp

    int bingoCreateDatabaseFile (const char *location, const char *type, const char *options);

    int bingoLoadDatabaseFile (const char *location, const char *options);

    int bingoCloseDatabase (int db);

2) Insertion/Removing chemical structure

.. code-block:: cpp

    int bingoInsertRecordObj (int db, int obj);

    int bingoInsertRecordObjWithId (int db, int obj, int id);

    int bingoDeleteRecord (int db, int id);

3) Searching

.. code-block:: cpp

    int bingoSearchSub (int db, int query_obj, const char *options);

    int bingoSearchExact (int db, int query_obj, const char *options);

    int bingoSearchMolFormula (int db, const char *query, const char *options);

    int bingoSearchSim (int db, int query_obj, float min, float max, const char *options);
