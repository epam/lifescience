# Text

A text object is a label placed on the drawing: a caption, reaction conditions, a note. It is a box of paragraphs; a paragraph is a sequence of parts, and a part is a run of characters written in one style.

The style of a part is made of three kinds of keys:

- `font` — the font family and size, see [Text font](text-font.md);
- `color` — the colour of the characters, written next to `font`, not inside it;
- `bold`, `italic`, `subscript` and `superscript` — the style flags.

Each of them can be set on the [Text](text-v2.md) object, on a [Text paragraph](text-paragraph.md) or on a [Text part](text-part.md). A paragraph’s value overrides the text object’s value, and a part’s value overrides both. A part in blue italic Arial of 10 px:

```json
{"text": "18-electron complex", "italic": true, "font": {"family": "Arial", "size": 10}, "color": "#1f6feb"}
```

[Styled text in the KET 2.0 form](../examples/text-v2-styled.md) shows a complete text object and how it looks.

This is the form of KET 2.0. A KET 1.0 document writes a text as a serialised Draft.js document instead: the [KET 1.0 text](text-v1.md).
