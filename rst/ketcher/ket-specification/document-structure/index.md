# Document structure

A KET file is one JSON object, the [Document](document.md). Its [Root](root.md) says what the document contains. Molecules, R-groups, monomers and monomer shapes are stored under top-level keys of their own and listed in [`root.nodes`](root.md#nodes) by reference; templates are stored the same way and listed in [`root.templates`](root.md#templates); drawing objects are written inline in `root.nodes`. [Concepts](../concepts.md) shows how the parts fit together.

- [Document](document.md) — the top-level object: the version, the root, the header and the objects stored under keys of their own.
- [Root](root.md) — what the document shows, the connections between its parts, and the templates they use.
- [Node reference](node-ref.md) — an element of `root.nodes` or `root.templates`, such as `{"$ref": "mol0"}`, that points to a stored object.
- [Point](point.md) — a position written as an object with named coordinates, used by arrows, multi-tailed arrows, simple objects, KET 1.0 texts and monomers.
