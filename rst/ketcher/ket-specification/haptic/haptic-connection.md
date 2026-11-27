---
kind: object
match: { type: haptic }
---

# Haptic connection

A haptic bond between an atom and an attachment group, or between two atoms.

A haptic bond is not an edge of the molecular graph: it never appears in `bonds`. Because its ends name molecules by key, it can join atoms of different molecules.

An atom or a group may take part in several haptic connections, as the iron atom of ferrocene does.

## Appears in

An element of [`root.connections`](../document-structure/root.md#connections), next to monomer [connections](../macromolecules/connection.md).

## Identified by

`"type": "haptic"`. A monomer [Connection](../macromolecules/connection.md) carries `connectionType` instead.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"haptic"`

Connection kind; always `haptic`.

### `endpoint1`

- Type: [Haptic endpoint](haptic-endpoint.md)
- Required: yes

One end of the bond.

### `endpoint2`

- Type: [Haptic endpoint](haptic-endpoint.md)
- Required: yes

The other end of the bond.

The order of the two ends carries no meaning.

## Rules

1. At least one end is an atom: two attachment groups are never joined.
2. An atom is not joined to an attachment group it belongs to.
3. The two atoms of an atom-to-atom connection are different atoms.

## Examples

- [Benzene–chromium half sandwich](../examples/haptic-half-sandwich.md)
- [Atom-to-atom haptic bond](../examples/haptic-atom-atom.md)
- [A haptic connection between two groups](../examples/haptic-group-group.md)
- [Group molecule missing from root.nodes](../examples/haptic-molecule-not-listed.md)

## Related

- [Attachment group](attachment-group.md)
- [Haptic endpoint](haptic-endpoint.md)
