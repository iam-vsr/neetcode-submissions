class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>=nums2[j]:
                arr.append(nums2[j])
                j+=1
            elif nums1[i]<nums2[j]:
                arr.append(nums1[i])
                i+=1
        
        while i<len(nums1):
            arr.append(nums1[i])
            i+=1
        while j<len(nums2):
            arr.append(nums2[j])
            j+=1
        
        l=0
        r=len(nums1)+len(nums2)

        if r%2!=0:
            return arr[((l+r-1)//2)]
        
        return (arr[(l+r-1)//2]+arr[((l+r-1)//2)+1])/2.0