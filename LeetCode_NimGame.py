# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:57:27 2020

@author: abhi0
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        
        if n<=3:
            return True
        
        if n%4==0:
            return False
        else:
            return True