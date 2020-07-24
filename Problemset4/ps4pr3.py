#File: ps4pr4.py
#Author: Nicholas Mosca
# Description: problemset 4 problem 3, more complex functions with recursion and LC
# Algorithm design


#4.1
# cube all values in list 

def cube_all_lc(values):
    ''' cube all values in the given list'''
    cube = [x**3 for x in values] # turns x into values and takes all values to third power
    return cube


#testing
cube_all_lc([-2, 5, 4, -3])  



#4.2
#cube all values in list but not wit Lc with recurion

def cube_all_rec(values):
    ''' cubing all values with recursion not LC'''
    if values != []:
        first = [values[0] ** 3]
        rest = cube_all_rec(values[1:])
        print('first ->',first,'rest->',rest)

        return first + rest
    else:
         return []


#4.3
def num_larger(threshold,values):
     ''' function that takes in a threshold or cap number, and a list
     only returrning the amount of values higher than the threshold'''
     s = sum([x > threshold for x in values])
     return s 


#testing
# num_larger(5, [1, 7, 3, 5, 10])

# 4.4

# supplement function


def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0]  in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest



# most consonants function
# was very difficult till i looked at the last part of the review videos in class


def most_consonants(words):
    ''' function that takes in a list of words and returns the word with the most consonants'''
# have to figure out the difference between len of each element in words
# and amount of vowels.
# that value is used to create a new lit with the coorisponding word.
    new_list = [[len(x) - num_vowels(x),x] for x in words] # generates new list
    element = max(new_list) # finds sub list with ost consonants
    return  element[1] # prints word only
    
# testing
# most_consonants(['python', 'is', 'such', 'fun'])
# most_consonants(['oooooooh', 'i', 'see', 'now'])

#4.5
# please continue with the easiest question last to keep moral high!!!

def price_string(cents):
    ''' converts total amount of cents into dollar amount'''
    
    d = cents // 100  # amount of full dollars
    c = cents - d * 100  # total large number - dollar amount to get cents
    if d == 0: # if amount is under 1 dollar
        price = c
        price = (str(price) +' cents') # just cents
    elif c == 0: # might not need this 
        price = d
        price = (str(price) + ' dollars') # just dollars
    elif d ==1 and c ==1: # Semantics
        price = (str(d) + ' dollar ' + str(c) + ' cent')
    elif c == 1: # Semantics
        price = (str(d) + ' dollars ' + str(c) + ' cent') 
    elif d == 1: # Semantics
        price = (str(d) + ' dollar ' + str(c) + ' cents')
    # most common case
    else:
        d = str(d)
        c = str(c)
        price = d + ' dollars' + ', ' + c + ' cents' # total with fancy string conversion to make it look clean
    return price
#testing
#price_string(101)
#price_string(452)
