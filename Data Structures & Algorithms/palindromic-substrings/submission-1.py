# from functools import lru_cache
# class Solution:
#     def countSubstrings(self, s: str) -> int:
        
#         @lru_cache(None)
#         def check(i,j):
#             if i>j:
#                 return True
#             if s[i]==s[j]:
#                 return check(i+1,j-1)
#             return False
        
#         c=0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 if check(i,j):
#                     c+=1
        
#         return c

#bottom-up approach
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        t=[[False]*n for _ in range(n)]
        c=0

        for l in range(1,n+1):
            for i in range(n+1-l):
                j=i+l-1

                if i==j:
                    t[i][j]=True
                elif i+1==j:
                    t[i][j]=(s[i]==s[j])
                else:
                    t[i][j]=(s[i]==s[j] and t[i+1][j-1])
                
                if t[i][j]==True:
                    c+=1
        
        return c