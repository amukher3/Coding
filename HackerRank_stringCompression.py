# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:40:28 2019

@author: Abhishek Mukherjee
"""

from itertools import groupby
S = list(input())
groups = []
for k, g in groupby(S):
    groups.append(list(g))
    
vec=[]    
for g in groups:
    g[0]=g[0].replace("'"," ")
    if len(g)>1:
        vec.append(list([g[0],len(g)]))
    else:
        vec.append(list([g[0],g]))    
    
newVec=sum(vec,[])    
str1 = ''.join(str(e) for e in newVec)  
 