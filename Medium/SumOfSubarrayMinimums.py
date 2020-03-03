# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# #
# # Since the answer may be large, return the answer modulo 10^9 + 7.

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length_of_array = len(A)

        left_stack =[]
        previous_less = [-1] * length_of_array
        for i in range(0, length_of_array):
            current = A[i]
            while len(left_stack) > 0 and left_stack[-1][1] > current:
                left_stack.pop()

            if len(left_stack) < 1:
                previous_less[i] = -1
            else:
                previous_less[i] = left_stack[-1][0]

            left_stack.append([i, A[i]])

        right_stack = []
        next_less = [-1] * length_of_array
        for i in range(length_of_array - 1, -1, -1):
            current = A[i]

            while len(right_stack) > 0 and right_stack[-1][1] > current:
                right_stack.pop()

            if len(right_stack) > 0:
                next_less[i] = right_stack[-1][0]
            else:
                next_less[i] = -1

            right_stack.append([i, A[i]])

        result = 0
        for i in range(0, length_of_array):
            prev_index = previous_less[i]
            left_result = 0
            if prev_index != -1:
                distance = i - prev_index
                left_result = distance * A[prev_index]


            next_index = next_less[i]
            right_result = 0
            if next_index != -1:
                distance = next_index - i
                right_result = distance * A[next_index]

            ans = left_result + right_result + A[i]
            result += ans

        subarray_sum = result % 1000000007
        return subarray_sum

my_sol = Solution()

nums = [3,1,2,4]
print(my_sol.sumSubarrayMins(nums))

# nums = [85]
# print(my_sol.sumSubarrayMins(nums))
#
# nums = [59,91]
# print(my_sol.sumSubarrayMins(nums))