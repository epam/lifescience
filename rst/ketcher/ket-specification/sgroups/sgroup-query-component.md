---
kind: object
match: { type: queryComponent }
query: true
---

# Query component

A set of query atoms that must match within one connected component of the target, as the component-level grouping of SMARTS does with `(C.O)`.

Atoms of one query component match atoms of the same component of the target, even when the query does not bond them to each other. Atoms of different query components match different components of the target.

## Appears in

An element of the [`sgroups`](../molecules/molecule.md#sgroups) array of a [Molecule](../molecules/molecule.md) that describes a query. Its atom indexes refer to that molecule's `atoms`.

## Identified by

`"type": "queryComponent"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"queryComponent"`

S-group type; always `queryComponent`.

### `atoms`

- Type: array of integer
- Required: yes
- Items: at least 1

Indexes of the atoms of the component, in the molecule's `atoms` array.

## Rules

1. `type` and `atoms` are required.
2. An atom belongs to at most one query component.
3. A molecule with a query component describes a query.

## Examples

- [Query component](../examples/sgroup-query-component.md)

## Related

- [Atom query properties](../molecules/query-properties.md)
