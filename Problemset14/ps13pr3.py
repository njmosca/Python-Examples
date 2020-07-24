#File: ps13pr3.py
# ps13pr3.py (Problem Set 13, Problem 3)
#Author: Nicholas Mosca
# Playing the game
#

from ps13pr1 import Board
from ps13pr2 import Player
import random
    #given

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
    '''takes two parameters: a Player object for the player whose move is being processed, and a Board object for the game that is being played.'''

    print(player.__str__() + "'s" + ' ' + 'turn')

    col_choice = player.next_move(board)
    board.add_checker(player.checker, col_choice)

    print()
    print(board)
    
    if board.is_win_for(player.checker) == True:
        print()
        print(player.__str__() +' wins in ' + str(player.num_moves) + ' moves' + '\n' + 'Congratulations!')
        return True
    #if board.is_full() == True:
        
        #if board.is_win_for(player.checker) == board.is_win_for(player.opponent_checker):
            # hidden error involving tie 
            # print()
            # print("It's a tie!")
            # return False
    if board.is_full():
        if board.is_win_for(player.opponent_checker()) == False and board.is_win_for(player.checker) == False:
            print()
            print("It's a tie!")
        return False

        
   
    else:
        print()
        return False


    
