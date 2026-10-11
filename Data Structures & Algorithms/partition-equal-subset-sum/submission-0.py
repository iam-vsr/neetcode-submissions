class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        dp=[[None]*(target+1) for _ in range(len(nums)+1)]

        def f(n,target):
            if target==0:
                return True
            if n==0:
                return False
            if dp[n][target]!=None:
                return dp[n][target]
            
            if target>=nums[n-1]:
                dp[n][target]=f(n-1,target) or f(n-1,target-nums[n-1])
            else:
                dp[n][target]=f(n-1,target)
            return dp[n][target]
        
        return f(len(nums),target)