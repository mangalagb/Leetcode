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
    def longestMountain1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return 0

        start = 0
        end = 0
        increasing = False
        decreasing = False
        peak = -1

        prev = A[0]
        result = 0
        A.append(None)

        for i in range(1, len(A)):
            current = A[i]

            if current is None or current > prev:
                if decreasing:
                    decreasing = False
                    end = i-1
                    window = end - start + 1
                    result = max(result, window)
                    start = i
                    end = i
                else:
                    increasing = True

            elif current < prev:
                if increasing:
                    increasing = False
                    decreasing = True

                else:
                    start = i
                    increasing = False

            prev = current
        return result

    def longestMountain(self, A):
        if len(A) < 3:
            return 0

        A.append(None)
        start = 0
        end = 0
        length_of_nums = len(A)

        prev = None
        result = 0
        i = 0
        increasing = False
        decreasing = False
        while end < length_of_nums:
            if prev is None:
                prev = A[i]
                i += 1

            while i < length_of_nums and A[i] is not None and A[i] > prev:
                prev = A[i]
                i += 1
                increasing = True

            while i < length_of_nums and A[i] is not None and A[i] < prev and increasing:
                prev = A[i]
                i += 1
                decreasing = True

            end = i - 1
            increasing = False

            if end - start >= 3 and decreasing:
                window = end - start + 1
                result = max(result, window)
                decreasing = False

            if A[i] is None:
                break

            i -= 1
            start = i
            end = i
            prev = None

        return result

# num1 = [1,4,7,3,2,5]
# print(my_sol.longestMountain(num1))
#
# num1 = [2,3,3,2,0,2]
# print(my_sol.longestMountain(num1))
#
# num1 = [2,2,2]
# print(my_sol.longestMountain(num1))
#
# num1 = [0,1,2,3,4,5,4,3,2,1,0]
# print(my_sol.longestMountain(num1))
#
# num1 = [0,1,0]
# print(my_sol.longestMountain(num1))
#
# num1 = [0,1,2,3,4,5,6,7,8,9]
# print(my_sol.longestMountain(num1))

# num1 = [875,884,239,731,723,685]
# print(my_sol.longestMountain(num1))

