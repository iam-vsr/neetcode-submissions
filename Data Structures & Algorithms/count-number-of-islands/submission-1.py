class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>rows-1 or c>cols-1 or grid[r][c]=='0':
                return
            grid[r][c]='0'
            
            dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)
        
        island=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island+=1
                    dfs(r,c)
        return island

