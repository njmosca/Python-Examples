#
# ps5pr1.py (Problem Set 5, Problem 1)
#
# Caesar cipher / decipher
#
def rot(c,n):
    """ rotate c forward by n characters,
wrapping as needed; only letters change """

    if 'a' <= c <= 'z':        # lower-case 
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
            
    elif 'A' <= c <= 'Z':       # upper-case
        new_ord = ord(c) + n 
            
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
    else: # non-alpha 
            new_ord = ord(c)
    return chr(new_ord)





#### Put your code for the encipher function below. ####

# problem 1.2 use rot function to include into Caesar cipher function\
def encipher(s,n):
     ''' rotate all strings in s by n amount where s is a string and n is a real number'''
     if s == '' or n == 0:
         return s
     else:
        rotate = rot(s[0],n)
        rest = encipher(s[1:],n)
        #print('rest is',rest,'rotate is',rotate)
        return rotate + rest 


    




# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####
## joined office hours at 5.26 pm and waited till 7.36 when we were told that we could no longer ask questions so i was just stuck without help. Not Hassans fault because hes spending 30+ mins for each student ahead of me but something has to change


def decipher(s):
    ''' trying to make string more english'''
    all_shifts = [[encipher(s,n)] for n in range(25) ] # all possible values
    almost_english = [sum([letter_probability(x) for x in s])for s in all_shifts] # tried to use list of lists method to create a list and add all probablities
    best_translation = all_shifts[almost_english.index(max(almost_english))]
    return best_translation

# not sure what to do 



#testing
#decipher('python')