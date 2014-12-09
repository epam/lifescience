R-Group Deconvolution Examples
==============================

Example 1
---------

The input molecules are:

+------------+------------+
| |image6|   | |image7|   |
+------------+------------+
| |image8|   | |image9|   |
+------------+------------+
| |image10|  | |image11|  |
+------------+------------+

The detected scaffold is:

+-------------+
| |image13|   |
+-------------+

The R-Group deconvolution is:

+------------------------+-------------+
| Highlighted Scaffold   | R-Groups    |
+========================+=============+
| |image26|              | |image27|   |
+------------------------+-------------+
| |image28|              | |image29|   |
+------------------------+-------------+
| |image30|              | |image31|   |
+------------------------+-------------+
| |image32|              | |image33|   |
+------------------------+-------------+
| |image34|              | |image35|   |
+------------------------+-------------+
| |image36|              | |image37|   |
+------------------------+-------------+

Example 2
---------

The input molecules are:

+-------------+-------------+
| |image42|   | |image43|   |
+-------------+-------------+
| |image44|   | |image45|   |
+-------------+-------------+

The detected scaffold is:

+-------------+
| |image47|   |
+-------------+

The R-Group deconvolution is:

+------------------------+-------------+
| Highlighted Scaffold   | R-Groups    |
+========================+=============+
| |image56|              | |image57|   |
+------------------------+-------------+
| |image58|              | |image59|   |
+------------------------+-------------+
| |image60|              | |image61|   |
+------------------------+-------------+
| |image62|              | |image63|   |
+------------------------+-------------+

Example 3
---------

This example was run with ``-na`` option, and so the scaffolds are not
aromatized.

The input molecules are:

+-------------+
| |image66|   |
+-------------+
| |image67|   |
+-------------+

All possible scaffolds are:

+-------------+-------------+
| |image74|   | |image75|   |
+-------------+-------------+
| |image76|   | |image77|   |
+-------------+-------------+
| |image78|   | |image79|   |
+-------------+-------------+

The selected scaffold is:

+-------------+
| |image81|   |
+-------------+

The R-Group deconvolution is:

+------------------------+-------------+
| Highlighted Scaffold   | R-Groups    |
+========================+=============+
| |image86|              | |image87|   |
+------------------------+-------------+
| |image88|              | |image89|   |
+------------------------+-------------+

Example 4
---------

The input molecules are:

+-------------+-------------+
| |image92|   | |image93|   |
+-------------+-------------+

Aromatic scaffold
~~~~~~~~~~~~~~~~~

The detected scaffold is:

+-------------+
| |image95|   |
+-------------+

The molecules are identical (up to aromatization), so the R-Group
deconvolution is trivial.

Nonaromatic scaffold
~~~~~~~~~~~~~~~~~~~~

With ``-na`` option, the following scaffolds were found:

+-------------+-------------+
| |image98|   | |image99|   |
+-------------+-------------+

The first one was selected for R-Group deconvolution:

+--------------+
| |image101|   |
+--------------+

The R-Group deconvolution is:

+------------------------+--------------+
| Highlighted Scaffold   | R-Groups     |
+========================+==============+
| |image106|             | |image107|   |
+------------------------+--------------+
| |image108|             | |image109|   |
+------------------------+--------------+

.. |image0| image:: ../../assets/indigo/concepts/deco_01_1m.svg
.. |image1| image:: ../../assets/indigo/concepts/deco_01_2m.svg
.. |image2| image:: ../../assets/indigo/concepts/deco_01_3m.svg
.. |image3| image:: ../../assets/indigo/concepts/deco_01_4m.svg
.. |image4| image:: ../../assets/indigo/concepts/deco_01_5m.svg
.. |image5| image:: ../../assets/indigo/concepts/deco_01_6m.svg
.. |image6| image:: ../../assets/indigo/concepts/deco_01_1m.svg
.. |image7| image:: ../../assets/indigo/concepts/deco_01_2m.svg
.. |image8| image:: ../../assets/indigo/concepts/deco_01_3m.svg
.. |image9| image:: ../../assets/indigo/concepts/deco_01_4m.svg
.. |image10| image:: ../../assets/indigo/concepts/deco_01_5m.svg
.. |image11| image:: ../../assets/indigo/concepts/deco_01_6m.svg
.. |image12| image:: ../../assets/indigo/concepts/deco_01_scaf.svg
.. |image13| image:: ../../assets/indigo/concepts/deco_01_scaf.svg
.. |image14| image:: ../../assets/indigo/concepts/deco_01_1hi.svg
.. |image15| image:: ../../assets/indigo/concepts/deco_01_1r.svg
.. |image16| image:: ../../assets/indigo/concepts/deco_01_2hi.svg
.. |image17| image:: ../../assets/indigo/concepts/deco_01_2r.svg
.. |image18| image:: ../../assets/indigo/concepts/deco_01_3hi.svg
.. |image19| image:: ../../assets/indigo/concepts/deco_01_3r.svg
.. |image20| image:: ../../assets/indigo/concepts/deco_01_4hi.svg
.. |image21| image:: ../../assets/indigo/concepts/deco_01_4r.svg
.. |image22| image:: ../../assets/indigo/concepts/deco_01_5hi.svg
.. |image23| image:: ../../assets/indigo/concepts/deco_01_5r.svg
.. |image24| image:: ../../assets/indigo/concepts/deco_01_6hi.svg
.. |image25| image:: ../../assets/indigo/concepts/deco_01_6r.svg
.. |image26| image:: ../../assets/indigo/concepts/deco_01_1hi.svg
.. |image27| image:: ../../assets/indigo/concepts/deco_01_1r.svg
.. |image28| image:: ../../assets/indigo/concepts/deco_01_2hi.svg
.. |image29| image:: ../../assets/indigo/concepts/deco_01_2r.svg
.. |image30| image:: ../../assets/indigo/concepts/deco_01_3hi.svg
.. |image31| image:: ../../assets/indigo/concepts/deco_01_3r.svg
.. |image32| image:: ../../assets/indigo/concepts/deco_01_4hi.svg
.. |image33| image:: ../../assets/indigo/concepts/deco_01_4r.svg
.. |image34| image:: ../../assets/indigo/concepts/deco_01_5hi.svg
.. |image35| image:: ../../assets/indigo/concepts/deco_01_5r.svg
.. |image36| image:: ../../assets/indigo/concepts/deco_01_6hi.svg
.. |image37| image:: ../../assets/indigo/concepts/deco_01_6r.svg
.. |image38| image:: ../../assets/indigo/concepts/deco_02_1m.svg
.. |image39| image:: ../../assets/indigo/concepts/deco_02_2m.svg
.. |image40| image:: ../../assets/indigo/concepts/deco_02_3m.svg
.. |image41| image:: ../../assets/indigo/concepts/deco_02_4m.svg
.. |image42| image:: ../../assets/indigo/concepts/deco_02_1m.svg
.. |image43| image:: ../../assets/indigo/concepts/deco_02_2m.svg
.. |image44| image:: ../../assets/indigo/concepts/deco_02_3m.svg
.. |image45| image:: ../../assets/indigo/concepts/deco_02_4m.svg
.. |image46| image:: ../../assets/indigo/concepts/deco_02_scaf.svg
.. |image47| image:: ../../assets/indigo/concepts/deco_02_scaf.svg
.. |image48| image:: ../../assets/indigo/concepts/deco_02_1hi.svg
.. |image49| image:: ../../assets/indigo/concepts/deco_02_1r.svg
.. |image50| image:: ../../assets/indigo/concepts/deco_02_2hi.svg
.. |image51| image:: ../../assets/indigo/concepts/deco_02_2r.svg
.. |image52| image:: ../../assets/indigo/concepts/deco_02_3hi.svg
.. |image53| image:: ../../assets/indigo/concepts/deco_02_3r.svg
.. |image54| image:: ../../assets/indigo/concepts/deco_02_4hi.svg
.. |image55| image:: ../../assets/indigo/concepts/deco_02_4r.svg
.. |image56| image:: ../../assets/indigo/concepts/deco_02_1hi.svg
.. |image57| image:: ../../assets/indigo/concepts/deco_02_1r.svg
.. |image58| image:: ../../assets/indigo/concepts/deco_02_2hi.svg
.. |image59| image:: ../../assets/indigo/concepts/deco_02_2r.svg
.. |image60| image:: ../../assets/indigo/concepts/deco_02_3hi.svg
.. |image61| image:: ../../assets/indigo/concepts/deco_02_3r.svg
.. |image62| image:: ../../assets/indigo/concepts/deco_02_4hi.svg
.. |image63| image:: ../../assets/indigo/concepts/deco_02_4r.svg
.. |image64| image:: ../../assets/indigo/concepts/deco_03_1m.svg
.. |image65| image:: ../../assets/indigo/concepts/deco_03_2m.svg
.. |image66| image:: ../../assets/indigo/concepts/deco_03_1m.svg
.. |image67| image:: ../../assets/indigo/concepts/deco_03_2m.svg
.. |image68| image:: ../../assets/indigo/concepts/deco_03_scaf1.svg
.. |image69| image:: ../../assets/indigo/concepts/deco_03_scaf2.svg
.. |image70| image:: ../../assets/indigo/concepts/deco_03_scaf3.svg
.. |image71| image:: ../../assets/indigo/concepts/deco_03_scaf4.svg
.. |image72| image:: ../../assets/indigo/concepts/deco_03_scaf5.svg
.. |image73| image:: ../../assets/indigo/concepts/deco_03_scaf6.svg
.. |image74| image:: ../../assets/indigo/concepts/deco_03_scaf1.svg
.. |image75| image:: ../../assets/indigo/concepts/deco_03_scaf2.svg
.. |image76| image:: ../../assets/indigo/concepts/deco_03_scaf3.svg
.. |image77| image:: ../../assets/indigo/concepts/deco_03_scaf4.svg
.. |image78| image:: ../../assets/indigo/concepts/deco_03_scaf5.svg
.. |image79| image:: ../../assets/indigo/concepts/deco_03_scaf6.svg
.. |image80| image:: ../../assets/indigo/concepts/deco_03_scaf.svg
.. |image81| image:: ../../assets/indigo/concepts/deco_03_scaf.svg
.. |image82| image:: ../../assets/indigo/concepts/deco_03_1hi.svg
.. |image83| image:: ../../assets/indigo/concepts/deco_03_1r.svg
.. |image84| image:: ../../assets/indigo/concepts/deco_03_2hi.svg
.. |image85| image:: ../../assets/indigo/concepts/deco_03_2r.svg
.. |image86| image:: ../../assets/indigo/concepts/deco_03_1hi.svg
.. |image87| image:: ../../assets/indigo/concepts/deco_03_1r.svg
.. |image88| image:: ../../assets/indigo/concepts/deco_03_2hi.svg
.. |image89| image:: ../../assets/indigo/concepts/deco_03_2r.svg
.. |image90| image:: ../../assets/indigo/concepts/deco_04_1m.svg
.. |image91| image:: ../../assets/indigo/concepts/deco_04_2m.svg
.. |image92| image:: ../../assets/indigo/concepts/deco_04_1m.svg
.. |image93| image:: ../../assets/indigo/concepts/deco_04_2m.svg
.. |image94| image:: ../../assets/indigo/concepts/deco_05_scaf.svg
.. |image95| image:: ../../assets/indigo/concepts/deco_05_scaf.svg
.. |image96| image:: ../../assets/indigo/concepts/deco_04_scaf1.svg
.. |image97| image:: ../../assets/indigo/concepts/deco_04_scaf2.svg
.. |image98| image:: ../../assets/indigo/concepts/deco_04_scaf1.svg
.. |image99| image:: ../../assets/indigo/concepts/deco_04_scaf2.svg
.. |image100| image:: ../../assets/indigo/concepts/deco_04_scaf.svg
.. |image101| image:: ../../assets/indigo/concepts/deco_04_scaf.svg
.. |image102| image:: ../../assets/indigo/concepts/deco_04_1hi.svg
.. |image103| image:: ../../assets/indigo/concepts/deco_04_1r.svg
.. |image104| image:: ../../assets/indigo/concepts/deco_04_2hi.svg
.. |image105| image:: ../../assets/indigo/concepts/deco_04_2r.svg
.. |image106| image:: ../../assets/indigo/concepts/deco_04_1hi.svg
.. |image107| image:: ../../assets/indigo/concepts/deco_04_1r.svg
.. |image108| image:: ../../assets/indigo/concepts/deco_04_2hi.svg
.. |image109| image:: ../../assets/indigo/concepts/deco_04_2r.svg
