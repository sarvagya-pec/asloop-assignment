# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:02:29 2023

@author: LENOVO
"""

lst=[]
num=int(input("enter length of list: "))
for i in range(num):
    lst.append(input("enter an object: "))
lst2=list(set(lst))
for j in lst2:
    print(j,"occurs",lst.count(j),"times")
