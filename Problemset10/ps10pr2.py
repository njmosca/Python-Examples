#Author: Nicholas 
# ps10pr2.py (Problem Set 10, Problem 2)
#
# Matrix operations
#
# Computer Science 111
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a 2-D list numbers
    """
    ## You will revise this function. 
    #print(matrix) origional
    #edited
    
    height = len(matrix)
    width = len(matrix[0])
    for r in range(height):
        for c in range(width):
            print('%1.2f' % matrix[r][c],end = ' ')
        print()
    

        
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###


def mult_row(matrix,r,m):
    ''' multiplys elements in r(row) by integer m'''
    
    #parseing matrix
    rows = len(matrix) # determines height
    columns = len(matrix[0]) # determines width
    selected_row = matrix[r] # isolates the targeted row
    
    for row in range(len(matrix[r])): # loops through the targeted row
        # multiplys each element in targeted list by m
         selected_row[row] = selected_row[row] *m 

    matrix[r] = selected_row
        
           
def add_row_into(matrix,rs,rd):
    ''' adds rs to rd'''
    source_row = matrix[rs] # row that is going to be added to destination row
    #print('source row is',source_row)
    destination = matrix[rd] # target row that is going to change
    #print('destination is',destination)  
    # height = len(matrix)
    # width = len(matrix)
    for row in range(len(destination)): # for each element in final row
        destination[row] += source_row[row] # adding elements of source row into target row
    matrix[rd] = destination # assigning matrix location to new row that was changed
  # have to add this last line or type error will occur

#testing

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# add_row_into(matrix, 0, 2) 

def add_mult_row_into(matrix,m,rs,rd):
    ''' multiplys rs by m and adds to rd'''
    source_row = matrix[rs] # row that is going to be added to destination row
    backup = []
    backup = backup + source_row[:] # hard copy/deep copy of the source row
    #print('source row is',source_row)
    #print('backup is',backup)
    destination = matrix[rd] # target row that is going to change
    for row in range(len(destination)): 
        source_row[row] = source_row[row] * m # editing source row by multiplying by m
        destination[row] += source_row[row] # taking new source row and adding to destination row
    #print('source row is',source_row)
    matrix[rd] = destination # estalbishing new destination
    matrix[rs] = backup # replacing updated source with the deep copy
    #print('source row is',source_row)
 
#testing
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# add_mult_row_into(matrix, 3, 0, 2)

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

#transpose function

def transpose(matrix):
    ''' reverses rows and columns of matrix'''
    #hard copy
    
    height = len(matrix)
    width = len(matrix[0])
    #using the create grid function but opposite inputs
    new_matrix = create_grid(width,height)
    # print('matrix is',matrix)
    # print('new matrix is',new_matrix)
    for row in range(height):
        for column in range(width):

            new_matrix[column][row] = matrix[row][column] # reversing elements 
    return new_matrix
    


#testing
# matrix = [[1, 2, 3], [4, 5, 6]]
# print_matrix(matrix)
# print('transposed matrix below hopefully!')

# t= transpose(matrix)
# print_matrix(t)





# main function with human interaction
def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
        elif choice == 2:
            r = int(input('Row index: '))
            m = float(input('Multiplier for elements in row '))
            mult_row(matrix, r, m)
        elif choice == 3:
            rs= int(input('source row #: ' ))
            rd= int(input('destination row #: ' ))
            add_row_into(matrix, rs, rd)
        elif choice == 4:
            rs =int(input('source row #: '))
            rd = int(input('destination row #: '))
            m = float(input('Multiplier for elements in row: '))
            add_mult_row_into(matrix, m, rs, rd)
        elif choice ==5:
            matrix = transpose(matrix)
            

        ## add code to handle the other options here

        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == "__main__":
    main()
    