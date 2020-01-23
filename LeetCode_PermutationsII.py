# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:51:40 2020

@author: Abhishek Mukherjee
"""

arr=[1,1,2]

import itertools
lst_b=[]
lst_a=list(itertools.permutations(arr))

for i in range(len(lst_a)):
    if list(lst_a[i]) not in lst_b:
        lst_b.append(list(lst_a[i]))
        
        
