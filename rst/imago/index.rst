﻿Imago OCR
=========

.. toctree::
    :hidden:
    :includehidden:

    examples
    report
    imago-gui
    imago_console
    c
    java
    dependencies
    changelog

Overview
--------

Imago OCR is a toolkit for 2D chemical structure image recognition. It
contains a `GUI <imago-gui.html>`__ program and a `command-line
utility <imago_console.html>`__, as well as a documented
`API <c.html>`__ for developers. Imago is completely free and
open-source, while also available on a commercial basis.

The core part of Imago is written from scratch in modern C++. It uses
the best known algorithms for optical recognition. That guarantees
Imago's outstanding portability and performance.

Imago OCR project is under active development. You can post us your
`comments and suggestions <#feedback>`__ and get timely replies from the
developers' team.

.. list-table:: 
   :header-rows: 1
   :widths: 50 50

   * - Source image
     - Recognized structure
   * - |image2|
     - |image3|
   * - :download:`USRE039991-20080101-C00100.png <../assets/imago/4_source_USRE039991-20080101-C00100-1.png>`
     - :download:`molecule.mol <../assets/imago/molecule.mol>`

Recognizable Molecule Features
------------------------------

-  Single, double, triple bonds, bridged bonds
-  Atom labels, subscripts, isotopes, charges
-  Superatoms and abbreviations expansion
-  Aromatic rings
-  Stereochemistry (up- and down-bonds)

You can find more examples `on this page <examples.html>`__.

Online Demo
-----------

You can evaluate the Imago OCR recognition quality on the `Imago Demo
web page <TODO:imago-demo>`__.

Comparison with other systems
-----------------------------

We created a detailed report with sets of different images that compares
Imago OCR with other publicly available solutions. The report is
available on a `separate web page <TODO:imago-report>`__. The scripts
and the image sets are available in the `download
section <../download/imago.html>`__.

|Report|

If you can suggest other test sets or other publicly available solutions
we would be happy to include them too in the report.

Resources
---------

Presentation at the Symposium on 244th ACS National Meeting &
Exposition:

Portability
-----------

Imago library is written in portable C++ and supports Linux, Windows,
and Mac OS X operating systems, both 32-bit and 64-bit versions of each
system.

Imago exposes the `C interface <c.html>`__ to applications. `Java
wrapper <java.html>`__ is available for all supported platforms. A Java
GUI application called `Imago OCR Visual Tool <imago-gui.html>`__ is
provided, and a command-line utility
`imago\_console <imago_console.html>`__ is provided as well.

List of Dependencies
~~~~~~~~~~~~~~~~~~~~

The dependencies are included into the distribution packages, and so you
do not need to download any of them separately to run the programs or to
compile the source code.

Imago C++ dependencies:

-  `OpenCV <http://opencv.org/>`__ library
-  `Boost <http://www.boost.org/>`__
-  `PicoPNG <http://lodev.org/lodepng>`__ (optional module to load PNG
   images with changes for fail-safe PNG image loading)

Java-specific dependencies:

-  `JNA <http://jna.java.net/>`__ (for Java wrapper)
-  `PDFRenderer <http://java.net/projects/pdf-renderer>`__ (only for
   Imago OCR Visual Tool)
-  `Java Advanced Imaging (JAI) <http://java.net/projects/jai>`__ (only
   for Imago OCR Visual Tool, part of Java SDK)
-  `Launch4j <http://launch4j.sourceforge.net>`__

More details on the dependencies (including their licenses) you can find
on a `separate page <dependencies.html>`__

Supported Data Formats
----------------------

Both the Imago OCR project and the ``imago_console`` tool are supporting
the most popular raster image formats: ``PNG``, ``JPEG``, ``BMP``,
``DIB``, ``TIFF``, ``PBM``, ``RAS`` and others (depending on platform).
Imago OCR Visual Tool users can also open ``PDF`` files, choose the
needed document page (if it is ``PDF`` or ``TIFF``), and select a
fragment that should be recognized.

Developers who use the C API can pass supported format images or raw
image data to the library. Recognition result can be saved as ``MDL``
(Symyx, Accelrys) Molfiles. Imago OCR Visual Tool also provides a
possibility to copy the recognized molecule to the system clipboard.

Download and Install
--------------------

Look at the `Downloads <../download/imago.html>`__ page for the
installation package suitable for your system. There is an installer for
Windows, and zipfiles for Linux and Mac OS X, which you can just unpack
into ``/usr/local/bin`` or ``/opt`` directory, or into your home
directory.

You can run Imago OCR Visual Tool even without installing any files
using Java Web Start technology. Open the `following
JNLP-file <http://www.epam.com/content/dam/epam/open-source/library/imago-2.0.0/jnlp/imago-ocr-visual-tool.jnlp>`__
to execute Imago OCR Visual Tool.

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
with this program. If you did not, please see
http://www.gnu.org/licenses/.

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

If the GPL-licensed Imago does not fit your needs, please contact us to discuss the purchase of a commercial license.
You may need the commercial license if you want to:

-  Receive ongoing support and maintenance
-  Include Imago as a component in your proprietary software product

.. |image2| image:: ../assets/imago/4_source_USRE039991-20080101-C00100.*
.. |image3| image:: ../assets/imago/4_result_USRE039991-20080101-C00100.png.imago-2.0.*
.. |Report| image:: ../assets/imago/imago-report-small.png
   :target: TODO:imago-report
