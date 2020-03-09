# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# #
# # Since the answer may be large, return the answer modulo 10^9 + 7.

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        length_of_nums = len(A)

        # prev has i* - 1 in increasing order of A[i* - 1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * length_of_nums
        for i in range(length_of_nums):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()

            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next has k* + 1 in increasing order of A[k* + 1]
        # where k* is the answer to query j
        stack = []
        next_ = [None] * length_of_nums
        for k in range(length_of_nums - 1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else length_of_nums
            stack.append(k)

        # Use prev/next array to count answer
        result = 0
        for i in range(length_of_nums):
            result += (i - prev[i]) * (next_[i] - i) * A[i]
        result = result % MOD
        return result


my_sol = Solution()

nums = [3,1,2,4]
print(my_sol.sumSubarrayMins(nums)) #17

nums = [85]
print(my_sol.sumSubarrayMins(nums)) #85

nums = [59,91]
print(my_sol.sumSubarrayMins(nums)) #209
