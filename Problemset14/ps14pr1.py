#
# ps14pr1.py (Problem Set 14, Problem 1)
#Author: Nicholas Mosca
# An RandomPlayer for use in Connect Four
#

import random
from ps13pr3 import * # to use the connect_four and process_move functions
from ps13pr1 import *


#creating subclass called Random player that is part of Player main class

class RandomPlayer(Player):
    ''' sub class of player'''
    # def __init__(self,checker):

    #     super().__init__(checker)
        # initialize the Random player class

    def next_move(self, board):
        '''accepts a Board object as a parameter and returns the column where the player wants to make the next move.'''

        
        #x = random.choice(range(0,board.width -1))
        #scan all possible columns and chosie one where board.next_move() is true
        choice = []
        for col in range(board.width): # scanns whole board
            if board.can_add_to(col):
                choice.append(col)
        x = random.choice(choice)
        return x

        

        
        
p = RandomPlayer('X')
b = Board(2, 4)
b.add_checkers('001223')