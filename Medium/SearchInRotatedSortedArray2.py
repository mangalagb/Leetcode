
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        #Find rotation pivot
        pivot = self.find_pivot(nums, 0, len(nums) - 1)

        #Binary Search
        return self.binary_search(nums, pivot, target)

    def binary_search(self, nums, pivot, target):
        length = len(nums)
        low = 0
        high = length -1

        while low <= high:
            mid = low + (high - low)//2
            mid_pivot = (mid + pivot)%length

            if nums[mid_pivot] > target:
                high = mid -1
            elif nums[mid_pivot] < target:
                low = mid + 1
            elif nums[mid_pivot] == target:
                return True
        return False

    def find_pivot(self, nums, low, high):
        pivot = -1
        direction = None
        mid = low + (high-low)//2

        if nums[low] > nums[mid] and mid < high:
            direction = "left"
        elif nums[low] < nums[mid] and mid > high:
            direction = "right"

        if direction is "left":
            high = mid
            return self.find_pivot(nums, low, high)
        elif direction is "right":
            low = mid
            return self.find_pivot(nums, low, high)
        else:
            if mid == high and nums[low] > nums[mid]:
                pivot = mid
                return pivot
            elif low == mid and nums[high] < nums[mid]:
                pivot = high
                return pivot
            else:
                if low != high:
                    return self.find_pivot(nums, low+1, high)
        return 0


my_solution = Solution()

nums = [2,5,6,0,0,1,2]
target = 0
print(my_solution.search(nums, target))

nums = [5,6,0,0,1,2,2]
target = 3
print(my_solution.search(nums, target))

nums = [2,4,5,6,7,0,0]
target = 10
print(my_solution.search(nums, target))

nums = [1,3,1,1,1]
target = 3
print(my_solution.search(nums, target))

nums = [2,2,2,0,0,1]
target = 0
print(my_solution.search(nums, target))


