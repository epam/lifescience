---
kind: enum
---

# Bond stereo

How a bond shows the stereochemistry at its first atom, as the bond stereo of MOL files.

For values 1, 4 and 6 the first atom of the bond's `atoms` is the stereocentre.

| Value | Name | Meaning |
| --- | --- | --- |
| `0` | none | A plain bond. The default; writers omit the key. |
| `1` | up | A wedge: the second atom lies above the drawing plane. |
| `3` | cis/trans unspecified | A double bond whose configuration is unknown. |
| `4` | either | A wavy bond: the configuration at the stereocentre is unknown. |
| `6` | down | A hash: the second atom lies below the drawing plane. |
