from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i==len(s):
                return 1
            if i>len(s):
                return 0
            
            if s[i]!='0':
                if i+1<len(s) and '10'<=s[i:i+2]<='26':
                    return dfs(i+1)+dfs(i+2)
                else:
                    return dfs(i+1)
            else:
                return 0
        
        return dfs(0)
            