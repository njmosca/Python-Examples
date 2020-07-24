#File: ps3pr2.py
#Author: Nicholas Mosca
# Description: problemset3 problem 3

# must use recursion
# problem 3.1
def copy(s,n):
    ''' function that copies s n times '''
    if n == 0 or n == 1:  # if you just want one or 0 copies retuen base case
        return s
    else:
        r = s + copy(s,n - 1)  # building back to base case
        return r

copy('da', 2)
copy('Go BU!', 4)

#problem 3.2
# compare function


def compare(list1, list2):
    ''' comparing two lists and returning how many times values in list 1 are < list 2 '''
    if list1 == []:
        return 0
    else:
        c = compare(list1[1:],list2[1:])
        #print('compare', list1[1:],list2[1:],'result', c) showing me the results inside the recursive function
        # if the value in list 1 is less than list 2 return 1
        if list1[0] < list2[0]:
            c = c + 1
            return c
        else:
            return c
# testing

compare([4, 2,], [1, 5])
compare([4, 2, 3], [6, 5, 0, 8])

# problem 3.3
# double function

def double(s):
    ''' function that takes in a string and doubles each letter'''

    if s == '':  # base case
        return s
    else:
        d = s[0]*2  + double(s[1:]) # returns double first letter and trances back length of string
        print('each stack frame is', d)  # looking at the stacks
        return d


#testing functions
double('hello')
double('pythons')



       

