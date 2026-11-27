---
kind: example
shows: [rgroup, rgroup-member, rg-label]
---

# R-group

Methyl with an R-site R1, where R1 is a hydroxyl or an amino group and occurs at least once.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "rg1"}]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0]},
      {"type": "rg-label", "location": [1, 0, 0], "$refs": ["rg-1"]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]}
    ]
  },
  "rg1": {
    "type": "rgroup",
    "rlogic": {"number": 1, "range": ">0"},
    "fragments": [
      {"atoms": [{"label": "O", "location": [3, 0, 0], "attachmentPoints": 1}]},
      {"atoms": [{"label": "N", "location": [3, -1.5, 0], "attachmentPoints": 1}]}
    ]
  }
}
```
