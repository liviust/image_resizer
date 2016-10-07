from PIL import Image, ImageChops, ImageOps
from scipy.misc import imresize, imsave
import os
from resizeimage import resizeimage


### if aspect ratio needs to be maintained, but you're resizing to a single dimension


def resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = resizeimage.resize_width(im, 150)  # change desired width dimension here, or use `resize_height` for height changes
    new_im.save(file_path + "_resized.jpg")


def bulkResize(folder):
    imgExts = ["jpg"]
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            resize(path, file_name)


### if aspect ratio has to be maintained, but you want to crop or pad


def makeThumb(f_in, f_out, size=(80,80), pad=False):

    image = Image.open(f_in)
    image.thumbnail(size, Image.ANTIALIAS)
    image_size = image.size

    if pad:
        thumb = image.crop( (0, 0, size[0], size[1]) )

        offset_x = max( (size[0] - image_size[0]) / 2, 0 )
        offset_y = max( (size[1] - image_size[1]) / 2, 0 )

        thumb = ImageChops.offset(thumb, offset_x, offset_y)

    else:
        thumb = ImageOps.fit(image, size, Image.ANTIALIAS, (0.5, 0.5))

    thumb.save(f_out)


### if aspect ratio doesn't need to be maintained:


def resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = imresize(im, size=(150, 150))  # replace with desired dims
    imsave(file_path + "_resized.jpg", new_im)


def bulkResize(folder):
    imgExts = ["jpg"]
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            resize(path, file_name)


### alternate code that allows you to key off of a base height or base width for a single image


def single_resize(file_path):
	baseheight = 150
	img = Image.open(file_path)
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
	img.save('{0}x{1}.jpg'.format(wsize, baseheight))

	basewidth = 150
	img = Image.open(file_path)
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	img.save('{0}x{1}.jpg'.format(basewidth, hsize))

if __name__ == "__main__":
	source = "<path to file directory goes here>"
	bulkResize(source)
	makeThumb(f_in=source, f_out="<outpath>", pad=True)
	single_resize(source)
