# You are implementing a program to use as your calendar. We can
# add a new event if adding the event will not cause a double booking.
#
# A double booking happens when two events have some non-empty
# intersection (i.e., some moment is common to both events.).
#
# The event can be represented as a pair of integers start and
# end that represents a booking on the half-open interval
# [start, end), the range of real numbers x such that start <= x < end.
#
# Implement the MyCalendar class:
#
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event
# can be added to the calendar successfully without causing a
# double booking. Otherwise, return false and do not add the event to the calendar.

class MyCalendar(object):

    def __init__(self):
        self.dates = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.dates) == 0:
            self.dates.append([start, end])
            return True

        for i in range(len(self.dates)-1, -1, -1):
            current = self.dates[i]
            current_start = current[0]
            current_end = current[1]
            can_add = True

            if current_start <= start < current_end:
                return False

            #loop through other dates
            list1 = set(range(start, end))
            list2 = list(range(current_start, current_end+1))
            common = [item for item in list2 if item in list1]
            if len(common) == 0:
                continue
            else:
                can_add = True
                self.dates.append([start, end])
                return can_add






my_sol = MyCalendar()

# dates = [[10, 20], [15, 25], [20, 30]]
# for date in dates:
#     print(my_sol.book(date[0], date[1]))

dates = [[10, 20],[22, 30],[5,20]]
for date in dates:
    print(my_sol.book(date[0], date[1]))
