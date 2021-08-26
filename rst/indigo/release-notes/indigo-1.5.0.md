# Indigo 1.5.0


*18 Aug 2021*

## Summary

Indigo chemistry API now can be distributed in web browsers by using WebAssembly builds. Also new format was added to support modern web applications. Indigo Core parts and libraries were stabilized and improved. 


## New features and improvements

* Added WebAssembly support to run Indigo in a web browser. See [how to build](https://github.com/epam/Indigo#how-to-build-indigo-wasm). [[milestone]](https://github.com/epam/Indigo/milestone/8).
* Implemented NodeJS API for Indigo [[implemented]](https://github.com/epam/Indigo/issues/245).
* Added Java API for Bingo Elasticsearch cartridge [[feature]](https://github.com/epam/Indigo/pull/198).
* Implemented reactions in Python API of Bingo Elasticsearch cartridge [[feature]](https://github.com/epam/Indigo/issues/259).
* Added support for JSON-based interaction with Ketcher for supporting enhanced stereochemistry, simple graphics, etc. [[feature]](https://github.com/epam/Indigo/issues/180)
* Supported reactions in JSON-based format [[feature]](https://github.com/epam/Indigo/issues/396).
* Supported r-groups in JSON-based format [[feature]](https://github.com/epam/Indigo/issues/307).
* Added C++ unittests [[feature]](https://github.com/epam/Indigo/issues/403).
* Added multiple integration tests [[feature]](https://github.com/epam/Indigo/tree/master/api/tests/integration).
* Now Indigo uses CMake build system. See [how to build]( https://github.com/epam/Indigo#build-instruction )
* Migrated to standard C++11 smart pointers. Changed AutoPtr to [std::unique_ptr](https://github.com/epam/Indigo/issues/418) and [std::shared_ptr](https://github.com/epam/Indigo/issues/419).
* Unified molecule check function and changed the result format [[improvement]](https://github.com/epam/Indigo/issues/390).
* Miscelaneous C++11 related refactorings: added 'override', replaced plain C functions with corresponding from std:: ) [[improvement]](https://github.com/epam/Indigo/pull/335).
* Optimized the adding of elements to atoms and bonds arrays [[improvement]](https://github.com/epam/Indigo/pull/267).
* Exposed oneBitsList in .NET API [[fix]](https://github.com/epam/Indigo/pull/329).
* Implemented context manager and iterator for Bingo object [[improvement]](https://github.com/epam/Indigo/pull/241).
* Added Bingo CI for Postgres 9.6 [[improvement]](https://github.com/epam/Indigo/pull/411).

## Bug fixes

* Incorrect calculation and check on partially selected structure [[fix]](https://github.com/epam/Indigo/pull/353).
* PNG rendering crash [[fix]](https://github.com/epam/Indigo/pull/342).
* .NET Indigo nuget error: Unable to load DLL 'indigo' [[fix]](https://github.com/epam/Indigo/issues/450).
* Bingo-MSSQL compilation fails [[fix]](https://github.com/epam/Indigo/issues/189).
* Ionize segfault for deuterated molecule (if pKa-model-level >= 1) [[fix]](https://github.com/epam/Indigo/issues/153).
* SDF decomposition test fail [[fix]](https://github.com/epam/Indigo/issues/431).
* Fingerprints differ between mac os x and other platforms [[fix]](https://github.com/epam/Indigo/issues/207).
* Unstable behavior of Indigo on different platforms [[fix]](https://github.com/epam/Indigo/pull/385).
* CDX parser failure [[fix]](https://github.com/epam/Indigo/pull/387).
* Java API: native libs loading fail [[fix]](https://github.com/epam/Indigo/pull/261).
