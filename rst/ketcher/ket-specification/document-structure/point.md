---
kind: object
---

# Point

A position written as an object with named coordinates.

Atoms write their positions as arrays, `[x, y, z]`; drawing objects and monomers write theirs as points.

## Appears in

The positions of arrows, multi-tailed arrows, simple objects, KET 1.0 texts and monomers.

## Identified by

An object with `x` and `y`.

## Attributes

### `x`

- Type: number
- Required: yes
- Units: KET length units

Horizontal coordinate.

### `y`

- Type: number
- Required: yes
- Units: KET length units

Vertical coordinate, with the y axis pointing up.

### `z`

- Type: number
- Required: no
- Default: `0`

Depth; 0 in a two-dimensional drawing.

## Rules

1. `x` and `y` are required.

## Related

- [Arrow](../drawing/arrow.md)
- [Simple object](../drawing/simple-object.md)
