####################
Standardize options
####################


.. indigo_option::
    :name: standardize-stereo
    :type: boolean
    :short: Sets or repairs the stereo on a molecule.
    :default: false

.. indigo_option::
    :name: standardize-charges
    :type: boolean
    :short: Sets the charges on a molecule to a standard form.
    :default: false

.. indigo_option::
    :name: standardize-center-molecule
    :type: boolean
    :short: Translates a molecule so its geometric center lies at the origin.
    :default: false

.. indigo_option::
    :name: standardize-remove-single-atoms
    :type: boolean
    :short: Removes fragments that consist of only a single heavy atom.
    :default: false

.. indigo_option::
    :name: standardize-keep-smallest
    :type: boolean
    :short: Keeps only the smallest fragment in the molecule.
    :default: false

.. indigo_option::
    :name: standardize-keep-largest
    :type: boolean
    :short: Keeps only the largest fragment in the molecule.
    :default: false

.. indigo_option::
    :name: standardize-remove-largest
    :type: boolean
    :short: Removes the largest fragment in the molecule.
    :default: false

.. indigo_option::
    :name: standardize-make-non-h-to-c-atoms
    :type: boolean
    :short: Converts all non-Hydrogen atoms atoms in the molecule to carbon.
    :default: false

.. indigo_option::
    :name: standardize-make-non-h-to-a-atoms
    :type: boolean
    :short: Converts all non-Hydrogen atoms in the molecule to the A query atom type.
    :default: false

.. indigo_option::
    :name: standardize-make-non-h-c-to-q-atoms
    :type: boolean
    :short: Converts all non-Carbon, non-Hydrogen atoms in the molecule to the Q query atom type.
    :default: false

.. indigo_option::
    :name: standardize-make-all-bonds-single
    :type: boolean
    :short: Converts all bonds in the molecule to single bonds.
    :default: false

.. indigo_option::
    :name: standardize-clear-coordinates
    :type: boolean
    :short: Sets all x, y, z coordinates to zero.
    :default: false

.. indigo_option::
    :name: standardize-straighten-triple-bonds
    :type: boolean
    :short: Finds atoms with triple bonds and non-linear geometry and fixes them so that the bond angles are 180 degrees.
    :default: false

.. indigo_option::
    :name: standardize-straighten-allens
    :type: boolean
    :short: Finds atoms with two double-bonds and non-linear geometry and fixes them so that the bond angles are 180 degrees.
    :default: false

.. indigo_option::
    :name: standardize-clear-molecule
    :type: boolean
    :short: Deletes all atoms and bonds in the molecule, keeping the molecule object in the data record.
    :default: false

.. indigo_option::
    :name: standardize-clear-stereo
    :type: boolean
    :short: Sets all atoms and bonds to NoStereo.
    :default: false

.. indigo_option::
    :name: standardize-clear-enhanced-stereo
    :type: boolean
    :short: Removes all relative stereo groupings.
    :default: false

.. indigo_option::
    :name: standardize-clear-unknown-stereo
    :type: boolean
    :short: Sets all atoms and bonds marked UnknownStereo to NoStereo.
    :default: false

.. indigo_option::
    :name: standardize-clear-unknown-atom-stereo
    :type: boolean
    :short: Sets all atoms marked UnknownStereo to NoStereo.
    :default: false

.. indigo_option::
    :name: standardize-clear-unknown-bond-stereo
    :type: boolean
    :short: Sets all bonds marked UnknownStereo to NoStereo.
    :default: false

.. indigo_option::
    :name: standardize-clear-cis-trans
    :type: boolean
    :short: Sets all bonds marked CisStereo or TransStereo to UnknownStereo.
    :default: false

.. indigo_option::
    :name: standardize-stereo-from-coordinates
    :type: boolean
    :short: Uses 2D coordinates and up/down bond markings (or 3D coordinates) to assign the stereochemistry of the atoms or bonds.
    :default: false

.. indigo_option::
    :name: standardize-reposition-stereo-bonds
    :type: boolean
    :short: Repositions the stereo bond markings in an attempt to find the best bond to mark as a wedge bond for each stereo atom.
    :default: false

.. indigo_option::
    :name: standardize-reposition-axial-stereo-bonds
    :type: boolean
    :short: Repositions the stereo bond markings for axial stereo centers (allenes and atropisomers) in an attempt to find the best bond to mark as a wedge bond for each center.
    :default: false

.. indigo_option::
    :name: standardize-fix-direction-wedge-bonds
    :type: boolean
    :short: Checks the wedge bonds in the molecule to ensure that the wedge is drawn with the stereo atom at the narrow end of the wedge.
    :default: false

.. indigo_option::
    :name: standardize-clear-charges
    :type: boolean
    :short: Sets all formal charges to zero.
    :default: false

.. indigo_option::
    :name: standardize-highlight-colors
    :type: boolean
    :short: Clears any highlight colors from atoms and bonds.
    :default: false

.. indigo_option::
    :name: standardize-neutralize-zwitterions
    :type: boolean
    :short: Converts directly bonded zwitterions (positively charged atom bonded to negatively charged atom, A+B-) to the neutral representation (A=B).
    :default: false

.. indigo_option::
    :name: standardize-clear-unusual-valences
    :type: boolean
    :short: Clears any atom valence query features and resets all implicit hydrogen counts to their standard values.
    :default: false

.. indigo_option::
    :name: standardize-clear-isotopes
    :type: boolean
    :short: Clears all isotope markings from atoms.
    :default: false

.. indigo_option::
    :name: standardize-clear-dative-bonds
    :type: boolean
    :short: Clears all explicit zero-order coordination bonds of dative type (V3000 type-9 bonds).
    :default: false

.. indigo_option::
    :name: standardize-clear-hydrogen-bonds
    :type: boolean
    :short: Clears all explicit zero-order hydrogen bonds (V3000 type-10 bonds).
    :default: false

.. indigo_option::
    :name: standardize-create-dative-bonds
    :type: boolean
    :short: Create coordination bond (zero-order bond) instead of wrong co-valent bond.
    :default: false

.. indigo_option::
    :name: standardize-create-hydrogen-bonds
    :type: boolean
    :short: Create hydrogen bond (zero-order bond) instead of wrong co-valent bond.
    :default: false

