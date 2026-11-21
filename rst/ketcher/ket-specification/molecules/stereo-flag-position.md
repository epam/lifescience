---
kind: object
---

# Stereo flag position

Where the enhanced stereochemistry label of a molecule (ABS, AND, OR, Mixed) is drawn.

## Appears in

The value of the `stereoFlagPosition` key of a [Molecule](molecule.md).

## Identified by

The key that holds it.

## Attributes

### `x`

- Type: number
- Required: yes
- Units: KET length units

Horizontal position of the label.

### `y`

- Type: number
- Required: yes
- Units: KET length units

Vertical position of the label, with the y axis pointing **down**: the opposite of atom locations.

### `z`

- Type: number
- Required: no
- Default: `0`

Depth; 0 in a two-dimensional drawing.

## Rules

1. `x` and `y` are required.
2. The label is drawn at the point that has the atom coordinates `[x, -y, z]`.

## Gotchas

- Unlike every other position in KET, `y` points down. To place the label one unit above the highest atom of a molecule, at y = 2, write `"y": -3`.
- When the molecule holds several fragments, the label belongs to the fragment that holds atom 0.

## Examples

- [Stereo flag position](../examples/stereo-flag-position.md)

## Related

- [Molecule](molecule.md)
