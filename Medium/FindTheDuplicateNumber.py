# Given an array nums containing n + 1 integers where each integer is between 1 and n
# (inclusive), prove that at least one duplicate number must exist. Assume that there
# is only one duplicate number, find the duplicate one.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        loop = None

        while True:
            slow = nums [slow]
            fast = nums[nums[fast]]
            if slow == fast:
                loop = slow
                break

        slow = 0
        result = None
        while True:
            slow = nums[slow]
            loop = nums[loop]

            if slow == loop:
                result = loop
                break

        return result

my_sol = Solution()

nums = [1,3,4,2,2]
print(my_sol.findDuplicate(nums))

nums = [3,1,3,4,2]
print(my_sol.findDuplicate(nums))

nums = [2,5,9,6,9,3,8,9,7,1]
print(my_sol.findDuplicate(nums))
