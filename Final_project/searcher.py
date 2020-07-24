#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Nicholas Mosca  
# email: njmosca@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#




import random
from state import *
from board import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self,depth_limit):
        ''' constructor for searcher class'''
        self.depth_limit = depth_limit # a value that indicates x amount of searches before giving up
        self.states = [] # this is a list of states we should look 
        self.num_tested = 0
        


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def should_add(self,state):
        ''' check to see if current state is in bounds with state object as input'''
        if (self.depth_limit != -1 and state.num_moves > self.depth_limit) or state.creates_cycle():
            return False
        else:
            return True

    def add_state(self,new_state): # adds neew states will get
        ''' appends self.states'''
        self.states += [new_state]

    def add_states(self,new_states): # adds new states
        ''' adds multiple states to self'''
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)

    def next_state(self): # retuns next state that should be tested
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
    """
        s = random.choice(self.states)
        self.states.remove(s)
        return s


        
       # if searcher finds goal state, return it
        
        #get to goal state find previous moves
        #To begin, the method should add the parameter init_state to the list of untested states;
        #If the searcher finds a goal state, it should return it. While loop

    def find_solution(self, init_state): # starting from init state and search til goal state
        '''full random state space search'''
        
        
        self.add_state(init_state) # add init state to searchers list of untested states
        while self.states: # or len(self.states not zero)
            self.num_tested += 1
            s = self.next_state()
           
            #print(s,'un tested states = ',len(self.states)) # test statement
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None

     


######################################################################
### Add your BFSeacher and DFSearcher class definitions below. ### both are uninformaed, not aware of how close they are to goal
    # find solution at smallest possible depth
    #checks all possible answers at depth 1 the n2 ...
    #FIFO first in first out
    #optiomal if eac move cost the same 
    # next move method 

class BFSearcher(Searcher):
    '''FIFO uninformed class starting with lowest depth'''
    # do not need new constructor , recycle searcher one
    #super().__init__(Searcher) # inheritance

    def next_state(self): # retuns next state that should be tested
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
    """
        #s = random.choice(self.states)
        s = self.states[0] # first in 
        self.states.remove(s)
        return s


######################################################################
## DF is going to go as deep as possible and check
# LIFO last in first out
# less memory 
#may take more time 


class DFSearcher(Searcher):
    ''' last in first out, performs deepest depth search'''

    def next_state(self): # retuns next state that should be tested
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
    """
        #s = random.choice(self.states)
        s = self.states[-1] # last in
        self.states.remove(s)
        return s









#######################################################################
# heuristic function 1
# tells us how far from goal

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    ''' returns how many adtional moves are needed to get to goal state'''
    ''' helps choose priority'''
    steps = state.board.num_misplaced() # operates on board function, returns number of wrong tiles
    return steps 

def h2 (state):
    ''' custom heuristic''' 
    #starting point taking all possible states of board to goal state
    return state.board.total_steps()













##########################################################################
# solving using greedy method 
# priority of state x, p(x = -1 * h(x))
# want the states with highest P  
class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __init__(self, heuristic, depth_limit):
        ''' greedy search constructor object
        inputs:
         * heuristic - a reference to the function that should be used 
         when computing the priority of a state
         * depth_limit - the depth limit of the searcher'''
        self.heuristic = heuristic
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit





    def priority(self,state):
        ''' takes in state object and returns priority for that given state'''
        #priority = -1 * num_misplaced_tiles
        #p = -1 * self.heuristic(state) # had to build h1 to be able to use board method 
        return  -1 * self.heuristic(state) + 1


    def add_state(self, state):
        'overides searcher new state and returns a nested list with priority included with state'
        # include priority with state for nested list so max function can be used
        # adds to self.state
        self.states += [[self.priority(state),state]] # list of lists method

    def next_state(self):
        ''' overides searcher next state, this method chooses the state with highest priority'''
        # use max function
        #remove the priority after just return the state
        #s = self.states
        m = max(self.states)
        self.states.remove(m)
        highest_priority_state = m[1]
        return highest_priority_state # what about ties
        


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

##########################################################################################
### Add your AStarSeacher class definition below. ###
# like greedy but with g(x) cost of getting there 
# finds a optimal solution with minimal cost = lowest g(x)
# both complete and optimal 
# g(x) counts moves 
##### hint is to pass a heuristic function as a input

class AStarSearcher(GreedySearcher):
    #priority = -1 * (heuristic + num_moves)
    # needs new priority state?

    def priority(self,state):
        ''' takes in state object and returns priority for that given state'''
        #priority = -1 * (heuristic + num_moves)
        p = -1 * (self.heuristic(state) + state.num_moves)
        return p 

    







# Testing 

# b = Board('142358607')
# s = State(b, None, 'init')
# a = AStarSearcher(h1, -1)