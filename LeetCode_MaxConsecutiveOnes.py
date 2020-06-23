# -*- coding: utf-8 -*-

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                if count>maxCount:
                    maxCount=count
                count=0
                
        if count>maxCount:
            maxCount=count
            
        return maxCount    