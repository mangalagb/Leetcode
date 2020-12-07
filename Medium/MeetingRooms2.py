# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.

#https://leetcode.com/problems/meeting-rooms-ii/discuss/67855/Explanation-of-%22Super-Easy-Java-Solution-Beats-98.8%22-from-%40pinkfloyda

#SOLUTION
#Meetings that started which haven’t ended yet have to be put into different meeting rooms,
# and the number of rooms needed is the number of such meetings

class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0

        meeting_start = []
        meeting_end = []

        # Store start and end times
        for interval in intervals:
            meeting_start.append(interval[0])
            meeting_end.append(interval[1])

        start = sorted(meeting_start)
        end = sorted(meeting_end)

        rooms = 0
        j = 0

        for i in range(0, len(start)):
            meeting_start = start[i]
            meeting_end = end[j]

            #Meetins are starting before the first one has ended
            if meeting_start < meeting_end:
                rooms += 1

            else:
                # 1 room becomes free
                # But a new meeting has started. So 1 more room
                # No need to update rooms here

                #This also handles the case of metting ending and another one
                # starting at the same time


                #update end time for next meeting comparison
                j += 1

        return rooms




my_sol = Solution()

intervals = [[9,14],[5,6],[3,5],[12,19]]
print(my_sol.minMeetingRooms(intervals)) #2

# intervals = [[0, 30],[5, 10],[15, 20]]
# print(my_sol.minMeetingRooms(intervals)) #2
#
# intervals = [[7,10],[2,4]]
# print(my_sol.minMeetingRooms(intervals)) #1
