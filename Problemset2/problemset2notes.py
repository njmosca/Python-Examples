#####problem set notes

def wow(a):
    b = a * 2
    print('wow:', a, b)
    return b

def yay(b):
    a = wow(b) + wow(b + 2)
    print('yay:', a, b)
    return a

a = 4
b = 3
print(a, b)
b = wow(b)
print(a, b)
yay(a)
print(a, b)