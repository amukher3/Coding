# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:09:56 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushPtr=0
        popPtr=0
        temp=[]
        while pushPtr<=len(pushed)-1 or popPtr<=len(popped)-1:
            if len(temp)>0 and popped[popPtr]==temp[len(temp)-1]:
                temp.pop()
                popPtr+=1
            else:
                if pushPtr<=len(pushed)-1:
                    temp.append(pushed[pushPtr])
                    pushPtr+=1
                else:
                    return False
        if temp==[]:
            return True
        else:
            return False
                
        