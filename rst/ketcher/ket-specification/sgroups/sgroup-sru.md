---
kind: object
match: { type: SRU }
---

# Structural repeating unit

The repeating unit of a polymer, drawn in brackets with a label such as `n`.

The molecule holds one unit. The bonds that cross the bracket join a unit to the next one, and the number of units is unknown or not stated.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "SRU"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"SRU"`

S-group type; always `SRU`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms of one repeating unit, in the molecule's `atoms` array.

### `subscript`

- Type: string
- Required: no

Label shown at the closing bracket for the number of units, such as `n`.

### `connectivity`

- Type: string
- Required: yes
- Values: [S-group connectivity](../enums/sgroup-connectivity.md)

How consecutive units are joined: head to tail, head to head, or either.

## Rules

1. `type`, `atoms` and `connectivity` are required.
2. `connectivity` is one of `"HT"`, `"HH"` and `"EU"`, in upper case.

## Gotchas

- Write `subscript` even when it is `n`: a reader may show a missing subscript as `n` or show none.

## Examples

- [Structural repeating unit](../examples/sgroup-repeating-unit.md)

## Related

- [Copolymer](sgroup-cop.md)
- [Multiple group](sgroup-mul.md)
