#ps11pr1.py
# ps11pr1.py - starter code for Problem Set 11, problem 1
#Author: Nicholas Mosca
#


s1 = 'Three little kittens lost their mittens'
s2 = 'Star light, star bright'


# count all occurrences of the letter T (both upper-case and lower-case) in s1, 
# and assign the count to the variable answer0
answer0 = s1.count('T') + s1.count('t')

# do your work here!

#puzzle1

answer1 = s1.replace('tt','pp')

#puzzle2 

answer2 = s2.split('r')

#puzzle3

answer3 = s2.upper().replace('STAR','NIGHT')

#puzzle4

answer4 = s1.lower().split('th')

#puzzle5

answer5 =s2.replace("ight",'ook').split(',')



# put any print statements/test code inside this controlled block:
if __name__ == '__main__':
    
    print('s1 =', s1)
    print('s2 =', s2)
    
    print('answer0 =', answer0)
    print('answer1 =', answer1)
    print('answer2 =', answer2)
    print('answer3 =', answer3)
    print('answer4 =', answer4)
    print('answer5 =',answer5)
    
    # optional: add your test code here
    
    

