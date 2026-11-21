---
kind: enum
---

# Query hydrogen count

Query constraint on the hydrogen count of an atom, encoded as the count plus one, like the `hhh` field of MOL V2000 atom blocks.

The value is the count plus one, not the count: `"hCount": 1` means H0.

| Value | Name | Meaning |
| --- | --- | --- |
| `0` | unset | No constraint. The default; writers omit the key. |
| `1` | H0 | No hydrogens beyond those drawn explicitly. |
| `2 to 10` | H(n − 1) | At least `n − 1` hydrogens beyond those drawn: `2` is H1, `10` is H9. |
