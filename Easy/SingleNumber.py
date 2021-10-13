# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# 2∗(a+b+c)−(a+a+b+b+c)=c

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        two_sum = 2 * sum(set(nums))
        actual_sum = sum(nums)
        unique_num = two_sum - actual_sum
        return unique_num

my_sol = Solution()

nums = [2,2,1]
print(my_sol.singleNumber(nums)) #1

nums = [4, 1, 2, 1, 2]
print(my_sol.singleNumber(nums)) #4

nums = [1]
print(my_sol.singleNumber(nums)) #1
