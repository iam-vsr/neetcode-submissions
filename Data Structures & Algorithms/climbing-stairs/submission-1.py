class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[None]*(n+1)
        def f(i):
            if i>n:
                return 0
            if i==n:
                return 1
            
            if dp[i]!=None:
                return dp[i]
            
            dp[i]=f(i+1)+f(i+2)
            return dp[i]
        
        return f(0)