---
kind: example
shows: [atom]
---

# Atom properties

Acetate with a ¹³C methyl group and a charged oxygen, and an aminyl radical shown with an alias.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "mol1"}]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0], "isotope": 13},
      {"label": "C", "location": [0.866, 0.5, 0]},
      {"label": "O", "location": [1.732, 0, 0], "charge": -1},
      {"label": "O", "location": [0.866, 1.5, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 2, "atoms": [1, 3]}
    ]
  },
  "mol1": {
    "type": "molecule",
    "atoms": [
      {"label": "N", "location": [3.5, 0.5, 0], "radical": 2, "alias": "NH2"}
    ]
  }
}
```
