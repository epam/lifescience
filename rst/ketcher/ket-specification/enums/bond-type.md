---
kind: enum
---

# Bond type

Order of a bond, or the class of bonds a query bond matches, as the bond type of MOL files.

Types 5 to 8 match several kinds of bond and appear only in a query.

| Value | Name | Meaning |
| --- | --- | --- |
| `1` | single | A single bond. |
| `2` | double | A double bond. |
| `3` | triple | A triple bond. |
| `4` | aromatic | An aromatic bond. |
| `5` | single or double | Query: matches a single or a double bond. |
| `6` | single or aromatic | Query: matches a single or an aromatic bond. |
| `7` | double or aromatic | Query: matches a double or an aromatic bond. |
| `8` | any | Query: matches any bond. |
| `9` | coordination | A coordination (dative) bond from a donor to an acceptor. |
| `10` | hydrogen | A hydrogen bond. |
