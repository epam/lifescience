---
kind: object
match: { type: multi-tailed-arrow }
---

# Multi-tailed arrow

An arrow with several tails and one head: the molecules at the tails lead to the molecule at the head.

The arrow is drawn from three parts. A vertical spine joins the top tail to the bottom tail. Each tail is a horizontal line from its start point to the spine. The head is a horizontal line from the spine to the arrowhead.

## Appears in

An element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "multi-tailed-arrow"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"multi-tailed-arrow"`

Object type; always `multi-tailed-arrow`.

### `data`

- Type: object
- Required: yes

The geometry of the arrow.

#### `data.head`

- Type: object
- Required: yes

The head of the arrow.

##### `data.head.position`

- Type: [Point](../document-structure/point.md)
- Required: yes

Tip of the arrowhead.

#### `data.spine`

- Type: object
- Required: yes

The vertical line that the tails and the head meet.

##### `data.spine.pos`

- Type: array of [Point](../document-structure/point.md)
- Required: yes
- Items: exactly 2

The top end of the spine, then its bottom end.

#### `data.tails`

- Type: object
- Required: yes

The tails of the arrow.

##### `data.tails.pos`

- Type: array of [Point](../document-structure/point.md)
- Required: yes
- Items: at least 2

The start points of the tails, from the top tail to the bottom one.

#### `data.zOrder`

- Type: integer
- Required: no
- Default: `0`

Drawing order of the arrow. It carries no meaning, and a reader ignores it.

## Rules

1. The spine is vertical: its two points have the same `x`, and the first is higher than the second.
2. The head lies to the right of the spine, and its `y` is strictly between the two ends of the spine.
3. All tails start at the same `x`, to the left of the spine.
4. The highest tail is at the height of the top end of the spine, and the lowest tail at the height of its bottom end; the other tails lie between them.
5. No two tails are closer than 0.01 in `y`.
6. A reader may reject an arrow that breaks rules 1 to 5; distances are compared with a tolerance of 0.01.

## Examples

- [Multi-tailed arrow](../examples/multi-tailed-arrow.md)

## Related

- [Arrow](arrow.md)
- [Point](../document-structure/point.md)
