from livereload import Server, shell
import os, sys

if os.path.isdir('indigo'):       # we have indigo libs
  os.environ['PYTHONPATH'] = 'indigo'

if hasattr(sys, 'real_prefix'):   # check whether we are called from virtualenv
  sphinx_build = os.path.join(sys.prefix, 'bin/sphinx-build')
  if os.path.isfile(sphinx_build):
    os.environ['SPHINXBUILD'] = sphinx_build

server = Server()
server.watch('rst/', shell('make -e html'))
server.serve(root='build/html')