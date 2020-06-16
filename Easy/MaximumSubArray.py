# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest
# sum and return its sum.

class Solution:
    def maxSubArray(self, nums):
        total_sum = None
        local_sum = 0

        for i in range(0, len(nums)):
            current = nums[i]

            if current + local_sum < current:
                local_sum = current
            else:
                local_sum += current

            if total_sum is None:
                total_sum = current
            elif local_sum > total_sum:
                total_sum = local_sum
        return total_sum


my_solution = Solution()

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(nums, my_solution.maxSubArray(nums))


nums = [-2,-8,-10]
print(nums, my_solution.maxSubArray(nums))

nums = [-2,-8,-10, 1]
print(nums, my_solution.maxSubArray(nums))

nums = [-2]
print(nums, my_solution.maxSubArray(nums))

nums = []
print(nums, my_solution.maxSubArray(nums))