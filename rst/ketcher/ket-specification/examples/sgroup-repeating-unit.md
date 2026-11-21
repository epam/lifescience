---
kind: example
shows: [sgroup-sru]
---

# Structural repeating unit

Polyethylene, CH3–(CH2–CH2)n–CH3: one CH2–CH2 unit in brackets, joined head to tail.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0]},
      {"label": "C", "location": [0.866, 0.5, 0]},
      {"label": "C", "location": [1.732, 0, 0]},
      {"label": "C", "location": [2.598, 0.5, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 1, "atoms": [2, 3]}
    ],
    "sgroups": [
      {"type": "SRU", "atoms": [1, 2], "subscript": "n", "connectivity": "HT"}
    ]
  }
}
```
