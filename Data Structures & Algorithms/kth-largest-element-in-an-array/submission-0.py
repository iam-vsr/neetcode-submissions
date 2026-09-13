class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heap=nums
        heapq.heapify(heap)
        s=n-k
        while s>0:
            heapq.heappop(heap)
            s-=1
        return heap[0]