---
kind: enum
---

# Arrow mode

The kind of an arrow: how it is drawn, and what a reaction arrow means.

| Value | Name | Meaning |
| --- | --- | --- |
| `"open-angle"` | open angle | The ordinary reaction arrow: one shaft with an open, line-drawn head. |
| `"filled-triangle"` | filled triangle | One shaft with a filled triangular head. |
| `"filled-bow"` | filled bow | One shaft with a filled, swept-back head. |
| `"dashed-open-angle"` | dashed | A dashed shaft with an open head. |
| `"failed"` | failed | A shaft crossed by an X: a reaction that does not proceed. |
| `"retrosynthetic"` | retrosynthetic | Two parallel lines meeting at the head: a retrosynthetic step, from the target to its precursors. |
| `"both-ends-filled-triangle"` | both ends | Filled heads at both ends: resonance. |
| `"equilibrium-filled-half-bow"` | equilibrium, half bows | Two opposite half arrows with filled half-bow heads. |
| `"equilibrium-filled-triangle"` | equilibrium, triangles | Two opposite arrows with filled triangular heads. |
| `"equilibrium-open-angle"` | equilibrium, open angles | Two opposite arrows with open heads. |
| `"unbalanced-equilibrium-filled-half-bow"` | unbalanced equilibrium, half bows | Two opposite half arrows of unequal length with filled half-bow heads. |
| `"unbalanced-equilibrium-open-half-angle"` | unbalanced equilibrium, open half angles | Two opposite half arrows of unequal length with open half heads. |
| `"unbalanced-equilibrium-large-filled-half-bow"` | unbalanced equilibrium, large half bow | Two opposite half arrows of unequal length with a large filled half-bow head. |
| `"unbalanced-equilibrium-filled-half-triangle"` | unbalanced equilibrium, half triangles | Two opposite half arrows of unequal length with filled half-triangle heads. |
| `"elliptical-arc-arrow-filled-bow"` | arc, filled bow | An arc from tail to head with a filled bow head; the arrow has a `height`. |
| `"elliptical-arc-arrow-filled-triangle"` | arc, filled triangle | An arc with a filled triangular head; the arrow has a `height`. |
| `"elliptical-arc-arrow-open-angle"` | arc, open angle | An arc with an open head; the arrow has a `height`. |
| `"elliptical-arc-arrow-open-half-angle"` | arc, open half angle | An arc with an open half head; the arrow has a `height`. |
