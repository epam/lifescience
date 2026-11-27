---
kind: example
shows: [text-v2, text-paragraph, text-part]
---

# Styled text in the KET 2.0 form

A two-paragraph text with a default font, a centred first paragraph, bold and subscript runs and a coloured run.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {
        "type": "text",
        "boundingBox": {"x": 0, "y": 2, "width": 6, "height": 1.2},
        "alignment": "left",
        "font": {"family": "Arial", "size": 13},
        "paragraphs": [
          {
            "alignment": "center",
            "parts": [
              {"text": "Ferrocene, "},
              {"text": "Fe(C", "bold": true},
              {"text": "5", "bold": true, "subscript": true},
              {"text": "H", "bold": true},
              {"text": "5", "bold": true, "subscript": true},
              {"text": ")", "bold": true},
              {"text": "2", "bold": true, "subscript": true}
            ]
          },
          {
            "parts": [
              {
                "text": "18-electron complex",
                "italic": true,
                "font": {"size": 10},
                "color": "#1f6feb"
              }
            ]
          }
        ]
      }
    ]
  }
}
```
