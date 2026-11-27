---
kind: object
match: { type: ambiguousMonomerTemplate }
---

# Ambiguous monomer template

A monomer that is one of several monomers, or a mixture of them: each option names a monomer template.

Its class is the class its options share, and its attachment points are those all of its options have.

## Appears in

A top-level value under the key `ambiguousMonomerTemplate-<id>` of the [Document](../document-structure/document.md), listed in [`root.templates`](../document-structure/root.md#templates).

## Identified by

`"type": "ambiguousMonomerTemplate"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"ambiguousMonomerTemplate"`

Object type; always `ambiguousMonomerTemplate`.

### `id`

- Type: string
- Required: yes

Identifier of the template, unique among the ambiguous monomer templates of the document; ambiguous monomers refer to it by `templateId`.

### `subtype`

- Type: string
- Required: yes
- Values: [Ambiguous monomer subtype](../enums/ambiguous-monomer-subtype.md)

Whether the monomer is one of the options or a mixture of them.

### `alias`

- Type: string
- Required: yes

Symbol that labels the monomer, such as `X` or `%`.

### `options`

- Type: array of object
- Required: yes
- Items: at least 2

The monomers this one may be or may contain.

#### `options.templateId`

- Type: string
- Required: yes

The `id` of the monomer template of this option.

#### `options.probability`

- Type: number
- Required: no
- Values: at least 0

In an `alternatives` template: how likely this option is; omitted when unknown.

#### `options.ratio`

- Type: number
- Required: no
- Values: at least 0

In a `mixture` template: the relative amount of this option; omitted when unknown.

### `idtAliases`

- Type: [IDT aliases](idt-aliases.md)
- Required: no

The monomer's codes in the IDT notation of oligonucleotides.

## Rules

1. `type`, `id`, `subtype`, `alias` and `options` are required.
2. The template's key is `ambiguousMonomerTemplate-` followed by its `id`, and `root.templates` lists it.
3. Every option's `templateId` is the `id` of a monomer template that `root.templates` lists.
4. The options of an `alternatives` template give no `ratio`, and those of a `mixture` template no `probability`.

## Examples

- [Ambiguous monomer](../examples/ambiguous-monomer.md)

## Related

- [Ambiguous monomer](ambiguous-monomer.md)
- [Monomer template](monomer-template.md)
