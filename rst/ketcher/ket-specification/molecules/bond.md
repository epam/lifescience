---
kind: object
---

# Bond

A bond between two atoms of a molecule, or a query bond.

A bond is either typed, with a `type` from the [Bond type](../enums/bond-type.md) enumeration, or a custom query, with a SMARTS bond expression in `customQuery`. Keys marked **Query** describe search constraints and give the document the meaning of a query.

## Appears in

An element of the `bonds` array of a [Molecule](molecule.md), of an R-group and of a monomer template. Its position in the array is the bond index that data S-groups refer to.

## Identified by

An element of `bonds`; every element is a bond.

## Attributes

### `atoms`

- Type: array of integer
- Required: yes
- Items: exactly 2

Indexes of the two atoms the bond joins, in the molecule's `atoms` array.

For a wedge or hash bond, `atoms[0]` is the stereocentre, at the narrow end of the wedge.

### `type`

- Type: integer
- Required: no
- Values: [Bond type](../enums/bond-type.md)

Bond order, or the class of bonds a query bond matches; every bond without `customQuery` has one.

### `stereo`

- Type: integer
- Required: no
- Default: `0`
- Values: [Bond stereo](../enums/bond-stereo.md)

Stereo display of the bond: wedge, hash, wavy, or a double bond with unspecified configuration.

### `topology`

- Type: integer
- Required: no
- Default: `0`
- Values: [Bond topology](../enums/bond-topology.md)
- Query: yes

Whether the matched bond must be in a ring or in a chain.

### `center`

- Type: integer
- Required: no
- Default: `0`
- Values: [Reacting center](../enums/reacting-center.md)

What happens to the bond in a reaction, as the reacting-centre status of MOL files.

### `cip`

- Type: string
- Required: no
- Values: `"E"`, `"Z"`

CIP descriptor of a double bond; omitted when it is not known.

The descriptor is computed from the structure: a reader may recompute it.

### `customQuery`

- Type: string
- Required: no
- Values: a SMARTS bond expression, at most 4000 characters
- Query: yes

The complete bond query as a SMARTS bond expression, for example `-,=` for a single or double bond.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the bond is selected. Carries no chemical meaning; written only as `true`.

## Rules

1. `atoms` holds two different indexes of atoms of the same molecule.
2. A bond has exactly one of `type` and `customQuery`.
3. A bond with `customQuery` has no `stereo`, `topology`, `center` or `cip`.
4. Bond types 5 to 8, `topology` and `customQuery` appear only in a query.
5. `stereo` 1, 4 and 6 are written on single bonds whose first atom is the stereocentre; `stereo` 3 on double bonds.
6. Two atoms are joined by at most one bond.

## Examples

- [Bond types and stereo](../examples/bond-stereo.md)
- [Query bonds](../examples/bond-query.md)

## Related

- [Molecule](molecule.md)
- [Atom](atom.md)
