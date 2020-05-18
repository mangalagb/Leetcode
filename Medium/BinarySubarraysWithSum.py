#In an array A of 0s and 1s, how many non-empty subarrays have sum S?

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        sum_count = {}





my_sol = Solution()

A = [1,0,1,0,1]
S = 2
print(my_sol.numSubarraysWithSum(A, S)) #4
#
# A = [1,0,0,0,1]
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #1
#
# A = [0,0,0,0,0]
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #0
#
# A = []
# S = 2
# print(my_sol.numSubarraysWithSum(A, S)) #0

# A = [0,0,0,0,0]
# S = 0
# print(my_sol.numSubarraysWithSum(A, S)) #15
