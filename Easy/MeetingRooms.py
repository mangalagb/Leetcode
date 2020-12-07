#Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

from collections import defaultdict, OrderedDict

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])

        sorted_start = sorted(start)
        sorted_end = sorted(end)

        j = 0
        rooms = 0
        for i in range(0, len(sorted_start)):
            meeting_start = sorted_start[i]
            meeting_end = sorted_end[j]

            if meeting_start < meeting_end:
                rooms += 1
                if rooms > 1:
                    return False
            else:
                j += 1
        return True


my_sol = Solution()

intervals = [[0,30],[5,10],[15,20]]
print(my_sol.canAttendMeetings(intervals)) #False

intervals = [[7,10],[2,4]]
print(my_sol.canAttendMeetings(intervals)) #True
