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
        l,r=0,0

        while r<n-1:
            if l>r:
                return False
            maxi=0
            for i in range(l,r+1):
                maxi=max(maxi,i+nums[i])
            l=r+1
            r=maxi
            if r>=n-1:
                return True
            
        return r>=n-1


