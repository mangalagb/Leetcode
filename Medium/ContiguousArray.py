# Given a binary array, find the maximum length of a contiguous subarray
# with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        counts = {}
        max_len = -1

        for i in range(0, len(nums)):
            num = nums[i]
            if num == 0:
                current_sum -= 1
            else:
                current_sum += 1

            if current_sum == 0:
                max_len = max(max_len, i+1)

            if current_sum in counts:
                index = counts[current_sum]
                max_len = max(max_len, i-index)
            else:
                counts[current_sum] = i
        return max_len




my_sol = Solution()
#
# nums = [0,1]
# print(my_sol.findMaxLength(nums)) #2

nums = [0,1,0]
print(my_sol.findMaxLength(nums)) #2
#
# nums = [0,0,1,0,0,0,1,1]
# print(my_sol.findMaxLength(nums)) #6
#
# nums = [1,1,1,1,1,1,1,1]
# print(my_sol.findMaxLength(nums)) #0
#
# nums = [0,1,1,0,1,1,1,0]
# print(my_sol.findMaxLength(nums)) #6

