---
kind: object
match: { type: arrow }
---

# Arrow

A reaction arrow, or another arrow of a drawing, from a tail point to a head point.

The `mode` sets the kind of arrow: an ordinary reaction arrow, an equilibrium, a failed or retrosynthetic step, or an arc.

## Appears in

An element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "arrow"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"arrow"`

Object type; always `arrow`.

### `data`

- Type: object
- Required: yes

The kind and the geometry of the arrow.

#### `data.mode`

- Type: string
- Required: yes
- Values: [Arrow mode](../enums/arrow-mode.md)

Kind of arrow.

#### `data.pos`

- Type: array of [Point](../document-structure/point.md)
- Required: yes
- Items: exactly 2

The tail of the arrow, then its head.

#### `data.height`

- Type: number
- Required: no
- Units: KET length units

Height of an elliptical arc arrow: how far the arc bulges from the straight line between tail and head.

The arc is half of an ellipse whose axes are the tail–head distance and twice the absolute height. A positive height puts the arc on the left of the direction from tail to head, a negative one on the right.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the arrow is selected. Carries no meaning; written only as `true`.

## Rules

1. `type`, `data.mode` and `data.pos` are required, and `data.pos` holds exactly two points.
2. `data.height` is present for the four `elliptical-arc-arrow-…` modes and absent for the others.

## Examples

- [Reaction](../examples/reaction.md)
- [Arrow modes](../examples/arrow-modes.md)

## Related

- [Plus](plus.md)
- [Multi-tailed arrow](multi-tailed-arrow.md)
- [Point](../document-structure/point.md)
