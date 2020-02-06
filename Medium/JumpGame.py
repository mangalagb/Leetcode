class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #print(nums)
        if nums[0] == len(nums):
            return True

        initial_step = nums[0]
        result = self.jump(0, 0, nums)
        return result

    def jump(self, curr_index, step, nums):
        end_of_array = len(nums) - 1

        new_index = curr_index + step
        if new_index == end_of_array:
            return True
        elif new_index > end_of_array:
            return False

        value_at_new_index = nums[new_index]

        while value_at_new_index > 0:
            result = self.jump(new_index, value_at_new_index, nums)
            if result:
                return True
            else:
                value_at_new_index -= 1

        return False




my_sol = Solution()

# nums = [2,3,1,1,4]
# print(my_sol.canJump(nums))
#
# nums = [3,2,1,0,4]
# print(my_sol.canJump(nums))
#
# nums = [2,5,0,0]
# print(my_sol.canJump(nums))

nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(my_sol.canJump(nums))

