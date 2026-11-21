---
kind: object
match: { without: type }
---

# Atom

A chemical element, pseudo-atom or query atom of a molecule.

Most keys correspond to the atom properties of MOL files. All but `label` and `location` are optional, and a writer omits a key whose value is the default. Keys marked **Query** describe search constraints and give the document the meaning of a query.

## Appears in

An element of the `atoms` array of a [Molecule](molecule.md), of an R-group and of a monomer template. Its position in the array is the atom index that bonds, S-groups, attachment groups and connections refer to.

## Identified by

An element of `atoms` without a `type` key. Elements with `"type": "rg-label"` are [R-group labels](rg-label.md), elements with `"type": "atom-list"` [atom lists](atom-list.md).

## Attributes

### `label`

- Type: string
- Required: yes

Element symbol, generic query label or pseudo-atom text of the atom.

An element symbol (`C`, `Fe`) makes an ordinary atom; `D` and `T` are hydrogen with mass numbers 2 and 3. The generic labels `A`, `AH`, `Q`, `QH`, `M`, `MH`, `X`, `XH` and `*` are query atoms. Any other text is a pseudo-atom.

### `location`

- Type: array of 3 numbers
- Required: yes
- Units: KET length units (a standard bond length is 1.0)

Position of the atom as `[x, y, z]`, with the y axis pointing up; `z` is 0 in a 2D drawing.

### `alias`

- Type: string
- Required: no

Text displayed instead of the label, for example an abbreviation such as `Ph`.

### `charge`

- Type: integer
- Required: no
- Default: `0`
- Values: -15 to 15

Formal charge of the atom; omitted when the atom is uncharged.

### `explicitValence`

- Type: integer
- Required: no
- Values: 0 to 12

Valence set explicitly, overriding the calculated one; omitted when not set.

### `isotope`

- Type: integer
- Required: no
- Values: 1 to 1000

Mass number of the isotope; omitted for the natural isotopic mixture.

### `radical`

- Type: integer
- Required: no
- Default: `0`
- Values: [Radical](../enums/radical.md)

Radical state of the atom; omitted when there is none.

### `attachmentPoints`

- Type: integer
- Required: no
- Default: `0`
- Values: [R-group attachment point flags](../enums/rgroup-attachment-bits.md)

Marks the atom as an attachment point of the R-group member it belongs to.

### `stereoLabel`

- Type: string
- Required: no
- Values: `abs`, `&<n>` or `or<n>`, with n ≥ 1
- Pattern: `^(abs|&[1-9][0-9]*|or[1-9][0-9]*)$`

Enhanced stereochemistry group of the stereocentre: absolute, AND group *n* or OR group *n*.

Only a stereocentre — an atom whose wedge bonds define its configuration — carries a stereo label.

### `stereoParity`

- Type: integer
- Required: no
- Default: `0`
- Values: `0`, `1`, `2`, `3`

Stereo parity as in MOL V2000: 0 none, 1 odd, 2 even, 3 either or unmarked.

Informational: the configuration is defined by the wedge bonds.

### `ringBondCount`

- Type: integer
- Required: no
- Values: [Ring bond count](../enums/ring-bond-count.md)
- Query: yes

Number of ring bonds the atom must have; omitted when there is no constraint.

### `substitutionCount`

- Type: integer
- Required: no
- Values: [Substitution count](../enums/substitution-count.md)
- Query: yes

Number of non-hydrogen neighbours the atom must have; omitted when there is no constraint.

### `unsaturatedAtom`

- Type: boolean
- Required: no
- Default: `false`
- Query: yes

Requires the atom to have at least one multiple bond; written only as `true`.

### `hCount`

- Type: integer
- Required: no
- Default: `0`
- Values: [Query hydrogen count](../enums/h-count.md)
- Query: yes

Total hydrogen count the atom must have, encoded as the count plus one; omitted when there is no constraint.

`"hCount": 1` means no hydrogens (H0), `2` at least one (H1), and so on up to `10`.

### `implicitHCount`

- Type: integer
- Required: no
- Values: 0 to 9

Number of implicit hydrogens of the atom, fixed instead of calculated from its valence.

In a query it requires exactly that many implicit hydrogens.

### `mapping`

- Type: integer
- Required: no
- Values: at least 1

Atom-to-atom mapping number within a reaction; omitted for an unmapped atom.

### `invRet`

- Type: integer
- Required: no
- Default: `0`
- Values: [Inversion / retention](../enums/inv-ret.md)

Stereo outcome of the reaction at this atom: inversion or retention.

### `exactChangeFlag`

- Type: boolean
- Required: no
- Default: `false`

Marks that the reaction changes this atom exactly as drawn; written only as `true`.

### `cip`

- Type: string
- Required: no
- Values: [Atom CIP descriptor](../enums/atom-cip.md)

Cahn–Ingold–Prelog descriptor of the stereocentre.

Informational: a reader derives the configuration from the wedge bonds, not from this key.

### `queryProperties`

- Type: [Atom query properties](query-properties.md)
- Required: no
- Query: yes

Further search constraints of the atom.

### `selected`

- Type: boolean
- Required: no
- Default: `false`

Editor state: the atom is selected. Carries no chemical meaning; written only as `true`.

## Rules

1. A plain atom has no `type` key; `"type": "atom"` is not a valid atom.
2. `label` and `location` are required, and `location` holds exactly three numbers.
3. An atom carries only the keys listed here.
4. Integer values are JSON numbers, not strings: `"charge": 1`, never `"charge": "1"`.
5. A key whose value is the default is omitted.

## Examples

- [Atom properties](../examples/atom-properties.md)
- [An explicit "type": "atom"](../examples/atom-explicit-type.md)

## Related

- [Molecule](molecule.md)
- [Atom query properties](query-properties.md)
