---
kind: object
---

# Highlight

A set of atoms or of bonds of a molecule that is shown highlighted.

## Appears in

An element of the `highlight` array of a [Molecule](molecule.md).

## Identified by

An object with `entityType` and `items`.

## Attributes

### `entityType`

- Type: string
- Required: yes
- Values: `"atoms"`, `"bonds"`

Whether `items` holds atom indexes or bond indexes.

### `items`

- Type: array of integer
- Required: yes

Indexes of the highlighted atoms in the molecule's `atoms` array, or of the highlighted bonds in its `bonds` array.

## Rules

1. `entityType` and `items` are required.
2. `items` lists each index once, and every index is an atom or a bond of the same molecule.
3. A molecule's `highlight` holds at most one element for atoms and one for bonds.

## Examples

- [Highlighted atoms and bonds](../examples/highlight.md)

## Related

- [Molecule](molecule.md)
