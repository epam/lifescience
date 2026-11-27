---
kind: enum
---

# R-group attachment point flags

Bit set marking an atom of an R-group member as its attachment point, encoded as the `APO` property of MOL files.

| Value | Name | Meaning |
| --- | --- | --- |
| `0` | none | Not an attachment point. The default; writers omit the key. |
| `1` | primary | First (primary) attachment point. |
| `2` | secondary | Second (secondary) attachment point. |
| `3` | both | Both attachment points. |
