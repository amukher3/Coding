# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:13:24 2019

@author: Abhishek Mukherjee
"""

marksheet=[];
for _  in range(int(input())):
    name = input()
    score = float(input())
    marksheet.append([name, score])
sorted_marksheet=sorted(marksheet, key = lambda x: x[1])
secondLast=sorted_marksheet[1] 
ThirdLast=sorted_marksheet[2]
scoreSecondLast=secondLast[1]
scoreThirdLast=ThirdLast[1]
if scoreSecondLast==scoreThirdLast:
     sorted_names=sorted([secondLast[0],ThirdLast[0]])
     print(sorted_names[0])
     print(sorted_names[1])
else:     
    print(secondLast[0])

marksheet=[] 
dupNames=[]
for _  in range(int(input())):
    name = input()
    score = float(input())
    marksheet.append([name, score])
    
sorted_marksheet=sorted(marksheet, key = lambda x: x[1])
if sorted_marksheet[0][1]==sorted_marksheet[1][1]==sorted_marksheet[2][1]:
    secondLast=sorted_marksheet[3]
if sorted_marksheet[0][1]==sorted_marksheet[1][1]:
    secondLast=sorted_marksheet[2]
else:    
    secondLast=sorted_marksheet[1]
scoreSecondLast=secondLast[1] 
for i in range(len(marksheet)):
    if scoreSecondLast==marksheet[i][1]:
        dupNames.append(marksheet[i][0])
sorted_names=sorted(dupNames)   
print('\n'.join(map(str, sorted_names)))     