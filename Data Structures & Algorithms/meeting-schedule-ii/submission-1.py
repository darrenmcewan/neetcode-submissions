"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = defaultdict(int)

        for i in intervals:
            meetings[i.start] += 1
            meetings[i.end] -= 1

        prev = 0
        res = 0

        for i in sorted(meetings.keys()):
            prev+=meetings[i]
            res = max(res,prev)
        return res


        
