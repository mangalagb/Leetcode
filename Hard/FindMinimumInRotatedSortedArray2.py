# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]
        return self.find_pivot(nums)


    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1

        rotated_left = True
        while high > low:

            # Not rotated. Array is sorted
            if nums[low] < nums[high]:
                return nums[low]

            mid = low + (high - low)//2
            mid_element = nums[mid]
            low_element = nums[low]
            high_element = nums[high]

            if low == mid or high == mid:
                if low_element <= high_element:
                    return low_element
                else:
                    return high_element
            elif low_element == mid_element and mid_element == high_element:
                low = low + 1
                high = high - 1
                rotated_left = None
            elif low_element <= mid_element and mid_element >= high_element:
                rotated_left = False
            elif low_element >= mid_element and mid_element <= high_element:
                rotated_left = True

            if rotated_left:
                high = mid
            elif rotated_left is False:
                low = mid
        return nums[0]


my_sol = Solution()

nums = [1,3,5]
print(my_sol.findMin(nums)) #1

nums = [2,2,2,0,1]
print(my_sol.findMin(nums)) #0

nums = [3,1]
print(my_sol.findMin(nums)) #1

nums = [3,1,1]
print(my_sol.findMin(nums)) #1

nums = [1,3,3]
print(my_sol.findMin(nums)) #1

nums = [3, 1, 3]
print(my_sol.findMin(nums)) #1

nums = [10,1,10,10,10]
print(my_sol.findMin(nums)) #1