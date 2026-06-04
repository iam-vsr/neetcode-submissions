class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        l=0
        r=n1-1
        while r<n2:
            f1 =  Counter(s2[l:r+1])
            if f1==f:
                return True

            r+=1
            l+=1
        return False
