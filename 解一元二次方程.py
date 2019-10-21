# -*- coding: utf-8 -*-
import math
print("Please input three numbers for the formula ax**2 + bx + c =0:")
a=float(input('input a of the formula:'))
b=float(input('input b of the formula:'))
c=float(input('input c of the formula:'))
def quadratic(a, b, c):
   if (b**2 - 4*a*c)<0:
      print("无解")
      return
   else:
     x1 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
     x2 = (-b-math.sqrt(b**2 - 4*a*c))/(2*a)
     return x1,x2
print(quadratic(a,b,c))