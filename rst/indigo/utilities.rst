Indigo Utilities
================

.. toctree::
    :hidden:
    :includehidden:

    knime
    legio
    indigo-depict
    indigo-cano
    indigo-deco
    chemdiff
    service/index

Indigo service
--------------

Indigo service provides RESTful API for the following operations:
- Aromatize, dearomatize molecules and reactions
- 2D Layout for structures
- Converting formats in all directions (Molfile,Smiles,Inchi,IUPAC name,CML,etc.)
- Rendering structures from text format into images (PNG,PDF)
- Image recognition toolkit
- Calculating molecular and reaction properties

Use following `guides <service/index.html>`__ to run the service.

KNIME Nodes
-----------

We provide a number of freely available `nodes <knime.html>`__ for the
`KNIME <http://knime.org>`__ workflow engine. The nodes are based on
Indigo and its Java SDK.

Java GUI Utilities
------------------

Two Indigo-based Java GUI applications are provided:

-  `Legio <legio.html>`__ — combinatorial chemistry
-  `ChemDiff <chemdiff.html>`__ — visual comparison of two SDF or SMILES
   files

Command-Line Utilities
----------------------

Three Indigo-based command-line utilities written in plain C are
provided:

-  `indigo-depict <indigo-depict.html>`__ (former ``dingo-render``)
   Molecule and reaction rendering utility.
-  `indigo-cano <indigo-cano.html>`__ (former ``cano-utility``)
   Canonical SMILES generator.
-  `indigo-deco <indigo-deco.html>`__ (former ``deco``) R-Group
   deconvolution utility.
