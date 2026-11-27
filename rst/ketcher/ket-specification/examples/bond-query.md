---
kind: example
shows: [bond]
---

# Query bonds

A query ring of three carbons with a single-or-double ring bond, a single-or-aromatic bond and an any bond, and a custom-query bond to oxygen written in SMARTS.

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
      {"label": "C", "location": [1, 0, 0]},
      {"label": "C", "location": [0.5, 0.866, 0]},
      {"label": "O", "location": [2, 0, 0]}
    ],
    "bonds": [
      {"type": 5, "atoms": [0, 1], "topology": 1},
      {"type": 6, "atoms": [1, 2]},
      {"type": 8, "atoms": [2, 0]},
      {"customQuery": "-,=", "atoms": [1, 3]}
    ]
  }
}
```
