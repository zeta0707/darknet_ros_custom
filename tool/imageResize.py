import glob, os
new_path = 'data/'
count = 0
from PIL import Image
for file in glob.glob("*.jpg"):
    image = Image.open(file)
    resize_image = image.resize((416, 416))
    resize_image = resize_image.rotate(-90)
    resize_image.save(new_path + str(count) + '.jpg')
    count = count+1
