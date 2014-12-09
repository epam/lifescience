Building from Source
====================

Unpack the Source Code
----------------------

The source code links are available on the
`Downloads <../download/index.html>`__ page.

Unzip the ``bingo-src-XXXX.zip`` archive (``XXXX`` is the revision
number). After finishing the unpacking, go to the
``bingo-src-XXXX/bingo`` folder.

Copy the OCI files
------------------

On All Systems
~~~~~~~~~~~~~~

Copy ``oci.h``, ``ociextp.h``, and other header files from your Oracle
installation (usually located in ``$ORACLE_HOME/rdbms/public/`` and/or
``$ORACLE_HOME/oci/include/`` and/or ``$ORACLE_HOME/rdbms/demo/``) into
``../oci/include`` directory. On Solaris, copy them to the
``../oci/include.sun`` directory instead.

On 32-bit Windows
~~~~~~~~~~~~~~~~~

Copy ``oci.lib`` from your Oracle installation (usually located in
``%ORACLE_HOME%\oci\lib\msvc\``) into ``../oci/lib32/oci32.lib``.
**Note:** You should rename the file.

On 64-bit Windows
~~~~~~~~~~~~~~~~~

Copy ``oci.lib`` from your Oracle installation (usually located in
``%ORACLE_HOME%\oci\lib\msvc\``) into ``../oci/lib64/oci64.lib``.
**Note:** You should rename the file.

On Mac OS X
~~~~~~~~~~~

Copy ``liborasdk.dylib`` from your Oracle installation (usually located
in ``%ORACLE_HOME%\lib\``) into ``../oci/lib64/liborasdk.dylib``.

Build
-----

**Note:** You should have the ``zip`` command-line utility installed on
your system.

On Linux, run

::

    ./all-release-linux.sh $version

On Solaris, run

::

    ./all-release-sun.sh $version

On Windows, run

::

    all-release-windows.bat $version

where ``$version`` is some version identifier, like ``1.5-xxxx``.

You will get a number of ``.zip`` archives for your selected platform,
both 32-bit and 64-bit versions. (In case of Mac OS X, both 10.5 and
10.6 versions.) Please read the `Installation Manual for
Oracle <installation-manual-oracle.html>`__ or `Installation Manual for
SQL Server <installation-manual-sqlserver.html>`__ to know how to
install the package on your system.
