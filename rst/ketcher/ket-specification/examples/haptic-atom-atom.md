---
kind: example
shows: [haptic-connection, haptic-endpoint]
---

# Atom-to-atom haptic bond

Iron bonded to a single carbon through a haptic connection with two atom endpoints.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "mol1"}],
    "connections": [
      {
        "type": "haptic",
        "endpoint1": {"moleculeId": "mol0", "atomId": "0"},
        "endpoint2": {"moleculeId": "mol1", "atomId": "0"}
      }
    ]
  },
  "mol0": {
    "type": "molecule",
    "atoms": [
      {"label": "Fe", "location": [1.5, 0, 0]}
    ]
  },
  "mol1": {
    "type": "molecule",
    "atoms": [
      {"label": "C", "location": [0, 0, 0]}
    ]
  }
}
```
