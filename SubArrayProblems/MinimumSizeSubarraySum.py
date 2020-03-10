# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        window_start = 0
        min_window_size = None
        current_sum = 0

        for window_end in range(0, len(nums)):
            current_sum += nums[window_end]

            while current_sum >= s:
                current_window_size = window_end - window_start + 1
                if not min_window_size or current_window_size < min_window_size:
                    min_window_size = current_window_size

                current_sum -= nums[window_start]
                window_start += 1

        if not min_window_size:
            min_window_size = 0

        return min_window_size

my_sol = Solution()

# s = 7
# nums = [2, 3, 1, 2, 4, 3]
# print(my_sol.minSubArrayLen(s, nums))

s = 3
nums = [1,1]
print(my_sol.minSubArrayLen(s, nums))