---
kind: object
query: true
---

# Atom query properties

Additional search constraints on an atom, or a whole atom query written as SMARTS.

## Appears in

The value of the `queryProperties` key of an [Atom](atom.md).

## Identified by

A plain object: `customQuery` alone, or any combination of the other keys.

## Attributes

### `customQuery`

- Type: string
- Required: no
- Values: a SMARTS atom expression without the enclosing brackets, at most 4000 characters
- Query: yes

The complete atom query as a SMARTS atom expression, for example `#6;R2`.

When present it defines the atom on its own: the other query properties, and the atom’s label, carry no meaning. Writers set the label to `A`.

### `aromaticity`

- Type: string
- Required: no
- Values: `"aromatic"`, `"aliphatic"`
- Query: yes

Requires the atom to be aromatic or aliphatic, as SMARTS `a` or `A`.

### `ringMembership`

- Type: integer
- Required: no
- Values: 0 to 9
- Query: yes

Number of smallest rings the atom belongs to, as SMARTS `R<n>`.

### `ringSize`

- Type: integer
- Required: no
- Values: 0 to 9
- Query: yes

Size of the smallest ring the atom belongs to, as SMARTS `r<n>`.

### `connectivity`

- Type: integer
- Required: no
- Values: 0 to 9
- Query: yes

Total number of connections of the atom, implicit hydrogens included, as SMARTS `X<n>`.

### `chirality`

- Type: string
- Required: no
- Values: `"clockwise"`, `"anticlockwise"`
- Query: yes

Required chirality of the atom, as SMARTS `@@` (clockwise) or `@` (anticlockwise).

A chirality that may also be unspecified is written as `customQuery` instead.

## Rules

1. With `customQuery` present, no other query property is written.

## Related

- [Atom](atom.md)
