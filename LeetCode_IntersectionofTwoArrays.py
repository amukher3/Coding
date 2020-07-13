# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 02:51:07 2020

@author: abhi0
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setA=set(nums1)
        setB=set(nums2)
        
        setC=setA.intersection(setB)
        
        return list(setC)
    
##################################################
############## Another Way #######################
#################################################
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setA=set(nums1)
        setB=set(nums2)
        temp=[]
        for i in setA:
            if i in setB:
                temp.append(i)
        
        return temp