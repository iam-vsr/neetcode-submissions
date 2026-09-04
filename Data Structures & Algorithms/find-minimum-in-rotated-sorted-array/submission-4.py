class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        ans=float('inf')

        while(l<=r):
            m=r-(r-l)//2 # dont use r-(r-l)//2
            if nums[m]>=nums[l]:
                #left part is sorted
                ans=min(ans,nums[l])
                l=m+1
            else:
                #right part is sorted
                ans=min(ans,nums[m])
                r=m-1

        return ans
