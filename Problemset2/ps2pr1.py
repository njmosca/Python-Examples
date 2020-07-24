# 
# ps2pr1.py - Problem Set 2, Problem 1
#
# Functions with numeric inputs
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

#function 1 cube

def cube(x):
    ''' this function will cube x '''
    return x**3

#test
# print(cube(2)) # returns 8
# print(cube(-5)) # returns -125

#function 2 converting to inches from yards and feet

def convert_to_inches(yards,feet):
    ''' convert everything into inches, negative values = 0'''
    if yards < 0:
        yards = 0
        
    if feet < 0:
        feet = 0
    yards = yards * 36
    feet = feet * 12
    return (yards + feet)

#testing
# print(convert_to_inches(1,1))
# print(convert_to_inches(-4,2))
# print(convert_to_inches(3,-5))


## function 3 area in square inches function
# i wrote out both methods using a function within a function and without using it

def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    ''' calculating area in square inches'''
    height_inches = (height_yds * 36) + (height_ft * 12)
    width_inches = (width_yds * 36) + (width_ft * 12)
    # height_inches = convert_to_inches(height_yds,height_ft)
    # width_inches = convert_to_inches(width_yds,width_ft)
    # if height_inches < 0:
    #     height_inches = 0
    #     print('No negative values!')
    # if width_inches < 0:
    #     width_inches = 0
    #     print('No negative values!')
    return height_inches * width_inches


#testing
print('area_sq_inches(2,0,1,2)' ,area_sq_inches(2,0,1,2))

print('area_sq_inches(2,-1,1,2)',area_sq_inches(2,-1,1,2))






# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':
        
    # sample test call for function 0
    #testing other functions too
    print('opposite(-8) returns', opposite(-8))
    print(convert_to_inches(1,1))
    print(convert_to_inches(-4,2))
    print('area_sq_inches(2,0,1,2)' ,area_sq_inches(2,0,1,2))
    print('area_sq_inches(2,-1,1,2)',area_sq_inches(2,-1,1,2))

    

