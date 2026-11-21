---
kind: object
---

# Haptic endpoint

One end of a haptic connection: an atom or an attachment group of a named molecule.

## Appears in

The value of `endpoint1` and `endpoint2` of a [Haptic connection](haptic-connection.md).

## Identified by

An object with `moleculeId` and exactly one of `atomId` and `attachmentGroupId`.

## Attributes

### `moleculeId`

- Type: string
- Required: yes

Top-level key of the molecule that holds the atom or the group, for example `mol1`.

The molecule is listed in [`root.nodes`](../document-structure/root.md#nodes). The key is resolved by name, like a `$ref`.

### `atomId`

- Type: string (integer)
- Required: no

Index of the atom in that molecule’s `atoms`, written as a JSON string of decimal digits, for example `"2"`.

### `attachmentGroupId`

- Type: string
- Required: no

The `id` of an attachment group of that molecule.

## Rules

1. Exactly one of `atomId` and `attachmentGroupId` is present.
2. `moleculeId`, `atomId` and `attachmentGroupId` are JSON strings.

## Examples

- [Benzene–chromium half sandwich](../examples/haptic-half-sandwich.md)
- [Group molecule missing from root.nodes](../examples/haptic-molecule-not-listed.md)

## Related

- [Haptic connection](haptic-connection.md)
- [Attachment group](attachment-group.md)
