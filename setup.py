from setuptools import setup
import re

with open('imageGrid/__init__.py') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with open('README.rst') as f:
    readme = f.read()

setup(name='imageGrid',
      version=version,
      description='Split an image into grid',
      long_description=readme,
      url='https://github.com/wwwins/ImageGridPython',
      author='wwwins',
      author_email='cphuang72@gmail.com',
      license='MIT',
      packages=['imageGrid'],
      zip_safe=False,
      keywords='imageGrid instagram grid',
      install_requires=[
          'Pillow'
      ])
