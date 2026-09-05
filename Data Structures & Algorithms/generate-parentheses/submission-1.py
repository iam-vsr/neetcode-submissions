class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        
        def dfs(opening_brackets, closing_brackets, path):
            if len(path)==2*n:
                ans.append(path[:])
                return
            
            if opening_brackets>closing_brackets:
                dfs(opening_brackets, closing_brackets+1, path+")")

            if opening_brackets<n:
                dfs(opening_brackets+1, closing_brackets, path+"(")
        
        dfs(0,0,"")
        return ans
            