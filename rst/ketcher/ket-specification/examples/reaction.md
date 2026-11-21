---
kind: example
shows: [arrow, plus]
---

# Reaction

Ethene and bromine give 1,2-dibromoethane: the reactants on the tail side of the arrow, joined by a plus, and the product on its head side.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [
      {"$ref": "mol0"},
      {"$ref": "mol1"},
      {"$ref": "mol2"},
      {"type": "plus", "location": [1.75, 0, 0]},
      {"type": "arrow", "data": {"mode": "open-angle", "pos": [{"x": 4.5, "y": 0, "z": 0}, {"x": 6, "y": 0, "z": 0}]}}
    ]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0]},
      {"label": "C", "location": [1, 0, 0]}
    ],
    "bonds": [
      {"type": 2, "atoms": [0, 1]}
    ]
  },
  "mol1": {
    "type": "molecule",
    "atoms": [
      {"label": "Br", "location": [2.5, 0, 0]},
      {"label": "Br", "location": [3.5, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]}
    ]
  },
  "mol2": {
    "type": "molecule",
    "atoms": [
      {"label": "Br", "location": [7, 0.5, 0]},
      {"label": "C", "location": [7.866, 0, 0]},
      {"label": "C", "location": [8.732, 0.5, 0]},
      {"label": "Br", "location": [9.598, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 1, "atoms": [2, 3]}
    ]
  }
}
```
