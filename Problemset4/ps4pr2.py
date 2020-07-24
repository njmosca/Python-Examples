#File : ps4pr2.py
# ps4pr2.py (Problem Set 4, Problem 2)
#Author: Nicholas Mosca
# List Comprehension problems 
#

# INSTRUCTIONS: Uncomment these lines as you go, and test them at the console

lc1 = [ x * 2 for x in range(5)]


words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [ w[1]  for w in words]


lc3 = [  word[::-1] *2 for word in ['hello', 'bye', 'no']]


lc4 = [ x**2 for x in range(1, 10) if x**2 % 4 == 0 ]


lc5 = [ c == 'b' or c == 'u' for c in 'bu be you']



# continue with writing functions below:

# 2.2 powers of function

def powers_of(base,count):
    ''' function that takes in
    a number as a base and 
    a count and returns a list
    of the base to the power of count'''

    # using LC
    l = [base**x for x in range(count)]
    return l
    # end of function

#testing
#print(powers_of(2, 5))


# problem 2.3

# shorter than function

def shorter_than(n,wordlist):
    ''' takes in a list of strings and returns strings shorter than n'''
    short = [x for x in wordlist if len(x) <= n-1]
    return short

# testing
# print(shorter_than(4, ['only', 'recursion', 'on', 'the', 'brain']))
# cities = ['Boston', 'Chicago', 'Washington', 'Houston']
# print(shorter_than(7, cities))







if __name__ == '__main__':
    
    
    # test code below, do not modify!
    for x in ['lc1', 'lc2', 'lc3', 'lc4', 'lc5']:
        if x in dir():
            print(x + ' = ', eval(x))

