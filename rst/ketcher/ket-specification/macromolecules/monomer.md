---
kind: object
match: { type: monomer }
---

# Monomer

One occurrence of a monomer template in the drawing.

## Appears in

A top-level value under a key such as `monomer0` of the [Document](../document-structure/document.md), referenced from [`root.nodes`](../document-structure/root.md#nodes). Connections refer to the monomer by that key.

## Identified by

`"type": "monomer"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"monomer"`

Object type; always `monomer`.

### `id`

- Type: string
- Required: yes
- Pattern: `^(0|[1-9][0-9]*)$`
- Values: a decimal integer, such as `"0"`

Identifier of the monomer, unique among the monomers of the document; written as a string.

### `templateId`

- Type: string
- Required: yes

The `id` of the [Monomer template](monomer-template.md) this monomer is an occurrence of.

### `alias`

- Type: string
- Required: yes

Symbol that labels the monomer: the template's `alias`.

### `position`

- Type: [Point](../document-structure/point.md)
- Required: yes

Where the origin of the template's coordinates is placed in the drawing.

### `seqid`

- Type: integer
- Required: no
- Values: at least 1

Number of the monomer in its chain, counted from 1; the numbering need not run from left to right in the drawing.

### `expanded`

- Type: boolean
- Required: no
- Default: `false`

Whether the monomer is shown as its full structure rather than as a symbol.

### `transformation`

- Type: object
- Required: no

How the full structure of an expanded monomer is flipped, rotated and shifted relative to its template; omitted when it is not.

The three steps apply in this order: the flip, then the rotation, then the shift. The flip and the rotation are made about the centre of the bounding box of the template's atoms.

#### `transformation.flip`

- Type: string
- Required: no
- Values: `"horizontal"`, `"vertical"`

Mirror the structure left to right (`horizontal`) or top to bottom (`vertical`); omitted for no flip.

#### `transformation.rotate`

- Type: number
- Required: no
- Default: `0`
- Units: radians

Angle of rotation, counter-clockwise with the y axis pointing up.

#### `transformation.shift`

- Type: object
- Required: no

Displacement of the structure after the rotation.

##### `transformation.shift.x`

- Type: number
- Required: yes
- Units: KET length units

Horizontal displacement.

##### `transformation.shift.y`

- Type: number
- Required: yes
- Units: KET length units

Vertical displacement, with the y axis pointing up.

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
2. `templateId` is the `id` of a monomer template of the document, and `root.templates` lists that template.
3. The monomer is listed in `root.nodes`.
4. `id` values are unique among the monomers and ambiguous monomers of the document.
5. A `transformation` has at least one of `flip`, `rotate` and `shift`.
6. A writer omits a transformation that changes nothing.

## Gotchas

- Connections refer to a monomer by its top-level key, such as `monomer0`, not by its `id`.

## Examples

- [Peptide](../examples/peptide.md)
- [Monomer connected to a molecule](../examples/monomer-to-molecule.md)

## Related

- [Monomer template](monomer-template.md)
- [Connection](connection.md)
