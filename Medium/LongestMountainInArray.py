# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
#     B.length >= 3
#     There exists some 0 < i < B.length - 1 such that
#     B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
#
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_on_left = [-1] * len(A)
        left_stack = []
        for i in range(0, len(A)):
            current = A[i]

            while self.get_top_element(left_stack) is not None and current <= self.get_top_element(left_stack):
                left_stack.pop()

            if self.is_empty(left_stack):
                min_on_left[i] = -1
            else:
                min_on_left[i] = self.get_first_index(left_stack)

            left_stack.append([i, A[i]])


        min_on_right = [-1] * len(A)
        right_stack = []
        for i in range(len(A)-1, -1, -1):
            current = A[i]

            while self.get_top_element(right_stack) is not None and current <= self.get_top_element(right_stack):
                right_stack.pop()

            if self.is_empty(right_stack):
                min_on_right[i] = -1
            else:
                min_on_right[i] = self.get_first_index(right_stack)

            right_stack.append([i, A[i]])

        # print(A)
        # print(min_on_left)
        # print(min_on_right)

        result = 0
        for i in range(0, len(A)):
            min_left = min_on_left[i]
            min_right = min_on_right[i]

            if min_left != -1 and min_right != -1:
                distance = min_right - min_left
                if distance > 0:
                    result = max(result, distance+1)

        return result

    def get_top_element(self, stack):
        length_of_stack = len(stack)
        if length_of_stack < 1:
            return None
        result = stack[length_of_stack-1][1]
        return result

    def get_first_index(self, stack):
        length_of_stack = len(stack)
        if length_of_stack < 1:
            return -1

        return stack[0][0]

    def is_empty(self, stack):
        length_of_stack = len(stack)
        if length_of_stack < 1:
            return True
        return False



my_sol = Solution()

# num1 = [2,1,4,7,3,2,5]
# print(my_sol.longestMountain(num1))
#
# nums = [2,2,2]
# print(my_sol.longestMountain(nums))
#
# nums = [3,2]
# print(my_sol.longestMountain(nums))

# nums = [0,0,0,0,0]
# print(my_sol.longestMountain(nums))

nums = [2,3,3,2,0,2]
print(my_sol.longestMountain(nums))