class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        maxw=0

        while l<r:
            w=min(h[l],h[r])*(r-l)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
            maxw=max(maxw,w)
        return maxw
