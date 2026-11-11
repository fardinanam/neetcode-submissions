"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def isConflicting(self, a, b):
        return a.start < b.start < a.end \
            or a.start < b.end < a.end \
            or b.start < a.start < b.end \
            or b.start < a.end < b.end \
            or a.start == b.start and a.end == b.end

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if self.isConflicting(intervals[i], intervals[j]):
                    return False

        return True