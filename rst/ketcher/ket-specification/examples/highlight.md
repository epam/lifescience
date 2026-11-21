---
kind: example
shows: [highlight]
---

# Highlighted atoms and bonds

Methanol with both atoms and the bond between them highlighted.

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
      {"label": "O", "location": [1, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]}
    ],
    "highlight": [
      {"entityType": "atoms", "items": [0, 1]},
      {"entityType": "bonds", "items": [0]}
    ]
  }
}
```
