# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:14:33 2020

@author: Abhishek Mukherjee
"""

#LeetCode problem
#K closest points to origin on a plane
#distance metric -- euclidean

class Solution:
    def kClosest(self, points: List[List[int]], K: int): 
        arr=points
        origin=[0,0]
        dist=[]
        from scipy.spatial import distance
        for i in range(len(arr)):
            points=arr[i]
            dist.append([distance.euclidean(points,origin),points])
    
        dist.sort()
        FinalList=[]
        for i in range(K):
            FinalList.append(dist[i][1])          
            
        return FinalList  