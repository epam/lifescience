# Indigo 1.6.1


*28 Dec 2021*

## Features
* PoC implementation of Indigo modern C++ user API written on top of low-level C API. Later it will be used
  in Indigo-WASM and probably other languages.
* New Indigo service added as preview. Modernized Indigo service implements JSON:API protocol and can be installed as 
  Docker image `epmlsop/indigo-service:enhanced-latest`.
* Indigo API ported to ARM64 processor architecture. Python, Java and C# wrappers now contain required native libraries 
  for macOS (Apple M1) and Linux.
* Implemented loader for CDXML format.
* Dative and hydrogen bonds are now supported.
* Implemented partial aromatization/dearomatization for the structures with superatoms.
* Multifragment support for KET-format.
* Simple objects support for KET-format.
* Atom's aliases and functional groups' attributes support for KET-format.
* Indigo-Python: initial version of inorganic salt checker added.

## Improvements
* Bingo-NoSQL major refactoring with significant multithreading performance improvements.
* C++ unittests were separated in API and Core parts.
* CMake build system by default tries to enable as many components as possible and warns if building something
  is not possible on the current platform.
* Migrated to modern C++ standard mutexes and locks instead of own-written implementation.
* Using thread-safe objects in Indigo API instead of raw mutexes to guarantee thread safety.
* C++ code modernization: added 'override', replaced plain C functions with corresponding from std, etc.
* Indigo API integration tests engine parallelized. 
* Indigo WASM API for Ketcher reached stable status and is now published to NPM public repository.
* Indigo i386 libraries for Windows prepared.
* CI/CD: automatic code style checks and linters added for Python and C++ code.

## Bugfixes
* Fixed multiple data races in API and especially in Bingo-NoSQL (#476).
* InChI library bugfix for empty string support
* Multiple small bugfixes in Indigo-Ketcher WASM module and Indigo Service.
* Bingo-Elastic-Java: updated all dependencies to fix log4j security issue.
* Fixed an occasional error in RPE.
* Bingo-NoSQL: fixed `enumerateId()` in Java.

