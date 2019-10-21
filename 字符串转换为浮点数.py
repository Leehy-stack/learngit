# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    L=s.split(".",1)
    def char2num(s):
        return DIGITS[s]
    def fn(x,y):
        return x*10 + y
    return reduce(fn,map(char2num,L[0]))+reduce(fn,map(char2num,L[1]))/pow(10,len(L[1]))
st=input("Please input a string of float number: ")
print(str2float(st))
if type(str2float(st)):
    print('Yes')
