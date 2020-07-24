# Author: Nicholas Mosca
# ps1pr1.py - Problem Set 1, Problem 1
#
# Computes the integers 0 through 4 using exactly 4 fours.
#



# Complete the rest of the program below.
zero = 4 + 4 - 4 - 4
one = 4//4 *4//4
two = (4*4)// (4+4)
three =  (4+4+4)//4
four = (4*(4-4)) + 4 





# test code below, do not modify!
if __name__ == '__main__':
    
    for x in ['zero', 'one', 'two', 'three', 'four']:
        if x in dir():
            print(x + ' = ', eval(x))