# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0

        #Sort intervals
        rooms = []

        for interval in intervals:
            temp = [i for i in range(interval.start, interval.end)]
            rooms.append(temp)
        rooms = sorted(rooms)

        count = 1
        result = [rooms[0]]
        for i in range(1, len(rooms)):
            current_room = rooms[i]

            flag = True
            for result_room in result:
                if not set(current_room).isdisjoint(result_room):
                    flag = flag and True
                else:
                    flag = False

            if flag:
                count += 1

            result.append(current_room)
        return count










my_sol = Solution()

# intervals = [Interval(0,30), Interval(15,20), Interval(5,10)]
# print(my_sol.minMeetingRooms(intervals))
#
# intervals = [Interval(7,10), Interval(2,4)]
# print(my_sol.minMeetingRooms(intervals))
#
# intervals = [Interval(9,10), Interval(4,9), Interval(4,17)]
# print(my_sol.minMeetingRooms(intervals))

intervals = [Interval(1,5), Interval(8,12), Interval(9,13)]
print(my_sol.minMeetingRooms(intervals))

# intervals = [Interval(1,5), Interval(8,9), Interval(8,9)]
# print(my_sol.minMeetingRooms(intervals))


