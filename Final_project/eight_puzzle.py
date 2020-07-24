#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: Nicholas Mosca              
# email: njmosca@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, extra = -1):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(extra)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
       searcher = BFSearcher(extra)
    elif algorithm == 'DFS':
       searcher = DFSearcher(extra)
    elif algorithm == 'Greedy':
       searcher = GreedySearcher(extra, -1)
    elif algorithm == 'A*':
       searcher = AStarSearcher(extra, -1)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, extra=-1): # function that can run complete tests from init to goal and print steps between
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * extra - an optional extra parameter that can be used to
            specify either a depth limit or the number of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, extra)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def process_file(filename,algorithm, extra = -1):
    ''' Takes in a filename which has a list of digit strings based on eight_puzzle board. Specifys a search algorithm'''

    # open file 
    file = open(filename,'r')
    num_moves = 0 
    states_tested = 0
    puzzles_solved = 0

    # loop through file
    for line in file:
        line = line[:9]
        
        #create board
        b = Board(line)
        #create state
        init_state = State(b,None,'init')
        # use create searcher/ pass in arguments for process file
        searcher = create_searcher(algorithm,extra)

        if searcher  == None:
            return
        soln = None


        # print(line+':')
        try:
            soln = searcher.find_solution(init_state)

            if soln != None: # if possible to solve
                #display results on one line
                print(line + ':' + str(soln.num_moves) + ' moves, ' + str(searcher.num_tested) + ' '+ 'states tested')
                      
                 # keeping track of values for average later
                num_moves += soln.num_moves
                states_tested += searcher.num_tested
                puzzles_solved +=1

            else:
                print( line + ' :' + 'Failed to find a solution.' )

        except KeyboardInterrupt:
            print('Search terminated.')


    # final printout  at bottom of output, that displays averages 
    if puzzles_solved == 0:
        print( 'solved 0 puzzles')

    else:
        print() # blank line
        avg_moves = num_moves / puzzles_solved
        avg_states  = states_tested / puzzles_solved
        #cannot have space after \ char
        print('Solved ' + str(puzzles_solved)+ ' puzzles' + '\n' \
            + 'averages: ' + str(avg_moves) + ' moves ' + str(avg_states) + ' states tested')

       
        
