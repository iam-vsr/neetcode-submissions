class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(map(str,digits))
        x=int(s)
        x+=1

        s=str(x)
        ans=[int(c) for c in s]
        return ans