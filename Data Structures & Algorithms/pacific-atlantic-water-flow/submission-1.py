#multi-source solution
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c,num,visited):
            if r<0 or c<0:
                return
            if r>=m or c>=n:
                return
            
            if (r,c) in visited:
                return
            if heights[r][c]<num:
                return
            
            num=heights[r][c]
            visited.add((r, c))

            dfs(r+1,c,num,visited)
            dfs(r-1,c,num,visited)
            dfs(r,c+1,num,visited)
            dfs(r,c-1,num,visited)
        
        for r in range(m):
            dfs(r,0,heights[r][0],pacific)
            dfs(r,n-1,heights[r][n-1],atlantic)
        
        for c in range(n):
            dfs(0,c,heights[0][c],pacific)
            dfs(m-1,c,heights[m-1][c],atlantic)


        ans=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    ans.append([i,j])

        return ans
