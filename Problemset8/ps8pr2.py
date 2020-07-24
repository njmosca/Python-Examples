#
# ps8pr2.py (Problem Set 8, Problem 2)
#
# Estimating pi
#
# Computer Science 111
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###


#2.1

def for_pi(n):
    ''' takes positive int n and estimates pi for each dart thrown'''
    count = 0
    hit = 0
    for x in range(1,n+1):
        count += 1
        if throw_dart() == True:
            hit = hit +1
        p = hit * 4 / count
        print (hit,'hits out of',x,'throws so pi is',p)
    return p




## 2.2

def while_pi(error):
    ''' takes in positive float and returns amount of throws to get pi
    to 3.1'''
    count = 0
    hit = 0
    p =0
    while abs(p - math.pi) >= error: # as long as the abs is greater or = to error than it will loop
        
        count += 1
        if throw_dart() == True:
            hit += 1
        p = hit * 4/count
        print(hit,'hits out of',count,'throws so that pi is',p)
            
    return count 
        


