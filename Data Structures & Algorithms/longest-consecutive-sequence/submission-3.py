class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has=set(nums)
        ans=0

        for i in range(len(nums)):
            if nums[i]-1 not in has:
                cons=1
                while nums[i]+cons in has:
                    cons+=1
                
                ans=max(cons,ans)
        
        return ans
        