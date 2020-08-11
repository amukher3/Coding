# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:21:49 2020

@author: abhi0
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        tempDict=dict()
        puncMarks=[',','.','!','?',"'",';']
        for i in puncMarks:
            paragraph=paragraph.replace(i,' ')
        tempLst=paragraph.split(' ')
        print(tempLst)
        for i in tempLst:
            if i not in banned and i!=" " and i!="":
                if i not in tempDict:
                    tempDict.update({i:1})
                else:
                    tempDict[i]+=1

        sortedDict=sorted(tempDict.items(),key=lambda x:x[1],reverse=True)            
        return sortedDict[0][0]
                    