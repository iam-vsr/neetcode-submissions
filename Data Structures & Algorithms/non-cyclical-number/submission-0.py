class Solution:
    def isHappy(self, n: int) -> bool:
        def f(n):
            ans=0
            while n:
                d=n%10
                ans+=(d**2)
                n=n//10
            return ans
        
        visited=set()
        while n not in visited:
            visited.add(n)
            n=f(n)
            if n==1:
                return True
        return False