---
kind: example
shows: [sgroup-sup]
---

# Superatom

Acetic acid with its carboxyl group abbreviated as COOH. The carboxyl carbon is the attachment point that bonds to the methyl group.

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
      {"label": "O", "location": [0.866, 1.5, 0]},
      {"label": "O", "location": [1.732, 0, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 2, "atoms": [1, 2]},
      {"type": 1, "atoms": [1, 3]}
    ],
    "sgroups": [
      {
        "type": "SUP",
        "atoms": [1, 2, 3],
        "name": "COOH",
        "attachmentPoints": [{"attachmentAtom": 1, "attachmentId": "1"}]
      }
    ]
  }
}
```
