# Given an array A of integers, return the number of (contiguous, non-empty) subarrays
# that have a sum divisible by K.
from collections import defaultdict


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length_of_nums = len(A)
        if length_of_nums == 0:
            return

        current_sum = 0
        result = 0
        frequency = defaultdict(int)
        frequency[0] = 1

        for num in A:
            current_sum += num
            reminder = current_sum % K

            if reminder in frequency:
                result += frequency[reminder]

            frequency[reminder] += 1
        return result


my_sol = Solution()

A = [1,4,5]
K = 5
print(my_sol.subarraysDivByK(A, K)) # 3

A = [4,5,0,-2,-3,1]
K = 5
print(my_sol.subarraysDivByK(A, K)) # 7
