#Given an array of integers and an integer k, you need to find the
# total number of continuous subarrays whose sum equals to k.

from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):

        if not nums:
            return

        current_sum = 0
        result = 0
        frequencies = defaultdict(int)
        frequencies[0] = 1

        for i in range(0, len(nums)):
            current_sum += nums[i]

            if current_sum - k in frequencies:
                result += frequencies[current_sum - k]

            frequencies[current_sum] += 1
        return result


my_sol = Solution()

nums = [1,1,1]
k = 2
print(my_sol.subarraySum(nums, k))

nums = [1,2,3]
k = 3
print(my_sol.subarraySum(nums, k))

nums = [1]
k = 1
print(my_sol.subarraySum(nums, k))

nums = [1,2, 3]
k = 10
print(my_sol.subarraySum(nums, k))

nums = [-1,-1,1]
k = 0
print(my_sol.subarraySum(nums, k))
