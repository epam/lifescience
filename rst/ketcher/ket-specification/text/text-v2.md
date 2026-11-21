---
kind: object
match: { type: text, without: data }
since: 2.0.0
---

# Text

A styled, multi-paragraph text box on the canvas.

Styles cascade: a key set on the text object is the default for its paragraphs, a key set on a paragraph the default for its parts. A part’s own keys win.

This structured form was introduced by KET 2.0. The [KET 1.0 text](text-v1.md) form wraps a serialised Draft.js document in a `data` key instead; both are `"type": "text"` nodes, and the presence of `data` tells them apart.

## Appears in

An inline element of [`root.nodes`](../document-structure/root.md#nodes); it has no top-level key of its own.

## Identified by

`"type": "text"` with `boundingBox` and `paragraphs`, and without `data`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"text"`

Node type; always `text`.

### `boundingBox`

- Type: object
- Required: yes

The box the text is laid out in: its top-left corner, width and height.

`y` is the **top** edge: with the y axis pointing up, the box extends down to `y − height`.

#### `boundingBox.x`

- Type: number
- Required: yes

Left edge.

#### `boundingBox.y`

- Type: number
- Required: yes

Top edge.

#### `boundingBox.z`

- Type: number
- Required: no

Depth; 0 in a two-dimensional drawing.

#### `boundingBox.width`

- Type: number
- Required: yes
- Values: at least 0

Width of the box.

#### `boundingBox.height`

- Type: number
- Required: yes
- Values: at least 0

Height of the box.

### `paragraphs`

- Type: array of [Text paragraph](text-paragraph.md)
- Required: yes

The paragraphs of the text, top to bottom.

### `alignment`

- Type: string
- Required: no
- Values: [Text alignment](../enums/text-alignment.md)

Default alignment of the paragraphs.

### `indent`

- Type: number
- Required: no
- Units: KET length units

Default indentation of the paragraphs.

### `font`

- Type: [Text font](text-font.md)
- Required: no

Default font of the whole text.

### `color`

- Type: string
- Required: no
- Values: `#RRGGBB` or `#RGB`
- Pattern: `^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$`

Default colour of the whole text.

### `bold`

- Type: boolean
- Required: no
- Default: `false`

Bold default for the whole text.

### `italic`

- Type: boolean
- Required: no
- Default: `false`

Italic default for the whole text.

### `subscript`

- Type: boolean
- Required: no
- Default: `false`

Subscript default for the whole text.

### `superscript`

- Type: boolean
- Required: no
- Default: `false`

Superscript default for the whole text.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the text is selected. Carries no meaning for the drawing; written only as `true`.

## Rules

1. `boundingBox` and `paragraphs` are required, and every paragraph has `parts`.
2. The object has no `data` key.
3. The document declares `"ket_version": "2.0.0"`.

## Examples

- [Styled text in the KET 2.0 form](../examples/text-v2-styled.md)

## Related

- [Text paragraph](text-paragraph.md)
- [Text part](text-part.md)
- [Text font](text-font.md)
- [Document](../document-structure/document.md)
