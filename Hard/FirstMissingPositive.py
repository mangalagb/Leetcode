# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n)
# time and uses constant extra space.?

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)

        length = pow(2, 31) - 1
        ans = bin(length)[2:]

        print(ans)
        print("----")

        for i in range(1, 9):
            print(bin(i)[2:])

my_sol = Solution()

nums = [1,2,0]
print(my_sol.firstMissingPositive(nums)) #3
#
# nums = [3,4,-1,1]
# print(my_sol.firstMissingPositive(nums)) #2
#
# nums = [7, 8, 9, 11, 12]
# print(my_sol.firstMissingPositive(nums)) #1
