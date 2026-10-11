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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu=DSU(len(edges)+1) #+1 as nodes are numbered from 1 to n

        for u,v in edges:
            if not dsu.union(u,v):
                ans=[u,v]
        
        return ans
        