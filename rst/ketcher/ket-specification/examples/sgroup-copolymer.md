---
kind: example
shows: [sgroup-cop, sgroup-sru]
---

# Copolymer

A random copolymer of ethylene and propylene: two repeating units, each in its own brackets, inside a copolymer bracket.

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
      {"label": "C", "location": [2.598, 0.5, 0]},
      {"label": "C", "location": [3.464, 0, 0]},
      {"label": "C", "location": [3.464, -1, 0]},
      {"label": "C", "location": [4.33, 0.5, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 1, "atoms": [2, 3]},
      {"type": 1, "atoms": [3, 4]},
      {"type": 1, "atoms": [4, 5]},
      {"type": 1, "atoms": [4, 6]}
    ],
    "sgroups": [
      {"type": "SRU", "atoms": [1, 2], "subscript": "n", "connectivity": "HT"},
      {"type": "SRU", "atoms": [3, 4, 5], "subscript": "m", "connectivity": "HT"},
      {"type": "COP", "atoms": [1, 2, 3, 4, 5], "subtype": "RAN", "connectivity": "HT"}
    ]
  }
}
```
