# Concepts

## Document structure

A document is one JSON object, and its [Root](document-structure/root.md) says what the document contains:

- [`root.nodes`](document-structure/root.md#nodes) lists what the document shows. Molecules, R-groups, monomers and monomer shapes are stored under top-level keys of their own and appear in `root.nodes` as references such as `{"$ref": "mol0"}`. Arrows, pluses, shapes, texts and images are written inline.
- [`root.connections`](document-structure/root.md#connections) holds the bonds that are not edges of a single molecule: bonds between monomers, between monomers and atoms, and haptic bonds.
- [`root.templates`](document-structure/root.md#templates) lists the monomer templates the document uses. The templates themselves are stored under top-level keys, like molecules.

## References

| Reference | Points to | Written as |
| --- | --- | --- |
| an element of `root.nodes` or `root.templates` | an object under a top-level key | `$ref` holds the key, for example `"mol0"` |
| a bond, an S-group, an attachment group | atoms of the same molecule | integer indexes into the molecule’s `atoms`, starting at 0 |
| a haptic endpoint | an atom or an attachment group of a molecule | `moleculeId` holds the molecule’s key; `atomId` the atom index as a string, or `attachmentGroupId` the group’s `id` |

Keys are resolved by name. A reference to a key the document does not have makes the document invalid.

## Coordinates

- Positions are in KET length units. Writers lay structures out with a standard bond length of 1.0.
- The y axis points up: a larger `y` is higher on the canvas.
- One position is the exception: the [Stereo flag position](molecules/stereo-flag-position.md) of a molecule is measured with the y axis pointing down.
- Positions have three coordinates, `[x, y, z]`; `z` is 0 in a two-dimensional drawing.

## Versions

This reference describes version 2.0.0, which a document declares as `"ket_version": "2.0.0"` at the top level; a document without `ket_version` follows version 1.0.0. KET 1.0 and 2.0 differ only in text: KET 1.0 writes a text as a serialised Draft.js document in a `data` key ([KET 1.0 text](text/text-v1.md)), KET 2.0 as the structured [Text](text/text-v2.md) object. [Versioning](versioning.md) says what a version number means and how writers and readers use it.

## Query documents

Keys marked **Query** describe search constraints rather than a structure. A document that uses any of them describes a query molecule. A reader that cannot represent queries may reject such a document.

## Rules for writers

1. Write UTF-8 JSON that starts with `{`, with no byte-order mark or whitespace before it.
2. Write `"ket_version": "2.0.0"`, and only what version 2.0.0 has ([Versioning](versioning.md)).
3. Write only the keys this reference lists, and omit a key whose value is its default.
4. Write an integer as a plain JSON integer — `1`, not `1.0` or `"1"` — except where a key is defined as a string that holds a number, such as `atomId`.
5. List every molecule, R-group, monomer and monomer shape in `root.nodes`, and every template in `root.templates`.
6. Number molecule keys from `mol0` in the order in which `root.nodes` lists the molecules.

## Rules for readers

1. Where a number is expected, accept integer and fractional notation alike: `0` and `0.0` are the same value.
2. Resolve `$ref` and `moleculeId` by key, not by the position of a node in `root.nodes`.
3. Read `ket_version` first and act on it as [Versioning](versioning.md) says; a document without it is KET 1.0.
4. A key this reference does not list carries no meaning; a reader may ignore it or reject the document. In a document of a later minor version a reader skips it ([Versioning](versioning.md)).
