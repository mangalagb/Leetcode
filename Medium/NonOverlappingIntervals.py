# Given a collection of intervals, find the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        length_of_intervals = len(intervals)
        if length_of_intervals == 0 or length_of_intervals == 1:
            return 0

        sorted_intervals = sorted(intervals)
        result = []
        erasure = 0

        for interval in sorted_intervals:
            if not result:
                result.append(interval)
                continue

            previous = result[-1]
            previous_start = previous[0]
            previous_end = previous[1]

            next_start = interval[0]
            next_end = interval[1]

            if previous_end > next_start:
                new_start = min(previous_start, next_start)
                new_end = min(previous_end, next_end)
                result[-1] = [new_start, new_end]
                erasure += 1
            else:
                result.append(interval)
        return erasure



my_sol = Solution()

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(my_sol.eraseOverlapIntervals(intervals)) #1

intervals = [[1,2],[1,2],[1,2]]
print(my_sol.eraseOverlapIntervals(intervals)) #2

intervals = [[1,2],[2,3]]
print(my_sol.eraseOverlapIntervals(intervals)) #0

intervals = [[1,2]]
print(my_sol.eraseOverlapIntervals(intervals)) #0
