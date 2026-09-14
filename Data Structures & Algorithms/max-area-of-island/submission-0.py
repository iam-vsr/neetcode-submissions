class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])

        def dfs(r,c):
            if r>row-1 or c>col-1 or r<0 or c<0 or grid[r][c]==0:
                return 0
            
            grid[r][c]=0

            return 1+(dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        
        max_area=0

        for r in range(row):
            for c in range(col):
                max_area=max(max_area,dfs(r,c))
        return max_area