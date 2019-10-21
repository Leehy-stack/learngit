# -*- coding: utf-8 -*-
x=int(input('Please input the first number you want to multifly:'))
y=int(input('Please input the second number you want to multifly: (default is 1)'))
z=tuple(input('Please input another numbers you want to multifly: '))
def product(x,y=1,*z):
    result = x*y
    for n in z:
        n1=int(n)
        result = result * n1
    return result
print(product(x,y,z))