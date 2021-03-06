#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: Nicholas Mosca
# email: njmosca@bu.edu


from board import * # giving a grade scope error
from searcher import *





# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###

    def __init__ (self,board,predecessor,move):
        ''' estalbishing the new class'''
        self.board = board
        self.predecessor = predecessor
        self.move = move
        if predecessor == None:
            self.num_moves = 0
        else:
            self.num_moves = predecessor.num_moves +1



        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True


    def is_goal(self):
        ''' checks if current state of board matches labeled goal state'''
        return self.board.tiles == GOAL_TILES

    def generate_successors(self):
        ''' generates list of possible moves from current state'''

        successors = []
        for move in MOVES:
            b = self.board.copy() # new deep copy for each loop
            if b.move_blank(move) != False: # if move is possible
                state = State(b,self,move) # keep track of move
                successors.append(state) # add to list successors
        return successors


    def print_moves_to(self):
        ''' prints sequence of moves that starts from init state to state object self'''
        # printing in reverse order
        # state object given
        # init to object called
        if self.predecessor == None: # if the puzzle cannot be solved
            print(self.__init__(self.board,self.predecessor,self.move)) # initial state
            print('initial state:')
            print(self.board)
        else:
            self.predecessor.print_moves_to()
            print('move the blank',self.move +':')

            print(self.board)











# testing 
# b = Board('142305678')
# s = State(b, None, 'init')  
# searcher = Searcher(-1)
# goal = searcher.find_solution(s)
