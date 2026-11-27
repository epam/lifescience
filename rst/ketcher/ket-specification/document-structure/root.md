---
kind: object
---

# Root

The contents of the document: the nodes it shows, and the connections and templates they use.

## Appears in

The value of the `root` key of the [Document](document.md).

## Identified by

A plain object with a `nodes` array.

## Attributes

### `nodes`

- Type: array of one of [Node reference](node-ref.md), [Arrow](../drawing/arrow.md), [Plus](../drawing/plus.md), [Simple object](../drawing/simple-object.md), [Text](../text/text-v2.md), [KET 1.0 text](../text/text-v1.md), [Image](../drawing/image.md), [Multi-tailed arrow](../drawing/multi-tailed-arrow.md)
- Required: yes

What the document shows: references to molecules, R-groups and monomers, and inline drawing objects.

The order of the nodes carries no meaning, except that it numbers the molecule keys (see the `mol<N>` key of the [Document](document.md)).

### `connections`

- Type: array of one of [Connection](../macromolecules/connection.md), [Haptic connection](../haptic/haptic-connection.md)
- Required: no

Bonds that are not edges of a molecule: bonds between monomers, between monomers and atoms, and haptic bonds.

### `templates`

- Type: array of [Node reference](node-ref.md)
- Required: no

References to the monomer templates, ambiguous monomer templates and monomer group templates the document holds.

### `annotation`

- Type: object
- Required: no

Annotation of the document as a whole, as the extended annotation section of HELM.

#### `annotation.extended`

- Type: any
- Required: yes

The extended annotation as a JSON value, kept as it is.

## Rules

1. `nodes` is required.

## Examples

- [Atom properties](../examples/atom-properties.md)
- [Benzene–chromium half sandwich](../examples/haptic-half-sandwich.md)

## Related

- [Document](document.md)
- [Node reference](node-ref.md)
- [Object annotation](../macromolecules/object-annotation.md)
