indigo-cano
===========

::

    Usage:
      indigo-cano filename.{mol,smi,sdf,sdf.gz,rdf,rdf.gz} [parameters]
      indigo-cano - SMILES [parameters]
    Parameters:
      -smiles          Output canonical SMILES (default)
      -layered         Output canonical layered code
      -id      ID field in SDF file
      -no-arom         Do not aromatize molecules
      -no-tetrahedral  Ignore tetrahedral stereocenters
      -no-cistrans     Ignore cis-trans bonds information
    Examples:
       indigo-cano infile.sdf
       indigo-cano infile.sdf.gz -id molregno > results.txt
       indigo-cano infile.smi -layered -no-cistrans
       indigo-cano - 'NC1C=CC(O)=CC=1'

