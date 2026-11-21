---
kind: object
---

# Object annotation

A free-text note attached to a monomer or a connection, as the inline annotations of HELM.

## Appears in

The value of the `annotation` key of a [Monomer](monomer.md), an [Ambiguous monomer](ambiguous-monomer.md) or a [Connection](connection.md).

## Identified by

The key that holds it.

## Attributes

### `text`

- Type: string
- Required: yes

The text of the note.

## Rules

1. `text` is required.

## Related

- [Root](../document-structure/root.md)
