# Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
import sys


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_array = len(nums)
        if length_of_array == 1:
            return nums[0]

        # Initialize maximum products
        # in forward and backward directions
        max_forward = -sys.maxsize - 1
        max_backward = -sys.maxsize - 1

        # Initialize current product
        current_product = 1

        # max_forward for maximum contiguous
        # product in forward direction
        for i in range(length_of_array):

            # if arr[i]==0, it is breaking
            # condition for contiguous subarray
            current_product = current_product * nums[i]
            if current_product == 0:
                current_product = 1
                continue

            if current_product > max_forward:  # update max_forward
                max_forward = current_product

        current_product = 1

        # max_backward for maximum contiguous
        # product in backward direction
        for i in range(length_of_array - 1, -1, -1):
            current_product = current_product * nums[i]

            if current_product == 0:
                current_product = 1
                continue

            # update max_backward
            if current_product > max_backward:
                max_backward = current_product

        # return max of max_forward and max_backward
        result = max(max_forward, max_backward)

        # Product should not be negative.
        # Instead return product of an empty subarray which is
        # considered as 0
        return max(result, 0)
my_sol = Solution()

nums = [2,-5,-2,-4,3]
print(my_sol.maxProduct(nums)) # 24

nums = [2,3,-2,4]
print(my_sol.maxProduct(nums)) # 6

nums = [2,3,-2,10]
print(my_sol.maxProduct(nums)) # 10

nums = [-2,0,-1]
print(my_sol.maxProduct(nums)) #0

nums = [0,2]
print(my_sol.maxProduct(nums)) #2

nums = [-4,-3]
print(my_sol.maxProduct(nums)) # 12

nums = [-2,3,-4]
print(my_sol.maxProduct(nums)) # 24

nums = [-2,13,-4]
print(my_sol.maxProduct(nums)) # 104

nums = [7,-2,-4]
print(my_sol.maxProduct(nums)) # 56