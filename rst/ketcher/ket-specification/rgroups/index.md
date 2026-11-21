# R-groups

An R-group query describes a family of structures: a core molecule with R-sites, and for each R-site a set of fragments, the [members](rgroup-member.md), any one of which may take its place.

- The core is an ordinary [Molecule](../molecules/molecule.md). Each R-site in it is an [R-group label](../molecules/rg-label.md) that names one or more R-groups: `"$refs": ["rg-1"]` for R1.
- Each R-group is an [R-group](rgroup.md) object stored under the top-level key `rg<N>`, where `N` is its number, and listed in [`root.nodes`](../document-structure/root.md#nodes) as `{"$ref": "rg1"}`.
- An atom of a member that bonds to the R-site is marked with the atom key `attachmentPoints`. A member bonded to an R-site with two bonds has a first and a second attachment point.
- The logic of each R-group, its [`rlogic`](rgroup.md#rlogic), says how many times it may occur and how it depends on the other R-groups.

R-group numbers run from 1 to 32.
