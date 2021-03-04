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
        length_of_array = 10000
        result = self.do_binary_search(0, length_of_array, reader, target)
        return result

    def do_binary_search(self, low, high, reader, target):
        mid = low + (high-low)//2
        element = reader.get(mid)

        if element == 2147483647:
            high = mid
        elif element == target:
            return mid
        elif high == low:
            return -1
        elif element < reader.g:
            high = mid - 1
        elif element > target:
            low = mid + 1
        else:
            return -1

        return self.do_binary_search(low, high, reader, target)

my_sol = Solution()

# array = [-1,0,3,5,9,12]
# my_array_reader = ArrayReader(array)
# target = 9
# print(my_sol.search(my_array_reader, target)) #4

array = [-1,0,3,5,9,12]
my_array_reader = ArrayReader(array)
target = 2
print(my_sol.search(my_array_reader, target)) #-1
