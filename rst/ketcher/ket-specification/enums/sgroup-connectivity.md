---
kind: enum
---

# S-group connectivity

How the consecutive units of a polymer are joined, as in the `SCN` property of MOL files.

A unit has a head and a tail: the two atoms of the unit with bonds that cross the bracket.

| Value | Name | Meaning |
| --- | --- | --- |
| `"HT"` | head-to-tail | The tail of each unit bonds to the head of the next one. |
| `"HH"` | head-to-head | The units alternate in direction: head bonds to head, and tail to tail. |
| `"EU"` | either or unknown | The direction is unknown or varies along the chain. |
