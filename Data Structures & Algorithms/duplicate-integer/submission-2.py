class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has={}
        for i in nums:
            if i in has:
                has[i]+=1  
            else:
                has[i]=1
        
        for key in has:
            if has[key]>1:
                return True
        
        return False
