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

        local_peak_size = 0
        total_peak_size = 0
        peak_reached = False

        prev = A[0]

        for i in range(1, len(A)):
            if A[i] > prev and not peak_reached:
                local_peak_size += 1

            if A[i] < prev:
                peak_reached = True
                local_peak_size += 1

            if A[i] > prev and peak_reached:
                if local_peak_size >= 3 and local_peak_size > total_peak_size:
                    total_peak_size = local_peak_size
                local_peak_size = 0
            prev = A[i]

        print(total_peak_size)




my_sol = Solution()

num1 = [2,1,4,7,3,2,5]
my_sol.longestMountain(num1)