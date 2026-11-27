---
kind: object
---

# Connection endpoint

One end of a connection: an attachment point of a monomer, a monomer as a whole, or an atom of a molecule.

| End | Keys |
| --- | --- |
| an attachment point of a monomer | `monomerId` and `attachmentPointId` |
| a monomer, in a hydrogen connection | `monomerId` |
| an atom of a molecule | `moleculeId` and `atomId` |
| an attachment point of a template, in a monomer group template | `templateId` and `attachmentPointId` |

## Appears in

The value of `endpoint1` or `endpoint2` of a [Connection](connection.md).

## Identified by

The key that holds it.

## Attributes

### `monomerId`

- Type: string
- Required: no

The top-level key of the monomer or ambiguous monomer, such as `monomer0`.

### `attachmentPointId`

- Type: string
- Required: no
- Pattern: `^R[1-8]$`
- Values: `R1` to `R8`

Name of the monomer's attachment point.

### `moleculeId`

- Type: string
- Required: no
- Pattern: `^mol[0-9]+$`
- Values: `mol0`, `mol1` and so on

The top-level key of the molecule.

### `atomId`

- Type: string (integer)
- Required: no
- Values: at least 0

Index of the atom in the molecule's `atoms` array, written as a string: `"2"`, not `2`.

### `templateId`

- Type: string
- Required: no

In a monomer group template: the top-level key of the monomer template at this end, such as `monomerTemplate-R___Ribose`.

## Rules

1. An endpoint has exactly one of the combinations of keys in the table above.
2. `monomerId` names a monomer or an ambiguous monomer of the document by its key, not by its `id`.
3. `moleculeId` names a molecule of the document, and `atomId` an atom of that molecule.
4. The molecule named by `moleculeId` is one connected fragment.

## Examples

- [Peptide](../examples/peptide.md)
- [Monomer connected to a molecule](../examples/monomer-to-molecule.md)

## Related

- [Connection](connection.md)
- [Monomer attachment point](monomer-attachment-point.md)
