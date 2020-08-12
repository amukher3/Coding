# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:38:28 2020

@author: abhi0
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        tempDict=dict()
        self.tempDict=tempDict
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.tempDict:
            self.tempDict.update({message:timestamp})
            return True
        else:
            tempTimeStamp=self.tempDict[message]
            if abs(timestamp-tempTimeStamp)<10:
                return False
            else:
                self.tempDict.update({message:timestamp})
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)