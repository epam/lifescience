---
kind: object
match: { type: plus }
---

# Plus

A plus sign between the molecules of one side of a reaction.

## Appears in

An element of [`root.nodes`](../document-structure/root.md#nodes).

## Identified by

`"type": "plus"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"plus"`

Object type; always `plus`.

### `location`

- Type: array of 3 numbers
- Required: yes
- Units: KET length units

Centre of the plus sign as `[x, y, z]`, with the y axis pointing up; `z` is 0 in a two-dimensional drawing.

### `prop`

- Type: object
- Required: no

An empty object that some writers add. It carries no meaning, and a reader ignores it.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the plus is selected. Carries no meaning; written only as `true`.

## Rules

1. `type` and `location` are required, and `location` holds exactly three numbers.

## Examples

- [Reaction](../examples/reaction.md)

## Related

- [Arrow](arrow.md)
