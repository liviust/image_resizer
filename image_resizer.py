import os
from PIL import Image, ImageChops, ImageOps
from scipy.misc import imresize, imsave
from resizeimage import resizeimage

img_width, img_height = 150, 150


### if aspect ratio doesn't need to be maintained:
def resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = imresize(im, size=(img_width, img_height))
    imsave(file_path + "_resized.jpg", new_im)

	
### if aspect ratio needs to be maintained, and you're resizing to a single dimension
def one_dim_resize(folder, file_name):
    file_path = os.path.join(folder, file_name)
    im = Image.open(file_path)
    new_im = resizeimage.resize_width(im, img_width)  # use `resize_height` for height changes
    new_im.save(file_path + "_resized.jpg")


### if aspect ratio has to be maintained, but you want to crop or pad
def thumb_resize(f_in, f_out, size=(img_width, img_height), pad=False):
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


### alternate code that allows you to key off of a base height or base width for a single image
def base_resize(file_path):
	baseheight = img_height
	img = Image.open(file_path)
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
	img.save('{0}x{1}.jpg'.format(wsize, baseheight))

	basewidth = img_width
	img = Image.open(file_path)
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
	img.save('{0}x{1}.jpg'.format(basewidth, hsize))


### for bulk operations (glob is also good for this)
def bulkResize(folder):
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            resize(path, file_name)  # or can sub one of alternative resizing functions above


if __name__ == "__main__":
	data_dir = "../images/to/be/resized/"
	bulkResize(data_dir)  # or just use one of single image scripts here

# Note: CV2 has a lot of good tools for this too -- will add some useful scripts later
