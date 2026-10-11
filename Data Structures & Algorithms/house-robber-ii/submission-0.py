class Solution:
    def rob(self, nums: List[int]) -> int:
        x=len(nums)
        if x==1:
            return nums[0]
            
        dp=[None]*x

        def f(i,n):
            if i>n-1:
                return 0
            if dp[i]!=None:
                return dp[i]
            dp[i]=max(f(i+1,n),f(i+2,n)+nums[i])
            return dp[i]
        
        c1=f(0,x-1)
        dp=[None]*x
        c2=f(1,x)
        return max(c1,c2)
        