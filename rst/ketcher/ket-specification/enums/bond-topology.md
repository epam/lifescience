---
kind: enum
---

# Bond topology

Whether a query bond must lie in a ring or in a chain.

| Value | Name | Meaning |
| --- | --- | --- |
| `0` | either | No constraint. The default; writers omit the key. |
| `1` | ring | Matches only a bond in a ring. |
| `2` | chain | Matches only a bond not in a ring. |
