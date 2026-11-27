---
kind: object
---

# Text part

A run of characters of a paragraph that share one style.

## Appears in

An element of the `parts` array of a [Text paragraph](text-paragraph.md). The paragraph’s text is the concatenation of its parts.

## Identified by

A plain object with a `text` key.

## Attributes

### `text`

- Type: string
- Required: yes

The characters of the run; not empty.

### `font`

- Type: [Text font](text-font.md)
- Required: no

Font of the run, overriding the paragraph’s font.

### `color`

- Type: string
- Required: no
- Values: `#RRGGBB` or `#RGB`
- Pattern: `^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$`

Colour of the run, overriding the paragraph’s colour.

### `bold`

- Type: boolean
- Required: no
- Default: `false`

Bold run.

### `italic`

- Type: boolean
- Required: no
- Default: `false`

Italic run.

### `subscript`

- Type: boolean
- Required: no
- Default: `false`

Subscript run.

### `superscript`

- Type: boolean
- Required: no
- Default: `false`

Superscript run.

## Related

- [Text paragraph](text-paragraph.md)
- [Text font](text-font.md)
