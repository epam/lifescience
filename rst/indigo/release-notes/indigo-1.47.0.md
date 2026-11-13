# Indigo 1.47.0
Released 2026-11-12

## Features
* #228 - Support reading custom properties from SDF files during indexing in Bingo Elastic
* #3758 - Add isotope validation to Structure Check
* #3778 - Update the isoelectric point calculation for peptides

## Bugfixes and improvements
* #1256 - Inability to save a structure with R-Group in the SDF file format
* #3640 - Escaped characters in SGroup labels in CXSMILES not properly handled 
* #3759 - Wrong connection on import mol contains atom with some ap
* #3766 - Create PtrReusablePool that is a full replacement for ObjPool and PtrPool
* #3823 - valence-mode option has no impact on fold/unfold hydrogens operation


**Full Changelog**: https://github.com/epam/Indigo/compare/indigo-1.46.0-rc.1...indigo-1.47.0