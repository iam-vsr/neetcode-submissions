class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        max_len=0
        left=0
        right=0

        for l in range(1,n+1):
            for i in range(n+1-l):
                j=i+l-1

                if i==j:
                    dp[i][j]=True
                elif i+1==j:
                    dp[i][j]= (s[i]==s[j])
                else:
                    dp[i][j]= (s[i]==s[j] and dp[i+1][j-1])
                
                if dp[i][j]==True:
                    if abs(j-i+1)>max_len:
                        max_len=abs(j-i+1)
                        left=i
                        right=j
        
        return s[left:right+1]
