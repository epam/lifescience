---
kind: example
shows: [sgroup-mul]
---

# Multiple group

Propan-1-ol written as CH3–(CH2)2–OH: the molecule holds one CH2 group, and the multiple group stands for two.

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
      {"label": "C", "location": [0.866, 0.5, 0]},
      {"label": "O", "location": [1.732, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]}
    ],
    "sgroups": [
      {"type": "MUL", "atoms": [1], "mul": 2}
    ]
  }
}
```
