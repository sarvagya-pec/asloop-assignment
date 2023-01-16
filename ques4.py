# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 01:59:22 2023

@author: LENOVO
"""

n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')