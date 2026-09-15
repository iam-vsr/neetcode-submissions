class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        pacific, atlantic = False, False

        def dfs(r,c,num):
            nonlocal pacific, atlantic
            if r<0 or c<0:
                pacific=True
                return
            if r>=m or c>=n:
                atlantic=True
                return
            
            if (r,c) in visited:
                return
            if heights[r][c]>num:
                return
            
            num=heights[r][c]
            visited.add((r, c))

            dfs(r+1,c,num)
            dfs(r-1,c,num)
            dfs(r,c+1,num)
            dfs(r,c-1,num)
        
        ans=[]
        for i in range(m):
            for j in range(n):
                pacific, atlantic = False, False
                visited=set()
                dfs(i,j,heights[i][j])

                if pacific and atlantic:
                    ans.append([i,j])

        return ans
