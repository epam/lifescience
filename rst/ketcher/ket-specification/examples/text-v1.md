---
kind: example
shows: [text-v1]
---

# Text in the KET 1.0 form

The text "H2O yield 95%" with a subscript 2, a bold "yield" and "95%" in 18-pixel type, as a serialised Draft.js document.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {
        "type": "text",
        "data": {
          "content": "{\"blocks\":[{\"key\":\"a1b2c\",\"text\":\"H2O yield 95%\",\"type\":\"unstyled\",\"depth\":0,\"inlineStyleRanges\":[{\"offset\":1,\"length\":1,\"style\":\"SUBSCRIPT\"},{\"offset\":4,\"length\":5,\"style\":\"BOLD\"},{\"offset\":10,\"length\":3,\"style\":\"CUSTOM_FONT_SIZE_18px\"}],\"entityRanges\":[],\"data\":{}}],\"entityMap\":{}}",
          "position": {"x": 0, "y": 1, "z": 0},
          "pos": [
            {"x": 0, "y": 1, "z": 0},
            {"x": 0, "y": 0.5, "z": 0},
            {"x": 3, "y": 0.5, "z": 0},
            {"x": 3, "y": 1, "z": 0}
          ]
        }
      }
    ]
  }
}
```
