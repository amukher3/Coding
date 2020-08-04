# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:51:55 2020

@author: abhi0
"""

class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.count=0
        brr=[]
        for i in v:
            brr.extend(i)
        self.brr=brr
            

    def next(self) -> int:
        temp=self.brr[self.count]
        self.count=self.count+1
        return temp
        

    def hasNext(self) -> bool:
        if self.count<len(self.brr):
            return True
        else:
            return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()