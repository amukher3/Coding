# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:16:34 2020

@author: abhi0
"""

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp=set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.temp:
            self.temp.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if  val in self.temp:
            self.temp.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.temp)!=0:
            tempPrime=randrange(len(self.temp))
            return list(self.temp)[tempPrime]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()