class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)

        vis=[0]*n
        path_vis=[0]*n
        #dfs for cycle detection
        def dfs(node):
            vis[node]=1
            path_vis[node]=1

            for ne in adj[node]:
                if not vis[ne]:
                    if dfs(ne):
                        return True
                elif path_vis[ne]:
                    return True
            path_vis[node]=0
            return False

        for i in range(n):
            if not vis[i]:
                if dfs(i):
                    return False #cycle detected then return false
        return True

        