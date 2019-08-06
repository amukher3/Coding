# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 20:00:06 2019

@author: amukher3
"""

K=int(input())
listA=list(map(int,input().split()))

# taking it in a set to reduce the number of 
# iterables. Set removes the duplicate items. 
setA=set(listA)
count = {}

for i in range(len(listA)):
    if listA[i] in count:
        count[listA[i]] += 1
        if count[listA[i]] == K:
            del(count[listA[i]])
    else:
        count[listA[i]] = 1

print(list(count.keys())[0])
