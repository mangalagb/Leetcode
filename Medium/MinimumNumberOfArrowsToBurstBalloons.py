# There are some spherical balloons spread in two-dimensional space. For each
# balloon, provided input is the start and end coordinates of the horizontal
# diameter. Since it's horizontal, y-coordinates don't matter, and hence the
# x-coordinates of start and end of the diameter suffice. The start is always
# smaller than the end.
#
# An arrow can be shot up exactly vertically from different points along the
# x-axis. A balloon with xstart and xend bursts by an arrow shot at x
# if xstart ≤ x ≤ xend. There is no limit to the number of arrows that
# can be shot. An arrow once shot keeps traveling up infinitely.
#
# Given an array points where points[i] = [xstart, xend], return the
# minimum number of arrows that must be shot to burst all balloons.
from collections import OrderedDict


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        sorted_points = sorted(points)
        result = []
        arrows = 1

        for point in sorted_points:
            if not result:
                result.append(point)
                continue

            previous = result[-1]
            previous_start = previous[0]
            previous_end = previous[1]

            next_start = point[0]
            next_end = point[1]

            if previous_end >= next_start:
                new_start = max(previous_start, next_start)
                new_end = min(previous_end, next_end)
                result[-1] = [new_start, new_end]
            else:
                arrows += 1
                result.append(point)
        return len(result)
my_sol = Solution()

points = [[10,16],[2,8],[1,6],[7,12]]
print(my_sol.findMinArrowShots(points))   #2

points = [[1,2],[3,4],[5,6],[7,8]]
print(my_sol.findMinArrowShots(points)) #4

points = [[1,2],[2,3],[3,4],[4,5]]
print(my_sol.findMinArrowShots(points)) #2

points = [[1,2]]
print(my_sol.findMinArrowShots(points)) #1

points = [[2, 3], [2, 3]]
print(my_sol.findMinArrowShots(points)) #1

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(my_sol.findMinArrowShots(points)) #2
