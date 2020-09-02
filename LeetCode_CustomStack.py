# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:32:51 2020

@author: Abhishek Mukherjee
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.temp=list()
        self.maxSize=maxSize
     
        
    def push(self, x: int) -> None:
        if len(self.temp)<self.maxSize:
            self.temp.append(x)
         
        

    def pop(self) -> int:
        if len(self.temp)!=0:
            return self.temp.pop()
        else:
            return -1
        
    def increment(self, k: int, val: int) -> None:
        if len(self.temp)<k:
            for i in range(len(self.temp)):
                self.temp[i]+=val
        else:
            for i in range(k):
                self.temp[i]+=val
        
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)