#
# ps14pr2.py (Problem Set 14, Problem 2)
#Author: Nicholas Mosca
# An AI Player for use in Connect Four
#

import random
from ps13pr3 import * # to use the connect_four and process_move functions
from ps13pr1 import *


# AI player that is more advanced than random player
#subclass of player

class AIPlayer(Player):
    ''' sub class of player'''
    def __init__(self,checker,tiebreak,lookahead):
        ''' smarter AI player '''
        assert(checker == 'X' or checker == 'O') # must be X or O
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)

        # initialize the  AIPlayer class
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    # repr method converts memory location into string 

    def __repr__(self):
        #do not print, must be string 
        # does not work horizontailly
        string = 'Player '
        string += self.checker
        string += ' ('
        string += self.tiebreak
        string += ', '
        string += str(self.lookahead)
        string += ')'
        return string

    def max_score_column(self,score):
        ''' returns column with max score based on tiebreak method'''
        choices = []
        count = 0
        for num in score:
            count += 1
            if num == max(score):
                choices += [count-1] # produces sublist of all max score indexes
        # return choices
        if self.tiebreak == 'LEFT':
            return choices[0]
        if self.tiebreak == 'RIGHT':
            return choices[-1]
        if self.tiebreak == 'RANDOM':
            return random.choice(choices)
        else:
            return choices

    def scores_for(self,board):
        ''' determines AIPlayer score for each column based on current board'''
        #scores = list(range(board.width)) # list with enough slots to fit each column of board
        scores = [50] * board.width
        for col in range(board.width):
            #opponent_scores = self.opponent_checker.scores_for(board)
            if board.can_add_to(col) == False: # if column is full then score is -1
                scores[col] = -1
            elif board.is_win_for(self.checker): # if column is a win then score is 100
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                 #self.lookahead == 1:
                 # add checker
                board.add_checker(self.checker,col)
                # create second AI player
                ai = AIPlayer(self.opponent_checker(),self.tiebreak,self.lookahead-1)
    
                #look ahead 1/ recursive call
                opponent_scores = ai.scores_for(board)
                m = max(opponent_scores)
                #print('col num',col,'opponent_scores()',opponent_scores,'max opponent score',m)
                scores[col] = 100 - m
                
                #remove checker
                board.remove_checker(col)
        return scores

            
    def next_move(self,board):
            ''' best possible move for ai'''
            self.num_moves += 1
            l = self.scores_for(board)
            return self.max_score_column(l)
            
            

            
                
        
    

#testing
# b = Board(6, 7)
# b.add_checkers('1211244445')


