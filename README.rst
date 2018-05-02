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

Output images to ``/tmp`` for instagram grid

.. code:: python

   import imageGrid
   imageGrid.saveGrid('image.jpg', 3, 4)