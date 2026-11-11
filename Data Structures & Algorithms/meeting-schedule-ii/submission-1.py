"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: (interval.start, -interval.end))
        pq = []
        for interval in intervals:
            if pq and pq[0] <= interval.start:
                heapq.heappop(pq)

            heapq.heappush(pq, interval.end)
        
        return len(pq)