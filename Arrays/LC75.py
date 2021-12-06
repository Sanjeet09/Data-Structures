'''
https://leetcode.com/problems/sort-colors/
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        c=0
        c1=0
        c2=0
        
        for i in range (len(nums)):
            e=nums[i]
            if e== 0:
                c+=1
            elif e==1:
                c1+=1
            else:
                c2+=1
        
        nums.clear()
        
        while(c):
            nums.append(0)
            c-=1
        
        while(c1):
            nums.append(1)
            c1-=1
        
        while(c2):
            nums.append(2)
            c2-=1
