indigo-deco
===========

::

    Usage:
      indigo-deco files [options]
    Perfoms molecule scaffold detection and R-group deconvolution
    Accepted formats are: Molfile, SDFile, RDFile, SMILES
    Options:
    -h         print this help message
    -a         calculate approximate scaffold (default is exact)
    -s   write maximum found scaffold to molfile
    -S   write all found scaffolds to SD-file
    -d   do not calculate scaffold, but load it from file
    -o   write resulting highlighted molecules to file
    -r   write resulting molecules with separated r-groups to file
    -na        no aromatic consideration
    --         marks end of options

    Examples:

    indigo-deco *.mol -o hl.sdf -s scaf.sdf
      read molecules from molfiles in the current directory
      save maximum found scaffold to scaf.mol
      save highlighted molecules to hl.sdf
    indigo-deco structure.mol many.sdf -s scaf.mol -S allscafs.sdf -r rg.sdf 
      read one molecule from structure.mol and multiple molecules from many.sdf
      save molecules with r-rgoups to rg.sdf
      save all found scaffolds to allscafs.sdf
    indigo-deco *.smi -d readyscaf.mol -o hl.sdf
      read multiple molecules from every SMILES file in the current directory
      read scaffold from readyscaf.mol
      save highlighted molecules to hl.sdf

