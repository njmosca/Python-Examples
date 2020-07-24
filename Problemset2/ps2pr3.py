#file:ps2pr2.py
#Author: Nicholas Mosca
#description:  problem 3 problemset 2  functions on lists part 1

# problem 3.1
def first_and_last(values):
    """ put your docstring here """
    first = values[0]
    last = values[-1]
    return [first, last]

###testing

first_and_last([1, 2, 3, 4])
print(first_and_last(['how', 'are', 'you?']))


#problem 3.2
def longer_len(s1, s2):
    s1 = len(s1)
    s2 = len(s2)
    if s1 > s2:
        x = s1
    else:
        x = s2
    return x
### testing
longer_len('computer', 'compute')
print(longer_len('begin', 'on'))

##problem 3.3
## function that moves letters to the end of string

def move_to_end(s,n):
    '''moves parts of strings around'''   
    if len(s) < n:  # if s has less charaters than n then just return string s
        f = s 
    else:
         x = s[:n] # grabbing n from s
         y = s[n:] # grabbing leftover 
         f = y + x  # attaching both parts of string
    return f

#testing
print(move_to_end('computer', 3))
print(move_to_end('computer', 5))
print(move_to_end('hi', 5))
