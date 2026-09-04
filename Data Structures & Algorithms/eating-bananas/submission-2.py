import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=float('inf')

        while(l<=r):
            k=r-(r-l)//2
            t=0
            for i in range(len(piles)):
                t+=math.ceil(piles[i]/k)
            if t<=h:
                ans=min(ans,k)
                r=k-1
            else:
                l=k+1
        
        return ans





