ImageGridPython
===============

Split an image into grid with python

Install
-------

.. code:: shell

   pip install imageGrid
   or
   pip install -e .

Usage
-----

Output images to ``tmp/`` for instagram grid

.. code:: python

   import imageGrid
   imageGrid.saveGrid('image.jpg', 3, 4)

Work with Instagram-API-python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`example`_

.. _example: https://github.com/wwwins/Instagram-API-python/blob/master/examples/upload_photo_grid.py