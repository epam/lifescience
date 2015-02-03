Comparison Report
=================

Our evaluation framework compares various versions of `Imago
OCR <index.html>`__ application with other applications for molecule
image optical character recognition. For each image the testing
framework measures execution time and similarity score with a reference
molecule file in Molfile format. `Indigo <../indigo/index.html>`__
toolkit is used to measure molecule similarity. Because different
application produces output differently testing framework applies the
following rules to standardize molecules:

-  Hydrogens are folded.
-  If the output contains multiple molecules in SDF format then all of
   them are merged into a single molecule with several disconnected
   fragments.
-  Both aromatized and dearomatized structures are compared and best
   score is selected.

Diverse Dataset Report
----------------------

Report file is avialable at `the separate page <TODO:imago-report>`__.
You can also download all the report files (with script files) from the
`Downloads page <../download/imago.html>`__.

|Report|

This report contains 5 datasets of 500 molecule images each from
different sources:

-  `Image2Structure <TODO:imago-report#g1>`__
   (`description <TODO:imago-report>`__)
   A random subset of 500 images from Image2Structure task at `TREC
   Chem 2011
   conference <http://trec.nist.gov/pubs/trec20/t20.proceedings.html>`__.

-  `Mobile Camera <TODO:imago-report#g2>`__
   (`description <TODO:imago-report>`__)
   Photos from a mobile phone of 500 PubChem molecules rendered using
   Indigo toolkit.

-  `Rendered <TODO:imago-report#g3>`__
   (`description <TODO:imago-report>`__)
   500 PubChem molecules rendered using Indigo toolkit.

-  `USPTO <TODO:imago-report#g4>`__
   (`description <TODO:imago-report>`__)
   A random subset of 500 structures from a validation set avialable
   at `OSRA website <http://cactus.nci.nih.gov/osra/>`__.

-  `chem-infty <TODO:imago-report#g5>`__
   (`description <TODO:imago-report>`__)
   A random subset of 500 structure from `Chem-Infty
   Dataset <http://www.iapr-tc11.org/mediawiki/index.php/Chem-Infty_Dataset:_A_ground-truthed_dataset_of_Chemical_Structure_Images>`__.

If you can suggest other test sets or other publicly available solutions
we would be happy to include them too in the report.

.. |Report| image:: ../assets/imago/imago-report-small-1.png
   :target: TODO:imago-report
