# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].

class Solution:
    def find_start(self, nums, target):
        low = 0
        high = len(nums) -1
        start = -1

        while low <= high:

            mid = low + (high - low)//2
            mid_num = nums[mid]

            if mid_num == target:
                start = mid

                prev_index = mid - 1
                if prev_index in range(0, len(nums)):
                    prev_num = nums[prev_index]

                    if prev_num < mid_num:
                        return mid
                    else:
                        high = mid -1
                else:
                    return start

            elif target > mid_num:
                low = mid + 1
            else:
                high = mid -1
        return start


    def find_end(self, nums, target):
        low = 0
        high = len(nums) -1
        stop = -1

        while low <= high:
            mid = low + (high-low)//2
            mid_num = nums[mid]

            if mid_num == target:
                next_index = mid + 1
                stop = mid

                if next_index >= 0 and next_index< len(nums):
                    if nums[next_index] == target:
                        low = next_index
                    else:
                        return mid
                else:
                    return stop

            elif target > mid_num:
                low = mid + 1
            else:
                high = mid -1
        return stop

    def searchRange(self, nums, target):
        if len(nums) == 0 or target > nums[len(nums)-1] or target < nums[0]:
            return [-1,-1]

        start = self.find_start(nums, target)
        end = self.find_end(nums, target)
        return [start, end]


mySolution = Solution()


nums1 = [5,7,7,8,8,10]
target1 = 8
print(mySolution.searchRange(nums1, target1))

nums2 = [5,7,7,8,8,10]
target2 = 6
print(mySolution.searchRange(nums2, target2))

nums3 = [1]
target3 = 1
print(mySolution.searchRange(nums3, target3))

nums3 = [2,2]
target3 = 2
print(mySolution.searchRange(nums3, target3))