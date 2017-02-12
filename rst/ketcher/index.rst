Ketcher
=======

.. toctree::
    :hidden:
    :includehidden:

    editing-tips
    developers-manual
    help
    demo
    Downloads <../download/ketcher>

Overview
--------

Ketcher is a web-based chemical structure editor.

|image0|

Since Ketcher is written in pure Javascript, it incorporates high
performance, good portability and light weight. You will not need any
Java or Flash plugins to use it in your browser. Ketcher is completely
free and open-source, while also available on a commercial basis.

You can easily integrate Ketcher into your web application. The process
of integration is very simple and
`well-documented <developers-manual.html>`__.

Note
~~~~

Ketcher is under active development. You can post us your `comments and
suggestions <../contact.html#feedback-on-open-source-products>`__ and
get timely replies from the developers' team.


Features
--------

Standalone mode
~~~~~~~~~~~~~~~

Ketcher supports the standalone mode in which no server support is
required. In this mode, SMILES loading, automatic layout and automatic
atom-atom mapping are not available.

Scalable Vector Graphics (SVG) for rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ketcher uses `Raphael <http://raphaeljs.com/>`__ as a backend, which
means that `SVG <../resources.html#web-standards>`__ or
`VML <../resources.html#web-standards>`__ (Vector Markup Language) is
used for rendering, depending on the browser.

Automatic layout (clean up), AAM (atom-to-atom mapping) and (de)aromatization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ketcher delegates these computationally intensive procedures to the
`Indigo <../indigo/index.html>`__ toolkit on the server side.

Supported file formats
~~~~~~~~~~~~~~~~~~~~~~

Ketcher can import and export
`Molfile/Rxnfile <../resources.html#file-formats>`__, as well as
`SMILES <../resources.html#file-formats>`__. Server is required to
import a `SMILES <../resources.html#file-formats>`__ string, since
layout is needed to obtain the coordinates.

Other features
~~~~~~~~~~~~~~

**Fast and convenient editing.** We strive to make Ketcher as easy to
use and as fast as the state-of-the-art desktop structure editing tools.
See `Editing Tips <editing-tips.html>`__ for details. Here are some
highlights:

-  Lasso and Rectangle selection tools, plus a special Fragment
   selection tool to deal with connected components, rather than single
   atoms/bonds.
-  A variety of `hotkeys <editing-tips.html#hotkeys>`__.
-  Undo/Redo.

**Stereochemistry.** Ketcher provides complete stereochemistry support
during the editing, loading, and saving of chemical structures.

**Reactions.** Full-featured reaction support including reacting
centers, atom flags and AAM.

**S-groups.** All major S-group types are supported including generic,
SRU polymers, multiple groups, superatoms and data S-groups.

**R-groups.** R-site and R-fragment assignment is supported, as well as
attachment point specification and R-logic.

Supported browsers
------------------

The complete functionality of Ketcher has been tested on the following
browsers:

-  Internet Explorer 6+
-  Firefox 3.5+
-  Safari 4+
-  Opera 9.6+
-  Chrome 2+

Third-party code
----------------

Ketcher makes use of `Raphael <http://raphaeljs.com/>`__ and
`Prototype <http://prototypejs.org/>`__.

The current icon set was taken from `Tango Desktop
Project <http://tango.freedesktop.org/Tango_Icon_Library>`__

Ketcher 2.0
-----------

Right now the new version of Ketcher is developed. It includes modern interface, good performance 
and lot of useful features. 

|ketcher2|


You can already try the `Ketcher 2.0 demo <demo.html>`__
But please be informed, that it is unstable and not all browsers are supported


Download
--------

Look at the `Downloads <../download/ketcher.html>`__ page for the
`installation <developers-manual.html#installation>`__ package and a
sample `server <developers-manual.html#ketcher-server>`__
implementation.

License
-------

Copyright © 2010-2014 LifeSciences unit of EPAM Systems, Inc.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see http://www.gnu.org/licenses/.

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

If the AGPL-licensed Ketcher does not fit your needs, please contact us 
to discuss the purchase of a commercial license.
You may need the commercial license if you want to:

-  Receive ongoing support and maintenance
-  Include Ketcher as a component in your proprietary software product

.. |image0| image:: ../assets/ketcher/ketcher_2.png
   :target: demo.html

.. |ketcher2| image:: ../assets/ketcher/2.0.0-alpha.1+r78.png 
