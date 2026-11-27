---
kind: example
shows: [atom]
---

# An explicit "type": "atom"

A carbon atom written with an explicit `"type": "atom"`.

**Rule broken:** A plain atom has no `type` key.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"type": "atom", "label": "C", "location": [0, 0, 0]}
    ]
  }
}
```
