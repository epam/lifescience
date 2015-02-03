Java Bindings
=============

Distribution
------------

The ``imago.jar`` file containing ``com.gga.imago.Imago`` wrapper class
is included in the distribution package for each platform. It contains
all the required binary modules for Windows, Linux and Mac OS X,
depending on the selected platform. Imago-Java Universal package
contains binaries for all the support platforms.

Depending on the OS and architecture, proper binaries are loaded
automatically.

Workflow
--------

The ``Imago`` class object represents a library instance. All operations
are represented by methods of this object. Several library instances may
be created within one thread to act simultaneously and independently.
However, each instance requires a certain amount of memory, and thus it
is recommended to have as few instances as possible.

The procedure for rendering workflow is the following:

#. Create a library instance.
#. Load a PNG image from the file or in-memory buffer.
#. Set the optional parameters.
#. Set the logging mode if required.
#. Call ``recognize()``.
#. Get the resulting molfile via ``getResult()``.

Any method of the ``Imago`` class can throw an ``Exception`` if
something went wrong. The ``recognize()`` method can throw an
``Imago.NoResultException`` in the event that the image has failed to be
recognized as a molecule.

Imago Class Public Methods
--------------------------

Constructor
~~~~~~~~~~~

::

    Imago ();

Instances are independent and are safe to be used in parallel.

Loading the Image
~~~~~~~~~~~~~~~~~

::

    void loadImage (byte[] buf);

Loads a supported image from the memory buffer.

::

    void loadImage (String filename);

Loads a supported type image from file.

Setting the Options
~~~~~~~~~~~~~~~~~~~

::

    void setFilter (String filter_name);

    void setConfig (String config_name);

Sets one of the pre-loaded configuration parameter sets.

Performing the Recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    void recognize ();

Getting the Result
~~~~~~~~~~~~~~~~~~

::

    string getResult ();

Returns a string with the recognized molecule in Molfile format.

Example
-------

::

       com.gga.imago.Imago imago = new com.gga.imago.Imago();   
       imago.setFilter("prefilter_basic");  // optional
       imago.setConfig("config_indigo_render.txt"); // optional
       imago.loadImage("my-image.png");
       imago.recognize();
       System.out.println(imago.getResult());

