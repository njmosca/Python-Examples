#
# ps10pr1.py (Problem Set 10, Problem 1)
#Author: Nicholas Mosca
# 2-D Lists
#
# Computer Science 111




import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line


def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

# grid = diagonal_grid(10, 10)
# print_grid(grid)

1.1 # inner grid function

def inner_grid(height, width):
    """ creates and returns a matrix where only the inside of the grid is changed to 1
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(1,height-1): # cancels out the top and bottom more
        for c in range(1,width-1):# cancels out left and right more
            grid[r][c] = 1 # everything is 1 inside
    return grid

#testing
# grid = inner_grid(5, 5)
# print_grid(grid)


# 1.2 random grid
#looks like inner but with the middle random
#setup inner loops and change grid to random

def random_grid(height, width):
    """ creates a matrix where inside is a random 1 or 0
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(1,height-1): # cancels out the top and bottom more
        for c in range(1,width-1):# cancels out left and right more
            # randomly assigning inner part of the grid to either 1 or 0
            grid[r][c] = random.choice([0,1]) 

    return grid
#testing
# grid = random_grid(10,10)
# print_grid(grid)


### Deep copy of a grid ###


#1.3

def copy(grid):
    ''' creates a deep copy of a 2D list'''
    rows = len(grid) # determines rows in new grid
    colums = len(grid[0]) # determines the columns in new grid
    # using a helper function create_grid to new grid that is the same size
    #this new grid is empty
    new_grid = create_grid(rows,colums) 

    #using nested for loop to create deep copy that will populate the new list
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            new_grid[r][c] = grid[r][c]
    return new_grid
    

#1.4
    
def invert(grid):
    ''' creates a inverted matrix'''
    
    rows = len(grid) # determines rows in new grid
    colums = len(grid[0]) # determines the columns in new grid
    # using a helper function create_grid to new grid that is the same size
    #this new grid is empty
    #new_grid = create_grid(rows,colums) 

    #using nested for loop to create deep copy that will populate the new list
    for r in range(len(grid)):
        
        for c in range(len(grid[0])):
            if grid [r][c] == 0:
                grid[r][c] = 1
            else:
                grid[r][c] =0
            
    return
            

#testing
# grid1 = inner_grid(5, 5)
# print_grid(grid1)

# print('invert grid below')

# invert(grid1)
# print_grid(grid1)





