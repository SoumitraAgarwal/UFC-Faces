from PIL import Image
import os
import cv2

def black_background_thumbnail(path_to_image):
    img = cv2.imread(path_to_image)
    source_image = Image.open(path_to_image).convert("RGBA")
    thumbnail_size = (520, 325)
    background = Image.new('RGBA', thumbnail_size, "black")    
    
    source_image.thumbnail(thumbnail_size)
    (w, h) = source_image.size
    background.paste(source_image, ((thumbnail_size[0] - w) / 2, (thumbnail_size[1] - h) / 2 ))
    return background

# Video capture via webcam
images = os.listdir('Pictures')
images.sort()
for image in images:
    img = black_background_thumbnail('Pictures/' + image)
    img.save('Upper/' + image)