class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp=[[None]*(n+1) for _ in range(m+1)]
        
        def f(m,n):
            if n==0 or m==0:
                return 0
            if dp[m][n]!=None:
                return dp[m][n]

            if text1[m-1]==text2[n-1]:
                dp[m][n]= 1+f(m-1,n-1)
            else:
                dp[m][n]= max(f(m,n-1),f(m-1,n))
            return dp[m][n]

        return f(len(text1),len(text2))