'''
https://leetcode.com/problems/single-number/
'''

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        
        if (len(nums))==1:
            return nums[0]
        
        di=dict()
        
        for n in nums:
            if n in di.keys():
                di[n]+=1
            else:
                di[n]=1
                
        for k,v in di.items():
            if v==1:
                return k
              
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans=0
        
        for n in nums:
            ans=ans^n
            
        return ans     
