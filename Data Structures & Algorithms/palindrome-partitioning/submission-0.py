class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def is_palindrome(s):
            if s==s[::-1]:
                return True
            return False

        def dfs(i,path):
            if i>=len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                if is_palindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
        
        dfs(0,[])
        return res