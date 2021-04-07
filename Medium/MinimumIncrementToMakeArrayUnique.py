# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
#
# Return the least number of moves to make every value in A unique.
import collections
import sys


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        unique_nums = set()
        unordered_repeated_nums = {}

        for i in range(0, len(A)):
            num = A[i]

            if num not in unique_nums:
                unique_nums.add(num)

            else:
                if num in unordered_repeated_nums:
                    unordered_repeated_nums[num] += 1
                else:
                    unordered_repeated_nums[num] = 1

        count = 1
        repeated_nums = collections.OrderedDict(sorted(unordered_repeated_nums.items()))
        moves = 0

        for key, value in repeated_nums.items():
            while value != 0:
                first_available_num = next(v for v in range(count, sys.maxsize) if v not in unique_nums and v > key)
                moves += first_available_num - key
                unique_nums.add(first_available_num)
                count = first_available_num + 1
                value -= 1
        return moves

my_sol = Solution()

A = [3,2,1,2,1,7]
print(my_sol.minIncrementForUnique(A)) #6

A = [1,2,2]
print(my_sol.minIncrementForUnique(A)) #1
