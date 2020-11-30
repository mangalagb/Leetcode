#Given a collection of intervals, merge all overlapping intervals.
from collections import defaultdict, OrderedDict

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        timeline = defaultdict(int)

        # For every start time add 1, end time -1
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            timeline[start] += 1
            timeline[end] -= 1

        # Sort timeline based on start times
        sorted_timeline = OrderedDict(sorted(timeline.items()))

        start = 0
        count = 0
        result = []
        for key, value in sorted_timeline.items():
            if count == 0:
                start = key

            count += value
            if count == 0:
                result.append([start, key])
        return result




my_sol = Solution()

intervals = [[1,3], [2,6], [8,10], [15,18]]
print(my_sol.merge(intervals)) #[[1, 6], [8, 10], [15, 18]]
#
# intervals = [[1,4],[4,5]]
# print(my_sol.merge(intervals)) #[[1,5]]
#
# intervals = [[1,4],[1,4]]
# print(my_sol.merge(intervals)) #[[1,4]]
#
# intervals = [[1,4],[0,0]]
# print(my_sol.merge(intervals)) # [[1,4],[0,0]]
