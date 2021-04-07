# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.

#The idea behind this method is that the correct position of the minimum element
# in the unsorted subarray helps to determine the required left boundary.
# Similarly, the correct position of the maximum element in the unsorted subarray
# helps to determine the required right boundary.
#
# Thus, firstly we need to determine when the correctly sorted array goes wrong.
# We keep a track of this by observing rising slope starting from the beginning
# of the array. Whenever the slope falls, we know that the unsorted array has
# surely started. Thus, now we determine the minimum element found till the
# end of the array nums, given by min.
#
# Similarly, we scan the array nums in the reverse order and when the
# slope becomes rising instead of falling, we start looking for the maximum
# element till we reach the beginning of the array, given by max.
#
# Then, we traverse over nums and determine the correct
# position of min and max by comparing these elements with the other
# array elements. e.g. To determine the correct position of min, we know
# the initial portion of nums is already sorted. Thus, we need to find
# the first element which is just larger than min. Similarly, for max's
# position, we need to find the first element which is just smaller than max
# searching in nums backwards.
import sys


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_array = len(nums)
        if length_of_array == 0 or length_of_array == 1:
            return 0

        #Find the min num in the unsorted subarray
        min_num = sys.maxsize
        for j in range(1, len(nums)):
            if nums[j-1] > nums[j]:
                min_num = min(min_num, nums[j])

        # Find the max num in the unsorted subarray
        max_num = sys.maxsize * -1
        for j in range(len(nums)-2, -1, -1):
            if nums[j] > nums[j+1]:
                max_num = max(max_num, nums[j])

        #Special case : If array is already sorted
        if min_num == sys.maxsize and max_num == -1*sys.maxsize:
            return 0

        #Find where the min element in the unsorted array should go
        # aka find begin
        begin = 0
        for j in range(0, len(nums)):
            current = nums[j]
            if current > min_num:
                begin = j
                break

        # Find where the max element in the unsorted array should go
        # aka find bend
        end = len(nums) - 1
        for j in range(len(nums)-1, -1, -1):
            current = nums[j]
            if current < max_num:
                end = j
                break

        result = end - begin + 1
        return result

my_sol = Solution()

nums = [2, 6, 4, 8, 10, 9, 15]
print(my_sol.findUnsortedSubarray(nums)) #5

nums = [1,2,4,5,3]
print(my_sol.findUnsortedSubarray(nums)) #3

nums = [2,1]
print(my_sol.findUnsortedSubarray(nums)) #2

nums = [5,4,3,2,1]
print(my_sol.findUnsortedSubarray(nums)) #5

nums = [1,3,2,2,2]
print(my_sol.findUnsortedSubarray(nums)) #4

nums = [2,1,1,1,1]
print(my_sol.findUnsortedSubarray(nums)) #5

nums = [1,3,5,4,2]
print(my_sol.findUnsortedSubarray(nums)) #4

nums = [1,2,3,4]
print(my_sol.findUnsortedSubarray(nums)) #0
