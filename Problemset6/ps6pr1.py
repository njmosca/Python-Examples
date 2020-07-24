#file: ps6pr1
#Author: Nicholas Mosca
# Description: problem set 6 problem 1, binary conversion problems with recursion

#1.1
#converting decimal number to binary string
# always print input of the function when building
#
def dec_to_bin(n):
    ''' converting number to binary string'''
    print('n =', n)
    if n == 0:
        return '0'
    elif n == 1:
        return '1'

    else: # solve right most bit and label it
        if n % 2 == 1: # if answer is odd
            right_bit = '1'
        if n % 2 == 0: # if number is even
            right_bit = '0'
        rem = n >> 1 # halfing n 
        rest_bin = dec_to_bin(rem) # recursive for half of n value
        
        answer_binary = rest_bin + right_bit
        print('n=',n,'answer_binary is',answer_binary)
        return answer_binary
        
        
#testing
#dec_to_bin(9)

#1.2
# converting binary to decimal
def bin_to_dec(b):
    ''' converting b which is a binary string into a integer'''
    #print('b is',b)
    #base cases
    if b =='1':
        return 1
    if b =='0':
        return 0
    else:
        #recursive case  

        return bin_to_dec(b[:-1]) *2 + int(b[-1]) 

#test

#testing
bin_to_dec('101')