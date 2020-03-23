# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays where the product of all the elements in the
# subarray is less than k.

# Initialize start and end to index 0. Initialize prod to 1. Iterate end from 0 to len(nums)-1.

# Now if prod * nums[end] is less than k, then all subarray between start and end contribute to
# the solution. Since we are moving from left to right, we would have already counted all valid
# subarrays from start to end-1. How many new subarrays with nums[end]? Answer: end-start+1.

# What will be the updated prod? Answer: prod * nums[end].

# What if prod * nums[end] >= k? We need to contract the subarray by advancing start
# until we get a valid solution again.
#
# Now what do we do when start > end? Answer: prod=1.

# Special case: k=0.
# Time is O(N) and space is O(1).
# Issue: Overflow with multiplication.
#

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0:
            return 0

        start = 0
        prod = 1
        count = 0

        for end in range(len(nums)):
            while start <= end and prod * nums[end] >= k:
                prod = prod / nums[start]
                start += 1

            if start > end:
                prod = 1
                count = count
            else:
                prod = prod * nums[end]
                count = count + (end - start + 1)

        return count

my_sol = Solution()

nums = [10, 5, 2, 6]
k = 100
print(my_sol.numSubarrayProductLessThanK(nums, k))  # 8

nums = [1, 2, 3]
k = 0
print(my_sol.numSubarrayProductLessThanK(nums, k))  # 0

nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
k = 19
print(my_sol.numSubarrayProductLessThanK(nums, k))  # 18 4 [[4,3], [3,3], [3,6], [6,2]]

nums = [10,2,2,5,4,4,4,3,7,7]
k = 289
print(my_sol.numSubarrayProductLessThanK(nums, k)) #31 21

# nums = [10,2,2,5,4,4]
# k = 289
# print(my_sol.numSubarrayProductLessThanK(nums, k)) #18 12

# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# k = 2
# print(my_sol.numSubarrayProductLessThanK(nums, k)) #8 4
