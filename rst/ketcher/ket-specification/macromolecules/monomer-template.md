---
kind: object
match: { type: monomerTemplate }
---

# Monomer template

The definition of a monomer: its structure, names, class and attachment points.

## Appears in

A top-level value under the key `monomerTemplate-<id>` of the [Document](../document-structure/document.md), listed in [`root.templates`](../document-structure/root.md#templates). A monomer library holds many of them.

## Identified by

`"type": "monomerTemplate"`.

## Attributes

### `type`

- Type: string
- Required: yes
- Values: `"monomerTemplate"`

Object type; always `monomerTemplate`.

### `id`

- Type: string
- Required: yes

Identifier of the template, unique among the templates of the document; monomers refer to it by `templateId`.

Libraries form it from the alias and the full name, as in `A___Alanine`; any non-empty string is allowed.

### `class`

- Type: string
- Required: yes
- Values: [Monomer class](../enums/monomer-class.md)

Chemical role of the monomer, such as amino acid, sugar or base.

### `classHELM`

- Type: string
- Required: no
- Values: [HELM polymer type](../enums/helm-polymer-type.md)

The HELM polymer type the monomer belongs to.

### `alias`

- Type: string
- Required: yes

Short symbol that labels the monomer, such as `A` for alanine.

### `name`

- Type: string
- Required: no

Name of the monomer used by sequence formats, such as `Ala`.

### `fullName`

- Type: string
- Required: no

Full, human-readable name of the monomer, such as `Alanine`.

### `naturalAnalogShort`

- Type: string
- Required: no

One-letter code of the natural monomer this one is a modified version of, such as `A`; for a natural monomer, its own code.

### `naturalAnalog`

- Type: string
- Required: no

Three-letter code of the natural monomer this one is a modified version of, such as `Ala`, `Rib` or `Ade`; omitted when the monomer has no natural analogue.

### `aliasHELM`

- Type: string
- Required: no

The monomer's symbol in HELM, when it differs from `alias`: at most 23 characters, without spaces.

An empty string means that the monomer has no HELM symbol.

### `aliasAxoLabs`

- Type: string
- Required: no

The monomer's symbol in the AxoLabs notation.

### `aliasBILN`

- Type: string
- Required: no
- Pattern: `^[A-Za-z0-9_*-]+$`
- Values: letters, digits, `_`, `*` and `-`

The monomer's symbol in the BILN notation.

### `idtAliases`

- Type: [IDT aliases](idt-aliases.md)
- Required: no

The monomer's codes in the IDT notation of oligonucleotides.

### `modificationTypes`

- Type: array of string
- Required: no
- Items: at least 1

The kinds of modification the monomer carries, such as `"N-methylation"` or `"Phosphorylation"`.

### `unresolved`

- Type: boolean
- Required: no
- Default: `false`

Whether the structure of the monomer is unknown; an unresolved template has no atoms.

### `hidden`

- Type: boolean
- Required: no
- Default: `false`

Whether a library hides the template from the list of monomers offered to the user.

### `comment`

- Type: string
- Required: no

A free-text comment on the template.

### `attachmentPoints`

- Type: array of [Monomer attachment point](monomer-attachment-point.md)
- Required: no

The points where the monomer connects to others, in the order R1, R2, then the side points.

### `atoms`

- Type: array of one of [Atom](../molecules/atom.md), [R-group label](../molecules/rg-label.md), [Atom list](../molecules/atom-list.md)
- Required: no

The atoms of the monomer, including the atoms of its leaving groups.

### `bonds`

- Type: array of [Bond](../molecules/bond.md)
- Required: no

The bonds of the monomer.

### `sgroups`

- Type: array of one of [Generic S-group](../sgroups/sgroup-gen.md), [Multiple group](../sgroups/sgroup-mul.md), [Structural repeating unit](../sgroups/sgroup-sru.md), [Superatom](../sgroups/sgroup-sup.md), [Data S-group](../sgroups/sgroup-dat.md), [Copolymer](../sgroups/sgroup-cop.md), [Query component](../sgroups/sgroup-query-component.md)
- Required: no

The S-groups of the monomer's structure.

## Rules

1. `type`, `id`, `class` and `alias` are required, and every template but an unresolved one has `atoms`.
2. The template's key is `monomerTemplate-` followed by its `id`, and `root.templates` lists it.
3. `classHELM` agrees with `class`: `PEPTIDE` for amino acids, `RNA` for sugars, phosphates, bases and nucleotides, `CHEM` for other monomers.
4. When both `naturalAnalog` and `naturalAnalogShort` are given, they name the same monomer.
5. Atom indexes in `attachmentPoints` are positions in the template's `atoms`.

## Examples

- [Peptide](../examples/peptide.md)
- [Monomer connected to a molecule](../examples/monomer-to-molecule.md)

## Related

- [Monomer](monomer.md)
- [Monomer attachment point](monomer-attachment-point.md)
- [IDT aliases](idt-aliases.md)
