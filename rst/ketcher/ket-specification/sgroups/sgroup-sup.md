---
kind: object
match: { type: SUP }
---

# Superatom

An abbreviation: a set of atoms that can be shown contracted under one name, such as `COOH` or `Ph`.

The atoms of a superatom are written in full in the molecule; the group adds the name to show instead of them. Its attachment points say which atoms bond to the rest of the structure when the abbreviation is used.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "SUP"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"SUP"`

S-group type; always `SUP`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms the abbreviation stands for, in the molecule's `atoms` array.

### `name`

- Type: string
- Required: yes

Text shown instead of the atoms when the abbreviation is contracted.

### `expanded`

- Type: boolean
- Required: no
- Default: `false`

Whether the abbreviation is shown expanded, as its atoms, rather than contracted to its name.

### `class`

- Type: string
- Required: no

Class of the abbreviation, as in the `SCL` property of MOL files.

The value is free text. The classes `SUGAR`, `BASE` and `PHOSPHATE` mark the parts of a nucleotide.

### `id`

- Type: integer
- Required: no

An identifier for the writer's own use. It carries no meaning, and a reader ignores it.

### `attachmentPoints`

- Type: array of object
- Required: no

The points where the abbreviation bonds to the rest of the structure; omitted when it has none.

#### `attachmentPoints.attachmentAtom`

- Type: integer
- Required: yes
- Values: at least 0

Index of the atom of the superatom that bonds to the outside, in the molecule's `atoms` array.

#### `attachmentPoints.leavingAtom`

- Type: integer
- Required: no
- Values: at least 0

Index of the atom removed when a bond is formed at this point, in the molecule's `atoms` array; omitted when no atom leaves.

#### `attachmentPoints.attachmentId`

- Type: string (integer)
- Required: no
- Values: at least 1

Number of the attachment point within its superatom, written as a string: `"1"` for the first point, `"2"` for the second.

## Rules

1. `type`, `atoms` and `name` are required.
2. Every `attachmentAtom` of the attachment points is one of the group's `atoms`.
3. The `attachmentId` values of the group are unique.
4. Each attachment point stands alone: a key it omits has no value, and is never taken from the previous point.

## Gotchas

- Contracting and expanding change only how the group is shown: the atoms are in the molecule in both states.

## Examples

- [Superatom](../examples/sgroup-superatom.md)
