# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 07:26:28 2019

@author: Abhishek Mukherjee
"""

#LeetCodeProblem
#75.SortColors
#Inplace algorithm -- can't take auxillary list/array

def numColors(nums):
    
    #size pointer
    size_ptr=len(nums)

    import numpy as np
    for i in range(len(list(set(nums)))):
        nums.extend(list(set(nums))[i]*np.ones(nums.count(list(set(nums))[i])))
    
    nums=nums[size_ptr:] 

    for i in range(len(nums)):
        nums[i]=int(nums[i])
    
    return nums    

