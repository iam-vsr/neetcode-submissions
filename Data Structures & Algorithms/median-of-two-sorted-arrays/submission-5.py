class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)+len(nums2)
        c1=n//2
        c2=(n//2)-1
        cnt=0
        i,j=0,0
        ac1,ac2=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>=nums2[j]:
                if cnt==c1:
                    ac1=nums2[j]
                if cnt==c2:
                    ac2=nums2[j]
                cnt+=1
                j+=1
            else:
                if cnt==c1:
                    ac1=nums1[i]
                if cnt==c2:
                    ac2=nums1[i]
                cnt+=1
                i+=1
        
        while i<len(nums1):
            if cnt==c1:
                ac1=nums1[i]
            if cnt==c2:
                ac2=nums1[i]
            cnt+=1    
            i+=1
        while j<len(nums2):
            if cnt==c1:
                ac1=nums2[j]
            if cnt==c2:
                ac2=nums2[j]
            cnt+=1
            j+=1
        

        if n%2!=0:
            return ac1
        
        return (ac1+ac2)/2