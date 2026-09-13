class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-s for s in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap)>1:
            first_max_ele=-heapq.heappop(max_heap)
            second_max_ele=-heapq.heappop(max_heap)
            
            if first_max_ele!=second_max_ele:
                heapq.heappush(max_heap, -(first_max_ele-second_max_ele))
            
        return -max_heap[0] if max_heap else 0
