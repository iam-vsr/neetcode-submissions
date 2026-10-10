class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        visited=[False]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for ne in adj[node]:
                if not visited[ne]:
                    visited[ne]=True
                    dfs(ne)
        
        ans=0
        for i in range(n):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                ans+=1
        
        return ans