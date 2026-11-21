---
kind: object
match: { type: MUL }
---

# Multiple group

A fragment that stands for several identical copies of itself, such as the `(CH2)3` of a chain.

The molecule holds one copy of the repeated fragment, and the group says how many copies the structure has in total. A reader that expands the group adds the missing copies, and the bonds that cross the bracket join the copies into a chain.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "MUL"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"MUL"`

S-group type; always `MUL`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms of one copy of the repeated fragment, in the molecule's `atoms` array.

The other copies are not written: their atoms are not in the molecule.

### `mul`

- Type: integer
- Required: yes
- Values: 1 to 1000

Total number of copies of the fragment, the one written included.

## Rules

1. `type`, `atoms` and `mul` are required.
2. `atoms` lists each atom of one copy once; the molecule holds no other copy of the fragment.

## Gotchas

- `mul` counts all copies: `"mul": 3` with a written `CH2` stands for three `CH2` groups, not four.

## Examples

- [Multiple group](../examples/sgroup-multiple.md)

## Related

- [Structural repeating unit](sgroup-sru.md)
