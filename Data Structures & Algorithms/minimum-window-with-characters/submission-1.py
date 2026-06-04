class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        required = len(need)
        window = {}
        l,r = 0,0
        formed = 0
        ans = (1001,None,None)

        while r<len(s):
            window[s[r]] = window.get(s[r],0)+1 #agr hai toh +1, agr nhi hai toh default value 0 dekr +1

            if s[r] in need and window[s[r]] == need[s[r]]:
                formed+=1
            #jab valid hojaye tb chhota krne pe dhyaan dein, lekin uske pehle answer save krlein
            while l<=r and formed == required:
                if r-l+1<ans[0]:
                    ans = (r-l+1,l,r)
                #ab ghataya jaye
                window[s[l]]-=1
                #yha check krke formed ko update krna pdega
                if s[l] in need and window[s[l]]<need[s[l]]:
                    formed-=1
                #ab l badha do
                l+=1
            r+=1
        return '' if ans[0]==1001 else s[ans[1]:ans[2]+1]




        
        