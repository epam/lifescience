#################
Indigo 1.3.0 beta
#################

*23 Dec 2016*

*******
Summary
*******


**New features and improvements**:

* Lucene/SOLR cartdridge was added
* Name to structure prototype method was added
* Updated set of rules for CIP descriptors calculations
* Updated functionality for standardize method (option ``standardize-fix-direction-wedge-bonds`` ) for redirection stereo bonds out of cycle if it is possible. `fixed <https://github.com/epam/indigo/issues/49>`__ 
* Rendering sgroups `fixed <https://github.com/epam/indigo/issues/8>`__ 
* Depict version and inchi parameters `fixed <https://github.com/epam/indigo/issues/18>`__ 
* Charged pseudos rendering `fixed <https://github.com/epam/indigo/issues/41>`__ 
* Added support of saving reactions in CDXML format `fixed <https://github.com/epam/indigo/issues/52>`__ 
* OS X 10.11 support was added
* Keeping properties for reaction monomers was `fixed <https://github.com/epam/indigo/issues/53>`__ 
* clean2d() function for "small" layout changes was implemented
* New elements up to ``Uuo`` were added
* massComposition calculation added
* Added Sgroups (GEN, MUL, SRU, SUP types) support into CML loader/saver
* Dearomatization for R-Groups was `added <https://github.com/epam/indigo/issues/61>`__ 
* Fixed issue in Molfile loader for templates loading
* Modified encode/decode from ASCII to UTF-8 for support non-Latin characters in Indigo python output
* Added support Rgroup attachment points with query features combination
* Reaction Gross formula and mass were added
* Atom to atom mapping algorithm improvement (multiple matching possibility)
* Exception handling on macOS was `fixed <https://github.com/epam/indigo/issues/42>`__ 
* Added correct alias saving into V2000 molfile
* CTAB -> SCSR transformation algorithm was modified
* add reset settings method was `added <https://github.com/epam/indigo/issues/66>`__  for Indigo  
* New methods checkValence, checkQuery were added

**Maven  Repository**


**NuGet Repository**


Indigo .NET packages now available at `Nuget <https://www.nuget.org/packages/Indigo.Net/>`__

Just add ``Indigo.Net`` as a dependency into the project.


