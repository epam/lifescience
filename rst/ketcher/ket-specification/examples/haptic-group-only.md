---
kind: example
shows: [attachment-group]
---

# Attachment group without a connection

An attachment group that no haptic connection uses is valid.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}]
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
  }
}
```
