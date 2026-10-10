class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or board[r][c]!='O':
                return
            
            board[r][c]='cant'

            dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)
        
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='cant':
                    board[i][j]='O'
