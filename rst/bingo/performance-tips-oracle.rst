Performance Tips: Oracle
========================

General
-------

#. Please always use the most recent version of Bingo.
#. Please store as little data as possible in the indexed table. See the
   “Performance Notice” in the `user
   manual <user-manual-oracle.html#storage>`__ for details.
#. Oracle 10 and 11 usually perform better than Oracle 9.

Indexing
--------

#. Please turn off the ``ARCHIVELOG`` option in your database instance.
   This saves a significant amount of time and disk space during
   indexing.
#. Bingo takes advantage of multi-core processors. The number of
   indexing threads is detected automatically. If you want, for some
   reason, to use some specific number of threads, use the ``NTHREADS``
   indexing parameter.
#. You can disable the computation of specific fingerprint parts (saving
   both time and disk space) by setting the relevant parameter to zero.
   See the corresponding section of the `user
   manual <user-manual-oracle.html#creating-an-index>`__ for details.

Search
------

#. While running search queries, try not to close your SQL session until
   you really need to close it. See the note in the `user
   manual <user-manual-oracle.html#queries>`__ for details.
#. Please increase Oracle's “database buffers” parameter as much as you
   can, given the extent of server's memory. This step may require
   activation of `manual memory
   management <http://download.oracle.com/docs/cd/B19306_01/server.102/b14220/memory.htm>`__
   in Oracle.

