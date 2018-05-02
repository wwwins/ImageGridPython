from setuptools import setup

setup(name='imageGrid',
      version='0.1.0',
      description='Split an image into grid',
      url='https://github.com/wwwins/ImageGridPython',
      author='wwwins',
      author_email='jacky.huang@isobar.com',
      license='MIT',
      packages=['imageGrid'],
      zip_safe=False,
      keywords='imageGrid',
      install_requires=[
          'Pillow'
      ])