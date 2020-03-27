# A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of
# set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
#
# Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S
# should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.
#
# The tricky part here is that the numbers always form a ring, and no matter which number of this
# ring you start with total count will always be same, so no need to step on it one more time......

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        local_result = 0
        for i in range(0, len(nums)):
            index = i

            while True:
                current = nums[index]
                if current == -1:
                    result = max(result, local_result)
                    local_result = 0
                    break
                else:
                    local_result += 1
                    nums[index] = -1
                    index = current
        return result

my_sol = Solution()

A = [5, 4, 0, 3, 1, 6, 2]
print(my_sol.arrayNesting(A))
