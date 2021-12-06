'''
https://leetcode.com/problems/unique-number-of-occurrences/
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count={}
        
        for e in arr:
            if e in count.keys():
                count[e]+=1
            else:
                count[e]=1
                
        if sum(list(set(count.values())))==len(arr):
            return 1
        else:
            return 0
