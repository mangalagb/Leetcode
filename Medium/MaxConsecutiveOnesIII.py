# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        begin = 0
        end = 0
        count = 0
        longest_window = -1
        length_of_array = len(A)

        while end < length_of_array:
            if end + 1 == length_of_array and A[end] == 1:
                result = end - begin + 1
                if result > longest_window:
                    longest_window = result

            if A[end] == 0:
                count += 1

                if count > K:
                    result = end - begin
                    if result > longest_window:
                        longest_window = result

                    while A[begin] == 1:
                        begin += 1

                    if A[begin] == 0:
                        begin += 1
                        count -= 1
            end += 1

        if longest_window == -1:
            longest_window = length_of_array
        #print(longest_window)
        return longest_window

my_sol = Solution()

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
my_sol.longestOnes(A, K)

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
my_sol.longestOnes(A, K)

A = [1,1,1]
K = 2
my_sol.longestOnes(A, K)

A = [0,0,0,1]
K = 2
my_sol.longestOnes(A, K)

A = []
K = 2
my_sol.longestOnes(A, K)