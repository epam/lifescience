---
kind: example
shows: [sgroup-query-component]
---

# Query component

A query that finds a carbon and an oxygen in the same molecule of the target, bonded or not, like the SMARTS `(C.O)`.

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
      {"label": "O", "location": [2, 0, 0]}
    ],
    "sgroups": [
      {"type": "queryComponent", "atoms": [0, 1]}
    ]
  }
}
```
