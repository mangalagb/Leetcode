#Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

#Follow up: Could you implement a solution using only O(1) extra space
# complexity and O(n) runtime complexity?


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        for i in range(0, len(nums)+1):
            total_sum += i

        running_sum = 0
        for j in range(0, len(nums)):
            running_sum += nums[j]

        missing_num = total_sum - running_sum
        return missing_num

my_sol = Solution()

nums = [3,0,1]
print(my_sol.missingNumber(nums)) #2

nums = [9,6,4,2,3,5,7,0,1]
print(my_sol.missingNumber(nums)) #8