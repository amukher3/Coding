# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 01:57:33 2020

@author: Abhishek Mukherjee
"""

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.tempLst=list()
        self.size=size
        

    def next(self, val: int) -> float:
        if len(self.tempLst)<self.size:
            self.tempLst.append(val)
            return mean(self.tempLst)
        else:
            self.tempLst=self.tempLst[1:]
            self.tempLst.append(val)
            return mean(self.tempLst)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)