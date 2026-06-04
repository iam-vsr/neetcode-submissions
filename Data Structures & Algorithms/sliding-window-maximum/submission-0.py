class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,r = 0,k-1
        maxe=-1001
        ans=[]

        while (r<len(nums)):
            for i in range(l,r+1):
                maxe=max(maxe,nums[i])
            ans.append(maxe)
            r+=1
            l+=1
            maxe=-1001
        return ans