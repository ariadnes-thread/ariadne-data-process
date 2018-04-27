from skimage import io, transform, filters
from PIL import Image
from os import path

# Reference: https://viewer.nationalmap.gov/basic/
# https://services.nationalmap.gov/arcgis/rest/services/USGSNAIPPlus/MapServer/export?bbox=-13150916.668093424%2C4046564.3341315635%2C-13148346.473017335%2C4047808.824498332&size=1076%2C521&dpi=96&format=png24&transparent=true&bboxSR=3857&imageSR=3857&layers=show%3A1%2C1047423312%2C4%2C8%2C292379871%2C997486456%2C997486460&f=image

images_path = path.join(path.dirname(__file__), 'images')

rgb_image = io.imread(path.join(images_path, 'caltech-aerial.png'))
shape = rgb_image.shape
print('Image shape: ', shape)

green_image = rgb_image.copy()

for y in range(0, shape[0]):
    for x in range(0, shape[1]):
        r = green_image[y, x, 0]
        g = green_image[y, x, 1]
        b = green_image[y, x, 2]

        new_g = 0
        if g > r and g > b:
            new_g = 255

        green_image[y, x, 0] = 0
        green_image[y, x, 1] = new_g
        green_image[y, x, 2] = 0

io.imsave(path.join(images_path, 'caltech-aerial-green.png'), green_image)

pixel_size = 5.
image = Image.open(path.join(images_path, 'caltech-aerial-green.png'))
image = image.resize((int((shape[1]/pixel_size)), int(shape[0]/pixel_size)), Image.NEAREST)
image = image.resize((shape[1], shape[0]), Image.NEAREST)
image.save(path.join(images_path, 'caltech-aerial-green-pixelated.png'))
