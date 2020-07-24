#File: ps8pr3.py
#Author: Nicholas Mosca
# Description: problemset 8 problem 3



# 3.1

def double(s):
    ''' doubles every char in string'''
    char = ''
    if s == '':
        return ''
    for c in s:
        char += c *2
    return char

#test
#double('hello')

#3.2
def weave(s1, s2):
    """ weaves both strings into one string """
    result = ''
    len_shorter = min(len(s1), len(s2))
    len_larger = max(len(s1), len(s2))
    dif = len_larger - len_shorter
    if s1 == '':
        return s2
    elif s2 == '':
        return s1
    elif dif == 0:
        extra = ''
    elif len_shorter == len(s1):
        extra = s2[dif:]
    else:
        extra = s1[dif:]

    for i in range(len_shorter):
        result += s1[i] + s2[i] 

    return result + extra
        
#testing 
# weave('aaaaaa', 'bbbbbb')
# weave('aaaa', '')      
#weave('aaaa', 'bbbbbbbb')  

# 3.3#



def square_evens(values):
    ''' takes in list of values and only squares the even elements'''
    result = [] 
    square = []
    for num in range(len(values)): # index based
        if values[num] % 2 == 0: # if values at current idex even
            square = values[num] **2 # square that value
            #result =result + [square] # add that to result list
            values[num] = square
        #else:
            #result = result + [values[num]] # if odd add anyway
    return 


# testing
vals1 = [1, 2, 3, 4, 5, 6]
square_evens(vals1)
#print(vals1)
# 3.4

def index(elem,seq):
    ''' takes element and string/list and results the element from said list or string'''
    count = 0
    for element in range(len(seq)): # index based
        count += 1
        if seq[element] == elem: # if we have a match 
            return count -1 # return that spot minus 1 because count has a extra
        elif elem not in seq: # if not in return -1
            return -1

# testing
# index('a', 'banana')
# index('i','team')