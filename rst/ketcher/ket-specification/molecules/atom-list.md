---
kind: object
match: { type: atom-list }
query: true
---

# Atom list

A query atom that matches any element of a list, or any element not in it.

## Appears in

An element of the `atoms` array of a [Molecule](molecule.md) that describes a query. Its position in the array is the atom index that bonds refer to.

## Identified by

`"type": "atom-list"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"atom-list"`

Atom type; always `atom-list`.

### `location`

- Type: array of 3 numbers
- Required: yes
- Units: KET length units (a standard bond length is 1.0)

Position of the atom as `[x, y, z]`, with the y axis pointing up; `z` is 0 in a two-dimensional drawing.

### `elements`

- Type: array of string
- Required: yes
- Items: at least 1

Symbols of the elements in the list, such as `"N"` and `"O"`.

### `notList`

- Type: boolean
- Required: no
- Default: `false`

Whether the atom matches the elements not in the list, rather than those in it.

### `attachmentPoints`

- Type: integer
- Required: no
- Default: `0`
- Values: [R-group attachment point flags](../enums/rgroup-attachment-bits.md)

Marks the atom as an attachment point of the R-group member it belongs to, as on an atom.

## Rules

1. `type`, `location` and `elements` are required.
2. `elements` holds element symbols, each once: no generic labels, pseudo-atoms, `D` or `T`.
3. A molecule with an atom list describes a query.

## Examples

- [Atom list](../examples/atom-list.md)

## Related

- [Atom](atom.md)
- [Atom query properties](query-properties.md)
