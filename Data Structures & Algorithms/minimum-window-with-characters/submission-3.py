# #Brute force
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         hast=Counter(t)
#         l=0
#         r=len(t)-1
#         ans=""

#         while r<(len(s)):
#             hass=Counter(s[l:r+1])
#             if all(k in hass and hass[k] >= v for k, v in hast.items()):
#                 if len(ans)==0 or len(ans)>(r-l+1):
#                     ans=s[l:r+1]
#                 l+=1
#             else:
#                 r+=1
        
#         return ans
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t=Counter(t)

        required=len(hash_t)
        formed=0

        l,r=0,0

        hash_window=defaultdict(int)
        ans=(float('inf'),None,None)


        while r<len(s):
            char=s[r]
            hash_window[char]+=1

            if char in hash_t and hash_window[char]==hash_t[char]:
                formed+=1
            
            while l<=r and formed==required:
                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                
                hash_window[s[l]]-=1
                if s[l] in hash_t and hash_window[s[l]]<hash_t[s[l]]:
                    formed-=1
                l+=1
            r+=1
        
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

        
        
