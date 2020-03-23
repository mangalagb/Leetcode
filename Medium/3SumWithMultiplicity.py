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
        frequency = defaultdict(int)
        result = 0

        for i in range(0, length_of_nums):
            req_two_sum = target - A[i]

            local_answer = 0
            if req_two_sum in frequency:
                local_answer = frequency[req_two_sum]
            result += local_answer

            for j in range(0, i):
                two_sum = A[i] + A[j]
                frequency[two_sum] += 1

        MOD = 10 ** 9 + 7
        result = result % MOD
        return result


my_sol = Solution()

A = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
print(my_sol.threeSumMulti(A, target)) #20

A = [1,1,2,2,2,2]
target = 5
print(my_sol.threeSumMulti(A, target)) #12