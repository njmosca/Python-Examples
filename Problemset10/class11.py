#File:class11.py
#Aughtor: Nicholas Mosca
#Description: class 11 prep and notes Object oriented programming 

#object.method

# also remember help() for a given class

#useful methods
#.index
#.split   splits of white space


s = 'this is a test string  for methods'

s2= s.upper()

s3 = s.split() # breaks apart each space and creates substrings

s4 = s.index('a') # result is a interger of location of first a


#Constructing and using a object

class Rectangle: # brand new object
    ''' the rectangle constructor'''
# 2 arguments are shown but self does not count as one
    def __init__(self,init_width,init_height): # each rectangle has a width and height
        self.x = 0
        self.y = 0
        self.width = init_width
        self.height = init_height

    def grow(self,dwidth,dheight): # we can create functions that modifiy out new object
        self.width += dwidth
        self.height += dheight

    def area(self):
       
        return self.width * self.height # function to create area of new data type
    
    def perimeter(self):
        return 2 * self.width + 2 * self,height
    
    def scale(self,factor): # going to grow rectange by factor of x
        self.width *= factor
        self.height *= factor

    def __eq__(self, other): # special method  testing height and width
        return (self.width == other.width and self.height == other.height)

    def __repr__(self): # function that displays out new object as a printable string
        return str(self.width) + 'x' + str(self.height)




# tests
r1 = Rectangle(100,50)        
r1.width # will display 100
r1.x = 25 # changes the varible insde the homade class


        