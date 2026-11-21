# Molecules

A [Molecule](molecule.md) is a molecular graph stored under a top-level key `mol<N>` and listed in [`root.nodes`](../document-structure/root.md#nodes) as `{"$ref": "mol<N>"}`. Its atoms are an array, and the position of an atom in that array is the index that bonds, S-groups, attachment groups and connections refer to.

An element of [`atoms`](molecule.md#atoms) is one of three objects, told apart by its `type`:

| `type` | Object |
| --- | --- |
| absent | [Atom](atom.md): a chemical element, a pseudo-atom or a query atom |
| `"rg-label"` | [R-group label](rg-label.md): an R-site, such as R1 |
| `"atom-list"` | [Atom list](atom-list.md): a query atom that matches any element of a list, or any element not in it |

The other objects of a molecule:

- [Atom query properties](query-properties.md) — further search constraints on an atom, or a whole atom query written as SMARTS.
- [Bond](bond.md) — a bond between two atoms of the molecule, or a query bond.
- [Stereo flag position](stereo-flag-position.md) — where the enhanced stereochemistry label of the molecule is drawn.
- [Property](property.md) — a named text value attached to the molecule, such as a data field of an SD file record.
- [Highlight](highlight.md) — a set of atoms or of bonds of the molecule shown highlighted.

The S-groups of a molecule are described in [S-groups](../sgroups/index.md), and its attachment groups in [Haptic bonds](../haptic/index.md).
