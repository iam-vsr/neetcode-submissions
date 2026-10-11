class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[None]*(m+1) for _ in range(n+1)]

        def f(n,m):
            if m==0:
                return 1
            if n==0:
                return 0
            
            if dp[n][m]!=None:
                return dp[n][m]

            if s[n-1]==t[m-1]:
                dp[n][m]= f(n-1,m-1)+f(n-1,m)
            else:
                dp[n][m]= f(n-1,m)
            return dp[n][m]
        
        return f(n,m)
