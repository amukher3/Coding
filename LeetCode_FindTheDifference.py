# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:08:50 2020

@author: abhi0
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sPrime=[]
        tPrime=[]
        sPrime.extend(s)
        tPrime.extend(t)
        if len(tPrime)>len(sPrime):
            for count,i in enumerate(tPrime):
                if i not in sPrime:
                    return i
                else:
                    sPrime.remove(i)
        else:
            for count,i in enumerate(sPrime):
                if i not in tPrime:
                    return i
                else:
                    tPrime.remove(i)