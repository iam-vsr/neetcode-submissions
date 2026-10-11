class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[None]*(amount+1) for _ in range(n+1)]

        def f(n,s):
            if s==0:
                return 1
            if n==0:
                return 0
            if dp[n][s]!=None:
                return dp[n][s]

            if coins[n-1]<=s:
                dp[n][s]=f(n-1,s)+f(n,s-coins[n-1])
            else:
                dp[n][s]=f(n-1,s)
            return dp[n][s]
        
        return f(n,amount)