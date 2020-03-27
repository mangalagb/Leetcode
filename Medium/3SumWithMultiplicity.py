# Given an integer array A, and an integer target, return the number of tuples i, j, k
# such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
from collections import defaultdict


class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        length_of_nums = len(A)
        result = 0

        for k in range(0, length_of_nums):
            current = A[k]
            new_target = target - current
            new_nums = A[k+1:]

            count = self.two_sums(new_nums, new_target)
            result += count

        MOD = 10 ** 9 + 7
        result = result % MOD
        return result


    def two_sums(self, nums, target):
        frequency = defaultdict(int)
        result = 0

        for i in range(0, len(nums)):
            current = nums[i]
            remaining = target - current

            if current in frequency:
                result += frequency[current]
                frequency[remaining] += 1
            else:
                frequency[remaining] += 1
        return result


my_sol = Solution()

A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
print(my_sol.threeSumMulti(A, target)) #20

A = [1,1,2,2,2,2]
target = 5
print(my_sol.threeSumMulti(A, target)) #12

A = [0,2,0]
target = 2
print(my_sol.threeSumMulti(A, target)) #1

A = [0,2,0,0]
target = 2
print(my_sol.threeSumMulti(A, target)) #3
