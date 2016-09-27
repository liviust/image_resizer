from PIL import Image
from scipy.misc import imresize
import os
import sys

def resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = imresize(im, size=(150, 150))  # replace with desired dims
    new_im.save(file_path + "copy.jpg")

def bulkResize(folder):
    imgExts = ["jpg"]
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            resize(path, file_name)


if __name__ == "__main__":
    bulkResize("<path goes here>")
