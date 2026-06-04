class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeroes=0
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeroes+=1
        ans=[]
        if zeroes>1:
            return [0]*len(nums)

        for i in range(len(nums)):
            if nums[i]==0:
                ans.append(prod)
            else:
                if zeroes>0:
                    ans.append(0)
                else:
                    ans.append(prod//nums[i])
        return ans