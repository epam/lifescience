---
kind: enum
---

# Data S-group context

What the data of a data S-group describes, as the field context of MOL files.

| Value | Name | Meaning |
| --- | --- | --- |
| `"Atom"` | atom | The data describes an atom. |
| `"Bond"` | bond | The data describes a bond; the group holds the two atoms of the bond. |
| `"Group"` | group | The data describes a set of bonded atoms that is not a whole fragment. |
| `"Fragment"` | fragment | The data describes a whole connected fragment. |
| `"Multifragment"` | multifragment | The data describes atoms of several fragments together. |
