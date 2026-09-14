class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        
        t=0
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        
        while fresh>0 and queue:

            for _ in range(len(queue)):
                r,c=queue.popleft()
                
                for dr,dc in dirs:
                    nr=r+dr
                    nc=c+dc
                    
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        queue.append((nr,nc))
            t+=1
        
        return t if fresh==0 else -1

