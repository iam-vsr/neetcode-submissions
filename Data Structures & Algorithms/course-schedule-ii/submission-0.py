class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)

            for ne in adj[node]:
                indegree[ne]-=1

                if indegree[ne]==0:
                    queue.append(ne)
        
        return topo if len(topo)==n else []