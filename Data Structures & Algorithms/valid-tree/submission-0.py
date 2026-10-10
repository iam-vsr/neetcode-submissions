class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited=set()
        queue=deque([(0,-1)])
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for ne in adj[node]:
                if ne not in visited:
                    visited.add(ne)
                    queue.append((ne,node))
                elif ne!=parent:
                    return False #cycle detected
        
        return len(visited)==n #all are visited in a single component