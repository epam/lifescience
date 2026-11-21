---
kind: object
match: { with: connectionType }
---

# Connection

A bond between two monomers, or between a monomer and an atom of a molecule.

## Appears in

An element of [`root.connections`](../document-structure/root.md#connections), and of the `connections` of a [Monomer group template](../library/monomer-group-template.md).

## Identified by

An object with `connectionType`. A [Haptic connection](../haptic/haptic-connection.md) has `type` instead.

## Attributes

### `connectionType`

- Type: string
- Required: yes
- Values: [Connection type](../enums/connection-type.md)

Kind of bond: a covalent single bond or a hydrogen bond.

### `endpoint1`

- Type: [Connection endpoint](connection-endpoint.md)
- Required: yes

One end of the connection.

### `endpoint2`

- Type: [Connection endpoint](connection-endpoint.md)
- Required: yes

The other end of the connection.

### `label`

- Type: string
- Required: no

A free-text label of the connection.

### `annotation`

- Type: [Object annotation](object-annotation.md)
- Required: no

A note attached to the connection.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the connection is selected. Carries no meaning; written only as `true`.

## Rules

1. `connectionType`, `endpoint1` and `endpoint2` are required.
2. A `single` connection joins two monomer attachment points, or a monomer attachment point and an atom.
3. A `hydrogen` connection joins two monomers and names no attachment point.
4. An attachment point takes part in at most one `single` connection, and two monomers are joined by at most one connection.
5. The order of the two ends carries no meaning.

## Examples

- [Peptide](../examples/peptide.md)
- [Monomer connected to a molecule](../examples/monomer-to-molecule.md)

## Related

- [Connection endpoint](connection-endpoint.md)
- [Monomer](monomer.md)
- [Haptic connection](../haptic/haptic-connection.md)
