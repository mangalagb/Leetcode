# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.
from copy import deepcopy


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

    def twoSumWithoutDict(self, nums, target):
        if not nums:
            return []

        numbers = nums
        numbers = sorted(numbers)
        for i in range(0, len(numbers)):
            current = numbers[i]
            complement = target - current

            complement_number = self.binary_search(numbers, complement, i)
            if complement_number != -1:
                complement_index = nums.index(complement_number)
                original_index = nums.index(current)
                return [original_index, complement_index]

    def binary_search(self, nums, target, original_index):
        i = 0
        j = len(nums)-1

        while i <= j:
            mid = (i + j)//2
            mid_element = nums[mid]

            if mid_element == target:
                if mid != original_index:
                    return mid_element
                else:
                    i += 1
            elif target < mid_element:
                j = mid -1
            elif target > mid_element:
                i = mid + 1
        return -1



my_sol = Solution()

numbers = [2,7,11,15]
target = 9
# print(my_sol.twoSum(numbers, target))#[0, 1]
print(my_sol.twoSumWithoutDict(numbers, target))#[0, 1]

numbers = [3,2,4]
target = 6
print(my_sol.twoSumWithoutDict(numbers, target))#[1, 2]
