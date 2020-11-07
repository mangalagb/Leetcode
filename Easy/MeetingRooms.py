#Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

from collections import defaultdict, OrderedDict

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        timeline = defaultdict(int)
        for interval in intervals:
            timeline[interval[0]] += 1
            timeline[interval[1]] -= 1

        #Sort by keys
        sorted_timeline = OrderedDict(sorted(timeline.items()))

        current_room = 0
        for value in sorted_timeline.values():
            current_room += value

            # current room > 1 means he nneds to be in 2 rooms simultaneously
            if current_room > 1:
                return False
        return True

my_sol = Solution()

intervals = [[0,30],[5,10],[15,20]]
print(my_sol.canAttendMeetings(intervals)) #False

intervals = [[7,10],[2,4]]
print(my_sol.canAttendMeetings(intervals)) #True
