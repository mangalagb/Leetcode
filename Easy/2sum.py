# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.

class Solution(object):
    def twoSum(self, numbers, target):
        if not numbers:
            return []

        remaining_sums = {}

        for i in range(0, len(numbers)):
            num = numbers[i]
            remaining_num = target - num
            if remaining_num in remaining_sums:
                return [remaining_sums[remaining_num], i]
            else:
                remaining_sums[num] = i


my_sol = Solution()

numbers = [2,7,11,15]
target = 9
print(my_sol.twoSum(numbers, target))