from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dfs(r,c):
            if r==m-1 and c==n-1:
                return 1
            if r>m-1 or c>n-1:
                return 0
            
            return (dfs(r+1,c) + dfs(r,c+1))
        
        return dfs(0,0)