---
kind: object
match: { type: molecule }
---

# Molecule

A molecular graph — atoms, bonds and S-groups — with its attachment groups and properties.

A molecule object may hold several unconnected fragments; writers usually put each connected component in an object of its own. Atom indexes used by bonds, S-groups, attachment groups and connections are positions in this object’s `atoms` array.

## Appears in

A top-level value under a key such as `mol0`, referenced from [`root.nodes`](../document-structure/root.md#nodes) as `{"$ref": "mol0"}`.

## Identified by

`"type": "molecule"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"molecule"`

Object type; always `molecule`.

### `atoms`

- Type: array of one of [Atom](atom.md), [R-group label](rg-label.md), [Atom list](atom-list.md)
- Required: yes

The atoms of the molecule: plain atoms, R-group labels and atom lists.

### `bonds`

- Type: array of [Bond](bond.md)
- Required: no

The bonds of the molecule; may be omitted or empty.

### `sgroups`

- Type: array of one of [Generic S-group](../sgroups/sgroup-gen.md), [Multiple group](../sgroups/sgroup-mul.md), [Structural repeating unit](../sgroups/sgroup-sru.md), [Superatom](../sgroups/sgroup-sup.md), [Data S-group](../sgroups/sgroup-dat.md), [Copolymer](../sgroups/sgroup-cop.md), [Query component](../sgroups/sgroup-query-component.md)
- Required: no

S-groups defined on the atoms of the molecule; see [S-groups](../sgroups/index.md).

### `stereoFlagPosition`

- Type: [Stereo flag position](stereo-flag-position.md)
- Required: no

Where the enhanced stereochemistry label of the molecule (ABS, AND, OR, Mixed) is drawn.

### `properties`

- Type: array of [Property](property.md)
- Required: no

Key–value properties of the molecule, such as the data fields of an SD file record.

### `highlight`

- Type: array of [Highlight](highlight.md)
- Required: no
- Items: at most 2

Atoms and bonds shown highlighted.

### `attachmentGroups`

- Type: array of [Attachment group](../haptic/attachment-group.md)
- Required: no

Groups of atoms of this molecule that take part in haptic bonds as a whole.

## Rules

1. `type` and `atoms` are required.
2. Every atom index — in bonds, S-groups and attachment groups — is a position in this molecule’s own `atoms` array.
3. The molecule is listed in `root.nodes`; a molecule no node references is not part of the document.

## Examples

- [Atom properties](../examples/atom-properties.md)
- [Benzene–chromium half sandwich](../examples/haptic-half-sandwich.md)

## Related

- [Atom](atom.md)
- [Attachment group](../haptic/attachment-group.md)
- [Document](../document-structure/document.md)
