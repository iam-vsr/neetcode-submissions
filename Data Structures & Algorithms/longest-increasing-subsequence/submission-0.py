from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        @lru_cache(None)

        def f(i,prev):
            if i==n:
                return 0
            
            ans=f(i+1,prev) #not take
            if prev==-1 or nums[i]>nums[prev]:
                ans=max(1+f(i+1,i),ans) #take
            return ans
        
        return f(0,-1)