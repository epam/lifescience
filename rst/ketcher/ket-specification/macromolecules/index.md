# Macromolecules

Peptides, nucleic acids and other polymers are written as monomers joined by connections.

- A [Monomer template](monomer-template.md) is the full structure of a monomer — its atoms and bonds — with its names, class and [attachment points](monomer-attachment-point.md), and its codes in the IDT notation, the [IDT aliases](idt-aliases.md). It is stored under the top-level key `monomerTemplate-<id>` and listed in [`root.templates`](../document-structure/root.md#templates).
- A [Monomer](monomer.md) is one occurrence of a template in the drawing: a position and a reference to the template. It is stored under a top-level key such as `monomer0` and referenced from [`root.nodes`](../document-structure/root.md#nodes). Its [`transformation`](monomer.md#transformation) flips, rotates and shifts the structure of the expanded monomer relative to the template.
- A [Connection](connection.md) in [`root.connections`](../document-structure/root.md#connections) joins two monomers through their attachment points, or a monomer to an atom of a molecule. Each of its ends is a [Connection endpoint](connection-endpoint.md).
- An [Ambiguous monomer](ambiguous-monomer.md) stands for one of several monomers, or a mixture of them, defined by an [Ambiguous monomer template](ambiguous-monomer-template.md). Each of its [`options`](ambiguous-monomer-template.md#options) names a monomer template.
- A [Monomer shape](monomer-shape.md) draws a set of monomers as one symbol, such as an antibody.
- An [Object annotation](object-annotation.md) is a free-text note on a monomer, an ambiguous monomer or a connection; [`root.annotation`](../document-structure/root.md#annotation) annotates the document as a whole.

## Templates and their ids

A template has an `id`, and the same string is used everywhere the template is referred to:

| Where | Written as |
| --- | --- |
| the top-level key of the template | `monomerTemplate-<id>` |
| the reference in `root.templates` | `{"$ref": "monomerTemplate-<id>"}` |
| a monomer's `templateId` | `<id>` |
| an ambiguous template's option | `<id>` |

Ambiguous templates follow the same scheme with the prefix `ambiguousMonomerTemplate-`.

## Attachment points

A template's attachment points are named `R1`, `R2` and so on. In a chain, `R1` is the left point, `R2` the right one, and `R3` and above are side points. A point may have a leaving group: atoms of the template that are removed when a connection uses the point.

## Coordinates

A monomer's `position` places the origin of its template's coordinates in the drawing, in the same units and with the same y axis as atom locations. The atoms of an expanded monomer are at the position plus the template's atom locations, after the monomer's transformation.
