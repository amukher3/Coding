# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 14:49:22 2020

@author: abhi0
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
            #For bull-count(position match as well)
            
            i=0
            bullCount=0
            tempSecret=[]
            tempGuess=[]
            tempSecret.extend(secret)
            tempGuess.extend(guess)
            temp=[]
            
            while i<len(tempSecret):
                if tempSecret[i]==tempGuess[i]:
                    bullCount+=1
                    temp.append(tempSecret[i])
                i+=1  
                
            for i in temp:
                tempSecret.remove(i)
                tempGuess.remove(i)
                
            cowCount=0
            #For cow-count(just total count match)
            for i in tempSecret:
                if i in tempGuess:
                    cowCount+=1
                    tempGuess.remove(i)
                    
            
            tempBull=[]
            tempCow=[]
            tempCow.append(str(cowCount))
            tempBull.append(str(bullCount))
            
            tempBull.append('A')
            tempCow.append('B')
            tempArr=tempBull+tempCow
            
            return ''.join(tempArr)