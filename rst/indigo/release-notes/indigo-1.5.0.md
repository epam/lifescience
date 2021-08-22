# Indigo 1.5.0


*18 Aug 2021*


## Summary



**New features and improvements**:

* WASM support. See [how to build](https://github.com/epam/Indigo#how-to-build-indigo-wasm).
* Internal json-based ketcher format support [implemented](https://github.com/epam/Indigo/issues/180).
* Ketcher format reactions [supported](https://github.com/epam/Indigo/issues/396).
* Ketcher format r-groups [supported](https://github.com/epam/Indigo/issues/307).
* Selection support issues [fixed](https://github.com/epam/Indigo/pull/353).
* WASM memory issues [fixed](https://github.com/epam/Indigo/pull/342).
* Now Indigo uses CMake build system.
* .NET Indigo nuget error: Unable to load DLL 'indigo' [fixed](https://github.com/epam/Indigo/issues/450).
* Migrating to standard C++11 containers has started. [std::unique_ptr](https://github.com/epam/Indigo/issues/418) and [std::shared_ptr](https://github.com/epam/Indigo/issues/419).
* C++ unittests [added](https://github.com/epam/Indigo/issues/403).
* Check molecule [refactored and result format changed](https://github.com/epam/Indigo/issues/390).
* Bingo-mssql compilation issues [fixed](https://github.com/epam/Indigo/issues/189).
* Multiple integration tests [added](https://github.com/epam/Indigo/tree/master/api/tests/integration).
* Ionize segfault for deuterated molecule (if pKa-model-level >= 1) [fixed](https://github.com/epam/Indigo/issues/153).
* SDF decomposition test segfault [fixed](https://github.com/epam/Indigo/issues/431).
* Fingerprints difference between mac os x and other platforms [fixed](https://github.com/epam/Indigo/issues/207).
* Bindgo CI for Postgres 9.6 [added](https://github.com/epam/Indigo/pull/411).
* Reusable array shallow copy issue [fixed](https://github.com/epam/Indigo/pull/385).
* Indigo NodeJS wrapper [implemented](https://github.com/epam/Indigo/issues/245).
* Bingo Elastic python: reactions [supported](https://github.com/epam/Indigo/issues/259).
* List of exported symbols for libindigo.so [fixed](https://github.com/epam/Indigo/pull/276).
* Misc. C++11 related [refactoring](https://github.com/epam/Indigo/pull/335).
* Atoms and bonds arrays [optimization](https://github.com/epam/Indigo/pull/267).
* .NET API: oneBitsList [exposed](https://github.com/epam/Indigo/pull/329).
* Context manager and iterator for Bingo object [implemented](https://github.com/epam/Indigo/pull/241).
* CDX test [fixed](https://github.com/epam/Indigo/pull/387).
* Java API - native libs loading [fixed](https://github.com/epam/Indigo/pull/261).
* Bingo Elastic Java API [implemented](https://github.com/epam/Indigo/pull/198).



