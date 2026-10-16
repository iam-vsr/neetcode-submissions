class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        for i in range(1,len(nums)+1):
            x=x^i
        
        y=0
        for num in nums:
            y=y^num
        
        return x^y
