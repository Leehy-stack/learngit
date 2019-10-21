# -*- coding: utf-8 -*-
#s=input("Please input a string:")
def trim(str):
    if str[0]==" ":
        newstr=str[1:]
    elif str[-1]==" ":
        newstr=str[:-1]
    return newstr
