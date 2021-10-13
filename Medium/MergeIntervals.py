#Given a collection of intervals, merge all overlapping intervals.

#SOLUTION
#https://www.youtube.com/watch?v=qKczfGUrFY4

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals)

        stack = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]
            current_begin = current_interval[0]
            current_end = current_interval[1]

            top = stack[-1]
            top_begin = top[0]
            top_end = top[1]

            if current_begin <= top_end:
                top_end = max(top_end, current_end)
                stack[-1] = [top_begin, top_end]
            else:
                stack.append([current_begin, current_end])
        return stack


my_sol = Solution()

intervals = [[1,3], [2,6], [8,10], [15,18]]
print(my_sol.merge(intervals)) #[[1, 6], [8, 10], [15, 18]]

intervals = [[1,4],[4,5]]
print(my_sol.merge(intervals)) #[[1,5]]

intervals = [[1,4],[1,4]]
print(my_sol.merge(intervals)) #[[1,4]]

intervals = [[1,4],[0,0]]
print(my_sol.merge(intervals)) # [[1,4],[0,0]]
