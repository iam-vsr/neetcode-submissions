class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxl=0
        u=set()
        while r<len(s):
            if s[r] not in u:
                u.add(s[r])
                maxl=max(maxl,r-l+1)
                r+=1
            else:
                l+=1
                r=l
                u.clear()
        return maxl

