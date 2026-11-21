---
kind: example
shows: [arrow]
---

# Arrow modes

An equilibrium arrow, and above it an elliptical arc arrow whose arc bulges one unit to the left of its direction, that is upwards.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {"type": "arrow", "data": {"mode": "equilibrium-open-angle", "pos": [{"x": 0, "y": 0, "z": 0}, {"x": 2, "y": 0, "z": 0}]}},
      {"type": "arrow", "data": {"mode": "elliptical-arc-arrow-filled-bow", "pos": [{"x": 0, "y": 1, "z": 0}, {"x": 2, "y": 1, "z": 0}], "height": 1}}
    ]
  }
}
```
