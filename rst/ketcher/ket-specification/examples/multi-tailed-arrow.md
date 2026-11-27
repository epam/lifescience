---
kind: example
shows: [multi-tailed-arrow]
---

# Multi-tailed arrow

Two starting materials, at the two tails, lead to one product at the head. The spine runs from y = 1 down to y = −1 at x = 2, the tails start at x = 1, and the head points to x = 3.5.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {"$ref": "mol0"},
      {"$ref": "mol1"},
      {"$ref": "mol2"},
      {
        "type": "multi-tailed-arrow",
        "data": {
          "head": {"position": {"x": 3.5, "y": 0, "z": 0}},
          "spine": {"pos": [{"x": 2, "y": 1, "z": 0}, {"x": 2, "y": -1, "z": 0}]},
          "tails": {"pos": [{"x": 1, "y": 1, "z": 0}, {"x": 1, "y": -1, "z": 0}]},
          "zOrder": 0
        }
      }
    ]
  },
  "mol0": {"type": "molecule", "atoms": [{"label": "C", "location": [0, 1, 0]}]},
  "mol1": {"type": "molecule", "atoms": [{"label": "O", "location": [0, -1, 0]}]},
  "mol2": {"type": "molecule", "atoms": [{"label": "N", "location": [5, 0, 0]}]}
}
```
