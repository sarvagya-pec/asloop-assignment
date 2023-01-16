# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 01:59:35 2023

@author: LENOVO
"""

a=int(input("enter lower limit"))
for i in range(a,int(input("Enter upper limit: "))):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
