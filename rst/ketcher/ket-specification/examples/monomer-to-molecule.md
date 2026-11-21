---
kind: example
shows: [connection, connection-endpoint]
---

# Monomer connected to a molecule

Alanine bonded through its R2 point to the nitrogen of methylamine, atom 1 of `mol0`: an N-methyl amide. The atom index is written as a string.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "monomer0"}, {"$ref": "mol0"}],
    "connections": [
      {
        "connectionType": "single",
        "endpoint1": {"monomerId": "monomer0", "attachmentPointId": "R2"},
        "endpoint2": {"moleculeId": "mol0", "atomId": "1"}
      }
    ],
    "templates": [{"$ref": "monomerTemplate-A___Alanine"}]
  },
  "monomer0": {"type": "monomer", "id": "0", "position": {"x": 0, "y": 0}, "alias": "A", "templateId": "A___Alanine"},
  "mol0": {
    "type": "molecule",
    "atoms": [{"label": "C", "location": [3, 0, 0]}, {"label": "N", "location": [2, 0, 0]}],
    "bonds": [{"type": 1, "atoms": [0, 1]}]
  },
  "monomerTemplate-A___Alanine": {
    "type": "monomerTemplate",
    "atoms": [
      {"label": "N", "location": [-0.866, -0.25, 0]},
      {"label": "C", "location": [0, 0.25, 0], "stereoLabel": "abs"},
      {"label": "H", "location": [-1.732, 0.25, 0]},
      {"label": "C", "location": [0.866, -0.25, 0]},
      {"label": "O", "location": [1.732, 0.25, 0]},
      {"label": "O", "location": [0.866, -1.25, 0]},
      {"label": "C", "location": [0, 1.25, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [0, 2]},
      {"type": 1, "atoms": [1, 3]},
      {"type": 1, "atoms": [3, 4]},
      {"type": 2, "atoms": [3, 5]},
      {"type": 1, "atoms": [1, 6], "stereo": 1}
    ],
    "class": "AminoAcid",
    "classHELM": "PEPTIDE",
    "id": "A___Alanine",
    "fullName": "Alanine",
    "alias": "A",
    "aliasHELM": "A",
    "aliasBILN": "A",
    "attachmentPoints": [
      {"attachmentAtom": 0, "leavingGroup": {"atoms": [2]}, "type": "left"},
      {"attachmentAtom": 3, "leavingGroup": {"atoms": [4]}, "type": "right"}
    ],
    "naturalAnalogShort": "A",
    "modificationTypes": ["Natural amino acid"]
  }
}
```
