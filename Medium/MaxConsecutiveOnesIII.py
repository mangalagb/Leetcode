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
        if not A:
            return 0

        self.result = 0
        for i in range(0, len(A)):
            if A[i] == 1:
                self.extend_bidirectional(i, A, K)
        return self.result

    def extend_bidirectional(self, i, A, K):
        count = 0
        left = i-1
        right = i+1

        if left < 0:
            left = 0

        if right == len(A):
            right = len(A) - 1

        while left > 0:
            if A[left] == 1:
                left -= 1
            elif count < K:
                count += 1
                left -= 1
            else:
                break

        while right < len(A):
            if A[right] == 1:
                right += 1
            elif count < K:
                count += 1
                right += 1
            else:
                break

        local_result = right - left
        self.result = max(self.result, local_result)




my_sol = Solution()

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(my_sol.longestOnes(A, K)) #6
#
# A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# K = 3
# print(my_sol.longestOnes(A, K)) #10

A = [1,1,1]
K = 2
print(my_sol.longestOnes(A, K)) #3
#
# A = [0,0,0,1]
# K = 2
# print(my_sol.longestOnes(A, K)) #3
#
# A = []
# K = 2
# print(my_sol.longestOnes(A, K)) #0