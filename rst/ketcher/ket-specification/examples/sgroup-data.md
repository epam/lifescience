---
kind: example
shows: [sgroup-dat]
---

# Data S-group

Ethanol with the pKa of its hydroxyl group as a data field on the oxygen atom, drawn apart from the atoms at a given position.

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
      {"label": "O", "location": [1.732, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]}
    ],
    "sgroups": [
      {
        "type": "DAT",
        "atoms": [2],
        "context": "Atom",
        "fieldName": "pKa",
        "fieldData": "15.9",
        "x": 2.2,
        "y": -0.6
      }
    ]
  }
}
```
