# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:13:31 2020

@author: Abhishek Mukherjee
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        temp=[]
        for i in emails:
            locName=i.split('@')[0]
            domName=i.split('@')[1]
            if '.' in locName:
                locName=locName.replace('.','')
            if '+' in locName:
                locName=locName.split('+')[0]
                
            temp.append(locName+'@'+domName)
                
        return len(set(temp))