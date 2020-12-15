# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 01:44:20 2020

@author: abhi0
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
            if ops==[]:
                return m*n
            cur_ele_0=ops[0][0]
            cur_ele_1=ops[0][1]
            for i in range(1,len(ops)):
                cur_ele_0=min(cur_ele_0,ops[i][0])
                cur_ele_1=min(cur_ele_1,ops[i][1])
                
            return cur_ele_0*cur_ele_1