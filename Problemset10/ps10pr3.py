#
# ps11pr3.py (Problem Set 10, Problem 3)
#
# Images as 2-D lists
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []
    
    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels


def blank_image(height,width): 
    ''' creates a blank green image using create uniform function'''
    green = create_uniform_image(height,width,[0,255,0]) # brand new blank image
    return green


# pixels = blank_image(100, 50)
# save_pixels(pixels, 'blank.png')

def flip_horiz(pixels):
    ''' takes in 2D list of pixels and reverses it to flip horizontally'''
    new_image = blank_image(len(pixels), len(pixels[0])) # new image same size as input
    for row in range(len(pixels)):
        for c in range(len(pixels[0])):
            new_image[row][c] = pixels[row][len(pixels[0])-1-c] 
    return new_image


#testing
# pixels = load_pixels('spam.png')
# flipped = flip_horiz(pixels)
# save_pixels(flipped)

def flip_vert(pixels):
    """ takes in 2D list and flips it vertically.
    """
    vert = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            vert[r][c] = pixels[len(pixels) - r - 1][c] # opposite of horiz
    return vert


#testing
# pixels = load_pixels('spam.png')
# flipped = flip_vert(pixels)
# save_pixels(flipped)

def transpose(pixels):
    ''' input is a 2d matrix as image and returns transposed image/ reversed image'''
    t= blank_image(len(pixels[0]), len(pixels))
    for r in range(len(pixels[0])):
        for c in range(len(pixels)):
            t[r][c] = pixels[c][r]
    return t

# pixels = load_pixels('spam.png')
# trans = transpose(pixels)
# save_pixels(trans)


def rotate_clockwise(pixels):
    ''' rotates image  counter clockwise'''
    new_image = flip_horiz(transpose(pixels)) # use transpose
    return new_image




def rotate_counterclockwise(pixels):
    ''' rotates image clockwise'''
    new_image = flip_vert(transpose(pixels)) # use transpose
    return new_image


# pixels = load_pixels('spam.png')
# cclock = rotate_counterclockwise(pixels)
# save_pixels(cclock)