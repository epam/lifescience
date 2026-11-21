---
kind: object
---

# Document

The top-level JSON object of a KET file.

A document is one JSON object. [`root.nodes`](root.md#nodes) lists what the document shows. Molecules, R-groups and monomers are stored next to `root` under keys of their own (`mol0`, `rg1`, `monomer3`) and referenced from `root.nodes`; arrows, pluses, shapes, texts and images sit inline in `root.nodes`. Monomer templates are stored the same way and listed in [`root.templates`](root.md#templates).

## Appears in

The whole file.

## Identified by

A JSON object with a `root` key whose value has a `nodes` array.

## Attributes

### `ket_version`

- Type: string
- Required: no
- Values: a version, `MAJOR.MINOR.PATCH`, such as `"2.0.0"`
- Pattern: `^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$`
- Since: 2.0.0

Version of the format the document follows.

A document without `ket_version` follows version 1.0.0. [Versioning](../versioning.md) says what the number means, when it changes and what a reader does with a version it does not know.

### `root`

- Type: [Root](root.md)
- Required: yes

What the document contains: its nodes, and the connections and templates they use.

### `header`

- Type: object
- Required: no

Metadata of the document.

#### `header.moleculeName`

- Type: string
- Required: no

Name of the structure the document holds.

### `mol<N>`

- Type: [Molecule](../molecules/molecule.md)
- Required: no
- Key pattern: `^mol\d+$`

A molecule, referenced from [`root.nodes`](root.md#nodes) as `{"$ref": "mol<N>"}`.

Molecules are numbered from `mol0` in the order in which `root.nodes` lists them.

### `rg<N>`

- Type: [R-group](../rgroups/rgroup.md)
- Required: no
- Key pattern: `^rg([1-9]|[12][0-9]|3[0-2])$`

An R-group definition; `N` is the R-group number, so `rg1` holds R1.

`N` is from 1 to 32 and equals the R-group number given in the definition’s `rlogic`.

### `monomer<N>`

- Type: one of [Monomer](../macromolecules/monomer.md), [Ambiguous monomer](../macromolecules/ambiguous-monomer.md)
- Required: no
- Key pattern: `^monomer\d+$`

A monomer or an ambiguous monomer placed on the canvas, referenced from [`root.nodes`](root.md#nodes).

### `monomerTemplate-<id>`

- Type: [Monomer template](../macromolecules/monomer-template.md)
- Required: no
- Key pattern: `^monomerTemplate-.+$`

A monomer template, listed in [`root.templates`](root.md#templates); `<id>` is the template’s `id`.

### `ambiguousMonomerTemplate-<id>`

- Type: [Ambiguous monomer template](../macromolecules/ambiguous-monomer-template.md)
- Required: no
- Key pattern: `^ambiguousMonomerTemplate-.+$`

An ambiguous monomer template, listed in [`root.templates`](root.md#templates).

### `monomerShape-<id>`

- Type: [Monomer shape](../macromolecules/monomer-shape.md)
- Required: no
- Key pattern: `^monomerShape-.+$`

A monomer shape, referenced from [`root.nodes`](root.md#nodes).

### `monomerGroupTemplate-<id>`

- Type: [Monomer group template](../library/monomer-group-template.md)
- Required: no
- Key pattern: `^monomerGroupTemplate-.+$`

A monomer group template of a [monomer library](../library/index.md), listed in [`root.templates`](root.md#templates).

## Rules

1. `root` is required.
2. The top-level keys are `ket_version`, `root`, `header` and the keys listed here for objects that `root` references.
3. Every `$ref` names a top-level key of the document.
4. Every molecule, R-group, monomer and monomer shape is referenced from `root.nodes`, and every template from `root.templates`.

## Examples

- [Atom properties](../examples/atom-properties.md)

## Related

- [Root](root.md)
- [Node reference](node-ref.md)
- [Molecule](../molecules/molecule.md)
