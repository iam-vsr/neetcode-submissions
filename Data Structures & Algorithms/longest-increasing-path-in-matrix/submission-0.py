from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        # dp=[[0]*n for _ in range(m)]
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        
        @lru_cache(None)
        def dfs(r,c):
            # if dp[r][c]!=0:
            #     return dp[r][c]
            max_len=1
   
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    max_len=max(max_len,1+dfs(nr,nc))
            # dp[r][c]=max_len
            # return dp[r][c]
            return max_len
        
        ans=0
        for i in range(m):
            for j in range(n):
                ans=max(ans,dfs(i,j))  
        return ans
