#File:ps3pr4.py
#Author: Nicholas Mosca
# Description : problemset 3 problem 4

#4.1 letter score function

def letter_score(letter):
    """ rating system for letters """
    assert(len(letter) == 1)
    if (letter in ['a','e','i','o','u','n','t','s','l','r']):
        return 1
    elif (letter in ['b','c','m','p' ]):
        return 3
    elif(letter in ['f','h','v','w','y']):
        return 4
    elif(letter in ['d','g']):
        return 2
    elif letter == 'k':
        return 5
    # no 6
    # no 7
    elif(letter in ['j','x']):
        return 8
    #no 9
    elif(letter in ['q','z']):
        return 10
    elif (letter in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
        return ' Lower case only!'
    elif letter == '%':
        return 'lower case letters only!'
    elif len(letter) == 0:
        return 0
      # end of function  
        
#testing
# letter_score('n')

# 4.2 Scrabble problem
# have to use letter score function 

def scrabble_score(word):
    ''' assigns a score to a string, recursive and using letter score function'''
    #base case
    if word == '':
        return 0
    else: 
        #recursive case
        first = letter_score(word[0])  # calling previous function
        score = first + scrabble_score(word[1:]) # recirsive case
        return score


#testing
# scrabble_score('nick')
# scrabble_score('python')
# scrabble_score('pythonisfunbutistakingupalotoftime')

# 4.3

def add(vals1, vals2):
    ''' function adds coorispoding elements in each list and returns sum, assuming lists are the same length'''
    if len(vals1) == 0 or len(vals2) == 0:  # base case
        return []
    else:
        fsum = [vals1[0] + vals2[0]] # adding first elements, step one of function
        total = fsum + add(vals1[1:],vals2[1:]) # recursive case, step one for len(of lists)
        print('the stack is',total)
        return total

#testing
# add([1, 2, 3], [3, 5, 8])
# add([2, 3, 4, 5], [-3, -2, -1, 0])

# 4.4
# weave function

def weave(s1, s2):
    ''' interlock two string and print them weaved'''
    if len(s1) == 0 or len(s2) == 0: # base case
        return (s1+ s2)
    elif s1 == '' and s2 == '':
        return ''

    else:
       first = s1[0] + s2[0] # step 1
       r =  weave(s1[1:], s2[1:])  #step one plus recursive case
       return first + r

#testing 

# weave('aaaaaa', 'bbbbbb')
weave('aaaa', 'bbbbbbxxxxxx')
    






