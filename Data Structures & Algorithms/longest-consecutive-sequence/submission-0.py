class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns=set(nums)
        longest=0

        for i in range(len(nums)):
            if nums[i]-1 not in ns:
                length=1

                while nums[i]+length in ns:
                    length+=1
                longest=max(longest,length)
        return longest