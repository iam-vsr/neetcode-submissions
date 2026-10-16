class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            
            res=f(x*x,n//2)
            return x*res if n%2 else res

        res=f(x,abs(n))
        return res if n>=0 else 1/res