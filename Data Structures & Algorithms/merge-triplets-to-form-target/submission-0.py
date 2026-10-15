class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n=len(triplets)
        res=[0,0,0]
        for x,y,z in triplets:
            if x>target[0] or y>target[1] or z>target[2]:
                continue
            else:
                res[0]=max(res[0],x)
                res[1]=max(res[1],y)
                res[2]=max(res[2],z)
        
        return res==target