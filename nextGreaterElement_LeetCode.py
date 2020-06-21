class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempArr=[]
        import numpy as np
        for i in nums1:
            idx=nums2.index(i)
            newArr=nums2[idx+1:]
            
            if len(newArr)>=1:
                tempMax=max(newArr)
                
                if tempMax<=i:
                    tempArr.append(-1)
                    continue
                for j in range(len(newArr)):
                    if newArr[j]>i:
                        tempArr.append(newArr[j])
                        break        
            else:
                tempArr.append(-1)
                
            
                    
        return tempArr            
        
                    
        