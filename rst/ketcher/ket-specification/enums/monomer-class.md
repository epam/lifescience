---
kind: enum
---

# Monomer class

The chemical role of a monomer, as the monomer classes of MOL V3000 template definitions.

The values are case-sensitive: `"CHEM"`, not `"Chem"`.

| Value | Name | Meaning |
| --- | --- | --- |
| `"AminoAcid"` | amino acid | An amino acid of a peptide. |
| `"Sugar"` | sugar | The sugar of a nucleotide. |
| `"Base"` | base | The nucleobase of a nucleotide. |
| `"Phosphate"` | phosphate | The phosphate linker of a nucleotide. |
| `"RNA"` | RNA | A whole ribonucleotide as one monomer. |
| `"DNA"` | DNA | A whole deoxyribonucleotide as one monomer. |
| `"CHEM"` | chemical | Any other chemical monomer, such as a dye or a linker. |
| `"Terminator"` | terminator | A group that ends a chain. |
| `"Linker"` | linker | A group that links two chains. |
| `"Unknown"` | unknown | The class is not known. |
