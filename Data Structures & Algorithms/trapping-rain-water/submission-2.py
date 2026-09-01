class Solution:
    def trap(self, h: List[int]) -> int:

        n=len(h)
        pref_max=[h[0]]*n
        suff_max=[h[n-1]]*n

        for i in range(1,n):
            pref_max[i]=max(pref_max[i-1],h[i])
        
        for i in range(n-2,-1,-1):
            suff_max[i]=max(suff_max[i+1],h[i])
        
        water=0
        for i in range(n):
            water+= min(suff_max[i],pref_max[i])-h[i]
        
        return water
