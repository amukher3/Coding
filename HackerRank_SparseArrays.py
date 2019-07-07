# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 04:56:36 2019

@author: Abhishek Mukherjee
"""
# the size of the strings
n=int(input())
inpStr=[]

#input strings
for i in range(n):
    inpStr.append(str(input()))
    
# the size of queries 
q=int(input())    
inpQue=[]

#input queries
for i in range(q):
    inpQue.append(str(input()))
  
res=[]  
for i in range(len(inpQue)):
    Cnt=0
    if inpQue[i] in inpStr:
        Cnt=Cnt+1
    res.append(Cnt)    
        
    