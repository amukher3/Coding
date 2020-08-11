# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 00:16:28 2020

@author: abhi0
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        temp=[]
        for i in s:
            if i.isalpha() is True or i.isnumeric() is True:
                temp.append(i)

        if temp==temp[::-1]:
            return True
        else:
            return False
        