# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:54:12 2019

@author: amukher3
"""

testStr=str(input())


LowerCases=[]
UpperCases=[]
DigitCases=[]

for i in range(len(testStr)):
    
    if(testStr[i].islower()):
        LowerCases.append(testStr[i])
        
    elif testStr[i].isupper():
        UpperCases.append(testStr[i])
        
    elif testStr[i].isdigit():
        DigitCases.append(testStr[i])
        
sortedOddList=sorted(list(filter(lambda x: (int(x) %2 != 0) , DigitCases)))
  

sortedEvenList = sorted(list(filter(lambda x: (int(x)%2 == 0) , DigitCases)))
        
    
sortedUpperCase= ''.join(sorted(UpperCases))        
sortedLowerCase= ''.join(sorted(LowerCases))
sortedEvenCase= ''.join(sortedEvenList)
sortedOddCase= ''.join(sortedOddList)

FinalString=sortedLowerCase+sortedUpperCase+sortedOddCase+sortedEvenCase

print(FinalString)




    