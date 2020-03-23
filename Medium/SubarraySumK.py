#Given an array of integers and an integer k, you need to find the
# total number of continuous subarrays whose sum equals to k.

# Suppose that our array is: [1,2,3…,n]. How many contiguous subarrays contain k
# Look at the following drawing:
# |1|2|3|4|…|k−1|k|k+1|…|n|
#
# Every subarray containing k
# can be obtained by selecting a "barrier" to the left of k and a barrier
# to the right of k. There are k barriers to the left of k and n−k+1 barriers to the right of k
#
# Therefore there are k(n−k+1)
# contiguous subarrays containing k in the array [1,2,3…n]

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
