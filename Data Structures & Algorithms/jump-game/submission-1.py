# from functools import lru_cache
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n=len(nums)
#         @lru_cache(None)
#         def dfs(i):
#             if i>=n-1:
#                 return True
#             if nums[i]==0:
#                 return False
            
#             for j in range(1,nums[i]+1):
#                 if dfs(i+j):
#                     return True
#             return False

#         return dfs(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        f=0
        for i in range(n):
            if i>f:
                return False
            f=max(f,i+nums[i])
            if f>=n-1:
                return True
        return True


