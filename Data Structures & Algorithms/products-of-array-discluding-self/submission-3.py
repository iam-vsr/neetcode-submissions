class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        for num in nums:
            if num==0:
                zeros+=1
        
        if zeros>1:
            return [0]*len(nums)

        x1=1
        x2=1
        for num in nums:
            if num!=0:
                x1=x1*num
            else:
                x2=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=x1
            else:
                nums[i]=(x1*x2)//nums[i]
        
        return nums