#file: ps12pr2.py
#Author: Nicholas Mosca
#Description: problem set 12 problem 2 Markov test generation
import random

### problem 2.1

def create_dictionary(filename):
    ''' takes in file and adds each word as key and values as associated words'''
    file = open(filename,'r')
    full_text = file.read()
    full_text = full_text.split()
    
    d = {}
    start_word = '$' # start of a sentence
    for word in full_text: # scanning whole document
        if start_word not in d: # if word not in curret d
            d[start_word] = [word] # add that word
        else:
            d[start_word] += [word] # if word is in d then extend the list for that key

        if word[-1] in '.?!':  # if last charater  in word has '.?! 
            start_word = '$' # next word is automatically a start word
        else:
            start_word = word # if not than the current word is key
    return d 
            
#word_dict = create_dictionary('sample.txt')

def generate_text(word_dict,num_words):
    ''' takes in dictionary of words and number and produces a paragragh using that given dictionary'''
    key = '$'   #store key
    string = '' # start blank string 
    #store generated string
    for i in range(num_words): # looping through the amount of times requested 
        word = random.choice(word_dict[key]) # selects random value from word_dictionary with $ as key
        string  += ' ' + word # adds words to string along with spaces 
        if key not in word_dict: # if a word is not in the dictionary of words then start new word
            key = '$' # how t ostart new word
        if word[-1] in '.!?': # if the last element of the word is a sentence ending word then start new word
            key = '$'
        else:
            key = word # if word is okay than continue to add words 

    print(string)
            
       





