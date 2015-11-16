Indigo Development Releases
===========================

This page contains experimental development builds that can have issues
and API can change in future.

We provide library bindings for Python, Java, and .NET. These bindings
contain Indigo binary modules for the specified platform. For example,
build for Windows includes 32-bit and 64-bit versions of Indigo binary
modules and can be used both in 32-bit and 64-bit applications. Indigo
library automatically loaded required binary module depending on your
platform. Universal builds include all other binary modules and can be
used in cross-platform applications.

We also provide native shared libraries to use Indigo in your native
application, or use static libraries if your prefer to avoid shared
libraries dependencies.

Indigo 1.2.1-dev
----------------

*22 May 2014*

Main changes:

-  New Bingo plugin for Indigo.
-  C++ dependent libraries being statically linked with Indigo to avoid
   external dependency on libstd++ or libc++
-  Indigo code uses C++11 standard with the build binaries are
   absolutely portable across various Windows, Linux and Mac OS version

Language Bindings
~~~~~~~~~~~~~~~~~

Python
^^^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-python-1.2.1dev-win.zip>`__,
`Linux <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-python-1.2.1dev-linux.zip>`__,
`Mac OS
X <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-python-1.2.1dev-mac.zip>`__,
`Universal <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-python-1.2.1dev-universal.zip>`__

Java
^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-java-1.2.1dev-win.zip>`__,
`Linux <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-java-1.2.1dev-linux.zip>`__,
`Max OS
X <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-java-1.2.1dev-mac.zip>`__,
`Universal <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-java-1.2.1dev-universal.zip>`__

.NET
^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-dotnet-1.2.1dev-win.zip>`__,
`Linux <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-dotnet-1.2.1dev-linux.zip>`__,
`Max OS
X <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-dotnet-1.2.1dev-mac.zip>`__,
`Universal <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-dotnet-1.2.1dev-universal.zip>`__

Native library
^^^^^^^^^^^^^^

Shared libraries:
`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-libs-1.2.1dev-win-shared.zip>`__,
`Linux <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-libs-1.2.1dev-linux-shared.zip>`__,
`Mac OS
X <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/indigo-1.2.1dev/indigo-libs-1.2.1dev-mac-shared.zip>`__

Static libraries are not distributed because they depends on the
compiler. You can build you version from the sources.

Indigo 1.2.1-layout-dev
-----------------------

*17 April 2014*

In this version we added significantly improved our 2D coordinate
generation algorithm for molecules with macrocycles. SDF with several
structures is included in the archives. Ask us for Linux and Mac
versions if needed in the indigo-dev support group
http://groups.google.com/group/indigo-dev.

Language Bindings
~~~~~~~~~~~~~~~~~

Python
^^^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/1.2.1-layout-dev/indigo-python-1.2.1-layout-dev-win.zip>`__

Java
^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/1.2.1-layout-dev/indigo-java-1.2.1-layout-dev-win.zip>`__

.NET
^^^^

`Windows <http://www.epam.com/download?downloadParam=/content/dam/epam/library/open-source/indigo-1.2-dev/1.2.1-layout-dev/indigo-dotnet-1.2.1-layout-dev-win.zip>`__
