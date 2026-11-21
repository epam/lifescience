# Monomer library

A monomer library is a KET document that holds templates and nothing to draw: its [`root.nodes`](../document-structure/root.md#nodes) is empty, and its [`root.templates`](../document-structure/root.md#templates) lists every template it holds.

A library holds three kinds of template, each under a top-level key of its own:

| Key | Template |
| --- | --- |
| `monomerTemplate-<id>` | [Monomer template](../macromolecules/monomer-template.md) |
| `ambiguousMonomerTemplate-<id>` | [Ambiguous monomer template](../macromolecules/ambiguous-monomer-template.md) |
| `monomerGroupTemplate-<id>` | [Monomer group template](monomer-group-template.md): a preset of several monomers, such as a nucleotide made of a sugar, a base and a phosphate |

The template ids of a library are unique, and every template a group template or an ambiguous template refers to is in the library.
