class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        has=set()
        ans=0

        while r<len(s):
            while s[r] in has:
                has.remove(s[l])
                l+=1
        
            has.add(s[r])
            ans=max(ans,r-l+1)
            r+=1
        
        return ans

            