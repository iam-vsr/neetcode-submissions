class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        pos_diag=set()
        neg_diag=set()
        board=[["."]*n for _ in range(n)]
        ans=[]

        def not_valid(row, col):
            return(col in cols or (row+col) in pos_diag or (row-col) in neg_diag)
        
        def dfs(r):
            if r==n:
                ans.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if not_valid(r,c)==0:
                    board[r][c]='Q'
                    cols.add(c)
                    pos_diag.add(r+c)
                    neg_diag.add(r-c)

                    dfs(r+1)

                    board[r][c]="."
                    cols.remove(c)
                    pos_diag.remove(r+c)
                    neg_diag.remove(r-c)
        
        dfs(0)
        return ans

