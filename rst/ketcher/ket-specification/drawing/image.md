---
kind: object
match: { type: image }
---

# Image

A PNG or SVG image placed on the canvas.

## Appears in

An element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "image"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"image"`

Object type; always `image`.

### `format`

- Type: string
- Required: yes
- Values: `"image/png"`, `"image/svg+xml"`

Media type of the image data.

### `boundingBox`

- Type: object
- Required: yes

The box the image fills: its top-left corner, width and height.

`y` is the **top** edge: with the y axis pointing up, the box extends down to `y − height`.

#### `boundingBox.x`

- Type: number
- Required: yes
- Units: KET length units

Left edge.

#### `boundingBox.y`

- Type: number
- Required: yes
- Units: KET length units

Top edge.

#### `boundingBox.z`

- Type: number
- Required: no
- Default: `0`

Depth; 0 in a two-dimensional drawing.

#### `boundingBox.width`

- Type: number
- Required: yes
- Units: KET length units

Width of the box; greater than 0.

#### `boundingBox.height`

- Type: number
- Required: yes
- Units: KET length units

Height of the box; greater than 0.

### `data`

- Type: string
- Required: yes

The image file encoded in base64, without a `data:` URL prefix; at least 160 characters.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the image is selected. Carries no meaning; written only as `true`.

## Rules

1. `type`, `format`, `boundingBox` and `data` are required.
2. `boundingBox.width` and `boundingBox.height` are greater than 0.
3. `data` is plain base64 of a file in the `format`, with no `data:image/png;base64,` prefix.

## Examples

- [Image](../examples/image.md)

## Related

- [Simple object](simple-object.md)
