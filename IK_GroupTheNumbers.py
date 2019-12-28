# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:42:06 2019

@author: Abhishek Mukherjee
"""

#The problems asks to group the even and 
#odd numbers together in an array. 
#The size of the array can be anywhere between 0 to 10**5

#size of array 1<=n<=10^5
#In Linear time complexity 
#In Contant space
#Auxillary space can't be used

#Using Lumotto's partitioning 


def solve(arr):
    
    start=0
    oddPtr=start
    EvenPtr=start
    
    #n is the length of the array
    n=len(arr)
    #removing the zero th element 
    #since its just the size
    #arr=arr[1:]
    
    #Edge case 1 where there is only
    #element in the array. No grouping is 
    #required here.
    if(n==1):
        return arr
    
    #Edge case 2 where there are only
    #2 elements in the array. No grouping is 
    #required here as well.
    if(n==2):
        return arr
    
    #Paritioning starts here
    #Group the elements according to their 
    #relative pointer position. Similar idea to 
    #lumotto's partiioning.
    for EvenPtr in range(start+1,n):
        if(arr[EvenPtr]%2!=0):
            oddPtr+=1
            temp=arr[oddPtr]
            arr[oddPtr]=arr[EvenPtr]
            arr[EvenPtr]=temp
    
    #Place the pivot element at the boundary
    #between odd and even. 
    pivot=arr[0]
    arr[0]=arr[oddPtr]
    arr[oddPtr]=pivot
                        
    return arr