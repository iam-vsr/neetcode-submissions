from functools import lru_cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        @lru_cache(None)
        def dfs(i):
            if i>=n-1:
                return True
            if nums[i]==0:
                return False
            
            for j in range(1,nums[i]+1):
                if dfs(i+j):
                    return dfs(i+j)
            return False

        return dfs(0)