class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has1=defaultdict(int)
        for ch in s1:
            has1[ch]+=1
        
        l=0
        r=len(s1)-1
        n=len(s2)

        while r<n:
            has2=defaultdict(int)
            for i in range(l,r+1):
                has2[s2[i]]+=1
            
            if has2==has1:
                return True
            
            else:
                l+=1
                r+=1
        
        return False

            

