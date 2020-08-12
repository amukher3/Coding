# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 23:24:11 2020

@author: abhi0
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        temp=list()
        self.temp=temp
        

    def push(self, x: int) -> None:
        self.temp.append(x)
        

    def pop(self) -> int:
        return self.temp.pop()
        

    def top(self) -> int:
        return self.temp[len(self.temp)-1]
        
        

    def peekMax(self) -> int:
        return max(self.temp)
        

    def popMax(self) -> int:
        temp1=max(self.temp)
        tempCount=self.temp.count(temp1)
        if tempCount>1:
            tempPrime=self.temp.copy()
            tempAlpha=[]
            for i in range(tempCount):
                tempIdx=tempPrime.index(temp1)
                tempAlpha.append(tempIdx+i)
                tempPrime.pop(tempIdx)
            tempMax=max(tempAlpha)
            print(tempAlpha)
            self.temp.pop(tempMax)
        else:
            self.temp.remove(temp1)
        return temp1
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()