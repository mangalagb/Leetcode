# Given an array of non-negative integers, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump_possible_so_far = 0
        for index, number in enumerate(nums):
            if index > max_jump_possible_so_far:
                return False
            max_jump_possible_so_far = max(max_jump_possible_so_far, index + number)
            if max_jump_possible_so_far == len(nums):
                return True
        return True


my_sol = Solution()

# nums = [2,3,1,1,4]
# print(my_sol.canJump(nums)) #True

nums = [3,2,1,0,4]
print(my_sol.canJump(nums)) #False
#
# nums = [2,5,0,0]
# print(my_sol.canJump(nums)) #True
#
# nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
# print(my_sol.canJump(nums)) #False
