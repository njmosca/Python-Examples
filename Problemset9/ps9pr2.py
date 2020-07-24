#
# ps9pr2.py (Problem Set 9, Problem 2)
#Author: Nicholas Mosca
# Image processing with loops and image objects
#
# Computer Science 111
# 

from cs111png import *

#2.1

# flip and invert function

def flip_vert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates new image flipped and inverted
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
   
    

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    print(height,width)
    new_img = Image(height, width)   # create a new, blank image object

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(height - r-1,c)

            

            
            new_img.set_pixel(r, c, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'flipv_' + filename
    new_img.save(new_filename)




2.2
# if row cord > 1/2 height then we flip 
# else we copy origional image
def mirror_vert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates new image flipped and inverted
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
   
    
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    #print(height,width)
    new_img = Image(height, width)   # create a new, blank image object

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c

            if r >= height//2 : # this is the flip 
                rgb = img.get_pixel(height - r-1,c)
                new_img.set_pixel(r, c, rgb)

            else: # this is origional
                rgb = img.get_pixel(r,c)
                new_img.set_pixel(r, c, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'mirrorv_' + filename
    new_img.save(new_filename)



def reduce(filename):

    """ loads a PNG image from the file with the specified filename
        and only displays odd pixels
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
   

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    #print(height,width)
    new_img = Image(height//2, width//2)   # create a new, blank image object

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the every other pixel in r,c
            if r % 2 == 1 and c % 2 ==1:


                rgb = img.get_pixel(r,c)
    
                new_img.set_pixel(r//2, c//2, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)

def extract(filename,rmin,rmax,cmin,cmax):

    """ loads a PNG image from the file with the specified filename
        and only displays odd pixels
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
   
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    #print(height,width)
    new_img = Image(rmax-rmin, cmax-cmin)   # create a new, blank image object at new size

    # process the image, one pixel at a time
    for r in range(rmin,rmax):
        for c in range(cmin,cmax):
            # get the RGB values for new cropped image
            rgb = img.get_pixel(r,c)
            new_img.set_pixel(r - rmin,c - cmin,rgb)
             

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'extract_' + filename
    new_img.save(new_filename)



