---
kind: example
shows: [stereo-flag-position]
---

# Stereo flag position

A stereocentre with absolute configuration. The label is drawn one unit above the highest atom, which is at y = 1: with `y` pointing down, that is `"y": -2`.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0], "stereoLabel": "abs"},
      {"label": "F", "location": [0, 1, 0]},
      {"label": "Cl", "location": [0.866, -0.5, 0]},
      {"label": "Br", "location": [-0.866, -0.5, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1], "stereo": 1},
      {"type": 1, "atoms": [0, 2]},
      {"type": 1, "atoms": [0, 3]}
    ],
    "stereoFlagPosition": {"x": 0.866, "y": -2, "z": 0}
  }
}
```
