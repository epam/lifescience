Building from sources
---------------------

Sources can be obtained directly or from GitHub repository:

   -  `Source code <http://www.epam.com/content/dam/epam/open-source/library/indigo-1.1.12/indigo-1.1.12-src.zip>`__
   -  `Repository on GitHub <http://github.com/ggasoftware/indigo>`__

Requirements
^^^^^^^^^^^^

1) Cmake (minimum required version is 2.8)
2) Make
3) Python (version 2.7)
4) MSVC compiler for Windows and gcc for Linux

Building
^^^^^^^^

To build Indigo sources go to the ``build_scripts`` folder and run ``indigo-release-libs.py`` script:

::

   Usage: indigo-release-libs.py [options]

   Indigo libraries build script

   Options:
     -h, --help            show this help message and exit
     --generator=GENERATOR
                           this option is passed as -G option for cmake
     --params=PARAMS       additional build parameters
     --config=CONFIG       project configuration
     --nobuild             configure without building
     --clean               delete all the build data
     --preset=PRESET       build preset ['linux32-universal', 'win32-mingw',
                           'mac10.10', 'win64-2012', 'win64', 'win32', 'mac10.9',
                           'linux64', 'mac10.7', 'linux64-universal',
                           'win32-2013', 'win32-2012', 'mac-universal',
                           'win64-2013', 'mac10.8', 'linux32', 'mac10.6']
     --with-static         Build Indigo static libraries
     --verbose             Show verbose build information
     --cairo-gl            Build Cairo with OpenGL support
     --cairo-vg            Build Cairo with CairoVG support
     --cairo-egl           Build Cairo with EGL support
     --cairo-glesv2        Build Cairo with GLESv2 support
     --find-cairo          Find and use system Cairo
     --find-pixman         Find and use system Pixman

Example
"""""""
::

   python indigo-release-libs.py --preset=win64-2012

     
Language Bindings
^^^^^^^^^^^^^^^^^
Python
""""""
Go to the ``api/python`` directory and run ``copy-libs.py`` script. After that ``libs`` directory will appear.
To use Indigo API and its plugins in python script import them as follows:

.. code-block:: python

   import sys;
   sys.path.append('path_to_indigo/api/python')
   sys.path.append('path_to_indigo/api/inchi/python')
   sys.path.append('path_to_indigo/api/renderer/python')
   sys.path.append('path_to_indigo/api/bingo/python')
   from indigo import *
   from indigo_inchi import *
   from indigo_renderer import *
   from bingo import *

Java
""""

Run ``indigo-make-by-libs.py`` script:

::

   python indigo-make-by-libs.py
   
It will create ``indigo-java- ... .zip`` archive in ``dist`` directory which will contain jar files with Indigo and its plugins.

.NET
""""

Native library
""""""""""""""


