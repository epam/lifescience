---
kind: example
shows: [haptic-connection]
---

# A haptic connection between two groups

A haptic connection whose two ends are attachment groups of two rings.

**Rule broken:** At least one end of a haptic connection is an atom.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "mol1"}],
    "connections": [
      {
        "type": "haptic",
        "endpoint1": {"moleculeId": "mol0", "attachmentGroupId": "0"},
        "endpoint2": {"moleculeId": "mol1", "attachmentGroupId": "0"}
      }
    ]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 1, 0]},
      {"label": "C", "location": [-0.866, 0.5, 0]},
      {"label": "C", "location": [-0.866, -0.5, 0]},
      {"label": "C", "location": [0, -1, 0]},
      {"label": "C", "location": [0.866, -0.5, 0]},
      {"label": "C", "location": [0.866, 0.5, 0]}
    ],
    "bonds": [
      {"type": 2, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 2, "atoms": [2, 3]},
      {"type": 1, "atoms": [3, 4]},
      {"type": 2, "atoms": [4, 5]},
      {"type": 1, "atoms": [5, 0]}
    ],
    "attachmentGroups": [
      {"id": "0", "atoms": [0, 1, 2, 3, 4, 5]}
    ]
  },
  "mol1": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [4, 1, 0]},
      {"label": "C", "location": [3.134, 0.5, 0]},
      {"label": "C", "location": [3.134, -0.5, 0]},
      {"label": "C", "location": [4, -1, 0]},
      {"label": "C", "location": [4.866, -0.5, 0]},
      {"label": "C", "location": [4.866, 0.5, 0]}
    ],
    "bonds": [
      {"type": 2, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 2, "atoms": [2, 3]},
      {"type": 1, "atoms": [3, 4]},
      {"type": 2, "atoms": [4, 5]},
      {"type": 1, "atoms": [5, 0]}
    ],
    "attachmentGroups": [
      {"id": "0", "atoms": [0, 1, 2, 3, 4, 5]}
    ]
  }
}
```
