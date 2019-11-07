# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        window_start = 0
        number_of_subarrays = 0
        current_sum = 0

        for window_end in range(0, len(A)):
            current_sum += A[window_end]

            while current_sum % K == 0:
                number_of_subarrays += 1

                current_sum -= A[window_start]
                window_start += 1

        return number_of_subarrays

my_sol = Solution()

A = [4,5,0,-2,-3,1]
K = 5
print(my_sol.subarraysDivByK(A, K))
