# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:11:45 2020

@author: abhi0
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        temp=[]
        cnt=0
        for i in range(len(points)-1):
            ptA=points[i]
            ptB=points[i+1]
            while ptA[0]!=ptB[0] or ptA[1]!=ptB[1]:
                if ptA[0]==ptB[0] and ptB[1]!=ptA[1]:
                    if ptB[1]>ptA[1]:
                        ptA[1]+=1
                    else:
                        ptA[1]-=1
                    cnt+=1
                elif ptA[0]!=ptB[0] and ptB[1]==ptA[1]:
                    if ptB[0]>ptA[0]:
                        ptA[0]+=1
                    else:
                        ptA[0]-=1
                    cnt+=1
                else:
                    if ptB[1]>ptA[1]:
                        ptA[1]+=1
                    else:
                        ptA[1]-=1
                    if ptB[0]>ptA[0]:
                        ptA[0]+=1
                    else:
                        ptA[0]-=1
                    cnt+=1
            temp.append(cnt)
        return cnt
    
                
                
                
            
            
            
            
        