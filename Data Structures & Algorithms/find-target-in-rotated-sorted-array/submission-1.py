class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while(l<=r):
            m=r-(r-l)//2

            if nums[m]==target:
                return m

            if(nums[m]>=nums[l]): #left part sorted
                if target>nums[m] or target<nums[l]:
                    l=m+1
                else:
                    r=m-1
                
            else: #right part sorted
                if target<nums[m] or target>nums[r]:
                    r=m-1
                else:
                    l=m+1
            
        return -1



