## Site's source branch

To compile site install [Sphinx](http://sphinx-doc.org/) v1.3.1

    `sudo pip install -r requirements.txt`

Also, you will need *Indigo* if you want to use the special `indigorenderer` directives. You can simply copy the python binaries into the *root* folder.


and then run:

    `make html`


Optionaly you could also install the [livereload](https://livereload.readthedocs.org/en/latest/) package, run
`python watch.py` and see how the documentation recompiles/updates as you modify sources.
