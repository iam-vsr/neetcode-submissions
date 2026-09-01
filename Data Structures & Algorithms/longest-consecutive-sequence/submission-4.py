class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        has=set(nums)
        ans=0

        for num in nums:
            if num-1 not in has:
                cons=1
                while num+cons in has:
                    cons+=1
                ans=max(ans,cons)
        
        return ans