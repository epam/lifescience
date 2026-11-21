---
kind: object
match: { type: ambiguousMonomer }
---

# Ambiguous monomer

One occurrence of an ambiguous monomer template in the drawing.

## Appears in

A top-level value under a key such as `monomer0` of the [Document](../document-structure/document.md), referenced from [`root.nodes`](../document-structure/root.md#nodes). Connections refer to it by that key, as to a monomer.

## Identified by

`"type": "ambiguousMonomer"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"ambiguousMonomer"`

Object type; always `ambiguousMonomer`.

### `id`

- Type: string
- Required: yes
- Pattern: `^(0|[1-9][0-9]*)$`
- Values: a decimal integer, such as `"0"`

Identifier of the monomer, unique among the monomers of the document; written as a string.

### `templateId`

- Type: string
- Required: yes

The `id` of the [Ambiguous monomer template](ambiguous-monomer-template.md) this monomer is an occurrence of.

### `alias`

- Type: string
- Required: yes

Symbol that labels the monomer: the template's `alias`.

### `position`

- Type: [Point](../document-structure/point.md)
- Required: yes

Where the monomer is placed in the drawing.

### `seqid`

- Type: integer
- Required: no
- Values: at least 1

Number of the monomer in its chain, counted from 1.

### `annotation`

- Type: [Object annotation](object-annotation.md)
- Required: no

A note attached to the monomer.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the monomer is selected. Carries no meaning; written only as `true`.

## Rules

1. `type`, `id`, `templateId`, `alias` and `position` are required.
2. `templateId` is the `id` of an ambiguous monomer template of the document.
3. The monomer is listed in `root.nodes`.

## Examples

- [Ambiguous monomer](../examples/ambiguous-monomer.md)

## Related

- [Ambiguous monomer template](ambiguous-monomer-template.md)
- [Monomer](monomer.md)
