---
kind: enum
---

# Substitution count

Query constraint on the number of non-hydrogen neighbours of an atom, encoded as the `SUB` property of MOL files.

An atom without the constraint has no `substitutionCount` key.

| Value | Name | Meaning |
| --- | --- | --- |
| `-1` | none | No substituents. |
| `-2` | as drawn | Exactly as many substituents as drawn. |
| `1 to 9` | exactly n | Exactly that many substituents. |
