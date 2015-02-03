Installation Manual: Oracle
===========================

System Requirements
-------------------

Operating Systems
~~~~~~~~~~~~~~~~~

-  Windows 2000/XP/2003/Vista/2008 (32-bit and 64-bit)
-  Linux (all modern distributions, 32-bit and 64-bit)
-  Solaris (including SPARC hardware)
-  Mac OS X 10.5 Leopard/10.6 Snow Leopard (64-bit)

Database Servers
~~~~~~~~~~~~~~~~

-  Oracle 9, 10, 11 (including 11.2)
-  Oracle 10 XE

Tested Configurations
~~~~~~~~~~~~~~~~~~~~~

Bingo has been successfully tested on the following configurations:

+-----------------+-------------------------+-----------------------------------+------------------+
| Bingo Version   | Database                | Operating System                  | Architecture     |
+=================+=========================+===================================+==================+
| 32-bit          | Oracle 9 (32-bit)       | Windows XP Professional           | Intel x86        |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 10 (32-bit)      | Windows XP Professional           | Intel x86        |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 10 XE (32-bit)   | Windows XP Professional           | Intel x86        |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 11 (32-bit)      | Windows XP Professional           | Intel x86        |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 11 (64-bit)      | Windows 2003 Server               | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 11 (64-bit)      | Windows 2003 Server               | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 11 (64-bit)      | Windows Vista Business            | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 11 (64-bit)      | Windows Server 2008 R2 Standard   | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 11 (64-bit)      | Windows 7 Enterprise              | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 10 XE (32-bit)   | Linux: Ubuntu 9.04                | Intel x86        |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 10 (64-bit)      | Linux: Debian sid                 | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 11 (64-bit)      | Linux: Debian sid                 | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 11 (64-bit)      | Linux: Debian sid                 | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 10 (64-bit)      | Linux: CentOS 5.1                 | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+
| 32-bit          | Oracle 9 (64-bit)       | Solaris: SunOS 5.10               | UltraSPARC III   |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 9 (64-bit)       | Solaris: SunOS 5.10               | UltraSPARC III   |
+-----------------+-------------------------+-----------------------------------+------------------+
| 64-bit          | Oracle 10 (64-bit)      | Mac OS X 10.6.1                   | Intel x86-64     |
+-----------------+-------------------------+-----------------------------------+------------------+

Installation Prerequisities
---------------------------

All Systems
~~~~~~~~~~~

-  The value of the ``open_cursors`` parameter of the Oracle database
   server should be increased to 1000.
-  The ``extproc`` listener must be run in Oracle. The example of the
   ``listener.ora`` configuration file is provided below.
-  Note the ``EXTPROC_DLLS=ANY`` setting: It makes Oracle tolerant to
   the location of external libraries (including the Bingo library).
   However, this setting is not required when you install the Bingo
   library in the Oracle system directory (default).

Windows
~~~~~~~

The configuration is the same for all 32-bit and 64-bit Windows
distributions.

::

    SID_LIST_LISTENER =
      (SID_LIST =
        (SID_DESC =
          (PROGRAM = extproc)
          (SID_NAME = PLSExtProc)
          (GLOBAL_DBNAME = orcl)
          (ORACLE_HOME = C:\oracle\product\10.2.0\db_1)
          (ENVS="EXTPROC_DLLS=ANY")
        )
      )

Linux (32-bit or 64-bit) or Solaris
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    SID_LIST_LISTENER =
      (SID_LIST =
        (SID_DESC =
          (PROGRAM = extproc)
          (SID_NAME = PLSExtProc)
          (GLOBAL_DBNAME = orcl)
          (ORACLE_HOME = /home/oracle/product/10.2.0/db_1)
          (ENVS = "EXTPROC_DLLS=ANY")
        )
      )

64-bit Linux or Solaris, with 32-bit extproc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have 64-bit Oracle but want to keep the 32-bit ``extproc`` for
some reason, you can still use the 32-bit version of Bingo.

::

    SID_LIST_LISTENER =
      (SID_LIST =
        (SID_DESC =
          (SID_NAME = PLSExtProc)
          (GLOBAL_DBNAME = orcl)
          (ORACLE_HOME = /oracle/11.1)
          (PROGRAM = extproc32)
          (ENVS = "EXTPROC_DLLS=ANY,LD_LIBRARY_PATH=/oracle/11.1/lib32")
        )
      )

Mac OS X (64-bit)
~~~~~~~~~~~~~~~~~

::

    SID_LIST_LISTENER =
      (SID_LIST =
        (SID_DESC =
          (PROGRAM = extproc)
          (SID_NAME = PLSExtProc)
          (GLOBAL_DBNAME = orcl)
          (ORACLE_HOME = /Users/oracle/product/10.2.0/db_1)
          (ENVS = "EXTPROC_DLLS=ANY")
        )
      )

In addition to the kernel parameters described in `Oracle® Database
Installation Guide 10g Release 2 (10.2) for Apple Mac OS
X <http://download.oracle.com/docs/cd/B19306_01/install.102/b25286/pre_install.htm#BABCHAED>`__
you should change ``kern.sysv.shmseg`` from its default value, which is
too low. Add the following line to ``/etc/sysctl.conf`` file:

::

    kern.sysv.shmseg=256

Installation Procedure
----------------------

All Systems
~~~~~~~~~~~

**Note:** The installation script creates a new user (usually
``bingo``), with the default tablespace ``bingo`` and the temporary
tablespace ``bingo_temp``. If you specify another username for Bingo
(for example, ``bingo1``), the tablespace names will be ``bingo1`` and
``bingo1_temp``. The datafiles, located at the default Oracle datafile
directory, will be 5 megabytes in size and will auto-extend by 5
megabytes without size limit. If you need to change the tablespace
names, datafile locations, or size conditions, please edit the
``system/bingo_init.sql`` file manually before running the installation
script. If you are installing on Oracle 9, edit the
``system/bingo_init_9.sql`` file instead.

**Note:** You cannot install Bingo on top of the existing installation.
You have to drop the cartridge user (usually ``bingo``) of the existing
installation (see the
`Uninstalling <installation-manual-oracle.html#uninstalling-the-cartridge>`__
section below). Or you can install a new version to another user.

Windows
~~~~~~~

Log in as Administrator if you are installing Bingo in the Oracle
library directory (this is the default behavior). If you do not have
administrator rights, please override the default setting by ``-libdir``
flag. In the latter case, you should have the ``EXTPROC_DLLS`` option
set up properly.

Run the ``bingo-oracle-install.bat`` file located in the Bingo
installation file set. The help message from the script follows:

::

    Usage: bingo-oracle-install.bat [parameters]
    Parameters:
      -?, -help
        Print this help message
      -libdir path
        Target directory to install bingo-oracle.dll (defaut %ORACLE_HOME%\bin).
        If the directory does not exist, it will be created.
      -dbaname name
        Database administrator login (default "system").
      -dbapass password
        Database administrator password (no default).
        If the password is not specified, you will have to enter it later.
      -instance instance
        Database instance (default "orcl").
        You can specify full address like "server:1521/instance" as well.
      -bingoname name
        Name of cartridge pseudo-user (default "bingo").
      -bingopass password
        Password of the pseudo-user (default "bingo").
      -y
        Do not ask for confirmation.

Linux, Solaris, or Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log in as ``oracle`` user if you are installing Bingo in the Oracle
library directory (this is the default behavior). If you do not have
rights to log in as ``oracle``, please override the default setting by
``-libdir`` flag. In the latter case, you should have the
``EXTPROC_DLLS`` option set up properly.

Run the ``bingo-oracle-install.sh`` file located in the ``sql`` folder
of the Bingo installation file set. The help message from the script is
the following:

::

    Usage: bingo-oracle-install.sh [parameters]
    Parameters:
      -?, -help
        Print this help message
      -libdir path
        Target directory to install libbingo.so (defaut $ORACLE_HOME/lib).
        If the directory does not exist, it will be created.
      -dbaname name
        Database administrator login (default "system").
      -dbapass password
        Database administrator password (no default).
        If the password is not specified, you will have to enter it later.
      -instance instance
        Database instance (default "orcl").
        You can specify full address like "server:1521/instance" as well.
      -bingoname name
        Name of cartridge pseudo-user (default "bingo").
      -bingopass password
        Password of the pseudo-user (default "bingo").
      -y
        Do not ask for confirmation.

Examples
~~~~~~~~

For the most simple installation, the defaults are taken:
``$ORACLE_HOME/lib`` directory for binary, 'orcl' instance, 'system' DBA
account, and 'bingo/bingo' pseudo-user.

::

    bingo-oracle-install.sh

If you do not have access to the ``$ORACLE_HOME/lib`` directory, you can
install the Bingo binary in your home directory:

::

    bingo-oracle-install.sh -libdir /home/myself

When you install on Oracle XE, the instance is usually called ``xe``:

::

    bingo-oracle-install.sh -instance xe

You can install Bingo to an Oracle user other than 'bingo':

::

    bingo-oracle-install.sh -bingoname bingo2

To run in the non-interactive mode, you must specify '-y' and
'-dbapass':

::

    bingo-oracle-install.sh -dbaname system -dbapass admin -y

In Windows, you often do not have the ``%ORACLE_HOME%`` setting, and so
you have to specify the library directory manually:

::

    bingo-oracle-install.bat -libdir C:\oracle\product\11.1.0\bin -dbaname system -dbapass admin -y

Checking the Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

If the installation has succeeded, the following report will be printed
at the end:

::

    --------- REPORT ---------
    Tables:             7
    Views:              0
    Packages:           4
    Procedures:         45
    Functions:          69
    Sequences:          1
    --------------------------

    DB check executed.

To check that the shared library file is loaded properly by Oracle, you
can try this simple query:

::

    SELECT Bingo.GetVersion from DUAL;

Uninstalling the Cartridge
--------------------------

To uninstall the cartridge, you must:

#. Remove all special domain indices that have been created by users.
   Removing the cartridge user without removing the indices will not
   harm your system, but the domain indices will be disabled.
#. Remove the cartridge user (usually ``bingo``) from the database: DROP
   USER BINGO CASCADE;
#. Remove the cartridge tablespaces (usually ``BINGO`` and
   ``BINGO_TEMP``). This step is necessary if you want to recover the
   disk space previously occupied by the indices. You can skip this step
   if you are willing to reinstall Bingo afterwards.

