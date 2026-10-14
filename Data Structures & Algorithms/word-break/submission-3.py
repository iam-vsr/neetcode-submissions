from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        words=set(wordDict)
        
        @lru_cache(None)
        def dfs(i):
            if i==n:
                return True
            if i>n:
                return False
            
            for j in range(i+1,n+1):
                if s[i:j] in words:
                    if dfs(j):
                        return True
            return False
        
        return dfs(0)