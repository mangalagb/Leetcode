#Given a collection of intervals, merge all overlapping intervals.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        #print(intervals)

        if not intervals:
            return []

        temp_intervals = []
        for interval in intervals:

            if interval.start == interval.end:
                temp_intervals.append([interval.start, interval.end])
            else:
                temp = [i for i in range(interval.start, interval.end+1)]
                temp_intervals.append(temp)

        intervals = sorted(temp_intervals)
        length_of_intervals = len(intervals)
        result = [intervals[0]]
        index_in_result = 0

        for k in range(1, length_of_intervals):
            nums = intervals[k]
            #print(nums)

            previous_interval = result[index_in_result]
            intersection = list(set(previous_interval).intersection(nums))

            if len(intersection) != 0:
                new_interval = []
                nums_length = len(nums) -1
                result_length = len(previous_interval) -1

                if nums[0] <= previous_interval[0]:
                    new_interval.insert(0, nums[0])
                else:
                    new_interval.insert(0, previous_interval[0])

                if nums[nums_length] >= previous_interval[result_length]:
                    new_interval.insert(1, nums[nums_length])
                else:
                    new_interval.insert(1, previous_interval[result_length])

                new_interval = [i for i in range(new_interval[0], new_interval[1] + 1)]
                result.insert(k-1, new_interval)
                result.remove(previous_interval)
                length_of_intervals -= 1

            else:
                result.append(nums)
                index_in_result += 1

        #print(result)

        temp_result = []
        for res in result:
            temp = Interval(res[0], res[len(res)-1])
            temp_result.append(temp)
        return temp_result


my_sol = Solution()


# intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
# print(my_sol.merge(intervals))
#
# intervals = [Interval(1,4), Interval(4,5)]
# print(my_sol.merge(intervals))
#
# intervals = [Interval(1,4), Interval(0,0)]
# print(my_sol.merge(intervals))
#
# intervals = [Interval(1,4), Interval(0,2), Interval(3,5)]
# print(my_sol.merge(intervals))

#[[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
intervals = [Interval(4,5), Interval(2,4), Interval(4,6), Interval(3,4), Interval(0,0), Interval(1,1),Interval(3,5), Interval(2,2)]
print(my_sol.merge(intervals))


