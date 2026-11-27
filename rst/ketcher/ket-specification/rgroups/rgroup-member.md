---
kind: object
---

# R-group member

One of the fragments that may take the place of an R-site.

## Appears in

An element of the `fragments` array of an [R-group](rgroup.md). Its atom and bond indexes are local to the member.

## Identified by

An element of `fragments`.

## Attributes

### `atoms`

- Type: array of one of [Atom](../molecules/atom.md), [R-group label](../molecules/rg-label.md), [Atom list](../molecules/atom-list.md)
- Required: yes

The atoms of the member. The atoms that bond to the R-site carry the atom key `attachmentPoints`.

### `bonds`

- Type: array of [Bond](../molecules/bond.md)
- Required: no

The bonds of the member; atom indexes refer to the member's own `atoms`.

### `sgroups`

- Type: array of one of [Generic S-group](../sgroups/sgroup-gen.md), [Multiple group](../sgroups/sgroup-mul.md), [Structural repeating unit](../sgroups/sgroup-sru.md), [Superatom](../sgroups/sgroup-sup.md), [Data S-group](../sgroups/sgroup-dat.md), [Copolymer](../sgroups/sgroup-cop.md), [Query component](../sgroups/sgroup-query-component.md)
- Required: no

The S-groups of the member.

## Rules

1. `atoms` is required.
2. The member is one connected fragment.
3. Atom indexes in `bonds` and `sgroups` are positions in the member's own `atoms`.

## Examples

- [R-group](../examples/rgroup.md)

## Related

- [R-group](rgroup.md)
