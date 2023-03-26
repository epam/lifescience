# Indigo 1.10.0

*22 March 2023*

## Features
* #941 CDX export

## Bugfixes
* #1003 Some texts are not rendered and may lead to Indigo crash
* #987 docker-indigo-tester image build failed
* #994 Some UTF-8 characters from Ketcher Text panel are not displayed in Indigo WASM
* #889 When saving in PNG and SVG format UTF-8 text display incorrectly (Ketcher Standalone)
* #1032 Combine molecules that are related to a single s-group into one in .Ket format
* #974 SVG/PNG: Molecule reagent located below arrow is displayed in preview above arrow
* #1039 Opening file with a superatom label saved in RXN v3000 format removes a custom s-group
* #1063 Structure saved in CDX and Base64CDX with reaction arrow cannot be opened 
* #1068 CDX-loader crash 

**Full Changelog**:https://github.com/epam/Indigo/compare/release/1.9...release/1.10