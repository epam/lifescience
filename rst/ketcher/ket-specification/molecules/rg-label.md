---
kind: object
match: { type: rg-label }
---

# R-group label

An R-site: an atom position that stands for an R-group, such as R1.

The R-groups themselves are defined in [R-group](../rgroups/rgroup.md) objects stored under keys `rg1`, `rg2` and so on. When the R-site lists several R-groups, any one of them may take its place.

## Appears in

An element of the `atoms` array of a [Molecule](molecule.md). Its position in the array is the atom index that bonds refer to.

## Identified by

`"type": "rg-label"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"rg-label"`

Atom type; always `rg-label`.

### `location`

- Type: array of 3 numbers
- Required: yes
- Units: KET length units (a standard bond length is 1.0)

Position of the R-site as `[x, y, z]`, with the y axis pointing up; `z` is 0 in a two-dimensional drawing.

### `$refs`

- Type: array of string
- Required: yes
- Items: at least 1
- Pattern: `^rg-([1-9]|[12][0-9]|3[0-2])$`
- Values: `rg-1` to `rg-32`

The R-groups that may take this position, each written as `rg-` and the R-group number: `"rg-1"` for R1.

### `attachmentPoints`

- Type: integer
- Required: no
- Default: `0`
- Values: [R-group attachment point flags](../enums/rgroup-attachment-bits.md)

Marks the R-site as an attachment point of the R-group member it belongs to, as on an atom.

### `attachmentOrder`

- Type: array of object
- Required: no

Which neighbour of the R-site is its first attachment, which its second, and so on; omitted when the order is that of the neighbours' indexes.

#### `attachmentOrder.attachmentAtom`

- Type: integer
- Required: yes
- Values: at least 0

Index of an atom bonded to the R-site, in the molecule's `atoms` array.

#### `attachmentOrder.attachmentId`

- Type: integer
- Required: yes
- Values: at least 0

Rank of that neighbour among the attachments of the R-site, counted from 0.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the R-site is selected. Carries no chemical meaning; written only as `true`.

## Rules

1. `type`, `location` and `$refs` are required, and `$refs` is not empty.
2. Every R-group named in `$refs` is defined in the document under the key `rg<N>` and listed in `root.nodes`.
3. An R-group label carries only the keys listed here.

## Examples

- [R-group](../examples/rgroup.md)

## Related

- [R-group](../rgroups/rgroup.md)
- [Atom](atom.md)
