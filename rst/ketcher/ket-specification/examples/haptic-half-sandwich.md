---
kind: example
shows: [attachment-group, haptic-connection, haptic-endpoint]
---

# Benzene–chromium half sandwich

The benzene ring is an attachment group, and one haptic connection binds it to chromium. The metal and the ring are separate molecules here; one molecule holding both is equally valid.

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
      {"label": "Cr", "location": [2.5, 0, 0]}
    ]
  },
  "mol1": {
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
  }
}
```
