# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n=len(s)
#         dp=[[False]*n for _ in range(n)]
#         max_len=0
#         left=0
#         right=0

#         for l in range(1,n+1):
#             for i in range(n+1-l):
#                 j=i+l-1

#                 if i==j:
#                     dp[i][j]=True
#                 elif i+1==j:
#                     dp[i][j]= (s[i]==s[j])
#                 else:
#                     dp[i][j]= (s[i]==s[j] and dp[i+1][j-1])
                
#                 if dp[i][j]==True:
#                     if abs(j-i+1)>max_len:
#                         max_len=abs(j-i+1)
#                         left=i
#                         right=j
        
#         return s[left:right+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)

        max_len,left,right=0,0,0
        def check(i,j):
            nonlocal max_len, left, right
            while i>=0 and j<n and s[i]==s[j]:
                if(max_len<j-i+1):
                    max_len=j-i+1
                    left=i
                    right=j
                i-=1
                j+=1
        
        for i in range(n):
            check(i,i)
            check(i,i+1)
        
        return s[left:right+1]
