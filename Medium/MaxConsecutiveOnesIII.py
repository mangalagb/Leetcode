# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        num_of_zeroes = 0
        left = 0
        count = 0

        for right in range(0, len(nums)):
            if nums[right] == 0:
                num_of_zeroes += 1

            if num_of_zeroes > k:
                if nums[left] == 0:
                    num_of_zeroes -= 1
                left += 1
            count = max(count, (right - left + 1))
        return count



my_sol = Solution()

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(my_sol.longestOnes(A, K)) #6

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(my_sol.longestOnes(A, K)) #10

A = [1,1,1]
K = 2
print(my_sol.longestOnes(A, K)) #3

A = [0,0,0,1]
K = 2
print(my_sol.longestOnes(A, K)) #3

A = []
K = 2
print(my_sol.longestOnes(A, K)) #0