class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=-1

        while l<=r:
            mid= (l+r)//2
            t=0
            for i in range(len(piles)):
                t+= math.ceil(piles[i]/(mid*1.0))
            if t>h:
                l=mid+1
                
            elif t<=h:
                r=mid-1
                ans=mid
            

        return ans
            