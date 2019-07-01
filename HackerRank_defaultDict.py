# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 00:29:58 2019

@author: Abhishek Mukherjee
"""

# default Dict
from collections import defaultdict
d= defaultdict(list)


# n for group A
# m for group B
lst=list(map(str, input().split()))
n=int(lst[0])
m=int(lst[1])

for i in range(n):
   strA=list(map(str, input())) 
   d['groupA'].append(strA)
for i in range(m)   :
    strB=list(map(str, input())) 
    d['groupB'].append(strB)

lst1=list(d['groupA']) 
lst2=list(d['groupB'])  
for i in range(len(lst2)) :
    Idx=[]
    if lst2[i] in lst1:
        for j in range(len(lst1)):
            if lst2[i]==lst1[j]:
                Idx.append(j+1)
        print(*Idx)       
    else:
        print(-1)
