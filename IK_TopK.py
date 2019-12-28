# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:44:07 2019

@author: Abhishek Mukherjee
"""

## Top K 
##IK practice set...
def topk(arr,k):
    
    #size of array is the first element
    #Removing the length entry
    arr=arr[1:]
    
    #Removing duplicates, if any
    arr=list(set(arr))
    
    #let's do a sort now
    arr=sorted(arr,reverse=True)
    
    if(len(arr)<k):
        res=arr
    else:
        res=arr[:k]        
    
    return res
    
    
    
    