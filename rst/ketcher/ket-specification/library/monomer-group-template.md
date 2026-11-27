---
kind: object
match: { type: monomerGroupTemplate }
---

# Monomer group template

A preset of several monomer templates joined together, such as a nucleotide made of a sugar, a base and a phosphate.

## Appears in

A top-level value under the key `monomerGroupTemplate-<id>` of a monomer library, listed in [`root.templates`](../document-structure/root.md#templates).

## Identified by

`"type": "monomerGroupTemplate"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"monomerGroupTemplate"`

Object type; always `monomerGroupTemplate`.

### `id`

- Type: string
- Required: yes

Identifier of the group template, unique among the group templates of the library.

### `name`

- Type: string
- Required: yes
- Pattern: `^[A-Za-z0-9_*-]+$`
- Values: letters, digits, `_`, `*` and `-`

Name of the preset, at most 200 characters.

### `class`

- Type: string
- Required: yes
- Values: `"RNA"`

Class of the preset; always `RNA`.

### `templates`

- Type: array of [Node reference](../document-structure/node-ref.md)
- Required: yes
- Items: at least 1

The monomer templates of the preset, each as `{"$ref": "monomerTemplate-<id>"}`.

### `connections`

- Type: array of [Connection](../macromolecules/connection.md)
- Required: no

How the templates of the preset are joined; each end names a template by `templateId` and an attachment point.

### `idtAliases`

- Type: [IDT aliases](../macromolecules/idt-aliases.md)
- Required: no

The preset's codes in the IDT notation of oligonucleotides.

### `aliasAxoLabs`

- Type: string
- Required: no

The preset's symbol in the AxoLabs notation.

## Rules

1. `type`, `id`, `name`, `class` and `templates` are required.
2. The group template's key is `monomerGroupTemplate-` followed by its `id`, and `root.templates` lists it.
3. Every template of `templates` is a monomer template of the library.
4. The connections join the templates of `templates` into one connected group.

## Examples

- [Monomer library](../examples/monomer-library.md)

## Related

- [Monomer template](../macromolecules/monomer-template.md)
- [Connection](../macromolecules/connection.md)
