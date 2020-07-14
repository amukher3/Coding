# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:26:18 2020

@author: abhi0
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                tempIdx=t.index(i)
                t=t[tempIdx+1:]
            else:
                return False
        return True