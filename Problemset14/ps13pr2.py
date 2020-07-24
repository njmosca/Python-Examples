#File:ps13pr2.py
# ps13pr2.py (Problem Set 13, Problem 2)
#Author: Nicholas Mosca
# A Connect Four Player class 
#

from ps13pr1 import Board

# Write your class below.

class Player:
    
    def __init__(self, checker):
        '''constructs a new Player object'''
        
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0
        self.checker = checker

    def __str__(self):
        '''returns a string representing a Player object. '''

               
        s = 'Player '
        s += self.checker
        return s

    
    def __repr__(self):
        '''returns a string representing a Player object.'''

        return str(self)

    def opponent_checker(self):
        '''returns a one-character string representing the checker of the Player object’s opponent'''

        if self.checker == 'X':
            return 'O'

        return 'X'

    def next_move(self, board):
        '''accepts a Board object as a parameter and returns the column where the player wants to make the next move.'''

        x = int(input('Enter a column: '))

        while x < 0 or x > board.width - 1 or not board.can_add_to(x):
            print('Try again!')
            x = int(input('Enter a column: '))

        else:
            self.num_moves += 1
            return x



# testing 

# p = Player('X')
# b1 = Board(3,5)