class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has={}

        for i in s:
            if i in has:
                has[i]+=1
            else:
                has[i]=1
        
        for j in t:
            if j in has:
                has[j]-=1
            else:
                has[j]=-1
        
        for key in has:
            if has[key]!=0:
                return False
        
        return True