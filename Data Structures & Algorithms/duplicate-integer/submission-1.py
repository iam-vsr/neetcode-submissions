class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        f=Counter(nums)
        for i in f:
            if f[i]>1:
                return True
        return False