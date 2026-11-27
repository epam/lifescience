---
kind: object
match: { type: COP }
---

# Copolymer

The bracket of a copolymer: a polymer built of more than one kind of unit.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "COP"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"COP"`

S-group type; always `COP`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms inside the copolymer bracket, in the molecule's `atoms` array.

### `subtype`

- Type: string
- Required: no
- Values: [Copolymer subtype](../enums/copolymer-subtype.md)

How the units follow each other: alternating, random or in blocks; omitted when not stated.

### `connectivity`

- Type: string
- Required: yes
- Values: [S-group connectivity](../enums/sgroup-connectivity.md)

How consecutive units are joined: head to tail, head to head, or either.

## Rules

1. `type`, `atoms` and `connectivity` are required.
2. `subtype` and `connectivity` are written in upper case.

## Examples

- [Copolymer](../examples/sgroup-copolymer.md)

## Related

- [Structural repeating unit](sgroup-sru.md)
