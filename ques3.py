# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 01:59:02 2023

@author: LENOVO
"""

a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
import math
if a+b>c and b+c>a and a+c>b and a>0 and b>0 and c>0:
    s=(a+b+c)/2
    print("the area of triangle is: ",math.sqrt((s*(s-a)*(s-b)*(s-c))))
else:
    print("triangle not possible")