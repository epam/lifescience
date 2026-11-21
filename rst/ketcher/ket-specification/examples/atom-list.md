---
kind: example
shows: [atom-list]
---

# Atom list

A query carbon with two list atoms: one matches nitrogen, oxygen or sulfur, the other any element except chlorine and bromine.

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
      {"type": "atom-list", "elements": ["N", "O", "S"], "location": [1, 0, 0]},
      {"type": "atom-list", "elements": ["Cl", "Br"], "notList": true, "location": [-1, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [0, 2]}
    ]
  }
}
```
