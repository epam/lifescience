---
kind: object
---

# Property

A named text value attached to a molecule, such as a data field of an SD file record.

## Appears in

An element of the `properties` array of a [Molecule](molecule.md).

## Identified by

An object with `key` and `value`.

## Attributes

### `key`

- Type: string
- Required: yes

Name of the property, unique among the properties of the molecule.

### `value`

- Type: string
- Required: yes

Value of the property, as text.

## Rules

1. `key` and `value` are required, and both are strings: `"value": "5"`, not `"value": 5`.
2. The keys of a molecule's properties are unique.

## Gotchas

- Properties belong to the molecule object as a whole. A writer that splits a molecule into its connected fragments keeps them with the fragment that holds atom 0.

## Examples

- [Molecule properties](../examples/molecule-properties.md)

## Related

- [Molecule](molecule.md)
