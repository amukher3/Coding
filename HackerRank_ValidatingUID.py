# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:28:10 2019

@author: Abhishek Mukherjee
"""

#Number of test cases:
N=int(input())

lst=[] 
for i in range(N):
    UID=str(input())
    lst.append(UID)
    
for i in range(len(lst)):
    DigCount=0
    AlphaCount=0
    for j in lst[i]:
        if j.isdigit():
            DigCount=DigCount+1
        if j>='A' and j<='Z':
            AlphaCount=AlphaCount+1
            
    if len(lst[i]) != 10:
        print("Invalid")
    elif len(set(lst[i])) != len(lst[i]):
        print("Invalid")
    elif lst[i].isalnum()==False:
        print("Invalid")
    
    elif DigCount<3:
        print("Inavlid")
    elif AlphaCount<2:
        print("Invalid")
    else:
        print("Valid")
        
        
        
     
        