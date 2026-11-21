---
kind: example
shows: [attachment-group]
---

# Charged attachment group

Iron(II) bonded to a cyclopentadienyl ring whose π system carries the charge −1.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "mol1"}],
    "connections": [
      {
        "type": "haptic",
        "endpoint1": {"moleculeId": "mol0", "atomId": "0"},
        "endpoint2": {"moleculeId": "mol1", "attachmentGroupId": "0"}
      }
    ]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "Fe", "location": [2.2, 0, 0], "charge": 2}
    ]
  },
  "mol1": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0.8507, 0]},
      {"label": "C", "location": [-0.8091, 0.2629, 0]},
      {"label": "C", "location": [-0.5, -0.6882, 0]},
      {"label": "C", "location": [0.5, -0.6882, 0]},
      {"label": "C", "location": [0.8091, 0.2629, 0]}
    ],
    "bonds": [
      {"type": 2, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 2, "atoms": [2, 3]},
      {"type": 1, "atoms": [3, 4]},
      {"type": 1, "atoms": [4, 0]}
    ],
    "attachmentGroups": [
      {"id": "0", "charge": -1, "atoms": [0, 1, 2, 3, 4]}
    ]
  }
}
```
