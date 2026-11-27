# Examples

Every example is a complete KET document. An invalid example breaks exactly one rule, which it names; the list marks those examples as invalid.

## Molecules

- [Atom properties](atom-properties.md) — an isotope, a charge, a radical and an alias.
- [An explicit "type": "atom"](atom-explicit-type.md) — invalid: a plain atom written with a `type` key.
- [Bond types and stereo](bond-stereo.md) — a wedge bond at a stereocentre, and a double bond.
- [Query bonds](bond-query.md) — query bond types, a ring bond and a custom-query bond.
- [Atom list](atom-list.md) — list atoms that match some elements, or any element but some.
- [Stereo flag position](stereo-flag-position.md) — where the stereo label goes, with its y axis pointing down.
- [Molecule properties](molecule-properties.md) — named properties of a molecule.
- [Highlighted atoms and bonds](highlight.md) — a highlight of atoms and one of bonds.

## S-groups

- [Generic S-group](sgroup-generic.md) — a bracket with no further meaning.
- [Multiple group](sgroup-multiple.md) — one CH2 group that stands for two.
- [Structural repeating unit](sgroup-repeating-unit.md) — the repeating unit of polyethylene.
- [Copolymer](sgroup-copolymer.md) — two repeating units inside a copolymer bracket.
- [Superatom](sgroup-superatom.md) — a carboxyl group abbreviated as COOH, with its attachment point.
- [Data S-group](sgroup-data.md) — a data field on an atom, drawn at a given position.
- [Query component](sgroup-query-component.md) — two query atoms that must match in one molecule of the target.

## R-groups

- [R-group](rgroup.md) — an R-site with two members and the logic of its R-group.

## Reactions and drawing objects

- [Reaction](reaction.md) — reactants, a plus, an arrow and a product.
- [Arrow modes](arrow-modes.md) — an equilibrium arrow and an elliptical arc arrow.
- [Multi-tailed arrow](multi-tailed-arrow.md) — two starting materials that lead to one product.
- [Simple objects](simple-objects.md) — a rectangle, an ellipse and a line.
- [Image](image.md) — an SVG image placed by its bounding box.

## Text

- [Styled text in the KET 2.0 form](text-v2-styled.md) — paragraphs, a default font, alignment and styled runs.
- [Text in the KET 1.0 form](text-v1.md) — a text with styled runs, as a serialised Draft.js document.

## Macromolecules

- [Peptide](peptide.md) — two monomers joined by a connection.
- [Monomer connected to a molecule](monomer-to-molecule.md) — a connection from a monomer to an atom.
- [Ambiguous monomer](ambiguous-monomer.md) — a mixture of two monomers in a given ratio.
- [Monomer shape](monomer-shape.md) — a shape that stands for two monomers.
- [Monomer library](monomer-library.md) — templates and a group template, with nothing to draw.

## Haptic bonds

- [Benzene–chromium half sandwich](haptic-half-sandwich.md) — an attachment group bonded to a metal.
- [Atom-to-atom haptic bond](haptic-atom-atom.md) — a haptic connection between two atoms.
- [Attachment group without a connection](haptic-group-only.md) — a group that no connection uses.
- [A haptic connection between two groups](haptic-group-group.md) — invalid: neither end is an atom.
- [Group molecule missing from root.nodes](haptic-molecule-not-listed.md) — invalid: the molecule of the group is not listed in `root.nodes`.
- [Charged attachment group](haptic-group-charge.md) — a cyclopentadienyl group with the charge −1.
