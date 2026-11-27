# Reactions and drawing objects

Arrows, pluses, shapes and images are drawing objects. They are written inline in [`root.nodes`](../document-structure/root.md#nodes), each with a `type` that tells it apart:

| `type` | Object |
| --- | --- |
| `"arrow"` | [Arrow](arrow.md) |
| `"plus"` | [Plus](plus.md) |
| `"multi-tailed-arrow"` | [Multi-tailed arrow](multi-tailed-arrow.md) |
| `"simpleObject"` | [Simple object](simple-object.md): a line, rectangle or ellipse |
| `"image"` | [Image](image.md) |

## Reactions

KET has no reaction object. A reaction is a document with arrows, read from the layout:

- the molecules on the tail side of an arrow are its reactants;
- the molecules on the head side are its products;
- the molecules drawn above or below the arrow are its reagents, and a text above or below it states the conditions;
- pluses stand between the molecules of one side.

A retrosynthetic arrow points from the target back to its precursors, so the target is on its tail side. Several arrows describe a multistep reaction, and a [Multi-tailed arrow](multi-tailed-arrow.md) joins the molecules at its tails to the molecule at its head.

A document whose molecules are not separated by an arrow describes structures, not a reaction.
