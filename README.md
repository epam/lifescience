## Migration branch

Temporary command sequence to compile site:

 * `virtualenv --system-site-packages env`
 * `env/bin/pip env/bin/pip install -r requirements.txt`
 * `make html`

The folder `source` contains plain old html extracted from
the plain old GGA site. Install or compile `pandoc` package
(version >= 1.13) to convert it to rST yourself and then run

    `./convert.sh <dest-dir>`
