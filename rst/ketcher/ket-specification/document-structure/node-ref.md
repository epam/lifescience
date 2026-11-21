---
kind: object
match: { with: $ref, without: type }
---

# Node reference

A reference from `root.nodes` or `root.templates` to an object stored under a top-level key of its own.

## Appears in

An element of [`root.nodes`](root.md#nodes) (molecules, R-groups, monomers, monomer shapes) or of [`root.templates`](root.md#templates) (templates).

## Identified by

An object with a `$ref` key and no `type`.

## Attributes

### `$ref`

- Type: string
- Required: yes

The top-level key of the referenced object, for example `mol0`.

The referenced object’s `type` tells what it is.

## Related

- [Root](root.md)
- [Document](document.md)
