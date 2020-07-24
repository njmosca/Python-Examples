# Author: Nicholas Mosca
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
# 

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 

# Solve puzzles 1-4 here:


#puzzle 1:
# Creating the list [2, 7] from pi and e
answer1 = e[0:2]

#puzzle 2:
#Use pi and/or e to create the list [5, 4, 3], and assign 
# it to the variable answer2. Here again, make sure to follow the correct format, 
# and to leave a blank line between puzzles.

answer2 = pi[-2::-2]

#puzzle 3:
#Use pi and/or e to create the list [3, 5, 7], and assign it to the variable answer3. 
# (Optional challenge: See if you can do this with just three list operations!)

answer3 = pi[0:-1:4] + [e[1]]

#puzzle 4 

#Use pi and/or e to create the list [1, 2, 3, 4, 5], and assign it to the variable answer4. 
# (Optional challenge: See if you can do this with just three list operations!)

answer4 = e[-1::-2] + pi[0:5:2]




#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'



# Solve puzzles 5-10 here:

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

#puzzle 6
# create string universe
answer6 = u[0:-3] + t[1]


#puzzle 7
# create the string roster
answer7 = t[2] + b[1:4] + t[-3:-1]

#puzzle 8 
# create string boisterous (8 ops)
# 10 for now 
answer8= b[0:2] + t[4::3] + u[-2] + t[1:3] + b[1] + u[:-3:6]

#puzzle 9
# create the string 'yesyesyes'
answer9 = (u[::-5] + t[-1]) * 3 

#puzzle 10
#create the string 'trist'  4 ops is possible
# 3 ops
answer10 = t[:-2:2] + u[6:10:2]











# test code below, do not modify!
if __name__ == '__main__':
    
    for x in ['answer0', 'answer1', 'answer2', 'answer3', 'answer4',
              'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
              'answer10']:
        if x in dir():
            print(x + ' = ', eval(x))