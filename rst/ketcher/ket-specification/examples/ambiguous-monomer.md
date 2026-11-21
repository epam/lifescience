---
kind: example
shows: [ambiguous-monomer, ambiguous-monomer-template]
---

# Ambiguous monomer

A mixture of glycine and alanine in the ratio 1 : 3, placed once in the drawing.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "monomer0"}],
    "templates": [
      {"$ref": "monomerTemplate-G___Glycine"},
      {"$ref": "monomerTemplate-A___Alanine"},
      {"$ref": "ambiguousMonomerTemplate-GA-mix"}
    ]
  },
  "monomer0": {"type": "ambiguousMonomer", "id": "0", "position": {"x": 0, "y": 0}, "alias": "%", "templateId": "GA-mix"},
  "monomerTemplate-G___Glycine": {
    "type": "monomerTemplate",
    "atoms": [
      {"label": "N", "location": [-0.866, 0.25, 0]},
      {"label": "C", "location": [0, 0.75, 0]},
      {"label": "C", "location": [0.866, 0.25, 0]},
      {"label": "O", "location": [1.732, 0.75, 0]},
      {"label": "O", "location": [0.866, -0.75, 0]},
      {"label": "H", "location": [-1.732, 0.75, 0]}
    ],
    "bonds": [
      {"type": 1, "atoms": [0, 1]},
      {"type": 1, "atoms": [1, 2]},
      {"type": 1, "atoms": [2, 3]},
      {"type": 2, "atoms": [2, 4]},
      {"type": 1, "atoms": [0, 5]}
    ],
    "class": "AminoAcid",
    "classHELM": "PEPTIDE",
    "id": "G___Glycine",
    "fullName": "Glycine",
    "alias": "G",
    "aliasHELM": "G",
    "aliasBILN": "G",
    "attachmentPoints": [
      {"attachmentAtom": 0, "leavingGroup": {"atoms": [5]}, "type": "left"},
      {"attachmentAtom": 2, "leavingGroup": {"atoms": [3]}, "type": "right"}
    ],
    "naturalAnalogShort": "G",
    "modificationTypes": ["Natural amino acid"]
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
  },
  "ambiguousMonomerTemplate-GA-mix": {
    "type": "ambiguousMonomerTemplate",
    "id": "GA-mix",
    "subtype": "mixture",
    "alias": "%",
    "options": [{"templateId": "G___Glycine", "ratio": 1}, {"templateId": "A___Alanine", "ratio": 3}]
  }
}
```
