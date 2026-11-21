---
kind: object
match: { type: DAT }
---

# Data S-group

A named data field attached to a set of atoms, such as a measured value or a comment.

A data S-group carries a name and a value as text, and says how its label is drawn. It corresponds to the `DAT` S-group of MOL files, whose `SDT`, `SDD` and `SCD` properties hold the same data.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom and bond indexes refer to that molecule's `atoms` and `bonds`.

## Identified by

`"type": "DAT"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"DAT"`

S-group type; always `DAT`.

### `atoms`

- Type: array of integer
- Required: yes

Indexes of the atoms the data refers to, in the molecule's `atoms` array; empty for data about the molecule as a whole.

### `bonds`

- Type: array of integer
- Required: no

Indexes of the bonds the data refers to, in the molecule's `bonds` array: the bonds whose two atoms are both in `atoms`.

### `context`

- Type: string
- Required: no
- Values: [Data S-group context](../enums/data-sgroup-context.md)

What the data describes: an atom, a bond, a group of atoms, or one or several fragments.

### `fieldName`

- Type: string
- Required: no
- Default: `""`

Name of the data field.

### `fieldData`

- Type: string
- Required: no
- Default: `""`

Value of the data field, as text.

### `fieldType`

- Type: string
- Required: no

Units or format of the value, as free text.

### `queryType`

- Type: string
- Required: no

Kind of data query the field takes part in, as in the `SDT` property of MOL files.

### `queryOp`

- Type: string
- Required: no

Operator of the data query, as in the `SDT` property of MOL files.

### `display`

- Type: boolean
- Required: no
- Default: `false`

Whether the label shows the units from `fieldType` after the value.

### `dataDetached`

- Type: boolean
- Required: no
- Default: `true`

Whether the label is drawn apart from the atoms, at `x` and `y`, rather than next to the first atom of the group.

### `placement`

- Type: boolean
- Required: no
- Default: `false`

Whether `x` and `y` are an offset from the first atom of the group rather than a position in the document.

### `x`

- Type: number
- Required: no
- Units: KET length units

Horizontal position of a detached label: a coordinate in the document, or an offset when `placement` is `true`.

### `y`

- Type: number
- Required: no
- Units: KET length units

Vertical position of a detached label, with the y axis pointing up: a coordinate in the document, or an offset when `placement` is `true`.

### `tag`

- Type: string
- Required: no

Tag character of the field: one character.

### `displayedChars`

- Type: integer
- Required: no
- Values: at least 1

Number of characters of the value that the label shows; omitted when it shows the whole value.

## Rules

1. `type` and `atoms` are required.
2. `bonds` lists only bonds whose two atoms are both in `atoms`.
3. `tag` is a single character.
4. Without `x` and `y`, the position of a detached label is left to the reader.

## Gotchas

- `fieldType` holds the units or format of the value, not a type code.
- `display` concerns the units only. Whether the label sits next to the atoms is `dataDetached`.
- The value is text even when it is a number: `"fieldData": "15.9"`.

## Examples

- [Data S-group](../examples/sgroup-data.md)

## Related

- [Molecule](../molecules/molecule.md)
