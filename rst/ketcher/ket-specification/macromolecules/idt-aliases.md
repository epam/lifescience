---
kind: object
---

# IDT aliases

The codes of a monomer in the IDT notation of oligonucleotides.

A code depends on where the monomer stands in the chain: at the 5′ end, inside, or at the 3′ end. By default these are formed from the base code as `/5<base>/`, `/i<base>/` and `/3<base>/`; `modifications` gives them explicitly when they differ.

## Appears in

The value of the `idtAliases` key of a [Monomer template](monomer-template.md), an [Ambiguous monomer template](ambiguous-monomer-template.md) or a [Monomer group template](../library/monomer-group-template.md).

## Identified by

The key that holds it.

## Attributes

### `base`

- Type: string
- Required: yes

The base code, from which the codes for the three positions are formed.

### `modifications`

- Type: object
- Required: no

The codes for the positions, when they are not formed from `base`.

When present, only the positions it lists are allowed: a monomer whose `modifications` has no `endpoint3` cannot stand at the 3′ end.

#### `modifications.endpoint5`

- Type: string
- Required: no

Code of the monomer at the 5′ end.

#### `modifications.internal`

- Type: string
- Required: no

Code of the monomer inside the chain.

#### `modifications.endpoint3`

- Type: string
- Required: no

Code of the monomer at the 3′ end.

## Rules

1. `base` is required.
2. A code has at most 10 characters besides the slashes, and a slash appears only as its first or last character.

## Related

- [Monomer template](monomer-template.md)
