---
kind: object
---

# Attachment group

A set of atoms of one molecule that bonds to a metal as a whole, such as the π system of a cyclopentadienyl ring.

An attachment group is one end of a [Haptic connection](haptic-connection.md). It stores no coordinates: a reader that draws the bond computes the group’s centre from the positions of its atoms.

A group may exist without a haptic connection that uses it.

## Appears in

An element of the `attachmentGroups` array of a [Molecule](../molecules/molecule.md). Its atom indexes refer to that molecule’s `atoms`.

## Identified by

An object with `id` and `atoms`.

## Attributes

### `id`

- Type: string
- Required: yes

Identifier of the group, unique among the groups of its molecule; haptic endpoints refer to it.

The value identifies the group within the document and carries no other meaning.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 2

Indexes of the member atoms in the molecule’s `atoms` array; at least two, each listed once.

### `charge`

- Type: integer
- Required: no
- Default: `0`

Charge of the π system as a whole; omitted when it is 0.

The charge belongs to the group, not to its atoms: it is never distributed over them, and it takes no part in the gross formula, the molecular weight or the valence of the atoms. In MOL V3000 files the same charge is the `CHG` property of the `*` atom that marks the group’s centre.

### `radical`

- Type: integer
- Required: no
- Default: `0`
- Values: [Radical](../enums/radical.md)

Radical state of the π system as a whole, encoded like an atom’s `radical`; omitted when it is 0.

In MOL V3000 files the same state is the `RAD` property of the `*` atom that marks the group’s centre.

## Rules

1. `id` is a JSON string, unique among the attachment groups of the molecule.
2. `atoms` holds at least two different indexes of atoms of the same molecule.
3. The molecule that holds the group is listed in `root.nodes`.

## Gotchas

- Group ids are local to the document: a writer may renumber the groups, so an id is not a stable reference from outside the file.

## Examples

- [Benzene–chromium half sandwich](../examples/haptic-half-sandwich.md)
- [Attachment group without a connection](../examples/haptic-group-only.md)
- [Charged attachment group](../examples/haptic-group-charge.md)

## Related

- [Haptic connection](haptic-connection.md)
- [Haptic endpoint](haptic-endpoint.md)
- [Molecule](../molecules/molecule.md)
- [Atom](../molecules/atom.md)
