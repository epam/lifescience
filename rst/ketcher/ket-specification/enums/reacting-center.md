---
kind: enum
---

# Reacting center

What happens to a bond in a reaction, as the reacting-centre status of MOL and RXN files.

| Value | Name | Meaning |
| --- | --- | --- |
| `-1` | not a centre | The bond is not a reacting centre. |
| `0` | unmarked | No status. The default; writers omit the key. |
| `1` | centre | The bond is a reacting centre. |
| `2` | unchanged | The bond does not change in the reaction. |
| `4` | made or broken | The bond is made or broken. |
| `8` | order changes | The order of the bond changes. |
| `12` | made or broken, and order changes | Both 4 and 8. |
