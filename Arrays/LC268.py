'''
https://leetcode.com/problems/missing-number/
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=len(nums)
        
        for num in range(0,n+1):
            if num not in nums:
                return num
