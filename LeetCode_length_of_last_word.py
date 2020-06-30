# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:44:09 2020

@author: abhi0
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        import re
        temp=re.findall('\w+',s[::-1])
        if len(temp)!=0:
            return len(temp[0])
        else:
            return 0