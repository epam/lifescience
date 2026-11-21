---
kind: enum
---

# Ring bond count

Query constraint on the number of ring bonds of an atom, encoded as the `RBC` property of MOL files.

An atom without the constraint has no `ringBondCount` key. `1` is not a value: an atom in a ring has at least two ring bonds.

| Value | Name | Meaning |
| --- | --- | --- |
| `-1` | none | The atom has no ring bonds. |
| `-2` | as drawn | Exactly as many ring bonds as drawn. |
| `2 to 9` | exactly n | Exactly that many ring bonds. |
