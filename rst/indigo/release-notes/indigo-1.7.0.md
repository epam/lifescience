# Indigo 1.7.0

*26 May 2022*

## Features
* API web service: added /render endpoint for rendering compounds and reactions
* API: added logP calculation to Python API
* API: added atom hybridization calculation to Python API
* API: added salt stripping method to Python API
* Core: added support for multistep reactions
* Ketcher WASM API: added InChIKey calculation method
* API: Added Jupyter notebooks with examples of using Indigo in machine learning
* API: Added initial version of graph neural networks featurizers

## Improvements
* ZLib updated to 1.2.12
* LibPNG updated to 1.6.37
* TinyXML updated to TinyXML2 9.0.0
* Bingo PostgreSQL support to Postgres 13 and 14 added, thanks @SPKorhonen;
  dropped support for Postgres 9.6

## Bugfixes
* Bingo Elastic: fixed exact search (#644)
* Core: Ketcher format loader: options handling fixed (#588)
* API: Fixed `name()` calling for RXNV3000 format (#678)
* Numerous fixes for Ketcher data format (#689, #711, #733, #734)
* API web service: fixed descriptors calculation

