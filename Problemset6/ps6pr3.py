#file:ps6pr3.py
#Author: Nicholas Mosca
#Description: problemset 6 problem 3/ binary recursion

def bitwise_and(b1,b2):
    ''' function that takes in two binary strings and multiplys each column and returns string
    same length in binary format'''
    #print('b1 =',b1,'b2=',b2)
    #base cases
    if b1 == '' and b2 =='':
        return ''
    elif b1 == '':
        return '0' * len(b2)
    elif b2 =='':
        return '0' * len(b1)

    else:
        # recursive case
        rest = bitwise_and(b1[:-1],b2[:-1])
        if b1[-1] == '0' or b2[-1] == '0':
            last_digit = '0'
            final = rest + last_digit
            return final
        elif b1[-1] == '1' and b2[-1] == '1':
            last_digit = '1'
            final = rest + last_digit
            return final

#print(bitwise_and('11010', '10011'))

def add_bitwise(b1,b2):
    ''' function that adds binary numbers'''
    print('b1 =',b1,'b2=',b2)
    if b1 == '' and b2 =='':
        return ''
    elif b1 == '':
        return b2
    elif b2 =='':
        return b1
    else:
        rest = add_bitwise(b1[:-1],b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            carry = '1'
            rest = add_bitwise(rest,carry)
            return rest + '0'
        elif b1[-1] == '1' or b2[-1] =='1':
            return rest + '1'
        else:
            return rest + '0'
            
add_bitwise('11100', '11110')


        
        


