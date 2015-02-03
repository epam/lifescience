indigo-depict
=============

::

    Usage: indigo-depict infile.{mol,rxn,smi} outfile.{png,svg,pdf} [parameters]
           indigo-depict infile.{sdf,rdf,smi} outfile_%s.{png,svg,pdf} [parameters]
           indigo-depict infile.{sdf,rdf}.gz outfile_%s.{png,svg,pdf} [parameters]
           indigo-depict infile.smi outfile.{mol,rxn} [parameters]
           indigo-depict infile.smi outfile.{sdf} [parameters]
           indigo-depict - SMILES outfile.{png,svg,pdf} [parameters]
           indigo-depict - SMILES outfile.{mol,rxn} [parameters]

    Parameters:
    -w 
       Picture width in pixels
    -h 
       Picture height in pixels
    -bond 
       Average bond length in pixels (conflicts with -w and -h)
    -margins  
       Horizontal and vertical margins, in pixels. No margins by default
    -commentmargins  
       Horizontal and vertical margins around comment. No margins by default
    -thickness 
       Set relative thickness factor. Default is 1.0
    -hydro 
       Set implicit hydrogen display mode (default is terminalhetero)
    -label 
       Set atom label display mode (default is normal)
    -[de]arom
       Force [de]aromatization
    -stereo 
       Stereogroups display mode (default is 'old')
    -cdbwsa
       Center double bonds which have an adjacent stereo bond (disabled by default)
    -query
       Treat the input as a query molecule or reaction (disabled by default)
    -idfield 
       SDF/RDF field to be put in place of '%s' in the names of saved files
       (default is molecule/reaction number)
    -comment 
       Text comment to be put above the molecule or reaction. No default value
    -commentfield 
       Use specified SDF/RDF field as a comment
    -commentname
       Use molecule/reaction name as a comment
    -commentsize 
       Text comment font size factor relative to bond thickness (default 6)
    -commentpos 
       Text comment position (bottom by default)
    -commentalign 
       Text comment alignment (center by default)
    -coloring 
       Enable/disable coloring (enabled by default)
    -hlthick
       Enable highlighting with thick lines and bold characters
    -hlcolor   
       Enable highlighting with color. Component values must be in range [0..255]
    -bgcolor   
       Set the background color. Component values must be in range [0..255]
    -basecolor   
       Set the default foreground color. Component values must be in range [0..255]
    -aamcolor   
       Set the color of AAM indices. Component values must be in range [0..255]
    -commentcolor   
       Set the color of the comment. Component values must be in range [0..255]
    -atomnumbers
       Show atom numbers (for debugging purposes only)
    -bondnumbers
       Show bond numbers (for debugging purposes only)
    -help
       Print this help message

    Examples:
       indigo-depict infile.mol outfile.png -coloring off -arom
       indigo-depict database.sdf molecule_%s.png -idfield cdbregno -thickness 1.1
       indigo-depict database.smi database.sdf
       indigo-depict - "CC.[O-][*-]([O-])=O" query.png -query
       indigo-depict - "OCO>>CC(C)N" reaction.rxn

