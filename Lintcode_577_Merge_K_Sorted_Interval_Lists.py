"""
Input: [
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
Output: [(1,3),(4,8),(9,10)]

Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []
        tmp = []
        results = []
        
        for i in intervals:
            for interval in i:
                tmp.append(interval)

        tmp = sorted(tmp, key=lambda x: x.start)

        for interval in tmp:
            if results and interval.start <= results[-1].end:
                results[-1].end = max(interval.end, results[-1].end)
            else:
                results.append(interval)

        return results