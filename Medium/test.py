# Given an array with n objects colored red, white or blue, sort them in-place so
# that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.

class Solution:
    def sortColors(self, nums):
        if len(nums) == 0:
            return

        zero_pointer = 0
        one_pointer = None
        num_of_2 = 0
        position = -1

        for i in range(0, len(nums)):
            #[2,0,1]
            current = nums[i]
            if current == 2:
                num_of_2 += 1
                continue

            # swap with zero pinter position
            if current == 0:
                if nums[zero_pointer] == 1:
                    nums[i] = 1
                    one_pointer = i
                nums[zero_pointer] = 0
                zero_pointer += 1
            elif current == 1:
                if not one_pointer:
                    if zero_pointer != i:
                        nums[zero_pointer] = 1
                        one_pointer = zero_pointer

        two_begin_index = len(nums) - num_of_2
        for i in range(two_begin_index, len(nums)):
            nums[i] = 2
        return nums


my_solution = Solution()

nums = [0, 1, 0, 1, 2]
print(my_solution.sortColors(nums)) #[0, 0, 1, 1, 2]

nums = [0,2,0,1,0,2,2,2]
print(my_solution.sortColors(nums)) #[0, 0, 0, 1, 2, 2, 2, 2]

nums = [2,0,2,1,1,0]
print(my_solution.sortColors(nums)) #[0, 0, 2, 1, 2, 2]

nums = [2, 0, 1]
print(my_solution.sortColors(nums)) #[0, 1, 2]
