class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for u,v,cost in flights:
            adj[u].append((v,cost))

        price=[float('inf')]*n
        price[src]=0
        q=deque([(0,src,0)])

        while q:
            edges,node,cost=q.popleft()
            if edges<k+1:
                for ne,c in adj[node]:
                    if cost+c<price[ne]:
                        price[ne]=cost+c
                        q.append((edges+1,ne,cost+c))
        
        return -1 if price[dst]==float('inf') else price[dst]
