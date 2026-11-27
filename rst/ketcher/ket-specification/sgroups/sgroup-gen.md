---
kind: object
match: { type: GEN }
---

# Generic S-group

A bracket around a set of atoms, with no further meaning.

A generic S-group only groups its atoms; it carries no name, count or data. It corresponds to the `GEN` S-group of MOL files.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "GEN"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"GEN"`

S-group type; always `GEN`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms inside the bracket, in the molecule's `atoms` array.

## Rules

1. `type` and `atoms` are required.
2. `atoms` lists each atom once, and every index is an atom of the same molecule.

## Examples

- [Generic S-group](../examples/sgroup-generic.md)

## Related

- [Molecule](../molecules/molecule.md)
