class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((v,t))

        src=k
        heap=[(0,src)]
        dist=[float('inf')]*(n+1)
        dist[src]=0

        while heap:
            t,node = heapq.heappop(heap)
            if t>dist[node]:
                continue
            
            for ne,dt in adj[node]:
                if dist[ne]>t+dt:
                    dist[ne]=t+dt
                    heapq.heappush(heap,(dist[ne],ne))
        
        if max(dist[1:])==float('inf'):
            return -1
        return max(dist[1:])