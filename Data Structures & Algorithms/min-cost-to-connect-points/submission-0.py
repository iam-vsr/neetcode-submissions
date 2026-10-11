class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n

    def find(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return False
        
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        else:
            self.parent[pu]=pv
            self.rank[pv]+=1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        #create all possible connections and store in edges
        edges=[]

        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                man=abs(x2-x1)+abs(y2-y1)
                edges.append((i,j,man))
        edges.sort(key=lambda x:x[2]) #sort by manhattan distance
        mst_sum=0
        dsu=DSU(n)

        for u,v,w in edges:
            if dsu.find(u)!=dsu.find(v):
                mst_sum+=w
                dsu.union(u,v)
        
        return mst_sum




