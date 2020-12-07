# Given an array arr.  You can choose a set of integers and remove all the occurrences
# of these integers in the array.
#
# Return the minimum size of the set so that at least half of the integers of the array are removed.
import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_dict = {}
        length_of_half_the_array = len(arr)//2
        length_of_array = len(arr)

        for num in arr:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1

        nums_frequency = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

        count = 0
        number_of_deletions = 0
        for values in nums_frequency:
            value = values[1]
            count += value
            number_of_deletions += 1

            if length_of_array - count <= length_of_half_the_array:
                break

        return number_of_deletions


my_sol = Solution()

arr = [3,3,3,3,5,5,5,2,2,7]
print(my_sol.minSetSize(arr))

arr = [7,7,7,7,7,7]
print(my_sol.minSetSize(arr))

arr = [1,9]
print(my_sol.minSetSize(arr))

arr = [1000,1000,3,7]
print(my_sol.minSetSize(arr))

arr = [1,2,3,4,5,6,7,8,9,10]
print(my_sol.minSetSize(arr))
