---
kind: example
shows: [simple-object]
---

# Simple objects

A rectangle, an ellipse and a line side by side.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {"type": "simpleObject", "data": {"mode": "rectangle", "pos": [{"x": 0, "y": 2, "z": 0}, {"x": 3, "y": 0, "z": 0}]}},
      {"type": "simpleObject", "data": {"mode": "ellipse", "pos": [{"x": 4, "y": 2, "z": 0}, {"x": 7, "y": 0, "z": 0}]}},
      {"type": "simpleObject", "data": {"mode": "line", "pos": [{"x": 8, "y": 0, "z": 0}, {"x": 10, "y": 2, "z": 0}]}}
    ]
  }
}
```
