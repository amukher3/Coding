# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 19:04:09 2019

@author: Abhishek Mukherjee
"""
from itertools import combinations

inp=list(map(str, input().split()))

S=sorted(inp[0])
k=int(inp[1])

n=list(range(1,k+1))
combList=[]

for i in range(len(n)):
    combList.append(list(combinations(S,n[i])))
    
for i in range(len(n)):
    #sortedList=sorted(combList[i][:])
    sortedList=combList[i][:]
    for j in range(len(sortedList)):
        joinedList="".join(sortedList[j][:])
        print(joinedList.strip("'"))