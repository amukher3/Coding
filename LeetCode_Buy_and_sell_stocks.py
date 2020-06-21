# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:38:52 2020

@author: abhi0
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        if(len(prices)<=1):
            return maxprof
        minprice=prices[0]
        maxprice=prices[0]
        for i in prices[1:]:
            if i>maxprice:
                maxprice=i
            elif i<minprice:
                minprice=i
                maxprice=i
            if (maxprice-minprice)>maxprof:
                maxprof=maxprice-minprice
        return maxprof