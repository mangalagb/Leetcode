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
        print(A)

        #left_stack = [[0, A[0]]]
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
        #print(previous_less)

        #right_stack = [[length_of_array-1, A[length_of_array-1]]]
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
        #print(next_less)

        result = 0
        for i in range(0, length_of_array):
            left_dist = i - previous_less[i]
            # if previous_less[i] == -1:
            #     left_dist = 1

            right_dist = next_less[i] - i
            # if next_less[i] == -1:
            #     right_dist = 1

            num_of_subarrays = (A[i] * left_dist * right_dist) + 1
            result += num_of_subarrays

        return result

my_sol = Solution()

nums = [3,1,2,4]
print(my_sol.sumSubarrayMins(nums))