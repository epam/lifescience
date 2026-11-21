---
kind: example
shows: [property]
---

# Molecule properties

Methanol with two named properties.

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
    "properties": [
      {"key": "name", "value": "methanol"},
      {"key": "source", "value": "example"}
    ]
  }
}
```
