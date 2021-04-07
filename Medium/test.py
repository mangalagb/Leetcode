#Given an integer array sorted in ascending order, write a function
# to search target in nums.  If target exists, then return its index,
# otherwise return -1. However, the array size is unknown to you. You
# may only access the array using an ArrayReader interface, where
# ArrayReader.get(k) returns the element of the array at index k (0-indexed).
#
# You may assume all integers in the array are less than 10000, and
# if you access the array out of bounds, ArrayReader.get will return 2147483647.
#

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """

class ArrayReader(object):
    def __init__(self, nums):
        self.nums = nums

    def get(self, index):
        length_of_nums = len(self.nums)

        if index >= length_of_nums:
            return 2147483647
        else:
            return self.nums[index]

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low, high = self.find_high(reader, target)
        result = self.do_binary_search(low, high, reader, target)
        return result

    def find_high(self, reader, target):
        low = 0
        high = 1

        while reader.get(high) < target:
            low = high
            high *= 2
        return low, high

    def do_binary_search(self, low, high, reader, target):
        while low <= high:
            mid = low + (high - low)//2
            mid_element = reader.get(mid)

            if mid_element == target:
                return mid
            elif mid_element > target:
                high = mid - 1
            elif mid_element < target:
                low = mid + 1
        return -1


my_sol = Solution()

array = [-1,0,3,5,9,12]
my_array_reader = ArrayReader(array)
target = 9
print(my_sol.search(my_array_reader, target)) #4

array = [-1,0,3,5,9,12]
my_array_reader = ArrayReader(array)
target = 2
print(my_sol.search(my_array_reader, target)) #-1

array = [2,5]
my_array_reader = ArrayReader(array)
target = 2
print(my_sol.search(my_array_reader, target)) #0

array = [-1,0,3,5,9,12]
my_array_reader = ArrayReader(array)
target = 12
print(my_sol.search(my_array_reader, target)) #5
