---
kind: object
---

# Text font

Font family and size of a text object, a paragraph or a part.

Colour and the style flags are not part of the font: they are keys of their own next to `font`.

## Appears in

The value of the `font` key of a [Text](text-v2.md) object, of a [Text paragraph](text-paragraph.md) and of a [Text part](text-part.md).

## Identified by

A plain object. A key set on an inner level overrides the outer ones: part over paragraph over text object.

## Attributes

### `family`

- Type: string
- Required: no

Font family name, for example `Arial`.

### `size`

- Type: integer
- Required: no
- Units: px

Font size in pixels.

## Rules

1. `font` holds only `family` and `size`.

## Related

- [Text](text-v2.md)
- [Text paragraph](text-paragraph.md)
- [Text part](text-part.md)
