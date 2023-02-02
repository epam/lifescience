# Lifesciences Open Source portal documentation

## Overview

The repository contains sources for the EPAM Lifesciences Open Source portal.

https://lifescience.opensource.epam.com

## Build using Docker

    U=$UID docker-compose up

## Build instructions

To compile site install [Sphinx](http://sphinx-doc.org/)

    sudo pip install -r requirements.txt

and then run:

    make html


Optionally you could also install the [livereload](https://livereload.readthedocs.org/en/latest/) package, run
`python watch.py` and see how the documentation recompiles/updates as you modify sources.
