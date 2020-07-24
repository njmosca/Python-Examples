#File: ps5pr2.py
#Author: Nicholas Mosca
# Description: problem set 5 problem 2


#2.1
 # function that takes in a element in a list ans returns the location of that element is set list

def index(elem,seq):
    ''' takes element and list and returns where that element lies in that list'''

    if seq == '' or seq == []: # the target list cannot be empty

        return -1 # if so return -1 
    elif elem == seq[0]:  # if element = to first element in list return that position 0
        return 0
    else:
        rest = index(elem,seq[1:]) # recursive case running through whole list
        print('rest is',rest)
        if rest == -1: # if match at last position then return that
            return -1
        else:
            return 1 + rest # all other cases

# testing
#print(index('hi', ['hello', 111, 'anything']))
#index('a', 'banana')


#2.2
# ended up not using
def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == []:
        return ()
    elif values[0] == elem:
        return str(values[1:]) # adjusted to work with strings
    else:
        result_rest = rem_first(elem, values[1:])
        return str([values[0]] + result_rest)  # adjusted to work with strings
# works on strings


#jotto scoring function 

def jscore(s1,s2):
    ''' jotto scoring system for two strings'''
    both = 0 # both strings start with 0 score/ base score
    if s1 =='' or s2 =='': # if both strings or one string is empty
        return 0
    elif s1[0] in s2: # first char in string 1 inside string two (thanks for the hint)
        return both + 1 + jscore(s1[1:], s2.replace(s1[0], '', 1)) # 0+1 + recursive score of 1 for each match till end
    else:
        return both + jscore(s1[1:], s2) # if not in 0 + recursive score from second element of s1 on
# testing

#jscore('diner', 'syrup') 

2.3
# lcs function
# i got it to work without including gaps but im not sure how to include gaps, using the python visulize
# tool just says its 999 steps and im kinda stuck
def lcs(s1,s2):
    ''' finds the longest common substring of two strings without allowed'''
    if s1 == '' or s2 == '':
        return ''
    elif s1 == s2:
        return s1
    elif s1[0] == s2[0]:
        first = s1[0]
        result1 = lcs(s1[1:],s2[1:])
        longest_string = first + result1
    else:
        result1 = lcs(s1[1:],s2)
        result2 = lcs(s1,s2[1:])
        longest_string = max(result1,result2)
    return longest_string





#testing
# print(lcs('human', 'chimp'))
# lcs('gattaca', 'tacgaacta')