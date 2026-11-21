---
kind: object
match: { type: rgroup }
---

# R-group

The definition of one R-group: its members and its logic.

An R-group with one member writes the member's atoms and bonds directly in the object. An R-group with several members writes each member as an element of `fragments`.

## Appears in

A top-level value under a key `rg<N>` of the [Document](../document-structure/document.md), referenced from [`root.nodes`](../document-structure/root.md#nodes) as `{"$ref": "rg1"}`.

## Identified by

`"type": "rgroup"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"rgroup"`

Object type; always `rgroup`.

### `rlogic`

- Type: object
- Required: yes

The number of the R-group, and the conditions on its occurrence, as the `LOG` property of MOL files.

#### `rlogic.number`

- Type: integer
- Required: yes
- Values: 1 to 32

Number of the R-group: 1 for R1. It equals the `N` of the R-group's key `rg<N>`.

#### `rlogic.range`

- Type: string
- Required: no
- Pattern: `^([0-9]+|[0-9]+-[0-9]+|[<>][0-9]+)(,([0-9]+|[0-9]+-[0-9]+|[<>][0-9]+))*$`
- Values: comma-separated counts such as `1`, ranges such as `1-3`, and bounds such as `>0` and `<5`

How many times the R-group may occur, for example `>0` or `1-3,5`; omitted when not set.

An item `n` allows exactly n occurrences, `n-m` from n to m, `>n` more than n, and `<n` fewer than n. The value has no spaces and at most 50 characters.

#### `rlogic.resth`

- Type: boolean
- Required: no
- Default: `false`

Whether R-sites of this R-group that no member occupies carry hydrogen.

#### `rlogic.ifthen`

- Type: integer
- Required: no
- Default: `0`
- Values: at least 0

Number of another R-group that must occur whenever this one occurs; `0` for no such condition.

### `atoms`

- Type: array of one of [Atom](../molecules/atom.md), [R-group label](../molecules/rg-label.md), [Atom list](../molecules/atom-list.md)
- Required: no

The atoms of the only member, when the R-group has one.

### `bonds`

- Type: array of [Bond](../molecules/bond.md)
- Required: no

The bonds of the only member.

### `sgroups`

- Type: array of one of [Generic S-group](../sgroups/sgroup-gen.md), [Multiple group](../sgroups/sgroup-mul.md), [Structural repeating unit](../sgroups/sgroup-sru.md), [Superatom](../sgroups/sgroup-sup.md), [Data S-group](../sgroups/sgroup-dat.md), [Copolymer](../sgroups/sgroup-cop.md), [Query component](../sgroups/sgroup-query-component.md)
- Required: no

The S-groups of the only member.

### `stereoFlagPosition`

- Type: [Stereo flag position](../molecules/stereo-flag-position.md)
- Required: no

Where the enhanced stereochemistry label of the only member is drawn.

### `properties`

- Type: array of [Property](../molecules/property.md)
- Required: no

Named text values attached to the only member.

### `highlight`

- Type: array of [Highlight](../molecules/highlight.md)
- Required: no
- Items: at most 2

Atoms and bonds of the only member shown highlighted.

### `fragments`

- Type: array of [R-group member](rgroup-member.md)
- Required: no
- Items: at least 2

The members, one element each, when the R-group has more than one.

## Rules

1. `type` and `rlogic` are required.
2. The `N` of the key `rg<N>` equals `rlogic.number`.
3. An R-group has either `atoms`, for one member, or `fragments`, for several; never both.
4. Every member is one connected fragment.
5. The R-group is listed in `root.nodes`, and an R-group label of the document names it.
6. `rlogic.ifthen`, when not 0, is the number of an R-group defined in the document.

## Gotchas

- Two disconnected fragments written directly in the object are one member, not two: write several members as `fragments`.

## Examples

- [R-group](../examples/rgroup.md)

## Related

- [R-group member](rgroup-member.md)
- [R-group label](../molecules/rg-label.md)
