Imago Console Application
=========================

Distribution
------------

The utility is called ``imago_console.exe`` in Windows distribution or
simply ``imago_console`` in Linux and Mac OS X distributions. Binaries
are offered in 32-bit and 64-bit versions.

Command-line parameters reference
---------------------------------

The ``imago_console`` tool has an additional command line switches and
possibilities in comparison to `OCR Visual Tool <imago-gui.html>`__.

The help message from the program is the following:

::

    Usage: imago_console.exe [option]* [batches] [mode] [image_path] [-o output_file]

     MODE SWITCHES:
      image_path: full path to image to recognize (may be omitted if other switch is specified)
      -o output_file: save single recognition result to the specified file
      -characters: extracts only characters from image(s) and store in ./characters/
      -learn dir_name: process machine learning for specified collection
      -compare molfile1 molfile2: calculate similarity between molfiles
        -retcode: returns similarity 0..100 in ERRORLEVEL
      -test dir_name: calculate similarity score on specified test collection

     OPTION SWITCHES:
      -config cfg_file: use specified configuration cluster file
      -log: enables debug log output to ./log.html
      -logvfs: stores log in single encoded file ./log_vfs.txt
      -noexp: do not expand chemical abbreviations
      -pr: use probabilistic separator (experimental)
      -tl time_in_ms: timelimit per single image process (default is 10000)
      -similarity tool [-sparam additional_parameters]: override the default comparison method
      -pass: don't process images, only print their filenames
      -override config_string: override config by applying specified string

     BATCHES:
      -dir dir_name: process every image from dir dir_name
        -rec: process directory recursively
        -images: skip non-supported files from directory

     SHORTCUTS:
      -learnd dir_name: -learn -dir dir_name -images

The simplest use case is ``imago_console image.png`` which recognizes
image and saves output to ``molecule.mol``.

-  You can easily process multiple images from same directory by
   specifying the **-dir** switch.
-  The **-rec** switch allows recursively process and the **-images**
   switch skips all non-image data from directories. For example:
   ``imago_console -dir C:\test -rec -images``
-  The **-config** switch allows to select configuration cluster
   manually, for instance
   ``imago_console -config indigo_render.txt image_rendered_by_indigo.png``
-  The **-log** switch enables debug logging to ``log.html`` file (the
   required images will be stored in ``htmlimgs`` dir). The **-logvfs**
   stores all log data in single file ``logvfs.txt``
-  The **-compare** switch allows to compare two molfiles and print the
   similarity value. If the **-retcode** switch specified also the
   result will be returned as error level variable (can be obtained
   under Windows by ``echo %ERRORLEVEL%`` command)
-  The **-learn** switch performs the machine learning process. Before
   you start you need to create the test collection: folder (subfolders
   are allowed too) where the original images and corresponding
   recognized structures are placed (for instance: ``image1.png``,
   ``image1.mol``, ``image2.jpg``, ``image2.mol``, …). The program will
   try to generate the configuration cluster which gives the better
   recognition rate on the specified test collection. If so, the cluster
   will be saved in current folder as ``config_NNNOK_MMM.txt``. You can
   use this config further by specifying the
   ``-config config_NNNOK_MMM.txt`` switch.
-  The **-test** switch allows quickly check recognition result on a
   specified test collection (organized the same way as for machine
   learning) and returns count of correctly recognized images and
   average time. Can be combined with **-retcode** switch to return
   average recognition rate as process return code.
-  The **-tl** switch can be used for limiting the recognition time per
   image. If the recognition process takes more time than specified -
   the process will be stopped.
-  The **-override** switch can be used for setting config parameters.
   For example, ``-override "prefilterCV.MinGoodPixelsCount=30;"`` drops
   all connected segments with pixel count less than 30.
-  The **-o** switch sets the output filename for single image
   recognition.

