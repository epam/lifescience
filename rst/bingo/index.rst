﻿Bingo
=====

.. toctree::
    :hidden:
    :includehidden:

    bingo-oracle
    bingo-postgres
    bingo-sqlserver
    bingo-nosql
    Downloads <../download/bingo>

Overview
--------

Bingo is a RDBMS data cartridge that provides the industry’s
next-generation, fast, scalable, and efficient storage and searching
solution for chemical information.

Bingo seamlessly integrates the chemistry into Oracle, Microsoft SQL
Server and PostgreSQL databases. Its extensible indexing is designed to
enable scientists to store, index, and search chemical moieties
alongside numbers and text within one underlying relational database
server.

Bingo sets the industry standard in structure and reaction registration
and retrieval. You can register entities reliably with the confidence
that you can retrieve them rapidly.

Because Bingo implements state-of-the-art indexing algorithms within the
underlying database server, chemical searching is fast and reliable.
Users can seamlessly combine chemical substructure, reaction, and exact
structure searching with numeric and text SQL terms.

Why Select Bingo as Your Molecular Search Cartridge?
----------------------------------------------------


Bingo has all the necessary features required by modern cheminformatics
applications. It also has features not present in other cartridges — for
example, advanced tautomer search, resonance substructure search, and
fast updating of the index when adding new structures.

Bingo provides an interface for the Oracle cost-based optimizer where
possible, particularly in SMILES queries.

Bingo is reliable. Bingo has no legacy code to maintain, and it has been
subjected to extensive testing.

Bingo is fast. We have succeeded in achieving the best performance in
the industry for a search cartridge for both the screening phase and the
matching phase of various types of searches, especially substructure
search. Bingo has very effective memory management with no unnecessary
re-allocations. Communication with the underlying database, especially
LOB handling, is optimized as well. During substructure searches,
molecules and reactions are stored in shared memory to speed up the
access.

Features
--------


**Searches in a variety of ways:** For molecule structure searching,
Bingo supports 2D and 3D exact and substructure searches, as well as
SMARTS searches. It also supports similarity, tautomer, Markush,
formula, molecular weight, and flexmatch searches. Canonical SMILES,
with isomeric information included, are available as well. For reaction
searches, Bingo supports reaction substructure search (RSS) with the
optional automatic generation of atom-to-atom mapping. All of these
techniques are available through extensions to the SQL syntax.

A chemistry column in a table being searched can contain Molfile (V2000
or V3000) or SMILES data. Similarly, the query can be in Molfile or
SMILES format. For reactions, Rxnfile or reaction SMILES formats are
supported for both target and query structures.

Fragment highlighting is supported for substructure, tautomer, and
reaction substructure searches.

Different indexing options are available to optimize storage space
requirements versus the speed of registration. For example, by switching
off the tautomer fingerprints, the indexing will become faster. Indexes
can be updated or rebuilt with no downtime for maintenance. The addition
of new molecules/reactions does not require the rebuilding of the index.

**Flexibility and scalability of a true data cartridge:** Fully
compliant with the Oracle and MS SQL Server, Bingo allows structure and
reaction tables to be placed anywhere in the database, and the data can
be accessed by any SQL compliant application.

Bingo contains a combined structure and reaction cartridge. 2D and 3D
search features are supported by the same index.

Bingo supports a large database operation. It is successfully
`operating <TODO:bingo-demo>`__ on the PubChem database, with up to 27
million structures.

Bingo offers full support for Oracle 9/10/11 and for MS SQL Server 2008.
It is written in C++ and is thread- safe. Native binaries are built for
Windows 32/64 bit, Linux 32/64 bit, Mac OS X, and Solaris.

Bingo has a very simple installation procedure. It is possible to
install and use two (or more) versions at the same time.

**Integration:** With Bingo, you can build a fully relational
registration system: Insert, delete, and update records in a relational
structure or reaction database using data cartridge technology in
Oracle, or automatically generated triggers in MS SQL Server.

With Bingo, you can develop new applications that manage proprietary
structure and reaction information. Since the cartridge is data model
independent, it allows great flexibility in the design of applications
and the management of proprietary structure and reaction information.

Download and Install
--------------------

Look at the `Downloads <../download/bingo.html>`__ page for the
installation package suitable for your system.

For installation instructions, see the `installation manual for
Oracle <installation-manual-oracle.html>`__, `installation manual for
SQL Server <installation-manual-sqlserver.html>`__ or `installation
manual for PostgreSQL <installation-manual-postgres.html>`__

Read the `user manual for Oracle <user-manual-oracle.html>`__ before
using the cartridge in Oracle. For SQL Server users, please read the
`user manual for SQL Server <user-manual-sqlserver.html>`__. For
PostgreSQL users, please read the `user manual for
PostgreSQL <user-manual-postgres.html>`__.

For Oracle users, see also the `performance
tips <performance-tips-oracle.html>`__.

License
-------

Copyright © 2009-2014 LifeSciences unit of EPAM Systems, Inc.

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

**Additional permissions under GNU GPL version 3 section 7.** If you
modify this program, or any covered work, by linking or combining it
with an Oracle Database, containing parts covered by the terms of the
`Oracle Technology Network Developer
License <http://www.oracle.com/technetwork/testcontent/standard-license-088383.html>`__,
the licensors of this program grant you additional permission to convey
the resulting work.

If you modify this program, or any covered work, by linking or combining
it with a Microsoft SQL Server Standard Edition or Microsoft SQL Server
Express Edition, containing parts covered by the terms of the
appropriate Microsoft SQL Server End User License Agreement, the
licensors of this program grant you additional permission to convey the
resulting work.

Feedback
--------


Do you need assistance using our tools? Do you need a feature? Do you
want to send a patch to us? Did you find a bug? Please write to one of
the following newsgroups and let us know:

-  http://groups.google.com/group/indigo-bugs : for bug reports on all
   Open-Source projects.
-  http://groups.google.com/group/indigo-dev : for development topics.
-  http://groups.google.com/group/indigo-general : for any other
   discussions.

No registration is required: you can write from your ordinary e-mail
account to indigo-bugs@googlegroups.com, indigo-dev@googlegroups.com, or
indigo-general@googlegroups.com to get your message posted.

Commercial Availability
-----------------------


If the GPL-licensed Bingo does not fit your needs, please contact us to discuss the purchase of a commercial license.
You may need the commercial license if you want to:

-  Receive ongoing support and maintenance
-  Include Bingo as a component in your proprietary software product
-  Use Bingo with Oracle licensed not with OTN Developer License, or
   with MS SQL Server Enterprise Edition



Changelog
---------

Please see the `Bingo Changelog <changelog.html>`__ page
