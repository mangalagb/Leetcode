# Given an array of integers nums, write a method that returns the
# "pivot" index of this array.
#
# We define the pivot index as the index where the sum of the numbers to
# the left of the index is equal to the sum of the numbers to the right
# of the index.
#
# If no such index exists, we should return -1. If there are multiple
# pivot indexes, you should return the left-most pivot index.


class Solution:

    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)

        for i in range(0, len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

nums = [1, 7, 3, 6, 5, 6]
#nums = [1, 2, 3]
print(nums)

sol = Solution()
print(sol.pivotIndex(nums))