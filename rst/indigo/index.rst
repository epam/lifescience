Indigo Toolkit
==============

.. toctree::
    :hidden:
    :includehidden:

    API <api/index>
    Concepts <concepts/index>
    utilities
    installation
    options/index
    examples/index
    Downloads <../download/indigo/index>

.. meta::
   :description: Indigo is a universal molecular toolkit that can be used for molecular fingerprinting, substructure search, and molecular visualization. Also capable of performing a molecular similarity search, it is 100% open source and provides enhanced stereochemistry support for end users, as well as a documented API for developers.
   :keywords: rendering, visualization, canonical, stereochemistry, substructure, molecule


Overview
--------

Indigo is a universal molecular toolkit that can be used for molecular 
fingerprinting, substructure search, and molecular visualization. 
Also capable of performing a molecular similarity search, 
it is 100% open source and provides enhanced stereochemistry support for end users, 
as well as a documented `API <api/index.html>`__ for developers.


Indigo is based on a cheminformatics library that incorporates a number
of `unique algorithms <../resources.html#algorithms>`__ developed by
EPAM, as well as some standard algorithms well-known in the
cheminformatics world. Since the core part of Indigo is written in
modern C++ with no third-party code or dependencies except the
ubiquitous zlib and libcairo, the toolkit provides outstanding
performance and excellent portability.

Indigo is used by many corporations and institutions. This includes some
Indigo-based commercial tools developed exclusively for our clients.
Also, our open-source chemical search engine
`Bingo <../bingo/index.html>`__ is developed on top of the Indigo
library.

Why Select Indigo as Your Molecular SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Indigo SDK does not make any restrictions for developers. Whatever your
favorite platform is—Java, C#, or Python, not to mention plain C—you can
easily integrate Indigo into your application. All problems you may be
afraid of, such as loading binary modules appropriate for the system, or
threading issues, or stack overflows, are already solved for you. Also,
it is easy to start, as the `interface <api/index.html>`__ is very neat.
No data types besides the absolute minimum required for it to work. No
internal data formats. No painful initialization procedures.

Indigo SDK is highly `configurable <options/index.html>`__ and extensible.
You can write C/C++/C#/Java/Python plugins for it and distribute them
independently.

Indigo has got support from the cheminformatics
`community <../contact.html#feedback-on-open-source-software>`__. Any
question or comment you have, you can always post it publicly and get a
timely reply from the developers' team.

Features
--------

-  Input formats support: Molfiles/Rxnfiles v2000 and v3000, SDF, RDF,
   CML, SMILES, SMARTS.
-  Portability: Pre-built binary packages are provided for Linux and
   Windows (both 32-bit and 64-bit), and also for Mac OS X systems (both
   10.5 and 10.6).
-  Molecule and reaction rendering. Best picture quality among all
   available products. Easy SVG support.
-  Automatic layout for SMILES-represented molecules and reactions.
-  Canonical (isomeric) SMILES computation.
-  Exact matching, substructure matching, SMARTS matching.
-  Matching of tautomers and resonance structures.
-  Molecule fingerprinting, molecule similarity computation.
-  Fast enumeration of SSSR rings, subtrees, and edge subgraphs.
-  Molecular weight, molecular formula computation.
-  R-Group deconvolution and scaffold detection. Pioneer work in
   computing the *exact* maximum common substructure for an arbitrary
   amount of input structures.
-  `Combinatorial chemistry <concepts/combichem.html>`__
-  Plugins support in the API. As a reference, please see the Renderer
   plugin distributed together with the Indigo API.

Portability
-----------

Indigo is written from scratch in portable C++ and supports Linux,
Windows, and Mac OS X operating systems. The rendering is done via
`Cairo <http://cairographics.org/>`__ vector graphics library.
`zlib <http://www.zlib.net/>`__ and
`libpng <http://www.libpng.org/pub/png/libpng.html>`__ are needed for
Cairo. `tinyxml <http://www.grinninglizard.com/tinyxml/>`__ is used to
parse CML files. No other third-party components are used.

Indigo exposes the `C interface <api/reference.html#plain-c>`__ to applications. Java
and Python wrappers are available for all of the supported platforms.
For Windows, there is also a .NET wrapper.

All of the the code of Indigo is thread-safe, and so its use does not
present a problem in multi-threaded applications.

Documentation
-------------

To understand Indigo's scope, start with the
`Concepts <concepts/index.html>`__ page. A quick reference of the API
for all supported languages is provided in the `API <api/index.html>`__
page. A separate page deals with the `C interface <api/reference.html#plain-c>`__.
Various options that can be passed to the library are explained on the
`Options <options/index.html>`__ page.


GCC 2010 Presentation
---------------------

Here is the presentation for the talk that was given in November 2010 in
Goslar at the German Conference on Cheminformatics:
:download:`PDF <../assets/indigo/indigo_cic2010.pdf>` (396K).

And here is the poster presented at the same conference:
:download:`PDF <../assets/indigo/indigo_cic2010_poster.pdf>` (3.1M).

KNIME Nodes
-----------

We provide a number of freely available `nodes <knime.html>`__ for the
`KNIME <http://knime.org>`__ workflow engine. The nodes are based on
Indigo and its Java SDK.

Java GUI Utilities
------------------

Two Indigo-based Java GUI applications are provided:

-  `Legio <legio.html>`__ — combinatorial chemistry
-  `ChemDiff <chemdiff.html>`__ — visual comparison of two SDF or SMILES
   files

Command-Line Utilities
----------------------

Three Indigo-based command-line utilities written in plain C are
provided:

-  `indigo-depict <indigo-depict.html>`__ (former ``dingo-render``)
   Molecule and reaction rendering utility.
-  `indigo-cano <indigo-cano.html>`__ (former ``cano-utility``)
   Canonical SMILES generator.
-  `indigo-deco <indigo-deco.html>`__ (former ``deco``) R-Group
   deconvolution utility.

Download and Install
--------------------

Look at the `Downloads <../download/indigo/index.html>`__ page for the
installation package suitable for your system.

Building from sources
---------------------

Look at the `Build <../indigo/build.html>`__ page for the building manual.

License
-------

Copyright © 2009-2019 LifeSciences unit of EPAM Systems, Inc.

Indigo version 1.0.0 was released under GNU General Public License v3.0
Indigo version 1.4.0 was re-licensed under Apache License, Version 2.

This program is free software: You can redistribute it and/or modify it
under the terms of the Apache License, Version 2.0.

You should have received a copy of the Apache License along
with this program. If you did not not, please see
https://www.apache.org/licenses/LICENSE-2.0

Feedback
--------

Do you need assistance using our tools? Do you need a feature? Do you
want to send a patch to us? Did you find a bug? Please write to one of
the following newsgroups and let us know:

-  http://groups.google.com/group/indigo-bugs : for bug reports on all
   open-source projects.
-  http://groups.google.com/group/indigo-dev : for development topics.
-  http://groups.google.com/group/indigo-general : for any other
   discussions.

No registration is required: you can write from your ordinary e-mail
account to indigo-bugs@googlegroups.com, indigo-dev@googlegroups.com, or
indigo-general@googlegroups.com to get your message posted.

Commercial Availability
-----------------------

The Apache License v2.0 allows Indigo to be used as a component in proprietary software products.

If the Apache License v2.0 does not fit your needs, please contact us to discuss the purchase of a commercial license.
You may need the commercial license if you want to:

-  Receive ongoing support and maintenance
-  Design and implement custom changes for the SDK
-  Do any other development/testing required for a proprietary software product


