# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:48:06 2019

@author: amukher3
"""

# number of students subscribed to the english newspaper
n=int(input())

#the roll number list
EngNewPaper=list(map(int,input().split()))

#the number of students subscribed to the French newspaper
m=int(input())

# the roll-number list
FrenNewPaper=list(map(int,input().split()))

#union of the two lists
UnionLists=EngNewPaper+FrenNewPaper

UnionLists=set(UnionLists)

print(len(UnionLists))