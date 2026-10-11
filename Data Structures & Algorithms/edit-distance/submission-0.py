class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[[None]*(n+1) for _ in range(m+1)]

        def f(m,n):
            if m==0:
                return n
            if n==0:
                return m
            
            if dp[m][n]!=None:
                return dp[m][n]

            if s[m-1]==t[n-1]:
                dp[m][n]= f(m-1,n-1)
            else:
                dp[m][n]=1+min(f(m-1,n),f(m-1,n-1),f(m,n-1)) 
                #del, replace, insert
            return dp[m][n]

        return f(m,n)