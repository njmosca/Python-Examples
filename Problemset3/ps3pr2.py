# ps3pr2.py
#author: Nicholas Mosca
# Description: Problemset 3 problem 2
# functions without recursion

# 2.1
#flipside function

def flipside(s):
    ''' Function that splits a string and replaces second half with first half'''
    l = len(s) 
    first_half = s[0:l//2]  # grabbing first chunk of s
    second_half = s[l//2:]  # grabbing second chunk of s
    flip = second_half + first_half  # second half before first half
    return flip


#testing
flipside('homework')
flipside("carpets")


# 2.2
#adjust length function
    
def adjust(s,length):
    ''' adjustable string function'''
    l = len(s)
    dif = length - l  # difference between length of s and desired length
    if l == length:
        return s
    elif length > l:
        return dif * " " + s  # if length is greather than input string add spaces before
    elif length < l:
        return s[0:dif]

#testing 

adjust('alien', 4)
adjust('compute',6)


