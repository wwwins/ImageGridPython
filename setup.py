from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='imageGrid',
      version='0.1.0',
      description='Split an image into grid',
      long_description=readme(),
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
