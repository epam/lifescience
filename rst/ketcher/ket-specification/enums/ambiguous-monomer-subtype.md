---
kind: enum
---

# Ambiguous monomer subtype

Whether an ambiguous monomer is one of its options or a mixture of them.

| Value | Name | Meaning |
| --- | --- | --- |
| `"alternatives"` | alternatives | The monomer is exactly one of the options; an option may state its `probability`. |
| `"mixture"` | mixture | The monomer stands for all the options together; an option may state its `ratio`. |
