# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:06:22 2019

@author: amukher3
"""

from collections import OrderedDict

N=int(input())

d=OrderedDict()

for i in range(N):
    item,space,price=input().rpartition(' ')
    if d.get(item):
        d[item]+=int(price)
    else:
        d[item]=int(price)
        
for i in d.keys()      :
    print(i,d[i])
        
        
    