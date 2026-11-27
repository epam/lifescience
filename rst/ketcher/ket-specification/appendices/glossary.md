---
kind: glossary
---

# Glossary

- **KET**: A JSON format for chemical structures: molecules and query molecules, reactions, drawing objects, macromolecules and haptic bonds.
- **Document**: One KET file: a JSON object with a `root` key.
- **Writer**: A program that produces KET documents.
- **Reader**: A program that consumes KET documents.
- **Node**: An element of `root.nodes`: a reference to a molecule, R-group or monomer, or an inline drawing object.
- **Attachment group** (AG): A set of atoms of one molecule that bonds to a metal as a whole in a haptic bond.
- **Haptic bond**: A bond between a metal and several contiguous atoms of a ligand at once, as in ferrocene; in KET, a connection with `"type": "haptic"`.
- **S-group**: A set of atoms of one molecule with a meaning of its own: an abbreviation, a repeating unit, a data field and others; an element of a molecule's `sgroups`.
- **Superatom**: An S-group that can be shown contracted under one name, such as `COOH`.
- **Query molecule**: A structure used as a search pattern. A document that uses a key marked Query describes a query molecule.
- **KET length unit**: The unit of coordinates and lengths. Writers lay structures out with a standard bond length of 1.0.
