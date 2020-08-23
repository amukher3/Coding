# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 09:03:18 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        i=0
        tempLen=[]
        while i<=len(S)-1:
            idx=(len(S)-S[::-1].index(S[i]))-1
            j=i+1
            while j<idx:
                temp=(len(S)-S[::-1].index(S[j]))-1
                if temp>idx:
                    idx=temp
                j+=1
            tempLen.append((idx-i)+1)
            i=idx+1
        return tempLen