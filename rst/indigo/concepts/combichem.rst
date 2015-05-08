Reaction Enumeration Examples
=============================

Peptide Bond Formation
~~~~~~~~~~~~~~~~~~~~~~

+------------+
| Reaction   |
+============+
| |image1|   |
+------------+

Monomers were divided into two groups: acids and amines.

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1
   :widths: 24 24 24 24

   * - 
     - A
     - B
     - C
   * - Acids 
     - |image2| 
     - |image3| 
     - |image4| 
     
.. list-table:: 
   :header-rows: 1
   :stub-columns: 1
   :widths: 24 24 24 24

   * - 
     - X
     - Y
     - X
   * - Amines 
     - |image5| 
     - |image6| 
     - |image7| 

Without the specification any additional options, Legio generates six
products. Legio tries to perform specified reactions for each monomer
from both the first group (acids) and the second group (amines):

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1
   :widths: 24 24 24 24

   * - 
     - A
     - B
     - C
   * - X
     - |image8| 
     - |image9| 
     - |image10| 
   * - Y
     - |image11| 
     - |image12| 
     - |image13| 
   * - Z
     - |image14| 
     - |image15| 
     - |image16| 

You can see that all the stereochemistry configurations are preserved
during the reaction.

When the “all reactions” mode is specified, products can take place in
another reaction too, but only with original monomers or their products.
So with such options, three additional products are generated:

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1
   :widths: 24 24

   * - 
     - 
   * - B + X + X: 
     - |image17| 
   * - B + Y + Y: 
     - |image18| 
   * - B + Z + Z: 
     - |image19| 

When the “one tube” mode is specified, any monomers and their products
can make another reaction. With this mode, it is imagined that all
monomers are in one tube. Another three products are generated:

.. list-table:: 
   :header-rows: 1
   :stub-columns: 1
   :widths: 24 24

   * - 
     - 
   * - B + X + Y: 
     - |image20| 
   * - B + X + Z: 
     - |image21| 
   * - B + Y + Z: 
     - |image22| 

Reactants Matching
~~~~~~~~~~~~~~~~~~

When the reaction does not have any R-group atoms, matching of reactants
to monomers is done according to substructure search rules.

+-------------+
| Reaction    |
+=============+
| |image24|   |
+-------------+

**Monomers:**

+-------------+-------------+
| |image27|   | |image28|   |
+-------------+-------------+

**Products:**

+-------------+-------------+
| |image31|   | |image32|   |
+-------------+-------------+

Multistep Reactions
~~~~~~~~~~~~~~~~~~~

Legio can enumerate products appearing in the multistep reactions when
existing monomers or produced products can take place in the reaction.

+-------------+
| Reaction    |
+=============+
| |image34|   |
+-------------+

**Monomers:**

+-------------+-------------+
| |image37|   | |image38|   |
+-------------+-------------+

**Products:**

+-------------+-------------+
| |image41|   | |image42|   |
+-------------+-------------+

Generation Modes
~~~~~~~~~~~~~~~~

Legio supports two generation modes for multistep reactions. In the
"grid mode", only one monomer from each group can react. This can be
represented as a matrix where the columns correspond to the first group
and the rows correspond to the second group. The reaction is performed
in each cell. In the "one tube" mode, all of the monomers are in the
same tube.

+-------------+
| Reaction    |
+=============+
| |image44|   |
+-------------+

**Monomers:**

+-------------+-------------+
| A           | B           |
+=============+=============+
| |image47|   | |image48|   |
+-------------+-------------+

+-------------+
| X           |
+=============+
| |image50|   |
+-------------+

When the "grid mode" is on, each product can react with monomers from
the same cell and with other products, formed earlier in this cell. For
example:

+-------------+-------------+
| |image55|   | |image56|   |
+-------------+-------------+
| |image57|   | |image58|   |
+-------------+-------------+

When the "one tube" mode is active, all of the products and monomers are
contained in one tube and can react together. Legio generates the
following new products:

+-------------+-------------+
| |image61|   | |image62|   |
+-------------+-------------+

Intramolecular Interactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+
| Reaction    |
+=============+
| |image64|   |
+-------------+

+-------------+-------------+
| Monomer     | Product     |
+=============+=============+
| |image67|   | |image68|   |
+-------------+-------------+

Tetrahedral Stereochemistry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+
| Reaction    |
+=============+
| |image70|   |
+-------------+

+-------------+--------------+
| Monomers    | Products     |
+=============+==============+
| |image80|   | |image81|    |
+-------------+--------------+
| |image82|   | |image83|    |
+-------------+--------------+
| |image84|   | |image85|    |
+-------------+--------------+
| |image86|   | no product   |
+-------------+--------------+
| |image87|   | |image88|    |
+-------------+--------------+

Cis-trans stereochemistry
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+
| Reaction    |
+=============+
| |image90|   |
+-------------+

+-------------+-------------+
| Monomers    | Products    |
+=============+=============+
| |image97|   | |image98|   |
+-------------+-------------+
| |image99|   | |image100|  |
+-------------+-------------+
| |image101|  | |image102|  |
+-------------+-------------+

The third example shows that stereochemistry configuration modifications
are dependent.

Functional Groups with 2 Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+
| Reaction     |
+==============+
| |image104|   |
+--------------+

**Monomers:**

+--------------+--------------+
| |image107|   | |image108|   |
+--------------+--------------+

**Products:**

+--------------+
| |image112|   |
+--------------+
| |image113|   |
+--------------+
| |image114|   |
+--------------+

.. |image0| image:: ../../assets/indigo/concepts/legio_am_rxn.svg
.. |image1| image:: ../../assets/indigo/concepts/legio_am_rxn.svg
.. |image2| image:: ../../assets/indigo/concepts/legio_am_acids_1.svg
.. |image3| image:: ../../assets/indigo/concepts/legio_am_acids_2.svg
.. |image4| image:: ../../assets/indigo/concepts/legio_am_acids_3.svg
.. |image5| image:: ../../assets/indigo/concepts/legio_am_amines_1.svg
.. |image6| image:: ../../assets/indigo/concepts/legio_am_amines_2.svg
.. |image7| image:: ../../assets/indigo/concepts/legio_am_amines_3.svg
.. |image8| image:: ../../assets/indigo/concepts/legio_am_prod_1.svg
.. |image9| image:: ../../assets/indigo/concepts/legio_am_prod_4.svg
.. |image10| image:: ../../assets/indigo/concepts/legio_am_prod_7.svg
.. |image11| image:: ../../assets/indigo/concepts/legio_am_prod_2.svg
.. |image12| image:: ../../assets/indigo/concepts/legio_am_prod_5.svg
.. |image13| image:: ../../assets/indigo/concepts/legio_am_prod_8.svg
.. |image14| image:: ../../assets/indigo/concepts/legio_am_prod_3.svg
.. |image15| image:: ../../assets/indigo/concepts/legio_am_prod_6.svg
.. |image16| image:: ../../assets/indigo/concepts/legio_am_prod_9.svg
.. |image17| image:: ../../assets/indigo/concepts/legio_am_prod_all_10.svg
.. |image18| image:: ../../assets/indigo/concepts/legio_am_prod_all_11.svg
.. |image19| image:: ../../assets/indigo/concepts/legio_am_prod_all_12.svg
.. |image20| image:: ../../assets/indigo/concepts/legio_am_prod_all_one_11.svg
.. |image21| image:: ../../assets/indigo/concepts/legio_am_prod_all_one_12.svg
.. |image22| image:: ../../assets/indigo/concepts/legio_am_prod_all_one_14.svg
.. |image23| image:: ../../assets/indigo/concepts/legio_cisd_rxn.svg
.. |image24| image:: ../../assets/indigo/concepts/legio_cisd_rxn.svg
.. |image25| image:: ../../assets/indigo/concepts/legio_cisd_diene9.svg
.. |image26| image:: ../../assets/indigo/concepts/legio_cisd_dienophile9.svg
.. |image27| image:: ../../assets/indigo/concepts/legio_cisd_diene9.svg
.. |image28| image:: ../../assets/indigo/concepts/legio_cisd_dienophile9.svg
.. |image29| image:: ../../assets/indigo/concepts/legio_cisd_prod_1.svg
.. |image30| image:: ../../assets/indigo/concepts/legio_cisd_prod_2.svg
.. |image31| image:: ../../assets/indigo/concepts/legio_cisd_prod_1.svg
.. |image32| image:: ../../assets/indigo/concepts/legio_cisd_prod_2.svg
.. |image33| image:: ../../assets/indigo/concepts/legio_mult_rxn.svg
.. |image34| image:: ../../assets/indigo/concepts/legio_mult_rxn.svg
.. |image35| image:: ../../assets/indigo/concepts/legio_mult_accl.svg
.. |image36| image:: ../../assets/indigo/concepts/legio_mult_glucose.svg
.. |image37| image:: ../../assets/indigo/concepts/legio_mult_accl.svg
.. |image38| image:: ../../assets/indigo/concepts/legio_mult_glucose.svg
.. |image39| image:: ../../assets/indigo/concepts/legio_mult_prod_19.svg
.. |image40| image:: ../../assets/indigo/concepts/legio_mult_prod_31.svg
.. |image41| image:: ../../assets/indigo/concepts/legio_mult_prod_19.svg
.. |image42| image:: ../../assets/indigo/concepts/legio_mult_prod_31.svg
.. |image43| image:: ../../assets/indigo/concepts/legio_modes_rxn.svg
.. |image44| image:: ../../assets/indigo/concepts/legio_modes_rxn.svg
.. |image45| image:: ../../assets/indigo/concepts/legio_modes_mon_1.svg
.. |image46| image:: ../../assets/indigo/concepts/legio_modes_mon_2.svg
.. |image47| image:: ../../assets/indigo/concepts/legio_modes_mon_1.svg
.. |image48| image:: ../../assets/indigo/concepts/legio_modes_mon_2.svg
.. |image49| image:: ../../assets/indigo/concepts/legio_modes_symm.svg
.. |image50| image:: ../../assets/indigo/concepts/legio_modes_symm.svg
.. |image51| image:: ../../assets/indigo/concepts/legio_modes_prod_all_5.svg
.. |image52| image:: ../../assets/indigo/concepts/legio_modes_prod_all_18.svg
.. |image53| image:: ../../assets/indigo/concepts/legio_modes_prod_all_6.svg
.. |image54| image:: ../../assets/indigo/concepts/legio_modes_prod_all_25.svg
.. |image55| image:: ../../assets/indigo/concepts/legio_modes_prod_all_5.svg
.. |image56| image:: ../../assets/indigo/concepts/legio_modes_prod_all_18.svg
.. |image57| image:: ../../assets/indigo/concepts/legio_modes_prod_all_6.svg
.. |image58| image:: ../../assets/indigo/concepts/legio_modes_prod_all_25.svg
.. |image59| image:: ../../assets/indigo/concepts/legio_modes_prod_all_one_17.svg
.. |image60| image:: ../../assets/indigo/concepts/legio_modes_prod_all_one_37.svg
.. |image61| image:: ../../assets/indigo/concepts/legio_modes_prod_all_one_17.svg
.. |image62| image:: ../../assets/indigo/concepts/legio_modes_prod_all_one_37.svg
.. |image63| image:: ../../assets/indigo/concepts/legio_intr_rxn.svg
.. |image64| image:: ../../assets/indigo/concepts/legio_intr_rxn.svg
.. |image65| image:: ../../assets/indigo/concepts/legio_intr_mon.svg
.. |image66| image:: ../../assets/indigo/concepts/legio_intr_prod_1.svg
.. |image67| image:: ../../assets/indigo/concepts/legio_intr_mon.svg
.. |image68| image:: ../../assets/indigo/concepts/legio_intr_prod_1.svg
.. |image69| image:: ../../assets/indigo/concepts/legio_sc_rxn.svg
.. |image70| image:: ../../assets/indigo/concepts/legio_sc_rxn.svg
.. |image71| image:: ../../assets/indigo/concepts/legio_sc_mon_1.svg
.. |image72| image:: ../../assets/indigo/concepts/legio_sc_prod_1.svg
.. |image73| image:: ../../assets/indigo/concepts/legio_sc_mon_2.svg
.. |image74| image:: ../../assets/indigo/concepts/legio_sc_prod_2.svg
.. |image75| image:: ../../assets/indigo/concepts/legio_sc_mon_3.svg
.. |image76| image:: ../../assets/indigo/concepts/legio_sc_prod_3.svg
.. |image77| image:: ../../assets/indigo/concepts/legio_sc_mon_4.svg
.. |image78| image:: ../../assets/indigo/concepts/legio_sc_mon_5.svg
.. |image79| image:: ../../assets/indigo/concepts/legio_sc_prod_4.svg
.. |image80| image:: ../../assets/indigo/concepts/legio_sc_mon_1.svg
.. |image81| image:: ../../assets/indigo/concepts/legio_sc_prod_1.svg
.. |image82| image:: ../../assets/indigo/concepts/legio_sc_mon_2.svg
.. |image83| image:: ../../assets/indigo/concepts/legio_sc_prod_2.svg
.. |image84| image:: ../../assets/indigo/concepts/legio_sc_mon_3.svg
.. |image85| image:: ../../assets/indigo/concepts/legio_sc_prod_3.svg
.. |image86| image:: ../../assets/indigo/concepts/legio_sc_mon_4.svg
.. |image87| image:: ../../assets/indigo/concepts/legio_sc_mon_5.svg
.. |image88| image:: ../../assets/indigo/concepts/legio_sc_prod_4.svg
.. |image89| image:: ../../assets/indigo/concepts/legio_cs_rxn.svg
.. |image90| image:: ../../assets/indigo/concepts/legio_cs_rxn.svg
.. |image91| image:: ../../assets/indigo/concepts/legio_cs_mon_1.svg
.. |image92| image:: ../../assets/indigo/concepts/legio_cs_prod_1.svg
.. |image93| image:: ../../assets/indigo/concepts/legio_cs_mon_2.svg
.. |image94| image:: ../../assets/indigo/concepts/legio_cs_prod_2.svg
.. |image95| image:: ../../assets/indigo/concepts/legio_cs_mon_3.svg
.. |image96| image:: ../../assets/indigo/concepts/legio_cs_prod_3.svg
.. |image97| image:: ../../assets/indigo/concepts/legio_cs_mon_1.svg
.. |image98| image:: ../../assets/indigo/concepts/legio_cs_prod_1.svg
.. |image99| image:: ../../assets/indigo/concepts/legio_cs_mon_2.svg
.. |image100| image:: ../../assets/indigo/concepts/legio_cs_prod_2.svg
.. |image101| image:: ../../assets/indigo/concepts/legio_cs_mon_3.svg
.. |image102| image:: ../../assets/indigo/concepts/legio_cs_prod_3.svg
.. |image103| image:: ../../assets/indigo/concepts/legio_peps_rxn.svg
.. |image104| image:: ../../assets/indigo/concepts/legio_peps_rxn.svg
.. |image105| image:: ../../assets/indigo/concepts/legio_peps_glycine.svg
.. |image106| image:: ../../assets/indigo/concepts/legio_peps_lysine.svg
.. |image107| image:: ../../assets/indigo/concepts/legio_peps_glycine.svg
.. |image108| image:: ../../assets/indigo/concepts/legio_peps_lysine.svg
.. |image109| image:: ../../assets/indigo/concepts/legio_peps_prod_1.svg
.. |image110| image:: ../../assets/indigo/concepts/legio_peps_prod_2.svg
.. |image111| image:: ../../assets/indigo/concepts/legio_peps_prod_3.svg
.. |image112| image:: ../../assets/indigo/concepts/legio_peps_prod_1.svg
.. |image113| image:: ../../assets/indigo/concepts/legio_peps_prod_2.svg
.. |image114| image:: ../../assets/indigo/concepts/legio_peps_prod_3.svg
