#Given an array nums, write a function to move all 0's to the
#  end of it while maintaining the relative order of the non-zero elements.

class Solution(object):
    def moveZeroes(self, nums):
        if not nums:
            return

        # Just put all non-zero elements in the front one by one
        position = 0
        for num in nums:
            if num != 0:
                nums[position] = num
                position += 1

        # Fill the rest of the array with zeroes
        for i in range(position, len(nums)):
            nums[i] = 0
        #return nums

my_sol = Solution()

nums = [0,1,0,3,12]
print(my_sol.moveZeroes(nums))

nums = [0,0,0,1,0,3]
print(my_sol.moveZeroes(nums))

nums = [0,0,0,0,0]
print(my_sol.moveZeroes(nums))

nums = [4,6,7,8,93]
print(my_sol.moveZeroes(nums))

nums = [0]
print(my_sol.moveZeroes(nums))

