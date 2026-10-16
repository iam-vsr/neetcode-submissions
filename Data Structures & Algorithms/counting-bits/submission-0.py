class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def number_of_set_bits(n):
            c=0
            while n!=0:
                n=n&(n-1)
                c+=1
            return c
        
        ans=[]
        for i in range(n+1):
            ans.append(number_of_set_bits(i))
        return ans