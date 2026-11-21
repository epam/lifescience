---
kind: object
match: { type: text, with: data }
---

# KET 1.0 text

A text box in the form of KET 1.0: a Draft.js document serialised into a string.

Writers of KET 2.0 write the structured [Text](text-v2.md) form; readers accept both. The two are `"type": "text"` nodes, and the presence of `data` tells them apart.

## Appears in

An inline element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "text"` with a `data` key.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"text"`

Object type; always `text`.

### `data`

- Type: object
- Required: yes

The content and the position of the text.

#### `data.content`

- Type: string
- Required: yes

The text and its styles: a Draft.js raw content state, serialised as JSON into this string.

The serialised object has a `blocks` array, one block per paragraph, and an `entityMap` object, which is empty. Of a block, these keys carry meaning:

| Key | Meaning |
| --- | --- |
| `text` | The characters of the paragraph. |
| `inlineStyleRanges` | The styled runs of the paragraph: objects with `offset`, `length` and `style`. |
| `inlineStyleRanges[].offset` | Where the run starts, in UTF-16 code units from the start of `text`. |
| `inlineStyleRanges[].length` | Length of the run, in UTF-16 code units. |
| `inlineStyleRanges[].style` | `BOLD`, `ITALIC`, `SUBSCRIPT`, `SUPERSCRIPT`, or `CUSTOM_FONT_SIZE_<N>px` for a font size of N pixels. |

The other keys of a block — `key`, `type`, `depth`, `entityRanges` and `data` — carry no meaning for KET.

#### `data.position`

- Type: [Point](../document-structure/point.md)
- Required: yes

Top-left corner of the text box.

#### `data.pos`

- Type: array of [Point](../document-structure/point.md)
- Required: no
- Items: exactly 4

Corners of the text box: top-left, bottom-left, bottom-right, top-right.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the text is selected. Carries no meaning; written only as `true`.

## Rules

1. `type`, `data.content` and `data.position` are required.
2. `data.content` is a JSON object serialised into a string, with a `blocks` array.
3. `data.pos`, when present, holds the four corners of the box, and its first point equals `data.position`.

## Gotchas

- Style offsets count UTF-16 code units, as JavaScript strings do: a character outside the Basic Multilingual Plane counts as two.

## Examples

- [Text in the KET 1.0 form](../examples/text-v1.md)

## Related

- [Text](text-v2.md)
- [Point](../document-structure/point.md)
