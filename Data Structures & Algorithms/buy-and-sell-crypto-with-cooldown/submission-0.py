class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[None]*2 for _ in range(n+1)]

        def f(i,status):
            if i>=n:
                return 0
            
            if dp[i][status]!=None:
                return dp[i][status]
            if status==0:
                profit=max(-prices[i]+f(i+1,1),f(i+1,0))
            else:
                profit=max(prices[i]+f(i+2,0),f(i+1,1))
            
            dp[i][status]=profit
            return profit

        return f(0,0)