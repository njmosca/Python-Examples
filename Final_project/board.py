#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for row in range(0,3):
            for col in range(0,3):
                self.tiles[row][col] = int(digitstr[3 * row + col])
                if (self.tiles[row][col] == 0):
                    self.blank_r = row
                    self.blank_c = col


    # string repersentation method repr/ look at older methods for foramtting
    def __repr__(self):
        ''' str rep'''
        s = '' # blank string
        for row in range(0,3):
            for col in range(0,3):
                if self.tiles[row][col] != 0:
                    s = s + str(self.tiles[row][col]) + ' '  
                else:
                    s += '_ '
            s += '\n'# line break after each row of three
        return s

    # having trouble getting the return True to work  ask question if OH Friday
    def move_blank(self,direction):
        ''' takes direction as string input, moves blank '_' to that given location'''
        row = 0
        col = 0


        #first case
        if direction == 'up':  # col is same but row changes
            row = self.blank_r -1
            col = self.blank_c
            
            if row < 0 or row > 2:
                return False
            
           
            
            

        #second case
        elif direction == 'down': # col is same but row changes
            row = self.blank_r +1
            col = self.blank_c 
            if row < 0 or row > 2:
                return False
            

        # third case, col changing and row is same
        elif direction == 'left':
            row = self.blank_r
            col = self.blank_c - 1  # shifting col 1

            if col <0 or col >2: # checking for out of bounds in columns
                return False
            

        elif direction == 'right':
            row = self.blank_r
            col = self.blank_c + 1  # shifting col 1

            if col <0 or col >2: # checking for out of bounds in columns
                return False
            
        else:
            print('unknown direction: ',direction)

        #setting tiles/ 2D list editing

        self.tiles[self.blank_r][self.blank_c] = self.tiles[row][col] # making changes to actual board
        self.tiles[row][col] = 0
        self.blank_c = col
        self.blank_r = row
        return True # true must be last thing in method 


    # create string representation of current board
    def digit_string(self):
        ''' returns a string of the current state of board'''
        s = '' #start with blank
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[row])):
                # looping through 2D list
                s += str(self.tiles[row][col])
        return s

    def copy(self):
        ''' creates deep copy of current board, hint: create new board object'''
        #new board object
        board_copy = Board(self.digit_string()) # using .digit string as current representation
        return board_copy

    def num_misplaced(self):
        ''' counts number of wrong tiles or tiles not in goal state'''
        count = 0 
        current = self.digit_string()
        goal_state = '012345678'
        # compare current state to goal state
        for num in range(9):
            if current[num] == goal_state[num] or current[num] == 0: # do not count if in goal state or 0
                count +=0
            else:
                count += 1
        return count
    
    def __eq__(self,other):
        ''' compares current board(self) to other which is a different board class'''
        # simply use .digit_string to compare
        if self.digit_string() == other.digit_string():
            return True
        else:
            return False


    # second heuristic
    def total_steps(self):
        ''' for h2, counts total amount of steps needed to get to goal from a-b'''
        # had to loop through all possible options or steps for 3X3 grid.# goal is to look at current state - goal state as grid
        count = 0
        for i in range(3): # len
            for j in range(3): #wid
                    grid_row = self.tiles[i][j]%3  # rows
                    #print('grid_row is',grid_row)
                    grid_col = self.tiles[i][j]//3 # columns 
                    #print('grid_col is',grid_col)
                    count += abs(j-grid_row) # count all moves left/right or up and down
                    # col - rows
                    count += abs(i-grid_col)
                    # rows - col
        return count



        


#testing
# b = Board('142358607')
# b1 = Board('012345678')
# b2 = Board('012345678')