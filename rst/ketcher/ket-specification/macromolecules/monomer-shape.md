---
kind: object
match: { type: monomerShape }
---

# Monomer shape

A symbol, such as an antibody or a double helix, that stands for a set of monomers.

## Appears in

A top-level value under the key `monomerShape-<id>` of the [Document](../document-structure/document.md), referenced from [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "monomerShape"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"monomerShape"`

Object type; always `monomerShape`.

### `id`

- Type: string
- Required: yes

Identifier of the shape; the shape's key is `monomerShape-` followed by it.

### `shape`

- Type: string
- Required: yes
- Values: [Monomer shape type](../enums/monomer-shape-type.md)

The symbol drawn.

### `collapsed`

- Type: boolean
- Required: yes

Whether the monomers are shown collapsed into the shape.

### `position`

- Type: [Point](../document-structure/point.md)
- Required: yes

Where the shape is placed in the drawing.

### `monomers`

- Type: array of string
- Required: yes

The top-level keys of the monomers the shape stands for, such as `monomer0`.

## Rules

1. All keys are required.
2. Every element of `monomers` is the key of a monomer of the document.
3. The shape is listed in `root.nodes`.

## Examples

- [Monomer shape](../examples/monomer-shape.md)

## Related

- [Monomer](monomer.md)
