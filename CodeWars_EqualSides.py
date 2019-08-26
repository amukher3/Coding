# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:50:44 2019

@author: amukher3
"""

arr=[1,100,50,-51,1,1]




for i in range(0,len(arr)):
    rightSum=0
    leftSum=0
    
    for x in range(i+1,len(arr)):
        rightSum += arr[x]
    

    y=i-1
    while y>=0:
        leftSum+=arr[y]
        y=y-1
     
        
    if leftSum==rightSum:
        val=i  
        break
        
        
if leftSum != rightSum:
    val=-1    
    
    
print(val)    
        
        
        