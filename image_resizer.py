from PIL import Image
from scipy.misc import imresize, imsave
import os
from resizeimage import resizeimage


### if aspect ratio needs to be maintained, but you're resizing to a single dimension


def resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = resizeimage.resize_width(im, 500)  # change desired width dimension here, or use `resize_height` for height changes
    new_im.save(file_path + "_resized.jpg")


def bulkResize(folder):
    imgExts = ["jpg"]
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            resize(path, file_name)


### if aspect ratio doesn't need to be maintained:


# def resize(folder, file_name):
#     file_path = os.path.join(folder, file_name)
#     im = Image.open(file_path)
#     new_im = imresize(im, size=(150, 150))  # replace with desired dims
#     imsave(file_path + "_resized.jpg", new_im)


# def bulkResize(folder):
#     imgExts = ["jpg"]
#     for path, dirs, files in os.walk(folder):
#         for file_name in files:
#             resize(path, file_name)


### alternate code that allows you to key off of a base height or base width for a single image


# def single_resize(file_path)
	# baseheight = 250
	# img = Image.open(file_path)
	# hpercent = (baseheight / float(img.size[1]))
	# wsize = int((float(img.size[0]) * float(hpercent)))
	# img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
	# img.save('{0}x{1}.jpg'.format(wsize, baseheight))

	# basewidth = 728
	# img = Image.open(file_path)
	# wpercent = (basewidth / float(img.size[0]))
	# hsize = int((float(img.size[1]) * float(wpercent)))
	# img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	# img.save('{0}x{1}.jpg'.format(basewidth, hsize))

	
if __name__ == "__main__":
	bulkResize("<path to file directory goes here>")
	# single_resize("<path to file goes here>")
