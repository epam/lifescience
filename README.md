## Migration branch

To compile site install [Sphinx](http://sphinx-doc.org/) and
then run:

    `make html`

The folder `source` contains plain old html extracted from
the plain old GGA site. Install or compile
[pandoc](http://johnmacfarlane.net/pandoc/) package
(version >= 1.13) to convert it to rST yourself and then run

    `./convert.sh <dest-dir>`
