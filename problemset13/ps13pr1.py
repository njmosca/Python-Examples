#File: ps13pr1.py
# Author: Nicholas Mosca
# Description: This is problemset 13 problem 1, defining a checkers board class

##### object oriented board game  Connect 4

# game board

class Board:
    ''' new class that represents game board objects'''

    #constructor for board class
    def __init__(self,height,width):
        ''' constructor for board class'''
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)] # board starts empty and will be filled with X or O
        



    # representation of the whole board as string
    def __repr__(self):
        """ Returns a string representation for a Board object."""
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            
            for col in range(self.width):
                s += self.slots[row][col] + '|'
                
            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        s += (2 * self.width +1) * ('-') # adds a new row that is just __
        s += '\n' # line break

        # and the numbers underneath it.
        for col in range((self.width)): # for each column in s
            s += " " + str(col % 10) # add a space then the associated number

        return s
        
    def add_checker(self, checker, col):

        ''' checks to see that is in the given column'''
    
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        if self.slots[-1][col] == ' ':  # scans from bottom up, if column is empty then checker can be places there
            self.slots[-1][col] = checker # checker is that location
        else:
            row = 0
            while self.slots[row][col] == " ": # if the spot is not empty
                row += 1 # the cheker must be stacked
            self.slots[row -1][col] = checker # checker is the new location

    def reset(self):
        ''' resets board'''
        #copy = Board(self.width,self.height) # blan copy same size
        # scanning through the whole list and replacing everything 
        for r in range(self.height):
            for c in range(self.width):
                self.slots[r][c] = " "


    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
    """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self,col):
        ''' determines if a move is possible in the selected column'''
        if col >= self.width:
            return False
        elif col < -1:
            return False
        if self.slots[0][col] == ' ':
            return True
        else:
            return False

    def is_full(self):
        ''' checks if the board is completly full'''

        for c in range(self.width):
            if self.can_add_to(c):
                return False
        return True


    def remove_checker(self,col):

        ''' checks to see that is in the given column'''
    
        # scanning board
        if self.slots[-1][col] == ' ':  # scans from bottom up, if column is empty then checker can be places there
            self.slots[-1][col] = ' ' # checker is that location
        else:
            
            row = 0
            while self.slots[row][col] == " ": # if the spot is not empty
                row += 1 # the cheker must be stacked
            self.slots[row][col] = ' ' # checker is the new location



############# have to create 5 functions to determine if a game is won or not
    # horizontal_win

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        if self.width < 4:
            return False
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        if self.height < 4:
            return False
        for col in range(self.width):
            for row in range(self.height - 3):
                
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False


##### Diagonal wins 

    def is_down_diagonal_win(self, checker):
        """ Checks for a down diagonal win for the specified checker.
        """

        if self.height < 4 or self.width < 4:
            return False
        for col in range(self.width - 3):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
                
                    
        return False
                
    def is_up_diagonal_win(self, checker):
        """ Checks for a up diagonal win for the specified checker.
        """
        if self.height < 4 or self.width < 4:
            return False
        
        for col in range(self.width - 3):
            for row in range(3, self.height):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
                    
        return False

  




    # def is_down_diagonal_win(self, checker):
    #     """ Checks for a horizontal win for the specified checker."""
    #     if self.height < 4:
    #         return False
    #     for row in range(self.height):
    #         for col in range(self.width - 3):
    #             print('row is',row,'col is',col)
                
    #             if self.slots[row][col] == checker and \
    #                self.slots[row +1][col+1] == checker and \
    #                self.slots[row+2][col+2] == checker and \
    #                self.slots[row+3][col+3] == checker:
    #                 return True
    #     return False

    
    # def is_up_diagonal_win(self, checker):
    #     """ Checks for a horizontal win for the specified checker."""
    #     if self.height < 4 or self.width < 4:
    #         return False
    #     for col in range(self.width-3):
    #         for row in range(self.height):
    #             print('row is',row,'col is',col)
                
    #             if self.slots[row][col] == checker and \
    #                self.slots[row-1][col-1] == checker and \
    #                self.slots[row-2][col-2] == checker and \
    #                self.slots[row-3][col-3] == checker:
    #                 return True
    #     return False


    def is_win_for(self, checker):
        ''' checks if a player has won'''
        assert(checker == 'X' or checker == 'O') # checker must be X or O

        if self.is_horizontal_win(checker)  or \
            self.is_vertical_win(checker) or \
            self.is_down_diagonal_win(checker) or \
            self.is_up_diagonal_win(checker):
             return True

        else:
            return False

            
# testing  
b = Board(6, 7)
b.add_checkers('00102030')
    
        
b2 = Board(6, 7)
b2.add_checkers('23344545515')
    
b3 = Board(6,7)


b3.add_checkers('0000131122')


b = Board(3,4)