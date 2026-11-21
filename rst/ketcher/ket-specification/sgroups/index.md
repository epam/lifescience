# S-groups

An S-group marks a set of atoms of one molecule and gives it a meaning: a contracted abbreviation, a repeating unit of a polymer, a multiplied fragment, a data field, or a component of a query. The S-groups of a molecule are the elements of its [`sgroups`](../molecules/molecule.md#sgroups) array.

Every S-group has two keys:

- `type`, a fixed code that tells the kinds apart;
- `atoms`, the indexes of its member atoms in the molecule's `atoms` array.

The other keys depend on the kind:

| `type` | S-group |
| --- | --- |
| `"GEN"` | [Generic S-group](sgroup-gen.md): a bracket with no further meaning |
| `"MUL"` | [Multiple group](sgroup-mul.md): a fragment repeated a number of times |
| `"SRU"` | [Structural repeating unit](sgroup-sru.md): the repeating unit of a polymer |
| `"SUP"` | [Superatom](sgroup-sup.md): an abbreviation such as `COOH`; it bonds to the rest of the structure at its [attachment points](sgroup-sup.md#attachmentpoints) |
| `"DAT"` | [Data S-group](sgroup-dat.md): a named data field attached to atoms |
| `"COP"` | [Copolymer](sgroup-cop.md): the bracket of a copolymer |
| `"queryComponent"` | [Query component](sgroup-query-component.md): atoms that match within one component of the target |

The codes are case-sensitive: `"GEN"`, not `"gen"`.

## Atoms of an S-group

The atom indexes of an S-group are positions in the `atoms` array of the molecule that holds it. An S-group cannot reach atoms of another molecule, so every fragment that belongs to an S-group is written in the same molecule as the group.

A bond between an atom of the group and an atom outside it crosses the bracket. Crossing bonds follow from `atoms` and the bonds of the molecule, and are not listed in the S-group.
