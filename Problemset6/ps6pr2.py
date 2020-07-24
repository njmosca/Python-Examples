# file: ps6pr2.py
#Author: Nicholas Mosca
# Description: problemset 6 problem 2/ binary recursion
from ps6pr1 import *

## 2.1
# adding binary strings 

def add(b1,b2):
    ''' function that adds binary numbers, taking in strings as b1 and b2'''
    #print('b1=',b1,'b2=',b2)
    b1_int = bin_to_dec(b1)
    b2_int = bin_to_dec(b2)
    #print('b1_int',b1_int,'b2_int',b2_int)
    value = b1_int + b2_int
    new_binary = dec_to_bin(value)
    return new_binary # could make this more efficent i think 



#testing
# add('11', '1')
# add('11100', '11110')


## problem 2.2

def increment(b):
    ''' takes binary string thats 8 char and returns the next highest number in binary'''
    print('b is',b)
    if b == '11111111':
        return'00000000'
    
    else:
        value_of_b = bin_to_dec(b)
        new_value = value_of_b + 1
        result = dec_to_bin(new_value)
        dif = 8 - len(result)
        return '0' * dif + result
#testing

# increment('00000111')
# increment('00000001')
# increment('11111111')

