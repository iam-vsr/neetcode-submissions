class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[] #min heap
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            dfo=math.sqrt(x**2+y**2) #distance from origin
            heapq.heappush(heap,(dfo,[x,y])) #push(priority, data)
        
        res=[]
        while k>0:
            dof, data=heapq.heappop(heap)
            res.append(data)
            k-=1
            
        return res
        