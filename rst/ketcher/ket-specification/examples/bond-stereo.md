---
kind: example
shows: [bond]
---

# Bond types and stereo

A stereocentre with a wedge bond to fluorine, and a vinyl group with a double bond. The wedge starts at the stereocentre, atom 0.

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
      {"label": "F", "location": [0, 1, 0]},
      {"label": "Cl", "location": [0.866, -0.5, 0]},
      {"label": "C", "location": [-0.866, -0.5, 0]},
      {"label": "C", "location": [-1.732, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1], "stereo": 1},
      {"type": 1, "atoms": [0, 2]},
      {"type": 1, "atoms": [0, 3]},
      {"type": 2, "atoms": [3, 4]}
    ]
  }
}
```
