from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)          # required chars
        required = len(need)       # number of unique chars needed
        
        l, r = 0, 0
        window = {}
        formed = 0                 # how many unique chars satisfied
        ans = (float("inf"), None, None)  # (length, left, right)
        
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            # Contract window while valid
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # pop from left
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

        