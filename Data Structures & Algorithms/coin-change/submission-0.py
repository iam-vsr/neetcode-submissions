class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[None]*(amount+1) for _ in range(n+1)]

        def f(n,w):
            if w==0:
                return 0
            if n==0:
                return float('inf')
            
            if dp[n][w]!=None:
                return dp[n][w]

            if coins[n-1]<=w:
                dp[n][w]=min(f(n-1,w),1+f(n,w-coins[n-1]))
            else:
                dp[n][w]=f(n-1,w)
            return dp[n][w]
        ans=f(n,amount)
        return ans if ans!=float('inf') else -1