class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs',
        '8':'tuv', '9':'wxyz'}
        ans=[]

        if digits=="":
            return ans

        def dfs(idx, path):
            if idx>=len(digits):
                ans.append(path)
                return

            for i in digits_map[digits[idx]]:
                dfs(idx+1,path+i)
        
        dfs(0,"")
        return ans