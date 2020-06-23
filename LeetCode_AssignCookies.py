# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:32:32 2020

@author: abhi0
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        i=0
        s=sorted(s)
        while i<len(g): #greed factor for childrens
            for j in range(len(s)): #size of cookies
                if s[j]>=g[i]: #if the size is larger than greed factor,children is satisfied
                    count+=1 #increment the counter
                    s.pop(j) #Remove the cookie
                    break #go to the next children
            i+=1
        return count        