---
kind: object
---

# Text paragraph

One paragraph of a text object: its alignment, default style and parts.

## Appears in

An element of the `paragraphs` array of a [Text](text-v2.md) object.

## Identified by

A plain object with a `parts` array.

## Attributes

### `parts`

- Type: array of [Text part](text-part.md)
- Required: yes

Runs of characters with their styles, in reading order; empty for an empty paragraph.

### `alignment`

- Type: string
- Required: no
- Values: [Text alignment](../enums/text-alignment.md)

Alignment of the paragraph, overriding the alignment of the text object.

### `indent`

- Type: number
- Required: no
- Units: KET length units

Indentation of the paragraph, overriding the indentation of the text object.

### `font`

- Type: [Text font](text-font.md)
- Required: no

Default font of the paragraph’s parts.

### `color`

- Type: string
- Required: no
- Values: `#RRGGBB` or `#RGB`
- Pattern: `^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$`

Default colour of the paragraph’s parts.

### `bold`

- Type: boolean
- Required: no
- Default: `false`

Bold default for the paragraph’s parts.

### `italic`

- Type: boolean
- Required: no
- Default: `false`

Italic default for the paragraph’s parts.

### `subscript`

- Type: boolean
- Required: no
- Default: `false`

Subscript default for the paragraph’s parts.

### `superscript`

- Type: boolean
- Required: no
- Default: `false`

Superscript default for the paragraph’s parts.

### `lineStarts`

- Type: array of integer
- Required: no

Character offsets at which the writer broke the paragraph into lines.

Informational: a reader may lay the paragraph out again within the bounding box.

## Related

- [Text](text-v2.md)
- [Text part](text-part.md)
- [Text font](text-font.md)
