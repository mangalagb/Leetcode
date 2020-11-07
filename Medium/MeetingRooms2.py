from collections import defaultdict, OrderedDict

class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0

        timeline = defaultdict(int)

        # For every start time add 1, end time -1
        for interval in intervals:
            timeline[interval[0]] += 1
            timeline[interval[1]] -= 1

        # Sort timeline based on start times
        sorted_timeline = OrderedDict(sorted(timeline.items()))

        current_room = 0
        max_room = 0
        for value in sorted_timeline.values():
            current_room += value
            max_room = max(max_room, current_room)
        return max_room


my_sol = Solution()

intervals = [[0, 30],[5, 10],[15, 20]]
print(my_sol.minMeetingRooms(intervals)) #2

intervals = [[7,10],[2,4]]
print(my_sol.minMeetingRooms(intervals)) #1
