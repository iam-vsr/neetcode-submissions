from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)

        @lru_cache(None)

        def f(i, prev):
            if i == n:
                return 0
            if prev == -1 or nums[i] > nums[prev]:
                return max(1 + f(i + 1, i), f(i + 1, prev))
            else:
                return f(i + 1, prev)
        
        return f(0,-1)