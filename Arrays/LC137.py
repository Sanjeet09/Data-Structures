'''
https://leetcode.com/problems/single-number-ii/
'''

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        
        di=dict()
        
        for n in nums:
            if n in di.keys():
                di[n]+=1
            else:
                di[n]=1
                
        for k,v in di.items():
            if v==1:
                return k


              
