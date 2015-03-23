Bingo NoSQL
===========

.. toctree::

    installation-manual-nosql
    user-manual-nosql

Overview
--------

Bingo NoSQL is a Indigo plugin and non-relational database management system for storing chemical information and searching through it. With this plugin you can create databases which will be located on the hard drive of your local machine or some remote server. Bingo NoSQL uses only own and OS functionality for creating and accessing the databases, so there is no need in installing any additional third-party software. For storing chemical structures and other extra information memory-mapped files technology was used. This tecnhology shows better performance than using direct read and write operations, so I/O delays have no significant effect on the Bingo NoSQL speed.


Structure
---------

|image0|

Matchers
--------

Next several search types have been implemented already:

-  Exact matching
-  Substructure matching
-  Similarity search
-  Search by molecular formula

Files
-----

Every database has form of the directory with set of files. Files sizes increase with increasing of the database, so Bingo NoSQL can be used as for working with small local sets of chemical structures, so as for large databases. 

|image1|

Scalability
-----------

Bingo NoSQL databases have multiple-readers/single-writer access type. Together with the possibility of a partial search through one database it allows to parallelize querying between different threads.

|image2|

License
-------

Copyright 2009-2014 LifeSciences unit of EPAM Systems, Inc.

This program is free software: You can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If you did not not, please see
http://www.gnu.org/licenses/.

Commercial Availability
-----------------------

If the GPL-licensed Bingo NoSQL does not fit your needs, please contact us to discuss the purchase of a commercial license.
You may need the commercial license if you want to:

-  Receive ongoing support and maintenance
-  Include Bingo NoSQL as a component in your proprietary software product

.. |image0| image:: ../assets/bingo/bingo_nosql_structure.png
.. |image1| image:: ../assets/bingo/bingo_nosql_files.png
.. |image2| image:: ../assets/bingo/bingo_nosql_partial.png