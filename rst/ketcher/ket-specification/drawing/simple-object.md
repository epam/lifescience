---
kind: object
match: { type: simpleObject }
---

# Simple object

A line, rectangle or ellipse drawn on the canvas.

## Appears in

An element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "simpleObject"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"simpleObject"`

Object type; always `simpleObject`.

### `data`

- Type: object
- Required: yes

The shape and its geometry.

#### `data.mode`

- Type: string
- Required: yes
- Values: [Simple object mode](../enums/simple-object-mode.md)

Which shape is drawn.

#### `data.pos`

- Type: array of [Point](../document-structure/point.md)
- Required: yes
- Items: exactly 2

Two points that define the shape: the start and the end of a line, or two opposite corners of a rectangle or of the rectangle that bounds an ellipse.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the shape is selected. Carries no meaning; written only as `true`.

## Rules

1. `type`, `data.mode` and `data.pos` are required, and `data.pos` holds exactly two points.

## Examples

- [Simple objects](../examples/simple-objects.md)

## Related

- [Point](../document-structure/point.md)
