# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:45:28 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        flag=0
        if len(words1)!=len(words2):
            return False
        if words1==words2:
            return True
        
        for i in range(len(words1)):
            for j in range(len(pairs)):
                if words1[i] in pairs[j]:
                    if words2[i] in pairs[j]:
                        flag=0
                        break
                    else:
                        flag=1
                elif words2[i] in pairs[j]:
                    if words1[i] in pairs[j]:
                        flag=0
                        break
                    else:
                        flag=1
            if flag==1:
                return False
            
        return True
        