Embedding the Viewer
====================

Miew is available as a `UMD module <https://github.com/umdjs/umd>`__
thus being compatible with the most popular module loading schemes:

- ``<script>`` tag defining a global variable ``Miew``,
- `Require.js <http://requirejs.org/>`__ AMD module ``Miew``,
- CommonJS module for `Node.js <https://nodejs.org/>`__,
  `Browserify <http://browserify.org/>`__, and
  `Webpack <https://webpack.github.io/>`__.

Please note that Miew doesn't work under
`Node.js <https://nodejs.org/>`__ directly since the major viewer
requirement is WebGL rendering. However, it still can be installed via
`NPM <https://www.npmjs.com/>`__ and ``require``-ed in your browserify
or webpack-based projects.

Browser Globals
---------------

*index.html*

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Miew via Global</title>
      
      <link rel="stylesheet" href="Miew.min.css">
      <script src="Miew.min.js"></script>
    </head>
    <body>
      <div class="miew-container" style="width:640px; height:480px"></div>

      <script>
        (function() {
          var viewer = new Miew({
            container: document.getElementsByClassName('miew-container')[0],
            load: '1CRN',
          });

          if (viewer.init()) {
            viewer.run();
          }
        })();
      </script>
    </body>
    </html>

Require.js Module
-----------------

*index.html*

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Miew via Require.js</title>

      <link rel="stylesheet" href="Miew.min.css">
      <script src="require.min.js"></script>
    </head>
    <body>
      <div class="miew-container" style="width:640px; height:480px"></div>

      <script>
        require(['Miew.min'], function(Miew) {
          var viewer = new Miew({
            container: document.getElementsByClassName('miew-container')[0],
            load: '1CRN',
          });

          if (viewer.init()) {
            viewer.run();
          }
        });
      </script>
    </body>
    </html>

Node.js
-------

*index.js*

.. code-block:: js

    var Miew = require('miew');
    console.log(Miew.VERSION);

Browserify
----------

*index.html*

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Miew via Browserify</title>

      <link rel="stylesheet" href="Miew.min.css">
      <script src="bundle.js"></script>
    </head>
    <body>
      <div class="miew-container" style="width:640px; height:480px"></div>
    </body>
    </html>

*index.js*

.. code-block:: js

    var Miew = require('miew');

    window.onload = function() {
      var viewer = new Miew({
        container: document.getElementsByClassName('miew-container')[0],
        load: '1CRN',
      });

      if (viewer.init()) {
        viewer.run();
      }
    };

Webpack
-------

*index.html*

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Miew via Webpack</title>

      <script src="bundle.js"></script>
    </head>
    <body>
      <div class="miew-container" style="width:640px; height:480px"></div>
    </body>
    </html>

*index.js*

.. code-block:: js

    require('miew/dist/Miew.min.css');

    var Miew = require('miew');

    window.onload = function() {
      var viewer = new Miew({
        container: document.getElementsByClassName('miew-container')[0],
        load: '1CRN',
      });

      if (viewer.init()) {
        viewer.run();
      }
    };

*webpack.config.js*

.. code-block:: js

    module.exports = {
      entry: './index.js',
      output: {
        filename: 'bundle.js'
      },
      module: {
        rules: [{
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        }],
      },
    };
