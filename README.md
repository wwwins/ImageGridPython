# ImageGridPython
Split an image into grid with python

## Install
```shell
pip install imageGrid
or
pip install -e .
```
## Usage
### Output images to `tmp/` for instagram grid
```python
import imageGrid
imageGrid.saveGrid('image.jpg', 3, 4)
```
### Work with Instagram-API-python
[example](https://github.com/wwwins/Instagram-API-python/blob/master/examples/upload_photo_grid.py)