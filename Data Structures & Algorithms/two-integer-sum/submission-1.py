class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        
        for i in range(len(nums)):
            if target-nums[i] in has:
                x=i
                y=has[target-nums[i]]
                break
            else:
                has[nums[i]]=i
        
        return sorted([x,y])
