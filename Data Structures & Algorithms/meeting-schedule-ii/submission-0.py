"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, i: List[Interval]) -> int:
        i.sort(key=lambda x:x.start)
        min_heap=[]

        for interval in i:
            if min_heap and min_heap[0]<=interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        
        return len(min_heap)
