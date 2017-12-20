A substructure search query with no ``$parameters`` returns the
molecules that include the query structure as the substructure or exact
match. The matched part is highlighted in examples.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image2|             | |image3|                          |
+----------------------+-----------------------------------+

The query molecule can be disconnected. Matched fragments in the target
structure cannot overlap.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image7|             | |image8|                          | |image9|                              |
+----------------------+-----------------------------------+---------------------------------------+

Substructure Query Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explicit Hydrogens
''''''''''''''''''

The explicit hydrogens specified in the query structure must match any
(explicit or implicit) hydrogen in the target structure.

+-------------------------+-------------------------+-------------------------+
| Substructure Query      | Examples of Molecules   | Examples of Molecules   |
|                         | Retrieved               | Not Retrieved           |
+=========================+=========================+=========================+
| |image18|               | |image19|               | |image20|               |
+-------------------------+-------------------------+-------------------------+
| |image21|               | |image22|               | |image23|               |
+-------------------------+-------------------------+-------------------------+
| |image24|               | |image25|               |                         |
+-------------------------+-------------------------+-------------------------+

Charges and Radicals
''''''''''''''''''''

The presence of charged atoms in the query molecule is an additional
property. If the charge is specified, it must match the charge in the
target molecule. An atom without a specific charge can match an atom
with either charge. The same rule applies for radicals.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image35|            | |image36|                         | |image37|                             |
+----------------------+-----------------------------------+---------------------------------------+
| |image38|            | |image39|                         | |image40|                             |
+----------------------+-----------------------------------+---------------------------------------+
| |image41|            | |image42|                         | |image43|                             |
+----------------------+-----------------------------------+---------------------------------------+

Isotopes
''''''''

The presence of isotopes atoms in the query molecule is an additional
property, like charges.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image48|            | |image49|                         |
+----------------------+-----------------------------------+
| |image50|            | |image51|                         |
+----------------------+-----------------------------------+

Valence
'''''''

Valence can be specified on the query atoms.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image55|            | |image56|                         | |image57|                             |
+----------------------+-----------------------------------+---------------------------------------+

Preventing Hydrogen Substitutions
'''''''''''''''''''''''''''''''''

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image61|            | |image62|                         | |image63|                             |
+----------------------+-----------------------------------+---------------------------------------+

Number of Non-Hydrogen Substitutions
''''''''''''''''''''''''''''''''''''

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image67|            | |image68|                         | |image69|                             |
+----------------------+-----------------------------------+---------------------------------------+

Unsaturation flag
'''''''''''''''''

An unsaturated atom must have at least one non-single bond.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image73|            | |image74|                         | |image75|                             |
+----------------------+-----------------------------------+---------------------------------------+

Ring Bond Count
'''''''''''''''

You can specify the number of ring bonds that are connected to the atom.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image79|            | |image80|                         | |image81|                             |
+----------------------+-----------------------------------+---------------------------------------+

Bond Topology
'''''''''''''

“Ring” query bonds must match the ring(s) of the target molecule;
“chain” query bonds must not.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image88|            | |image89|                         | |image90|                             |
+----------------------+-----------------------------------+---------------------------------------+
| |image91|            | |image92|                         | |image93|                             |
+----------------------+-----------------------------------+---------------------------------------+

Query Atom Labels
'''''''''''''''''

“A” query atom matches any atom except hydrogen (or its isotopes). “Q”
query atom matches any atom except hydrogen and carbon.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image100|           | |image101|                        | |image102|                            |
+----------------------+-----------------------------------+---------------------------------------+
| |image103|           | |image104|                        | |image105|                            |
+----------------------+-----------------------------------+---------------------------------------+

Atom Lists
''''''''''

You can specify the list of elements that are allowed or prohibited for
the query atom. Hydrogen in the list can match the explicit or implicit
hydrogen of the target.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image110|           | |image111|                        |
+----------------------+-----------------------------------+
| |image112|           | |image113|                        |
+----------------------+-----------------------------------+

Query Bonds
'''''''''''

The following types of query bonds are supported:

-  Single or double
-  Single or aromatic
-  Double or aromatic
-  Any

Below is an example with 'Single or Double' bonds. Such bonds cannot
match aromatic target bonds.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image117|           | |image118|                        | |image119|                            |
+----------------------+-----------------------------------+---------------------------------------+

Cis-trans Isomerism
^^^^^^^^^^^^^^^^^^^

You can specify the “stereo” flag on a carbon double bond that you do
not want to rotate in order to exclude cis-trans isomers from the search
results. Explicit and implicit hydrogen substituents are supported.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image126|           | |image127|                        | |image128|                            |
+----------------------+-----------------------------------+---------------------------------------+
| |image129|           | |image130|                        | |image131|                            |
+----------------------+-----------------------------------+---------------------------------------+

Chirality
^^^^^^^^^

The following tetrahedral stereocenters are allowed:

-  C or Si or N+ with 3 single bonds (implicit hydrogen)
-  C or Si or N+ with 4 single bonds
-  S with 2 single bonds and 2 double bonds
-  P with 3 single bonds and 1 double bond
-  P+ with 4 single bonds

Also, a special type of tetrahedral stereocenter—with the pyramid is
formed by 3 neighbor atoms and the lone pair of electrons—is allowed:

-  N or P or S+ with 3 single bonds
-  S with 2 single bonds and 1 double bond

The stereocenter is defined by up- or down-oriented stereobond(s)
connected to it. The chirality is determined from the stereobond
orientation and the position of atoms. The stereocenter that has an
“absolute” configuration can match only “absolute” stereocenters that
have the same chirality.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image135|           | |image136|                        | |image137|                            |
+----------------------+-----------------------------------+---------------------------------------+

Here are two examples of non-carbon chiral centers:

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image142|           | |image143|                        |
+----------------------+-----------------------------------+
| |image144|           | |image145|                        |
+----------------------+-----------------------------------+

MDL notation of stereogroups is supported. “AND” stereocenters can match
“AND”, “OR”, and absolute ones; “OR” stereocenters can match “OR” and
absolute ones. Target stereo-groups cannot be more fragmented than the
query stereo-groups.

+-------------------------+-------------------------+-------------------------+
| Substructure Query      | Examples of Molecules   | Examples of Molecules   |
|                         | Retrieved               | Not Retrieved           |
+=========================+=========================+=========================+
| |image151|              | |image152|              | |image153|              |
+-------------------------+-------------------------+-------------------------+
| |image154|              | |image155|              |                         |
+-------------------------+-------------------------+-------------------------+

“Either” stereobond can be specified in the query. The corresponding
stereocenter matches any stereocenter regardless of chirality.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image159|           | |image160|                        | |image161|                            |
+----------------------+-----------------------------------+---------------------------------------+

**Note:** The embedding of the substructure is not limited to the way in
which it is drawn. Sometimes, single bonds can “swap”, producing the
hits that are correct, but appear strange.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image164|           | |image165|                        |
+----------------------+-----------------------------------+

**Note:** A chiral center with explicit hydrogen can match a chiral
center with implicit hydrogen, and vice versa.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image170|           | |image171|                        |
+----------------------+-----------------------------------+
| |image172|           | |image173|                        |
+----------------------+-----------------------------------+

Markush Search
^^^^^^^^^^^^^^

Markush search has the same syntax as the basic substructure search, and
it will be performed automatically if the query molecule contains one or
more R-groups.

+-----------------+-----------------------------------+---------------------------------------+
| Markush Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+=================+===================================+=======================================+
| |image180|      | |image181|                        | |image182|                            |
+-----------------+-----------------------------------+---------------------------------------+
| |image183|      | |image184|                        | |image185|                            |
+-----------------+-----------------------------------+---------------------------------------+

Aromaticity in Substructure Search and Markush Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Basic Queries
'''''''''''''

Aromatic bonds can match only aromatic bonds.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image195|           | |image196|                        | |image197|                            |
+----------------------+-----------------------------------+---------------------------------------+
| |image198|           | |image199|                        | |image200|                            |
+----------------------+-----------------------------------+---------------------------------------+
| |image201|           | |image202|                        | |image203|                            |
+----------------------+-----------------------------------+---------------------------------------+

Queries with Query Features
'''''''''''''''''''''''''''

Some queries with query features can have ambiguous aromaticity status:
they are aromatic in one matching and not aromatic in another matching.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image210|           | |image211|                        | |image212|                            |
+----------------------+-----------------------------------+---------------------------------------+
| |image213|           | |image214|                        | |image215|                            |
+----------------------+-----------------------------------+---------------------------------------+

Aromaticity and Markush Search
''''''''''''''''''''''''''''''

Markush queries are allowed to match both aromatic and non-aromatic
targets.

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image218|           | |image219|                        |
+----------------------+-----------------------------------+

Charge and Aromaticity
''''''''''''''''''''''

Charges and aromatic bonds are matched independently. In some structures
where the acquisition of the charge by an atom destroys the aromaticity
of a ring, matching is not possible due to the mismatch of bond orders.

+----------------------+-------------------------------------------+
| Substructure Query   | Examples of Molecules **Not** Retrieved   |
+======================+===========================================+
| |image222|           | |image223|                                |
+----------------------+-------------------------------------------+

However, uncharged aromatic queries match charged aromatic structures:

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image226|           | |image227|                        |
+----------------------+-----------------------------------+

Pseudo-atoms
^^^^^^^^^^^^

Pseudo-atom in the query structure can match only the same pseudo-atom
in the target structure. The matching is case-sensitive.

+----------------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===================================+=======================================+
| |image231|           | |image232|                        | |image233|                            |
+----------------------+-----------------------------------+---------------------------------------+

Pseudo-atoms in target structures are never expanded:

+----------------------+---------------------------------------+
| Substructure Query   | Examples of Molecules Not Retrieved   |
+======================+=======================================+
| |image236|           | |image237|                            |
+----------------------+---------------------------------------+

Query atoms can match pseudo-atoms:

+----------------------+-----------------------------------+
| Substructure Query   | Examples of Molecules Retrieved   |
+======================+===================================+
| |image240|           | |image241|                        |
+----------------------+-----------------------------------+

**Note:** 'X' atom is treated as 'any halogen' query atom by default,
but there is an option to treat it as pseudo-atom. In order to treat it
so, please run the following SQL statement prior to table indexing:

.. parsed-literal::

	|code_treat_x_as_pseudoatom_1|


After that, please reconnect to the database. This setting will be
saved, so you will never need to run the statement again (unless you
re-install the cartridge). To get the original behavior back, you can
run the following SQL statement:

.. parsed-literal::

	|code_treat_x_as_pseudoatom_0|


+----------------------+--------------------------------------------+-------------------------------------------------------------------+
| Substructure Query   | Examples of Molecules Retrieved (Or Not)   | Comment                                                           |
+======================+============================================+===================================================================+
| |image246|           | |image247|                                 | Matches with “x as pseudo atom” option;                           |
|                      |                                            |  Raises an error with “x as any halogen atom” option (default).   |
+----------------------+--------------------------------------------+-------------------------------------------------------------------+
| |image248|           | |image249|                                 | Matches with “x as any halogen atom” option (default);            |
|                      |                                            |  Does not match with “x as pseudo atom” option.                   |
+----------------------+--------------------------------------------+-------------------------------------------------------------------+

Resonance Search
^^^^^^^^^^^^^^^^

The resonance substructure search is provided by the ``Sub`` operator
with ``RES`` parameter:

.. parsed-literal::

	|code_select_resonance_option|

With this type of search you can find molecules whose resonance forms
contain the query molecule.

+----------------------+---------------------------------+--------------------------+
| Substructure Query   | Example of Molecule Retrieved   | Matched Resonance Form   |
+======================+=================================+==========================+
| |image256|           | |image257|                      | |image258|               |
+----------------------+---------------------------------+--------------------------+
| |image259|           | |image260|                      | |image261|               |
+----------------------+---------------------------------+--------------------------+

The query molecule can contain any query features:

+----------------------+---------------------------------+--------------------------+
| Substructure Query   | Example of Molecule Retrieved   | Matched Resonance Form   |
+======================+=================================+==========================+
| |image268|           | |image269|                      | |image270|               |
+----------------------+---------------------------------+--------------------------+
| |image271|           | |image272|                      | |image273|               |
+----------------------+---------------------------------+--------------------------+

Impossible resonance forms are not matched:

+----------------------+-------------------------------------+
| Substructure Query   | Example of Molecule Not Retrieved   |
+======================+=====================================+
| |image276|           | |image277|                          |
+----------------------+-------------------------------------+

Actually, only the *main resonance contributors* are matched. The main
resonance contributors are resonance forms that have the maximum number
of atoms with the full octet and/or the minimum number of atoms with
nonzero formal charge. For example, the following structure would not
match itself because both atoms are charged and only one atom has a full
octet:

+----------------------+-------------------------------------+
| Substructure Query   | Example of Molecule Not Retrieved   |
+======================+=====================================+
| |image280|           | |image281|                          |
+----------------------+-------------------------------------+

Uncharged atoms still match charged ones in the resonance search:

+----------------------+---------------------------------+--------------------------+
| Substructure Query   | Example of Molecule Retrieved   | Matched Resonance Form   |
+======================+=================================+==========================+
| |image285|           | |image286|                      | |image287|               |
+----------------------+---------------------------------+--------------------------+

A resonance chain can be of any length:

+----------------------+---------------------------------+
| Substructure Query   | Example of Molecule Retrieved   |
+======================+=================================+
| |image290|           | |image291|                      |
+----------------------+---------------------------------+

Cyclic resonance forms are currently not supported:

+----------------------+-------------------------------------+
| Substructure Query   | Example of Molecule Not Retrieved   |
+======================+=====================================+
| |image294|           | |image295|                          |
+----------------------+-------------------------------------+

3D Constraints
^^^^^^^^^^^^^^

Bingo supports all types of 3D constraints for the queries in MDL
(Symyx) Molfile 2000 format:

-  Distance ranges
-  Angle ranges
-  Dihedral angle ranges
-  Exclusion spheres

The substructure match with 3D constraints follows the rules of the
ordinary substructure match. In addition, the 3D constraints defined in
the query molecule must be fulfilled by the corresponding atoms of the
target. If the query can be embedded in several ways, all embeddings are
checked. The query matches the target when at least one embedding
conforms to the conditions.

**Note:** 3D constraints of Molfile 3000 format are not supported.

Affine Transformation Search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type of 3D search treats the molecule as a rigid structure
consisting of points in space. Similar to the case of the search with
constraints, all inclusions of the query are checked against the
following condition: the structure of the query is transformed to its
image on the target by an affine transformation
(translation+rotation+scale). 1 The syntax of the affine transformation
substructure search is as follows:

.. parsed-literal::

	|code_select_affine_option|

 
``rms`` is the maximum allowed root-mean-square deviation of all imposed
atoms. It is measured in angstroms.

The query atoms that are fixed must be labeled fixed. The imposition of
other atoms is not restricted to ``rms``.

The following example makes no chemical sense, but is included here as a
simple two-dimensional illustration of the affine transformation search:

+----------------------+---------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Parameters    | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+===============+===================================+=======================================+
| |image299|           | ``AFF 0.1``   | |image300|                        | |image301|                            |
+----------------------+---------------+-----------------------------------+---------------------------------------+

**Note:** When no atoms are labeled fixed, all of them are considered
fixed.

Conformational Search
^^^^^^^^^^^^^^^^^^^^^

Any conformation can be obtained by rotating the molecule around single
bonds. Thus, the inclusion is correct if the image of the query molecule
is the conformation of the query, i.e. a sequence of rotations of the
molecule around single bonds converts the query into a substructure of
the target. In a way similar to affine transformation search, you can
set the ``rms`` parameter in order to define the accuracy of the
transformation.

The syntax of the conformational substructure search is as follows:

.. parsed-literal::

	|code_select_conformational_option|


+----------------------+----------------+-----------------------------------+---------------------------------------+
| Substructure Query   | Parameters     | Examples of Molecules Retrieved   | Examples of Molecules Not Retrieved   |
+======================+================+===================================+=======================================+
| |image305|           | ``CONF 0.1``   | |image306|                        | |image307|                            |
+----------------------+----------------+-----------------------------------+---------------------------------------+

.. |image2| image:: ../assets/bingo/sub_q01.*
.. |image3| image:: ../assets/bingo/sub_t01.*
.. |image4| image:: ../assets/bingo/sub_q22.*
.. |image5| image:: ../assets/bingo/sub_t22.*
.. |image6| image:: ../assets/bingo/sub_n22.*
.. |image7| image:: ../assets/bingo/sub_q22.*
.. |image8| image:: ../assets/bingo/sub_t22.*
.. |image9| image:: ../assets/bingo/sub_n22.*
.. |image10| image:: ../assets/bingo/sub_q02.*
.. |image11| image:: ../assets/bingo/sub_t02.*
.. |image12| image:: ../assets/bingo/sub_tn02.*
.. |image13| image:: ../assets/bingo/sub_h_01q.*
.. |image14| image:: ../assets/bingo/sub_h_01t.*
.. |image15| image:: ../assets/bingo/sub_h_01n.*
.. |image16| image:: ../assets/bingo/sub_h_02q.*
.. |image17| image:: ../assets/bingo/sub_h_02t.*
.. |image18| image:: ../assets/bingo/sub_q02.*
.. |image19| image:: ../assets/bingo/sub_t02.*
.. |image20| image:: ../assets/bingo/sub_tn02.*
.. |image21| image:: ../assets/bingo/sub_h_01q.*
.. |image22| image:: ../assets/bingo/sub_h_01t.*
.. |image23| image:: ../assets/bingo/sub_h_01n.*
.. |image24| image:: ../assets/bingo/sub_h_02q.*
.. |image25| image:: ../assets/bingo/sub_h_02t.*
.. |image26| image:: ../assets/bingo/sub_q03.*
.. |image27| image:: ../assets/bingo/sub_t03.*
.. |image28| image:: ../assets/bingo/sub_tn03.*
.. |image29| image:: ../assets/bingo/sub_q04.*
.. |image30| image:: ../assets/bingo/sub_t04.*
.. |image31| image:: ../assets/bingo/sub_tn04.*
.. |image32| image:: ../assets/bingo/sub_q05.*
.. |image33| image:: ../assets/bingo/sub_t05.*
.. |image34| image:: ../assets/bingo/sub_tn05.*
.. |image35| image:: ../assets/bingo/sub_q03.*
.. |image36| image:: ../assets/bingo/sub_t03.*
.. |image37| image:: ../assets/bingo/sub_tn03.*
.. |image38| image:: ../assets/bingo/sub_q04.*
.. |image39| image:: ../assets/bingo/sub_t04.*
.. |image40| image:: ../assets/bingo/sub_tn04.*
.. |image41| image:: ../assets/bingo/sub_q05.*
.. |image42| image:: ../assets/bingo/sub_t05.*
.. |image43| image:: ../assets/bingo/sub_tn05.*
.. |image44| image:: ../assets/bingo/sub_q07.*
.. |image45| image:: ../assets/bingo/sub_t07.*
.. |image46| image:: ../assets/bingo/sub_q08.*
.. |image47| image:: ../assets/bingo/sub_t08.*
.. |image48| image:: ../assets/bingo/sub_q07.*
.. |image49| image:: ../assets/bingo/sub_t07.*
.. |image50| image:: ../assets/bingo/sub_q08.*
.. |image51| image:: ../assets/bingo/sub_t08.*
.. |image52| image:: ../assets/bingo/sub_q09.*
.. |image53| image:: ../assets/bingo/sub_t09.*
.. |image54| image:: ../assets/bingo/sub_tn09.*
.. |image55| image:: ../assets/bingo/sub_q09.*
.. |image56| image:: ../assets/bingo/sub_t09.*
.. |image57| image:: ../assets/bingo/sub_tn09.*
.. |image58| image:: ../assets/bingo/sub_q10.*
.. |image59| image:: ../assets/bingo/sub_t10.*
.. |image60| image:: ../assets/bingo/sub_tn10.*
.. |image61| image:: ../assets/bingo/sub_q10.*
.. |image62| image:: ../assets/bingo/sub_t10.*
.. |image63| image:: ../assets/bingo/sub_tn10.*
.. |image64| image:: ../assets/bingo/sub_q11.*
.. |image65| image:: ../assets/bingo/sub_t11.*
.. |image66| image:: ../assets/bingo/sub_tn11.*
.. |image67| image:: ../assets/bingo/sub_q11.*
.. |image68| image:: ../assets/bingo/sub_t11.*
.. |image69| image:: ../assets/bingo/sub_tn11.*
.. |image70| image:: ../assets/bingo/sub_q12.*
.. |image71| image:: ../assets/bingo/sub_t12.*
.. |image72| image:: ../assets/bingo/sub_tn12.*
.. |image73| image:: ../assets/bingo/sub_q12.*
.. |image74| image:: ../assets/bingo/sub_t12.*
.. |image75| image:: ../assets/bingo/sub_tn12.*
.. |image76| image:: ../assets/bingo/sub_q13.*
.. |image77| image:: ../assets/bingo/sub_t13.*
.. |image78| image:: ../assets/bingo/sub_tn13.*
.. |image79| image:: ../assets/bingo/sub_q13.*
.. |image80| image:: ../assets/bingo/sub_t13.*
.. |image81| image:: ../assets/bingo/sub_tn13.*
.. |image82| image:: ../assets/bingo/sub_q14.*
.. |image83| image:: ../assets/bingo/sub_t14.*
.. |image84| image:: ../assets/bingo/sub_tn14.*
.. |image85| image:: ../assets/bingo/sub_q15.*
.. |image86| image:: ../assets/bingo/sub_t15.*
.. |image87| image:: ../assets/bingo/sub_tn15.*
.. |image88| image:: ../assets/bingo/sub_q14.*
.. |image89| image:: ../assets/bingo/sub_t14.*
.. |image90| image:: ../assets/bingo/sub_tn14.*
.. |image91| image:: ../assets/bingo/sub_q15.*
.. |image92| image:: ../assets/bingo/sub_t15.*
.. |image93| image:: ../assets/bingo/sub_tn15.*
.. |image94| image:: ../assets/bingo/sub_q16.*
.. |image95| image:: ../assets/bingo/sub_t16.*
.. |image96| image:: ../assets/bingo/sub_tn16.*
.. |image97| image:: ../assets/bingo/sub_q17.*
.. |image98| image:: ../assets/bingo/sub_t17.*
.. |image99| image:: ../assets/bingo/sub_tn17.*
.. |image100| image:: ../assets/bingo/sub_q16.*
.. |image101| image:: ../assets/bingo/sub_t16.*
.. |image102| image:: ../assets/bingo/sub_tn16.*
.. |image103| image:: ../assets/bingo/sub_q17.*
.. |image104| image:: ../assets/bingo/sub_t17.*
.. |image105| image:: ../assets/bingo/sub_tn17.*
.. |image106| image:: ../assets/bingo/sub_q18.*
.. |image107| image:: ../assets/bingo/sub_t18.*
.. |image108| image:: ../assets/bingo/sub_q19.*
.. |image109| image:: ../assets/bingo/sub_t19.*
.. |image110| image:: ../assets/bingo/sub_q18.*
.. |image111| image:: ../assets/bingo/sub_t18.*
.. |image112| image:: ../assets/bingo/sub_q19.*
.. |image113| image:: ../assets/bingo/sub_t19.*
.. |image114| image:: ../assets/bingo/sub_q20.*
.. |image115| image:: ../assets/bingo/sub_t20.*
.. |image116| image:: ../assets/bingo/sub_tn20.*
.. |image117| image:: ../assets/bingo/sub_q20.*
.. |image118| image:: ../assets/bingo/sub_t20.*
.. |image119| image:: ../assets/bingo/sub_tn20.*
.. |image120| image:: ../assets/bingo/sub_stereo_10q.*
.. |image121| image:: ../assets/bingo/sub_stereo_10t.*
.. |image122| image:: ../assets/bingo/sub_stereo_10n.*
.. |image123| image:: ../assets/bingo/sub_stereo_11q.*
.. |image124| image:: ../assets/bingo/sub_stereo_11t.*
.. |image125| image:: ../assets/bingo/sub_stereo_11n.*
.. |image126| image:: ../assets/bingo/sub_stereo_10q.*
.. |image127| image:: ../assets/bingo/sub_stereo_10t.*
.. |image128| image:: ../assets/bingo/sub_stereo_10n.*
.. |image129| image:: ../assets/bingo/sub_stereo_11q.*
.. |image130| image:: ../assets/bingo/sub_stereo_11t.*
.. |image131| image:: ../assets/bingo/sub_stereo_11n.*
.. |image132| image:: ../assets/bingo/sub_stereo_01q.*
.. |image133| image:: ../assets/bingo/sub_stereo_01t.*
.. |image134| image:: ../assets/bingo/sub_stereo_01n.*
.. |image135| image:: ../assets/bingo/sub_stereo_01q.*
.. |image136| image:: ../assets/bingo/sub_stereo_01t.*
.. |image137| image:: ../assets/bingo/sub_stereo_01n.*
.. |image138| image:: ../assets/bingo/sub_stereo_08q.*
.. |image139| image:: ../assets/bingo/sub_stereo_08t.*
.. |image140| image:: ../assets/bingo/sub_stereo_09q.*
.. |image141| image:: ../assets/bingo/sub_stereo_09t.*
.. |image142| image:: ../assets/bingo/sub_stereo_08q.*
.. |image143| image:: ../assets/bingo/sub_stereo_08t.*
.. |image144| image:: ../assets/bingo/sub_stereo_09q.*
.. |image145| image:: ../assets/bingo/sub_stereo_09t.*
.. |image146| image:: ../assets/bingo/sub_stereo_05q.*
.. |image147| image:: ../assets/bingo/sub_stereo_05t.*
.. |image148| image:: ../assets/bingo/sub_stereo_05n.*
.. |image149| image:: ../assets/bingo/sub_stereo_06q.*
.. |image150| image:: ../assets/bingo/sub_stereo_06t.*
.. |image151| image:: ../assets/bingo/sub_stereo_05q.*
.. |image152| image:: ../assets/bingo/sub_stereo_05t.*
.. |image153| image:: ../assets/bingo/sub_stereo_05n.*
.. |image154| image:: ../assets/bingo/sub_stereo_06q.*
.. |image155| image:: ../assets/bingo/sub_stereo_06t.*
.. |image156| image:: ../assets/bingo/sub_stereo_07q.*
.. |image157| image:: ../assets/bingo/sub_stereo_07t.*
.. |image158| image:: ../assets/bingo/sub_stereo_07n.*
.. |image159| image:: ../assets/bingo/sub_stereo_07q.*
.. |image160| image:: ../assets/bingo/sub_stereo_07t.*
.. |image161| image:: ../assets/bingo/sub_stereo_07n.*
.. |image162| image:: ../assets/bingo/sub_stereo_02q.*
.. |image163| image:: ../assets/bingo/sub_stereo_02t.*
.. |image164| image:: ../assets/bingo/sub_stereo_02q.*
.. |image165| image:: ../assets/bingo/sub_stereo_02t.*
.. |image166| image:: ../assets/bingo/sub_stereo_03q.*
.. |image167| image:: ../assets/bingo/sub_stereo_03t.*
.. |image168| image:: ../assets/bingo/sub_stereo_04q.*
.. |image169| image:: ../assets/bingo/sub_stereo_04t.*
.. |image170| image:: ../assets/bingo/sub_stereo_03q.*
.. |image171| image:: ../assets/bingo/sub_stereo_03t.*
.. |image172| image:: ../assets/bingo/sub_stereo_04q.*
.. |image173| image:: ../assets/bingo/sub_stereo_04t.*
.. |image174| image:: ../assets/bingo/sub_mar_q01.*
.. |image175| image:: ../assets/bingo/sub_mar_t01.*
.. |image176| image:: ../assets/bingo/sub_mar_nt01.*
.. |image177| image:: ../assets/bingo/sub_mar_q02.*
.. |image178| image:: ../assets/bingo/sub_mar_t02.*
.. |image179| image:: ../assets/bingo/sub_mar_n02.*
.. |image180| image:: ../assets/bingo/sub_mar_q01.*
.. |image181| image:: ../assets/bingo/sub_mar_t01.*
.. |image182| image:: ../assets/bingo/sub_mar_nt01.*
.. |image183| image:: ../assets/bingo/sub_mar_q02.*
.. |image184| image:: ../assets/bingo/sub_mar_t02.*
.. |image185| image:: ../assets/bingo/sub_mar_n02.*
.. |image186| image:: ../assets/bingo/arom_sq1_q.*
.. |image187| image:: ../assets/bingo/arom_sq1_r.*
.. |image188| image:: ../assets/bingo/arom_sq1_nr.*
.. |image189| image:: ../assets/bingo/arom_sq2_q.*
.. |image190| image:: ../assets/bingo/arom_sq2_r.*
.. |image191| image:: ../assets/bingo/arom_sq2_nr.*
.. |image192| image:: ../assets/bingo/arom_sq3_q.*
.. |image193| image:: ../assets/bingo/arom_sq3_r.*
.. |image194| image:: ../assets/bingo/arom_sq3_nr.*
.. |image195| image:: ../assets/bingo/arom_sq1_q.*
.. |image196| image:: ../assets/bingo/arom_sq1_r.*
.. |image197| image:: ../assets/bingo/arom_sq1_nr.*
.. |image198| image:: ../assets/bingo/arom_sq2_q.*
.. |image199| image:: ../assets/bingo/arom_sq2_r.*
.. |image200| image:: ../assets/bingo/arom_sq2_nr.*
.. |image201| image:: ../assets/bingo/arom_sq3_q.*
.. |image202| image:: ../assets/bingo/arom_sq3_r.*
.. |image203| image:: ../assets/bingo/arom_sq3_nr.*
.. |image204| image:: ../assets/bingo/arom_qq1_q.*
.. |image205| image:: ../assets/bingo/arom_qq1_r.*
.. |image206| image:: ../assets/bingo/arom_qq1_nr.*
.. |image207| image:: ../assets/bingo/arom_qq2_q.*
.. |image208| image:: ../assets/bingo/arom_qq2_r.*
.. |image209| image:: ../assets/bingo/arom_qq2_nr.*
.. |image210| image:: ../assets/bingo/arom_qq1_q.*
.. |image211| image:: ../assets/bingo/arom_qq1_r.*
.. |image212| image:: ../assets/bingo/arom_qq1_nr.*
.. |image213| image:: ../assets/bingo/arom_qq2_q.*
.. |image214| image:: ../assets/bingo/arom_qq2_r.*
.. |image215| image:: ../assets/bingo/arom_qq2_nr.*
.. |image216| image:: ../assets/bingo/arom_qm1_q.*
.. |image217| image:: ../assets/bingo/arom_qm1_t.*
.. |image218| image:: ../assets/bingo/arom_qm1_q.*
.. |image219| image:: ../assets/bingo/arom_qm1_t.*
.. |image220| image:: ../assets/bingo/arom_cq1_q.*
.. |image221| image:: ../assets/bingo/arom_cq1_nr.*
.. |image222| image:: ../assets/bingo/arom_cq1_q.*
.. |image223| image:: ../assets/bingo/arom_cq1_nr.*
.. |image224| image:: ../assets/bingo/sub_q21.*
.. |image225| image:: ../assets/bingo/sub_t21.*
.. |image226| image:: ../assets/bingo/sub_q21.*
.. |image227| image:: ../assets/bingo/sub_t21.*
.. |image228| image:: ../assets/bingo/sub_pseudo_q1.*
.. |image229| image:: ../assets/bingo/sub_pseudo_t1.*
.. |image230| image:: ../assets/bingo/sub_pseudo_n1.*
.. |image231| image:: ../assets/bingo/sub_pseudo_q1.*
.. |image232| image:: ../assets/bingo/sub_pseudo_t1.*
.. |image233| image:: ../assets/bingo/sub_pseudo_n1.*
.. |image234| image:: ../assets/bingo/sub_pseudo_q2.*
.. |image235| image:: ../assets/bingo/sub_pseudo_n2.*
.. |image236| image:: ../assets/bingo/sub_pseudo_q2.*
.. |image237| image:: ../assets/bingo/sub_pseudo_n2.*
.. |image238| image:: ../assets/bingo/sub_pseudo_q3.*
.. |image239| image:: ../assets/bingo/sub_pseudo_t3.*
.. |image240| image:: ../assets/bingo/sub_pseudo_q3.*
.. |image241| image:: ../assets/bingo/sub_pseudo_t3.*
.. |image242| image:: ../assets/bingo/sub_pseudo_q4.*
.. |image243| image:: ../assets/bingo/sub_pseudo_t4.*
.. |image244| image:: ../assets/bingo/sub_pseudo_q5.*
.. |image245| image:: ../assets/bingo/sub_pseudo_t5.*
.. |image246| image:: ../assets/bingo/sub_pseudo_q4.*
.. |image247| image:: ../assets/bingo/sub_pseudo_t4.*
.. |image248| image:: ../assets/bingo/sub_pseudo_q5.*
.. |image249| image:: ../assets/bingo/sub_pseudo_t5.*
.. |image250| image:: ../assets/bingo/res_02_q.*
.. |image251| image:: ../assets/bingo/res_01_t.*
.. |image252| image:: ../assets/bingo/res_01_r.*
.. |image253| image:: ../assets/bingo/res_01_q.*
.. |image254| image:: ../assets/bingo/res_02_t.*
.. |image255| image:: ../assets/bingo/res_02_r.*
.. |image256| image:: ../assets/bingo/res_02_q.*
.. |image257| image:: ../assets/bingo/res_01_t.*
.. |image258| image:: ../assets/bingo/res_01_r.*
.. |image259| image:: ../assets/bingo/res_01_q.*
.. |image260| image:: ../assets/bingo/res_02_t.*
.. |image261| image:: ../assets/bingo/res_02_r.*
.. |image262| image:: ../assets/bingo/res_03_q.*
.. |image263| image:: ../assets/bingo/res_03_t.*
.. |image264| image:: ../assets/bingo/res_03_r.*
.. |image265| image:: ../assets/bingo/res_04_q.*
.. |image266| image:: ../assets/bingo/res_03_t-1.*
.. |image267| image:: ../assets/bingo/res_03_r-1.*
.. |image268| image:: ../assets/bingo/res_03_q.*
.. |image269| image:: ../assets/bingo/res_03_t.*
.. |image270| image:: ../assets/bingo/res_03_r.*
.. |image271| image:: ../assets/bingo/res_04_q.*
.. |image272| image:: ../assets/bingo/res_03_t-1.*
.. |image273| image:: ../assets/bingo/res_03_r-1.*
.. |image274| image:: ../assets/bingo/res_06_q.*
.. |image275| image:: ../assets/bingo/res_06_n.*
.. |image276| image:: ../assets/bingo/res_06_q.*
.. |image277| image:: ../assets/bingo/res_06_n.*
.. |image278| image:: ../assets/bingo/res_07_q.*
.. |image279| image:: ../assets/bingo/res_07_n.*
.. |image280| image:: ../assets/bingo/res_07_q.*
.. |image281| image:: ../assets/bingo/res_07_n.*
.. |image282| image:: ../assets/bingo/res_08_q.*
.. |image283| image:: ../assets/bingo/res_08_t.*
.. |image284| image:: ../assets/bingo/res_08_r.*
.. |image285| image:: ../assets/bingo/res_08_q.*
.. |image286| image:: ../assets/bingo/res_08_t.*
.. |image287| image:: ../assets/bingo/res_08_r.*
.. |image288| image:: ../assets/bingo/res_05_q.*
.. |image289| image:: ../assets/bingo/res_05_t.*
.. |image290| image:: ../assets/bingo/res_05_q.*
.. |image291| image:: ../assets/bingo/res_05_t.*
.. |image292| image:: ../assets/bingo/res_09_q.*
.. |image293| image:: ../assets/bingo/res_09_n.*
.. |image294| image:: ../assets/bingo/res_09_q.*
.. |image295| image:: ../assets/bingo/res_09_n.*
.. |image296| image:: ../assets/bingo/sub_aff_01q.*
.. |image297| image:: ../assets/bingo/sub_aff_01t.*
.. |image298| image:: ../assets/bingo/sub_aff_01n.*
.. |image299| image:: ../assets/bingo/sub_aff_01q.*
.. |image300| image:: ../assets/bingo/sub_aff_01t.*
.. |image301| image:: ../assets/bingo/sub_aff_01n.*
.. |image302| image:: ../assets/bingo/sub_conf_01q.*
.. |image303| image:: ../assets/bingo/sub_conf_01t.*
.. |image304| image:: ../assets/bingo/sub_conf_01n.*
.. |image305| image:: ../assets/bingo/sub_conf_01q.*
.. |image306| image:: ../assets/bingo/sub_conf_01t.*
.. |image307| image:: ../assets/bingo/sub_conf_01n.*
