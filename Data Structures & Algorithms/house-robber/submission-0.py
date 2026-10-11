class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[None]*n

        def f(i):
            if i>n-1:
                return 0
            if dp[i]!=None:
                return dp[i]
            dp[i]=max(f(i+1),f(i+2)+nums[i])
            return dp[i]
        return f(0)