#Given an array of integers A with even length, return true if and
# only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i]
# for every 0 <= i < len(A) / 2.

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        print("o")

my_sol = Solution()

A = [3,1,3,6]
print(my_sol.canReorderDoubled(A)) #False
