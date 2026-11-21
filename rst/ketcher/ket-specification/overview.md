# Overview

## What KET is

KET is a JSON format for chemical structures. One document can hold molecules and query molecules, reactions, drawing objects — arrows, pluses, shapes, texts and images — macromolecules built from monomers and their templates, and haptic bonds.

This reference defines the format: every object, every key, the values each key takes and the rules a valid document follows. It is written for developers of programs that write or read KET.

## A first document

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
      {"label": "O", "location": [0.866, 0.5, 0], "charge": -1}
    ],
    "bonds": [{"type": 1, "atoms": [0, 1]}]
  }
}
```

The document shows one node: a reference to the molecule stored under the key `mol0`. The molecule has two atoms — a carbon and a negatively charged oxygen — and a single bond between them. Coordinates are in KET length units, with the y axis pointing up.

## Notation

- Keys are written in `code`. A key in angle brackets stands for a family of keys: `mol<N>` is `mol0`, `mol1` and so on.
- **Must**, **must not**, **should** and **may** state requirements in the sense of RFC 2119. Rules for writers govern the documents a program produces; rules for readers govern how a program interprets a document.
- **Query** marks a key that describes a search constraint rather than a structure.
