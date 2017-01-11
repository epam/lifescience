######################
Indigo KNIME Nodes 2.0
######################

*26 Jan 2016*

*******
Summary
*******

We are glad to announce you the new version of Indigo nodes for KNIME 3. The nodes are available via community contribution `update site <http://update.knime.org/community-contributions/3.1>`__.

This version contains a number of important changes related to internal organization:

-  Now Indigo nodes use the concept of adapter cell allowing to store several representations of entity into one cell;
-  As a result there is no need anymore to make user transform data from or to Indigo type to process input and get output. This is the reason why the nodes for transformation data are excluded. It means that the standard types (Mol, Smiles, Rxn, etc.) should be used as input and expected as output. Nodes changing input data use Indigo renderer by default;
-  Settings from the deprecated transformation nodes (e.g. "Ignore stereochemistry errors") moved into settings dialog for every nodes as this still makes sense;
-  All the functional nodes are still available. But you can find that structure of nodes in Node repository had been changed.

Beside this, six more functional nodes are available:

- Molecule Nodes category:
   -  Formula filter 
   -  Organic splitter
   -  Weight splitter

- Manipulators category:
	-  Standardizer

- Properties:
   -  Canonical SMILES  (with new Reaction support)
   -  InChi

Descriptions for this nodes are in correspondent node's descriptions.

**NOTE:** it's important to note that the new version of nodes is incompatible with previous one. All the old nodes were marked as 'deprecated' and are not supposed to be supported in KNIME 3.x and higher anymore.
So, please, use Indigo 2 nodes to create new workflows working with KNIME 3.x (to be exact 3.1 and higher). Previous version of Indigo nodes is still available under KNIME 2.x.

In the near future we plan to add more nodes based on Indigo toolkit .

Hope all that modifications and additions will be useful and you will enjoy using it.  We will greatly appreciate any comments, thoughts, notes and proposals.

 