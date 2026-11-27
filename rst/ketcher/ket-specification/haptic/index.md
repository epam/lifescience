# Haptic bonds

A haptic bond binds a metal to several contiguous atoms of a ligand at once — the η⁵ bond of ferrocene is the classic case. KET represents it with two objects:

- an [Attachment group](attachment-group.md) on the ligand’s molecule, listing the atoms that bond as a whole;
- a [Haptic connection](haptic-connection.md) in [`root.connections`](../document-structure/root.md#connections), joining the group to the metal atom. Each of its two ends is a [Haptic endpoint](haptic-endpoint.md), and a haptic connection can also join two atoms directly.

```json
{
  "ket_version": "2.0.0",
  "root": {
    "nodes": [{"$ref": "mol0"}, {"$ref": "mol1"}],
    "connections": [
      {"type": "haptic", "endpoint1": {"moleculeId": "mol0", "atomId": "0"}, "endpoint2": {"moleculeId": "mol1", "attachmentGroupId": "0"}}
    ]
  },
  "mol0": {"type": "molecule", "atoms": [{"label": "Cr", "location": [2.5, 0, 0]}]},
  "mol1": {
    "type": "molecule",
    "atoms": [{"label": "C", "location": [0, 1, 0]}, {"label": "C", "location": [-0.866, 0.5, 0]}, {"label": "C", "location": [-0.866, -0.5, 0]}, {"label": "C", "location": [0, -1, 0]}, {"label": "C", "location": [0.866, -0.5, 0]}, {"label": "C", "location": [0.866, 0.5, 0]}],
    "bonds": [{"type": 2, "atoms": [0, 1]}, {"type": 1, "atoms": [1, 2]}, {"type": 2, "atoms": [2, 3]}, {"type": 1, "atoms": [3, 4]}, {"type": 2, "atoms": [4, 5]}, {"type": 1, "atoms": [5, 0]}],
    "attachmentGroups": [{"id": "0", "atoms": [0, 1, 2, 3, 4, 5]}]
  }
}
```

The metal and the ligand may be one molecule or separate molecules. Each end of a haptic connection names its molecule by key, so both layouts describe the same structure, and a reader accepts either.

## Charge and radical of a group

The charge and the radical state of a π system belong to the group, not to any of its atoms. They are the `charge` and `radical` keys of the attachment group; [Charged attachment group](../examples/haptic-group-charge.md) shows a cyclopentadienyl ligand with the charge −1.

## What is not a haptic bond

A bond of type 11 in `bonds`, a bond with `endpts` and `attach` lists, and an atom labelled `*` that stands for the centre of a group do not represent haptic bonds in KET.
