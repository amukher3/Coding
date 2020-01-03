# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:44:07 2019

@author: Abhishek Mukherjee
"""

## Top K 
##IK practice set...

arr=[16,5,7,10,2,2,4,4,9,9,4,10,2,6,7,3,8,7]

def topk(arr,k):
    
    #size of array is the first element
    #Removing the length entry.
    
    #N.B: If you are usinig the IK web
    #Interface you can comment the next line
    # otherwise remove the first element which is
    #the length of the array.
    arr=arr[1:]
    
    #Removing duplicates,if any
    arr=list(set(arr))
    
    #let's do a sort now
    arr=sorted(arr,reverse=True)
    
    if(len(arr)<k):
        res=arr
    else:
        res=arr[:k]        
    
    return res
    
    
    
    