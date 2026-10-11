class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        dp=[[None]*(2*total+1) for _ in range(len(nums)+1)] #-sum to +sum possible

        def dfs(i,curr_sum):
            if i==len(nums):
                return 1 if curr_sum==target else 0
             #offset needed
            if dp[i][curr_sum+total]!=None:
                return dp[i][curr_sum+total]

            plus=dfs(i+1,curr_sum+nums[i])
            minus=dfs(i+1,curr_sum-nums[i])
            dp[i][curr_sum+total]=plus+minus
            return dp[i][curr_sum+total]

        return dfs(0,0)