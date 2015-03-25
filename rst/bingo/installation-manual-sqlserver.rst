Installation Manual: SQL Server
===============================

System Requirements
-------------------

Operating Systems
~~~~~~~~~~~~~~~~~

-  Windows XP/Vista/7 (32-bit and 64-bit)
-  Windows 2003/2008 Server (32-bit and 64-bit)

Database Servers
~~~~~~~~~~~~~~~~

-  Microsoft SQL Server 2005
-  Microsoft SQL Server 2008

Tested Configurations
~~~~~~~~~~~~~~~~~~~~~

Bingo has been successfully tested on the following configurations:

+-------------------------------------+-----------------------------------+
| Database                            | Operating System                  |
+=====================================+===================================+
| SQL Server 2005 Express (32-bit)    | Windows XP Professional           |
+-------------------------------------+-----------------------------------+
| SQL Server 2005 Standard (32-bit)   | Windows 2003 Server               |
+-------------------------------------+-----------------------------------+
| SQL Server 2008 Express (32-bit)    | Windows Vista Home Premium        |
+-------------------------------------+-----------------------------------+
| SQL Server 2008 Standard (32-bit)   | Windows XP Professional           |
+-------------------------------------+-----------------------------------+
| SQL Server 2008 Standard (64-bit)   | Windows Server 2008 R2 Standard   |
+-------------------------------------+-----------------------------------+
| SQL Server 2008 Standard (64-bit)   | Windows 7 Enterprise              |
+-------------------------------------+-----------------------------------+

Setting Up a Server
-------------------

For indexing, Bingo uses @@SERVERNAME constant for establishing internal
connections and it should return the correct server name. If multiple
SQL Server instances are installed, then @@SERVERNAME should contain the
service name as well. To get the server name, you can execute the
following code:

::

    select @@SERVERNAME

If it returns an invalid name, you should execute the following
commands:

::

    sp_dropserver <invalid server name returned by @@SERVERNAME or from executing sp_helpserver procedure>
    sp_addserver <valid server name>, 'local'

'SQL Server Browser' service should be started for accepting connections
that are created during the Bingo indexing operation. If this service is
not started, then you might get the error during index creation
indicating that the connection cannot be established.

If you are using Bingo with large tables or a significant number of
tables, then you have to configure the memory parameters in Microsoft
SQL Server. The configuration depends on the 32-bit or 64-bit computer
architecture that you are using.

32-bit
~~~~~~

By default MS SQL Server provides the possibility to allocate only 256Mb
in all CLR code. If the memory limit is reached, then you will get the
following exception:

::

    .NET Framework execution was aborted by escalation policy because of out of memory.

To adjust the memory limit for CLR you have to specify the -g switch in
the SQL Server Configuration Manager. For example, to set the memory
limit for the CLR code to 512Mb, you need to add the ``-g512`` switch to
the Start-up Parameters in the properties for your SQL Server instance in
the SQL Server Configuration Manager.

**Note:** In the 32-bit architecture, the total allocatable memory is
limited to 2GB unless you add the ``/3gb`` switch to boot.ini file or
specify “Use AWE to allocate memory” in the SQL Server settings. So
increasing the memory limit for CLR, you reduce the memory limit for the
internal SQL Server cache.

64-bit
~~~~~~

By default, MS SQL Server tries to take all of the memory available in
the system. Sometimes (mostly on large databases), when the CLR engine
underlying the SQL Server tries to allocate some memory for Bingo, you
will get the same exception:

::

    .NET Framework execution was aborted by escalation policy because of out of memory.

And the following message will be logged to the system log:

::

    AppDomain <name> is marked for unload due to memory pressure.

To restrict the amount of memory that MS SQL Server can take (thus
leaving more memory for Bingo), we recommend setting the “Maximum
server memory” in the “Server Properties>Memory” tab in the SQL Server
Management Studio to some value less that than the actual size of your
memory minus 1 GB.

Installation Procedure
----------------------

Log in as Administrator. Run the ``bingo-sqlserver-install.bat`` file
located in the Bingo installation file set. The help message from the
script is the following:

::

    Usage: bingo-sqlserver-install.bat [parameters]
    Parameters:
      -?, -help
        Print this help message
      -server name
        SQL Server name (default is local SQL Server)
      -database database (obligatory)
        Database to install on.
      -dbaname name
        Database administrator login (default is current user).
      -dbapass password
        Database administrator password.
        If the password is not specified, you will have to enter it later.
      -bingoname name
        Name of cartridge pseudo-user (default "bingo").
      -bingopass password
        Password of the pseudo-user (default "bingo").
      -y
        Do not ask for confirmation.

**Note:** The installer automatically issues the
``ALTER DATABASE $(database) SET ENABLE_BROKER`` statement if the
``ENABLE_BROKER`` option is not activated on your database. As this
involves an exclusive database lock, we recommend that, in this case you
restart the database prior to the installation.

Examples
~~~~~~~~

For the simplest installation, the defaults are taken, including
``C:\bingo`` directory for binaries. You have to specify only the
``-database`` flag with the name of your database:

::

    bingo-sqlserver-install.bat -database mydb

If you use an SQL Server user account for the DBA user (normally 'sa'),
you have to specify it with the ``-dbaname`` option:

::

    bingo-sqlserver-install.bat -database mydb -dbaname sa

To run in the non-interactive mode, you must specify ``-y``

::

    bingo-sqlserver-install.bat -database mydb -y

(and also ``-dbass`` when you specify ``-dbaname``)

::

    bingo-sqlserver-install.bat -database mydb -dbaname sa -dbapass pwd123 -y

Uninstalling the Cartridge
--------------------------

To uninstall the cartridge, you must:

#. Remove all special indices created by users, by calling the
   ``bingo.DropIndex()`` function
#. Run ``bingo-sqlserver-uninstall.bat`` with the same ``-dbaname`` ,
   ``-bingoname``, and ``-database`` parameters that you passed to the
   installer.

The help message from the uninstall script is the following:

::

    Usage: bingo-sqlserver-uninstall.bat [parameters]
    Parameters:
      -?, -help
        Print this help message
      -database database (obligatory)
        Database to remove Bingo from.
      -dbaname name
        Database administrator login (default is current user).
      -dbapass password
        Database administrator password.
        If the password is not specified, you will have to enter it later.
      -bingoname name
        Name of cartridge pseudo-user (default "bingo").
      -y
        Do not ask for confirmation.

