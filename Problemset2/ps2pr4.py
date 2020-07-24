#File:ps2pr4.py
#Author: Nicholas Mosca
# description : Problemset 2 #4 functions on strings part 2


#4.1

def mirror(s):
    ''' takes in a string and creates a mirror or reverse string and attaches to origional'''
    mirror = s[-1::-1] # negative splicing
    return s + mirror # returns origional string plus reverse

#### testing function 
mirror('bacon')
print(mirror('XYZ'))

#4.2

def is_mirror(s):
    ''' testing is string is a mirror or not'''
    l = len(s)//2 # grabbing the length of the string and cutting in half to find the mirrored string
    half = s[0:l] # grabbing mirror
    return mirror(half) == s  # is the mirror a true mirror or not 


#testing
print(is_mirror('XYZZYX'))
print(is_mirror('baconnoca'))


#4.3
#replace value fuction 

def replace_end (values, new_end_vals):
    
    values_length = len(values) # length of values
    new_length = len(new_end_vals) # length of replacements
    new_values = values[0:] # may not need this line but just grabs values 
    if len(new_end_vals) >= len(values):
        x = new_end_vals
    else:

        x = new_values[0:-new_length] + new_end_vals
    return x  # returns origional list subtracting length of new values and replacing

### testing 
print(replace_end([1, 2, 3, 4, 5], [12]))
print(replace_end([1, 2, 3, 4, 5], [10, 11]))
print(replace_end([0, 2, 4, 6], [4, 3, 2, 1, 0]))


#4.4
#repeat element function 

def repeat_elem(values, index, num_times):
    ''' repeat element list'''
    target = values[index] # grabs key element
    repeat = [target for i in range(num_times)] # repeats that element x times
    new_list = values[:index] + repeat[:-1] + values[index:] # combine all 3 sub lists
    return new_list
 




#testing 

x = repeat_elem([5, 6, 7], 1, 3)
print(x)
y = repeat_elem([10, 11, 12, 13], 2, 6)
print(y)