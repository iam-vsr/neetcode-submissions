class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)+len(nums2)
        c=n//2

        a,b=nums1,nums2
        if len(a)>len(b):
            a,b=b,a
        
        l=0
        r=len(a)-1

        while True:
            i=(l+r)//2
            j=c-i-2

            al=a[i] if i>=0 else float('-inf')
            ar=a[i+1] if i+1<len(a) else float('inf')
            bl=b[j] if j>=0 else float('-inf')
            br=b[j+1] if j+1<len(b) else float('inf')

            if al<=br and bl<=ar:
                if n%2!=0:
                    return min(ar,br)
                return (max(al,bl)+min(ar,br))/2   
            elif al>br:
                r=i-1
            else:
                l=i+1
        return 0.0     