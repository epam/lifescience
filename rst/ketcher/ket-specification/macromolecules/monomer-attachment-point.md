---
kind: object
---

# Monomer attachment point

A point where a monomer connects to another monomer or to an atom.

The point has a name, `R1` to `R8`, given by its `label`, or derived from its `type` and position when the label is missing:

| `type` | Name when there is no `label` |
| --- | --- |
| `"left"` | `R1` |
| `"right"` | `R2` |
| `"side"` | `R3` for the first side point, `R4` for the second, and so on |
| *(absent)* | `R1` for the first point of the array, `R2` for the second, and so on |

## Appears in

An element of the `attachmentPoints` array of a [Monomer template](monomer-template.md).

## Identified by

An element of `attachmentPoints`.

## Attributes

### `attachmentAtom`

- Type: integer
- Required: yes
- Values: at least 0

Index of the atom that forms the bond, in the template's `atoms` array.

### `leavingGroup`

- Type: object
- Required: no

The atoms removed when a connection uses this point, such as the hydrogen of an amino group.

#### `leavingGroup.atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the leaving atoms, in the template's `atoms` array.

### `type`

- Type: string
- Required: no
- Values: `"left"`, `"right"`, `"side"`

Role of the point in a chain: the left end, the right end, or a side chain.

### `label`

- Type: string
- Required: no
- Pattern: `^R[1-8]$`
- Values: `R1` to `R8`

Name of the point, by which connections refer to it.

## Rules

1. `attachmentAtom` is required.
2. `type` and `label` agree: `left` is `R1`, `right` is `R2`, and `side` is `R3` or above.
3. The names of a template's attachment points are unique.
4. The leaving atoms of a point are atoms of the template, other than its `attachmentAtom`.

## Examples

- [Peptide](../examples/peptide.md)

## Related

- [Monomer template](monomer-template.md)
- [Connection endpoint](connection-endpoint.md)
