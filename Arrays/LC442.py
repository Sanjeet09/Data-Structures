'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=dict()
        for e in nums:
            if e in count.keys():
                count[e]+=1
            else:
                count[e]=1
                
        ans=list()
        
        for k,v in count.items():
            if v==2:
                ans.append(k)
                
        return ans
