# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:58:43 2020

@author: Abhishek Mukherjee
"""

n = 4
k = 2
arr=list(range(1,n+1))

from itertools import combinations
lst_a=list((combinations(arr,k)))

FinList=[]

for i in range(len(lst_a)):
    FinList.append(list(lst_a[i]))
