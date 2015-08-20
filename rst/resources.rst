Resources
=========

.. toctree::
    :hidden:

    resources

Algorithms
----------

Fingerprinting is a common technique for molecular screening. Daylight,
Inc. introduced this technique, and it is described in the following
`article <http://www.daylight.com/dayhtml/doc/theory/theory.finger.html>`__.
Bingo fingerprints, as compared to Daylight fingerprints, are built not
from bond paths, but from trees and rings. A Russian article describes
the `enumeration of
subtrees <http://shmat-razum.blogspot.com/2008/11/blog-post.html>`__,
which in turn is based on `reverse
search <http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.26.4487>`__
by David Avis and Komei Fukuda.

For tautomer substructure search, Bingo incorporates a unique type of
fingerprinting.

For subgraph matching, we developed an original algorithm. It is
somewhat similar to an algorithm by `Luigi Cordella et
al. <http://portal.acm.org/citation.cfm?id=1018377>`__

For the molecule layout in Indigo and Bingo, we developed a unique
algorithm, based on biconnected components extraction. It incorporates
some ideas of `Craig
Shelley <http://pubs.acs.org/doi/abs/10.1021/ci00038a002>`__.

For the aromaticity matching and resonance search, we developed unique
algorithms as well.

For the canonical SMILES, Brendan McKay's
`nauty <http://cs.anu.edu.au/~bdm/nauty/>`__ canonical labeling
algorithm was re-implemented. Many of the original nauty's features and
optimizations were not included. There is also a
`description <http://shmat-razum.blogspot.com/2009/06/graph-automorphisms-canonical-labeling.html>`__
of the algorithm in Russian.

For the affine transformation matching, `Wolfgang Kabsch's
algorithm <http://scripts.iucr.org/cgi-bin/paper?S0567739476001873>`__
was implemented.

In internal molecule and reaction formats, the
`LZW <http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch>`__
algorithm with some modifications was used for compression.

For the exact maximum common substructure search, we developed a unique
algorithm partially based on `Thierry Hanser's
algorithm <http://cdk.sourcearchive.com/documentation/1:1.0.2-2/dir_fc89e4c1c81ccda6d426c1b67ae622bd.html>`__
(which in turn has its roots in an algorithm by `Coen Bron and Joep
Kerbosh <http://portal.acm.org/citation.cfm?id=362367>`__). For the
approximate maximum common substructure search, the
`2DOM <http://ci.nii.ac.jp/naid/110003210164/>`__ algorithm with some
modifications was implemented. A :download:`Russian paper <assets/mcs_article.pdf>` describes both algorithms.

Oracle Interface
----------------

The C++ wrapper was implemented for the Oracle OCI library. One Russian
article describes `the pitfalls of handling Oracle LOBs in
OCI <http://lj.rossia.org/users/ringill/5064.html>`__, while another
Russian article covers the `performance of
queries <http://shmat-razum.blogspot.com/2009/01/oracle.html>`__.

Tautomer Methods
----------------

InChI Code
^^^^^^^^^^

The IUPAC International Chemical Identifier (InChI) is a textual identifier for chemical substances,
designed to provide a standard and human-readable way to encode molecular information.
Read more about `The IUPAC Chemical Identifier – Technical Manual <ftp://ftp.uk.freesbie.org/sites/downloads.sourceforge.net/n/ni/ninja/technical_manual/inchi-tech-manual-20060511/inchi_tech_man-20060511.pdf>`__.

InChI code provides information about mobile H atoms with allows us enumerate all possible tautomers based on (1,3)-shifts for open-chain molecules
and (1,n)-shifts (with n being an odd number >3) for ring systems. Please see :download:`Tautomer Identification and Tautomer Structure Generation Based on the InChI Code <assets/indigo/Inchi tautomers.pdf>` for details.


RSMARTS Rules
^^^^^^^^^^^^^

RSMARTS rules is another approach to enumerate tautomers. Currently the set of rules is taken from the article :download:`Tautomerism in large databases <assets/indigo/Tautomerism in large databases.pdf>`.

Cairo
-----

`Cairo <http://cairographics.org/>`__ 1.8.6 was used for rendering in
Indigo. In Linux builds, the system-wide installation of ``libcairo``
must be present (``-I/usr/include/cairo`` flag is passed to the compiler
and ``-lcairo`` is passed to the linker). In Mac OS X builds, the
system-wide installation of ``libcairo`` must be present as well
(``/opt/local/lib/libcairo.dylib`` path is passed to the linker). You
can install it using `MacPorts <http://www.macports.org/>`__. The 32-bit
and 64-bit Windows builds of Cairo are included in the source tree. They
can be downloaded from
`GTK <http://www.gtk.org/download/index.php>`__ and
`GNOME <http://ftp.gnome.org/pub/GNOME/binaries/win64/dependencies/>`__
project sites, respectively. Binaries of
`libpng <http://www.libpng.org/pub/png/libpng.html>`__,
`zlib <http://www.zlib.net>`__, `Freetype <http://www.freetype.org>`__,
`Fontconfig <http://www.fontconfig.org>`__, and
`Expat <http://expat.sourceforge.net/>`__, needed for Cairo, are there
as well.

File Formats
------------

The molecule and reaction format descriptions are available on the
following sites: `Daylight
SMILES <http://www.daylight.com/dayhtml/doc/theory/theory.smiles.html>`__,
`ChemAxon SMILES
extensions <http://www.chemaxon.com/marvin/help/formats/cxsmiles-doc.html>`__,
and `MDL (Symyx)
Molfiles <http://infochim.u-strasbg.fr/recherche/Download/Fragmentor/MDL_SDF.pdf>`__.

Web standards
-------------

More information about web standards used by Ketcher can be found here:
`SVG <http://www.w3.org/Graphics/SVG/>`__,
`VML <http://www.w3.org/TR/NOTE-VML>`__.

Web frameworks
--------------

Ketcher includes two JavaScript libraries:
`Raphaël <http://raphaeljs.com/>`__ for vector graphics and
`Prototype <http://prototypejs.org>`__ for overall code improvement.

Code Examples
-------------

`Chemistry Toolkit
Rosetta <http://ctr.wikia.com/wiki/Category:Indigo/C%2B%2B>`__ wiki
contains some examples of small utilities written using Indigo C++ API.

Development Tools
-----------------

For building projects `CMake <http://www.cmake.org/>`__ is used. We use `NetBeans <http://www.netbeans.org/>`__ on Linux
workstations, `Microsoft Visual Studio <http://msdn.microsoft.com/hi-in/vstudio/default.aspx>`__ on
Windows workstations, and `XCode <http://developer.apple.com/tools/xcode/>`__ on Mac OS X
workstations.

Commercial availability
-----------------------

We have dual-licensed our code. If the GPL-licensed code does not fit
your needs, please contact us to discuss the
purchase of a commercial license. You may need the commercial license if
you want to:

-  Receive ongoing support and maintenance of our code
-  Include our code in your proprietary software product

