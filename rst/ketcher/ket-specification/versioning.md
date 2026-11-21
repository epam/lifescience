# Versioning

A document says which version of the format it follows, so that a reader knows how to read it before it reads anything else. This chapter says what a version number means, when each of its parts changes, which version a writer declares, and what a reader does with a version it does not know.

## Version numbers

A version is three non-negative integers separated by dots, `MAJOR.MINOR.PATCH`, written without leading zeros, such as `2.0.0`. A document declares its version as a string in [`ket_version`](document-structure/document.md#ket_version). A document without `ket_version` follows version 1.0.0.

Versions are compared number by number from the left, as numbers: 2.10.0 is later than 2.9.0, and 3.0.0 is later than both.

## What changes a version

| Part | Raised for | What a reader of the earlier version can do |
| --- | --- | --- |
| MAJOR | A change after which a reader of the earlier version would misread a document: a key removed or renamed; a new required key; a type, unit, meaning or default changed; a value written in a different form. | Nothing: it cannot read the document correctly. |
| MINOR | An addition that a reader of the earlier version can skip: a new optional key, a new object, a new kind of node, a new value of an enumeration. | Read the document, losing only what was added. |
| PATCH | A correction of this reference that makes no valid document invalid and no invalid document valid. | Read the document as before. |

A change that fits none of the rows is a MAJOR change. Raising a part sets the parts to its right to 0: after 2.3.1 come 2.3.2, 2.4.0 and 3.0.0.

## Version history

| Version | Change from the version before |
| --- | --- |
| 1.0.0 | The first version. A document has no `ket_version`. |
| 2.0.0 | A text is written as the structured [Text](text/text-v2.md) object instead of a serialised Draft.js document, the [KET 1.0 text](text/text-v1.md). A document declares its version in `ket_version`. |

This reference marks what a version after 1.0.0 introduced with **Since** and that version: an object among the facts at the top of its page, an attribute among its facts, a value of an enumeration in a column of the table of values. What has no mark is in every version.

## Rules for writers

1. Write `ket_version` in every document, with the version of this reference the writer follows.
2. Use only the objects, keys and values the declared version has: nothing whose **Since** is a later version.

## Rules for readers

1. Read `ket_version` before the rest of the document. A document without it is version 1.0.0.
2. Reject a document whose `ket_version` is not a string of the form `MAJOR.MINOR.PATCH`, and say what the value is.
3. Compare versions as numbers and ignore PATCH: versions that differ only in PATCH are the same version.
4. A document of the reader's MAJOR, and of a MINOR no later than the reader's: read it.
5. A document of the reader's MAJOR and of a later MINOR: read it, and skip the keys, objects and values the reader does not know — they are the additions of the later versions. The reader may warn that their content is lost.
6. A document of a later MAJOR: reject it, and name its version and the latest version the reader reads.
7. A document of an earlier MAJOR: read it by the rules of its version, as the version history describes them, or reject it and name its version.
