# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:18:49 2019

@author: Abhishek Mukherjee
"""

N=int(input())

ss=set()

for i in range(N):
    tmp=input()
    ss.add(tmp)
print(len(ss))  